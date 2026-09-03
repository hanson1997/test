#!/usr/bin/env python3
"""Fill the Departmental Recovery Strategy Register from the Technical BIA."""

import csv
from pathlib import Path

from docx import Document
from docx.enum.section import WD_ORIENT
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

BIA_PATH = Path(
    "/home/ubuntu/.cursor/projects/workspace/uploads/"
    "Departmental_BIA_Register_Technical_260c.csv"
)
TEMPLATE_PATH = Path(
    "/home/ubuntu/.cursor/projects/workspace/uploads/"
    "2_-_Recovery_Strategy_Register_2_1e42.csv"
)
OUT_CSV = Path("/workspace/Technical_Department_Recovery_Strategy_Register.csv")
OUT_DOCX = Path("/workspace/Technical_Department_Recovery_Strategy_Register.docx")

NAVY = "1B365D"
TEAL = "1F7A8C"
WHITE = "FFFFFF"
BODY = "1A1A1A"

STRATEGY_TYPE = {
    "Requirements & Solution Design": "People + Technology",
    "Application Development (Coding)": "People + Technology",
    "Source Code & Version Control": "Technology",
    "Code Review": "People",
    "Testing & Quality Assurance": "People + Technology",
    "Build Management": "Technology",
    "CI/CD Pipeline Management": "Technology + People",
    "Release Deployment (Execution)": "Technology + People",
    "Database & Data Structure Management": "Technology",
    "Third-Party & Dependency Management": "People + Technology",
    "Security & Access Configuration": "Technology + People",
    "Environment Management": "Technology",
    "Data Handling & ETL": "Technology + People",
    "Production Support & Troubleshooting": "People + Technology",
    "Access & Account Management": "People + Technology",
    "Release Management": "People",
    "Cloud Infrastructure Management": "Technology",
    "Logging & Monitoring": "Technology",
    "Incident Management": "People + Technology",
    "Decommissioning": "People",
}

# Resource packs already mentioned in the BIA strategy / safeguards.
RESOURCES_DOCUMENTED = {
    "Requirements & Solution Design": "No",
    "Application Development (Coding)": "No",
    "Source Code & Version Control": "No",
    "Code Review": "No",
    "Testing & Quality Assurance": "Yes",
    "Build Management": "Yes",
    "CI/CD Pipeline Management": "Yes",
    "Release Deployment (Execution)": "Yes",
    "Database & Data Structure Management": "Yes",
    "Third-Party & Dependency Management": "Yes",
    "Security & Access Configuration": "Yes",
    "Environment Management": "Yes",
    "Data Handling & ETL": "Yes",
    "Production Support & Troubleshooting": "Yes",
    "Access & Account Management": "Yes",
    "Release Management": "No",
    "Cloud Infrastructure Management": "Yes",
    "Logging & Monitoring": "Yes",
    "Incident Management": "Yes",
    "Decommissioning": "Yes",
}


def clean(value):
    return (
        str(value)
        .replace("\xa0", " ")
        .replace("\n", " ")
        .replace("\r", " ")
        .replace("  ", " ")
        .strip()
    )


def load_bia():
    with BIA_PATH.open(newline="", encoding="latin-1") as f:
        rows = list(csv.reader(f))
    headers = [h.strip() for h in rows[3]]
    idx = {h: i for i, h in enumerate(headers)}
    records = []
    for row in rows[4:]:
        if not row or not str(row[0]).startswith("BIA-"):
            continue
        rec = {h: clean(row[idx[h]]) if h in idx and idx[h] < len(row) else "" for h in idx}
        records.append(rec)
    if len(records) != 20:
        raise SystemExit(f"Expected 20 BIA rows, got {len(records)}")
    return records


def comments_for(rec):
    bits = ["No practice drill has been run yet."]
    if rec["Cross-Trained Backup Staff Identified?"] == "No":
        bits.append("Backup-staff gap must close before next review.")
    return " ".join(bits)


def strategy_rows(bia_records):
    out = []
    for i, rec in enumerate(bia_records, start=1):
        name = rec["Function / Process Name"]
        out.append(
            [
                f"RS-2026-TU-{i:02d}",
                rec["BIA Ref"],
                rec["Department / Unit"],
                name,
                rec["Completed By"] or "R. Sulaimon (BCC)",
                rec["Profiling Date"] or "01-Sep-2026",
                "v1.0",
                rec["Overall Criticality Ranking"],
                rec["RTO (Hrs)"],
                rec["RPO"],
                rec["MTPD (Hrs)"],
                STRATEGY_TYPE[name],
                rec["Recommended Recovery Strategy"],
                rec["Alternate Site/Access Required?"],
                rec["Cross-Trained Backup Staff Identified?"],
                rec["Current Recovery Capability (Hrs)"],
                rec["RTO Gap?"],
                "Yes",
                RESOURCES_DOCUMENTED[name],
                "",  # Last Tested Date — no drill yet
                "Not yet tested",
                "",  # Next Test Due — no date
                "Not Tested",
                "",
                "",
                "",
                "",
                "",
                "",
                comments_for(rec),
            ]
        )
    return out


def write_csv(data_rows):
    with TEMPLATE_PATH.open(newline="", encoding="latin-1") as f:
        template = list(csv.reader(f))
    # Keep title, department line, group headers, column headers. Replace sample rows.
    header_block = template[:4]
    # Fill department on row 2
    dept_row = header_block[1]
    if dept_row:
        dept_row[0] = "Department: Implementation / Technical Unit"
        # keep Register Owner placeholder on the same row if present
        for i, cell in enumerate(dept_row):
            if "Register Owner" in cell:
                dept_row[i] = (
                    "Register Owner (BCC):  ______________________     "
                    "Last Updated:  03-Sep-2026"
                )
    with OUT_CSV.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerows(header_block)
        writer.writerows(data_rows)
    print(f"Wrote {OUT_CSV} ({len(data_rows)} strategies)")


def set_run(run, *, size=10, bold=False, color=BODY, font="Calibri"):
    run.font.name = font
    run._element.rPr.rFonts.set(qn("w:eastAsia"), font)
    run.font.size = Pt(size)
    run.bold = bold
    run.font.color.rgb = RGBColor.from_string(color)


def shade(cell, hex_color):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    for child in list(tcPr):
        if child.tag == qn("w:shd"):
            tcPr.remove(child)
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), hex_color)
    shd.set(qn("w:val"), "clear")
    tcPr.append(shd)


def borders(cell):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    b = OxmlElement("w:tcBorders")
    for edge in ("top", "left", "bottom", "right"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), "4")
        el.set(qn("w:space"), "0")
        el.set(qn("w:color"), "8AA0B4")
        b.append(el)
    tcPr.append(b)


def fill_cell(cell, text, *, bold=False, size=7, fill=None, font_color=BODY, center=False):
    cell.text = ""
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER if center else WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    run = p.add_run(str(text))
    set_run(run, size=size, bold=bold, color=font_color)
    borders(cell)
    if fill:
        shade(cell, fill)
    v = OxmlElement("w:vAlign")
    v.set(qn("w:val"), "center")
    cell._tc.get_or_add_tcPr().append(v)


def write_docx(data_rows):
    # Readable extract: the strategy working columns, not all 30 Excel fields.
    headers = [
        "Strategy Ref",
        "BIA Ref",
        "Function / Process Name",
        "Criticality",
        "RTO",
        "RPO",
        "MTPD",
        "Strategy Type",
        "Strategy Summary",
        "Alternate Site/Access?",
        "Cross-Trained Backup?",
        "Current Recovery (Hrs)",
        "RTO Gap?",
        "Test Result Summary",
        "Test Status",
        "Comments / Notes",
    ]
    # indices in data_rows
    pick = [0, 1, 3, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 20, 22, 29]
    widths = [2.4, 2.8, 3.6, 2.4, 1.5, 2.2, 1.6, 2.8, 5.4, 2.4, 2.6, 2.4, 1.8, 2.6, 2.2, 3.6]

    doc = Document()
    section = doc.sections[0]
    section.orientation = WD_ORIENT.LANDSCAPE
    section.page_width = Cm(42.0)
    section.page_height = Cm(29.7)
    section.left_margin = Cm(1.1)
    section.right_margin = Cm(1.1)
    section.top_margin = Cm(1.1)
    section.bottom_margin = Cm(1.1)

    title = doc.add_paragraph()
    r = title.add_run("Departmental Recovery Strategy Register")
    set_run(r, size=16, bold=True, color=NAVY)
    sub = doc.add_paragraph()
    r = sub.add_run(
        "Department: Implementation / Technical Unit. One recovery strategy per BIA "
        "function. Recovery targets (criticality, RTO, RPO, MTPD) and the strategy "
        "summary are taken from the final Technical BIA. Test Result Summary is "
        "“Not yet tested” on every row — that is not a date and not a prediction "
        "that the risk will happen. Sign-off is left blank for the workshop. "
        "The full Excel/CSV has every template column."
    )
    set_run(r, size=10, color=BODY)

    table = doc.add_table(rows=1 + len(data_rows), cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = table.rows[0]
    for i, label in enumerate(headers):
        fill_cell(hdr.cells[i], label, bold=True, size=7, fill=NAVY, font_color=WHITE, center=True)
        hdr.cells[i].width = Cm(widths[i])
    for r_i, row in enumerate(data_rows):
        zebra = "F4F7FA" if r_i % 2 else WHITE
        cells = table.rows[r_i + 1].cells
        for c_i, src in enumerate(pick):
            fill_cell(
                cells[c_i],
                row[src],
                bold=(c_i == 0 or c_i == 2),
                size=7,
                fill=zebra,
                center=c_i in (3, 4, 5, 6, 9, 10, 11, 12, 13, 14),
            )
            cells[c_i].width = Cm(widths[c_i])

    note = doc.add_paragraph()
    note.paragraph_format.space_before = Pt(8)
    r = note.add_run(
        "Open Technical_Department_Recovery_Strategy_Register.csv in Excel to see "
        "the full template (identification, readiness, testing, sign-off)."
    )
    set_run(r, size=9, color="5A6A7A")
    doc.save(OUT_DOCX)
    print(f"Wrote {OUT_DOCX}")


def main():
    bia = load_bia()
    data = strategy_rows(bia)
    write_csv(data)
    write_docx(data)


if __name__ == "__main__":
    main()
