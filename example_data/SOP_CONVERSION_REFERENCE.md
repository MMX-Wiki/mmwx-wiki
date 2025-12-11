# SOP Conversion Quick Reference

Use this guide when creating topics in Writerside. Create the topic in the IDE, then copy content from the corresponding generated file.

---

## Workbook 1: SOP Accountant Monthly Process

**Suggested Parent Topic:** "Accountant Monthly Process" (or similar)

| # | Sheet Name | Generated File | Preview |
|---|------------|----------------|---------|
| 1 | **Dates to Know** | `sop-accountant-monthly-process/dates-to-know.md` | Key dates: MS Sales Tax (15th), TN/AR Workcomp (15th), annual audits (Feb), TN SOS report (Apr) |
| 2 | **Step 1 Daily-Weekly** | `sop-accountant-monthly-process/step-1-daily-weekly.md` | Checklist version - daily tasks (positive pay, sync, bank feeds), weekly tasks by day |
| 3 | **Step 1 Daily-Weekly Instr** | `sop-accountant-monthly-process/step-1-daily-weekly-instr.md` | **DETAILED** (~250 lines) - Full instructions with rules for bank feeds, deposits, IIF downloads, reconciliation. This is the comprehensive version. |
| 4 | **Step 2 Month Throughout Process** | `sop-accountant-monthly-process/step-2-month-throughout-process.md` | Research PO#s, fuel credit account, A/P aging review in QB's and Bill.com |
| 5 | **Step 3 Month (Beginning) Process** | `sop-accountant-monthly-process/step-3month-beginning-process.md` | Beginning-of-month payments: BCBS, Lincoln, Microvellum, Innergy, MLGW, Comcast, GTB loans, etc. |
| 6 | **Step 4 Month End Process** | `sop-accountant-monthly-process/step-4-month-end-process.md` | EOM reconciliation checklist, loan interest/principal splits, bank/CC reconciliation |
| 7 | **Step 5 MO-QTR-YE Review for BBB** | `sop-accountant-monthly-process/step-5-mo-qtr-ye-review-for-bbb.md` | Month/Quarter/Year-end review, balance sheet tests, P&L review, year-end tax prep |

---

## Workbook 2: SOP Accounts Payable

**Suggested Parent Topic:** "Accounts Payable" (or similar)

| # | Sheet Name | Generated File | Preview |
|---|------------|----------------|---------|
| 1 | **Overview** | `sop-accounts-payable/overview.md` | Core rules (pay from invoices only, no auto-save), inbox guidelines, duplicate warnings, AI quirks |
| 2 | **Start to Finish** | `sop-accounts-payable/start-to-finish.md` | Weekly inbox processing workflow, AI vs memorization, PO# validation in Innergy |
| 3 | **Approvers-Approvals** | `sop-accounts-payable/approvers-approvals.md` | Short reference - who approves what (Ken: PO items, Donna: utilities/insurance, Trevor: owner items) |
| 4 | **Cardm (Chase) Process Trans.** | `sop-accounts-payable/cardm-chase-process-trans.md` | Chase credit card processing: CSV download, batch entry in QB's, memo format standards |
| 5 | **Home Depot - Process Trans.** | `sop-accounts-payable/home-depot-process-trans.md` | Home Depot account processing: aging section, batch entry, Innergy integration for job costs |
| 6 | **Credits - bill.cm** | `sop-accounts-payable/credits-billcm.md` | How to enter credit memos in Bill.com inbox, applying credits to invoices |
| 7 | **Classification - Updates Needs** | `sop-accounts-payable/classification-updates-needs.md` | Classification guidelines, expense report rules, meeting notes (appears to be WIP/notes) |
| 8 | **Loose Receipts - Credit Cards** | `sop-accounts-payable/loose-receipts-credit-cards-.md` | Handling loose receipts: sorting, scanning, labeling, weekly/monthly processing |

---

## Notes for Manual Polish

**Common issues to watch for:**

1. **Pipe characters (|)** - The parser used `|` to join multi-column content. You may want to convert these to proper tables or restructure.

2. **ALL CAPS sections** - Many headers came through as ALL CAPS from the spreadsheet. Consider title-casing them.

3. **Rule formatting** - Rules like "RULE #1:" are bolded but may benefit from Writerside admonitions (`{style="warning"}` or `{style="note"}`).

4. **Checklists** - Items like `_____` were meant as fill-in blanks. Consider converting to actual checkboxes or task lists.

5. **Step 1 has two versions** - "Daily-Weekly" is a checklist, "Daily-Weekly Instr" is the full detailed version. You may want to combine or keep separate based on audience needs.

6. **Classification sheet** - Appears to contain meeting notes and TODOs rather than finalized SOP content.

---

## File Locations

All generated files are in:
```
C:\Users\dkane\Projects\mmwx-wiki\Writerside\topics\
├── sop-accountant-monthly-process\
│   ├── dates-to-know.md
│   ├── step-1-daily-weekly.md
│   ├── step-1-daily-weekly-instr.md
│   ├── step-2-month-throughout-process.md
│   ├── step-3month-beginning-process.md
│   ├── step-4-month-end-process.md
│   └── step-5-mo-qtr-ye-review-for-bbb.md
└── sop-accounts-payable\
    ├── overview.md
    ├── start-to-finish.md
    ├── approvers-approvals.md
    ├── cardm-chase-process-trans.md
    ├── home-depot-process-trans.md
    ├── credits-billcm.md
    ├── classification-updates-needs.md
    └── loose-receipts-credit-cards-.md
```
