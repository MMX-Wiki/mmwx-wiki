"""
Convert SOP Excel workbooks to Markdown files for Writerside wiki.
Each workbook becomes a group, each worksheet becomes a child topic.
"""

import pandas as pd
import re
import os
from pathlib import Path

def clean_sheet_name_for_filename(name):
    """Convert sheet name to a valid, kebab-case filename."""
    # Remove special characters and extra spaces
    clean = re.sub(r'[^\w\s-]', '', name)
    clean = re.sub(r'\s+', '-', clean.strip())
    clean = re.sub(r'-+', '-', clean)
    return clean.lower()

def clean_text(text):
    """Clean and normalize text content."""
    if pd.isna(text):
        return ''
    text = str(text).strip()
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text)
    return text

def extract_sheet_content(df):
    """Extract meaningful content from a DataFrame."""
    content_lines = []
    
    for idx, row in df.iterrows():
        # Collect non-null values from all columns
        row_content = []
        for col_idx, val in enumerate(row):
            cleaned = clean_text(val)
            if cleaned:
                row_content.append(cleaned)
        
        if row_content:
            # Join multiple column values with ' | ' if they seem like separate content
            line = ' | '.join(row_content) if len(row_content) > 1 else row_content[0]
            content_lines.append(line)
    
    return content_lines

def convert_to_markdown(lines, sheet_name):
    """Convert extracted lines to well-formatted Markdown."""
    md_lines = []
    
    # Add title from sheet name
    title = sheet_name.strip()
    md_lines.append(f"# {title}")
    md_lines.append("")
    
    current_section = None
    in_list = False
    
    for line in lines:
        # Skip empty lines
        if not line.strip():
            continue
        
        # Detect section headers (ALL CAPS lines or lines ending with colon that are short)
        if (line.isupper() and len(line) < 80) or (line.endswith(':') and len(line) < 60 and not any(c.isdigit() for c in line[:3])):
            if in_list:
                md_lines.append("")
                in_list = False
            md_lines.append(f"## {line.rstrip(':')}")
            md_lines.append("")
            current_section = line
            continue
        
        # Detect numbered items (e.g., "1.", "1)", "1:", "Step 1", etc.)
        numbered_match = re.match(r'^(\d+)[\.\)\:]?\s*(.+)', line)
        step_match = re.match(r'^Step\s*(\d+)[:\s]*(.+)', line, re.IGNORECASE)
        
        if numbered_match:
            num, content = numbered_match.groups()
            md_lines.append(f"{num}. {content.strip()}")
            in_list = True
            continue
        elif step_match:
            num, content = step_match.groups()
            md_lines.append(f"{num}. {content.strip()}")
            in_list = True
            continue
        
        # Detect bullet-like items (lines starting with -, *, •)
        bullet_match = re.match(r'^[\-\*\•]\s*(.+)', line)
        if bullet_match:
            content = bullet_match.group(1)
            md_lines.append(f"- {content.strip()}")
            in_list = True
            continue
        
        # Detect Rule/Note patterns
        rule_match = re.match(r'^(Rule\s*#?\d+)[:\s]*(.+)', line, re.IGNORECASE)
        if rule_match:
            rule_label, content = rule_match.groups()
            md_lines.append(f"**{rule_label}:** {content.strip()}")
            md_lines.append("")
            continue
        
        # Regular paragraph
        if in_list:
            md_lines.append("")
            in_list = False
        md_lines.append(line)
        md_lines.append("")
    
    return '\n'.join(md_lines)


def process_workbook(excel_path, output_dir):
    """Process an Excel workbook and create Markdown files."""
    # Read all sheets
    sheets = pd.read_excel(excel_path, sheet_name=None)
    
    # Get workbook name for the group
    workbook_name = Path(excel_path).stem
    workbook_slug = clean_sheet_name_for_filename(workbook_name)
    
    # Create output directory
    output_path = Path(output_dir) / workbook_slug
    output_path.mkdir(parents=True, exist_ok=True)
    
    print(f"\n{'='*60}")
    print(f"Processing: {workbook_name}")
    print(f"Output directory: {output_path}")
    print(f"{'='*60}")
    
    created_files = []
    
    for sheet_name, df in sheets.items():
        # Extract content
        lines = extract_sheet_content(df)
        
        if not lines:
            print(f"  [SKIP] {sheet_name} - no content")
            continue
        
        # Convert to markdown
        markdown = convert_to_markdown(lines, sheet_name)
        
        # Create filename
        filename = clean_sheet_name_for_filename(sheet_name) + '.md'
        filepath = output_path / filename
        
        # Write file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(markdown)
        
        created_files.append({
            'sheet': sheet_name,
            'file': filename,
            'path': str(filepath),
            'lines': len(lines)
        })
        print(f"  [OK] {sheet_name} -> {filename} ({len(lines)} content lines)")
    
    return {
        'workbook': workbook_name,
        'slug': workbook_slug,
        'output_dir': str(output_path),
        'files': created_files
    }


def generate_tree_snippet(results):
    """Generate Writerside tree XML snippet for the converted files."""
    snippets = []
    
    for result in results:
        snippet_lines = [f'    <toc-element toc-title="{result["workbook"]}">']
        for f in result['files']:
            topic_file = f['file']
            snippet_lines.append(f'        <toc-element topic="{topic_file}"/>')
        snippet_lines.append('    </toc-element>')
        snippets.append('\n'.join(snippet_lines))
    
    return '\n\n'.join(snippets)


def main():
    """Main entry point."""
    base_path = Path(r"C:\Users\dkane\Projects\mmwx-wiki\example_data")
    output_dir = Path(r"C:\Users\dkane\Projects\mmwx-wiki\Writerside\topics")
    
    excel_files = [
        base_path / "SOP Accountant Monthly Process.xlsx",
        base_path / "SOP Accounts Payable.xlsx"
    ]
    
    results = []
    
    for excel_file in excel_files:
        if excel_file.exists():
            result = process_workbook(excel_file, output_dir)
            results.append(result)
        else:
            print(f"[ERROR] File not found: {excel_file}")
    
    # Generate tree snippet
    print("\n" + "="*60)
    print("WRITERSIDE TREE SNIPPET")
    print("Add the following to your .tree file:")
    print("="*60)
    print(generate_tree_snippet(results))
    
    print("\n" + "="*60)
    print("CONVERSION COMPLETE")
    print(f"Total workbooks processed: {len(results)}")
    total_files = sum(len(r['files']) for r in results)
    print(f"Total markdown files created: {total_files}")
    print("="*60)
    
    return results


if __name__ == "__main__":
    main()
