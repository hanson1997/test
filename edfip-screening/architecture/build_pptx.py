#!/usr/bin/env python3
"""Client-facing EDFIP architecture walkthrough for Emeraid."""
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

BG = RGBColor(0x0B, 0x0F, 0x0D)
INK = RGBColor(0xF4, 0xF0, 0xE6)
MUTED = RGBColor(0xA8, 0xB3, 0xAA)
GOLD = RGBColor(0xC4, 0xA0, 0x56)

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank = prs.slide_layouts[6]
TOTAL = 14


def paint_bg(slide):
    shape = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), prs.slide_width, prs.slide_height
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = BG
    shape.line.fill.background()
    spTree = slide.shapes._spTree
    sp = shape._element
    spTree.remove(sp)
    spTree.insert(2, sp)


def add_text(slide, l, t, w, h, text, size=18, color=INK, bold=False, font="Georgia", align=PP_ALIGN.LEFT):
    box = slide.shapes.add_textbox(Inches(l), Inches(t), Inches(w), Inches(h))
    tf = box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size = Pt(size)
    run.font.color.rgb = color
    run.font.bold = bold
    run.font.name = font
    return box


def footer(slide, num):
    add_text(slide, 0.7, 7.05, 9, 0.25, "Dexta Synergy Services  ·  Confidential", 11, MUTED, False, "Calibri")
    add_text(slide, 11.2, 7.05, 1.6, 0.25, f"{num:02d} / {TOTAL:02d}", 11, MUTED, False, "Calibri", PP_ALIGN.RIGHT)


def kicker_title(slide, kicker, title, num):
    paint_bg(slide)
    add_text(slide, 0.7, 0.35, 12, 0.35, kicker.upper(), 12, GOLD, True, "Calibri")
    add_text(slide, 0.7, 0.75, 12, 1.55, title, 30, INK, False, "Georgia")
    footer(slide, num)


# 1
s = prs.slides.add_slide(blank)
paint_bg(s)
add_text(s, 0.7, 0.4, 12, 0.35, "PROPOSED ARCHITECTURE", 13, GOLD, True, "Calibri")
add_text(s, 0.7, 1.0, 12, 2.2, "One platform Emeraid hosts.\nInstitutions are onboarded\nand licensed.", 34, INK, False, "Georgia")
add_text(s, 0.7, 3.6, 11.5, 1.8, "This walkthrough develops the Apache Fineract and Odoo architecture already shared. It shows how EDFIP operates as multi-tenant software-as-a-service that Emeraid will brand and sell.", 18, MUTED, False, "Calibri")
footer(s, 1)

# 2
s = prs.slides.add_slide(blank)
kicker_title(s, "Software as a service", "Emeraid does not install EDFIP\nat each institution.", 2)
add_text(s, 0.7, 2.55, 2.8, 3.2, "1. HOST\n\nOne platform on Emeraid’s environment.", 15, INK, False, "Calibri")
add_text(s, 3.7, 2.55, 2.8, 3.2, "2. ONBOARD\n\nSuper Administrator creates the institution.", 15, INK, False, "Calibri")
add_text(s, 6.7, 2.55, 2.8, 3.2, "3. LICENCE\n\nThe purchased module pack is switched on.", 15, INK, False, "Calibri")
add_text(s, 9.7, 2.55, 2.9, 3.2, "4. USE\n\nStaff work only in the licensed portion.", 15, INK, False, "Calibri")

# 3
s = prs.slides.add_slide(blank)
kicker_title(s, "Configurable packs", "The same platform, sold as\ndifferent products.", 3)
add_text(s, 0.7, 2.55, 3.0, 2.8, "MICROFINANCE\n\nCRM, core banking,\nagency, field app", 15, INK, False, "Calibri")
add_text(s, 3.9, 2.55, 3.0, 2.8, "COOPERATIVE\n\nCRM, share register,\ncore banking", 15, INK, False, "Calibri")
add_text(s, 7.1, 2.55, 3.0, 2.8, "VSLA NETWORK\n\nCRM, share-out,\ncore banking", 15, INK, False, "Calibri")
add_text(s, 10.3, 2.55, 2.4, 2.8, "PAYGO / GAF\n\nCRM, device credit,\nOEM tokens", 15, INK, False, "Calibri")
add_text(s, 0.7, 5.5, 12, 1.2, "Packs are assembled from a catalogue and can be changed during the contract. Unlicensed modules are unavailable in the screens and in the API.", 16, MUTED, False, "Calibri")

# 4
s = prs.slides.add_slide(blank)
kicker_title(s, "Platform", "Four parts. One ledger.", 4)
add_text(s, 0.7, 2.5, 3.0, 3.4, "ODOO\n\nWhere people work: CRM, KYC, VSLA, cooperatives, PayGo, agency, System Administration.", 14, INK, False, "Calibri")
add_text(s, 3.9, 2.5, 3.0, 3.4, "APACHE FINERACT\n\nCore banking: loans, savings, schedules, balances, general ledger. APIs only.", 14, INK, False, "Calibri")
add_text(s, 7.1, 2.5, 3.0, 3.4, "FASTAPI\n\nChannel and money path. Separate process, same environment as Odoo.", 14, INK, False, "Calibri")
add_text(s, 10.3, 2.5, 2.5, 3.4, "FLUTTER\n\nField Android (offline) and customer Android. Calls FastAPI only.", 14, INK, False, "Calibri")

# 5
s = prs.slides.add_slide(blank)
kicker_title(s, "How people enter", "Staff open Odoo.\nChannels open the API.", 5)
add_text(s, 0.7, 2.7, 5.8, 2.6, "ODOO\n\nInstitution staff, Emeraid Super Administrators, customer web portal.", 16, INK, False, "Calibri")
add_text(s, 7.0, 2.7, 5.6, 2.6, "FASTAPI  ·  /api\n\nFlutter, USSD, payment providers, OEM callbacks, partner integrations.", 16, INK, False, "Calibri")
add_text(s, 0.7, 5.5, 12, 1.2, "Fineract is not a public staff website. When a teller posts a repayment in Odoo, the Odoo server calls FastAPI, which posts to Fineract.", 16, MUTED, False, "Calibri")

# 6
s = prs.slides.add_slide(blank)
kicker_title(s, "How money moves", "Every naira is posted once,\nin Fineract.", 6)
add_text(s, 0.7, 2.55, 2.8, 3.0, "INSTRUCTION\n\nTeller, field app, USSD, or payment webhook", 15, INK, False, "Calibri")
add_text(s, 3.7, 2.55, 2.8, 3.0, "FASTAPI\n\nIdentity, licence, branch, idempotency key", 15, INK, False, "Calibri")
add_text(s, 6.7, 2.55, 2.8, 3.0, "FINERACT\n\nPosts the transaction and updates the ledger", 15, INK, False, "Calibri")
add_text(s, 9.7, 2.55, 2.9, 3.0, "ODOO\n\nShows confirmed status and issues the receipt", 15, INK, False, "Calibri")
add_text(s, 0.7, 5.7, 12, 1.0, "If the network fails after posting, the same key is retried. A second posting is not created.", 16, MUTED, False, "Calibri")

# 7
s = prs.slides.add_slide(blank)
kicker_title(s, "Onboarding an institution", "From licence to a live tenant.", 7)
add_text(s, 0.7, 2.5, 12, 4.2, "1.  Super Administrator creates the institution, branding, and module pack.\n\n2.  Head Office and branches are recorded.\n\n3.  The Institution Administrator is invited.\n\n4.  FastAPI creates the Fineract tenant and an office for each branch.\n\n5.  Institution Administrator assigns staff to roles and branches. Staff log into Odoo.", 16, INK, False, "Calibri")

# 8
s = prs.slides.add_slide(blank)
kicker_title(s, "Branch access", "Configured in Odoo.\nEnforced for money in Fineract.", 8)
add_text(s, 0.7, 2.7, 3.8, 2.8, "ODOO\n\nA Garki officer does not see Wuse records.", 16, INK, False, "Calibri")
add_text(s, 4.8, 2.7, 3.8, 2.8, "FASTAPI\n\nA request for another branch is refused.", 16, INK, False, "Calibri")
add_text(s, 8.9, 2.7, 3.8, 2.8, "FINERACT\n\nPostings can only land in the mapped office.", 16, INK, False, "Calibri")
add_text(s, 0.7, 5.6, 12, 1.1, "Institution finance may see all branches of their own institution. They cannot see another tenant.", 16, MUTED, False, "Calibri")

# 9
s = prs.slides.add_slide(blank)
kicker_title(s, "Control plane", "System Administration is how\nEmeraid operates the SaaS.", 9)
add_text(s, 0.7, 2.7, 5.8, 3.2, "EMERAID SUPER ADMINISTRATOR\n\nInstitutions, licences, packs, platform connectors, core-banking provisioning. Multi-factor authentication and a full audit trail.", 16, INK, False, "Calibri")
add_text(s, 7.0, 2.7, 5.6, 3.2, "INSTITUTION ADMINISTRATOR\n\nTheir branches, staff, and local branding. They cannot see another institution or Emeraid’s platform credentials.", 16, INK, False, "Calibri")

# 10
s = prs.slides.add_slide(blank)
kicker_title(s, "Ownership", "Each domain has one\nsystem of record.", 10)
add_text(s, 0.7, 2.55, 12, 3.8, "Odoo masters  —  tenant, licence, packs, CRM, KYC, VSLA ceremony, PayGo devices, agency operations.\n\nFineract masters  —  loans, savings, balances, general ledger.\n\nFastAPI  —  mobile, USSD, payments, and OEM calls, posting money in Fineract.", 18, INK, False, "Calibri")

# 11
s = prs.slides.add_slide(blank)
kicker_title(s, "Security", "Controls sit on every path,\nnot only the server.", 11)
add_text(s, 0.7, 2.6, 3.8, 3.5, "ACCESS\n\nTLS, OpenID Connect, multi-factor authentication, tenant and branch scope, licence enforcement on the API.", 15, INK, False, "Calibri")
add_text(s, 4.8, 2.6, 3.8, 3.5, "MONEY\n\nFineract is the only ledger. Idempotent posting. Maker-checker. Fineract is not a public staff site.", 15, INK, False, "Calibri")
add_text(s, 8.9, 2.6, 3.8, 3.5, "OPERATIONS\n\nEncryption, NDPR, encrypted field store, audit, backup and restore, software bill of materials, penetration testing.", 15, INK, False, "Calibri")

# 12
s = prs.slides.add_slide(blank)
kicker_title(s, "Same environment", "Odoo and FastAPI are neighbours,\nnot one programme.", 12)
add_text(s, 0.7, 2.55, 2.8, 3.2, "NGINX\n\nTLS at the edge", 15, INK, False, "Calibri")
add_text(s, 3.7, 2.55, 2.8, 3.2, "/  →  ODOO\n\nStaff and System Administration", 15, INK, False, "Calibri")
add_text(s, 6.7, 2.55, 2.8, 3.2, "/API  →  FASTAPI\n\nApps, USSD, partners", 15, INK, False, "Calibri")
add_text(s, 9.7, 2.55, 2.9, 3.2, "FINERACT\n\nInternal core banking only", 15, INK, False, "Calibri")
add_text(s, 0.7, 5.7, 12, 1.0, "Each component keeps its own database. They integrate through APIs.", 16, MUTED, False, "Calibri")

# 13
s = prs.slides.add_slide(blank)
kicker_title(s, "Proposal", "This develops the architecture\nalready discussed.", 13)
add_text(s, 0.7, 2.6, 12, 3.6, "The 13 August 2026 financial proposal used an Odoo-only foundation for core banking. Using Apache Fineract keeps Odoo as the operating platform and avoids building that engine from scratch.\n\nIt changes delivery composition. Effort and commercial terms for the combined stack will be confirmed with Emeraid under change control.", 18, INK, False, "Calibri")

# 14
s = prs.slides.add_slide(blank)
paint_bg(s)
add_text(s, 0.7, 0.4, 12, 0.35, "SUMMARY", 13, GOLD, True, "Calibri")
add_text(s, 0.7, 1.3, 12, 2.2, "One platform.\nConfigurable packs.\nOne ledger.", 36, INK, False, "Georgia")
add_text(s, 0.7, 4.0, 11.5, 2.0, "Emeraid hosts EDFIP, onboards institutions, and licenses modules. Staff work in Odoo. Apache Fineract is the core banking engine. FastAPI, beside Odoo, is the path that moves money.", 18, MUTED, False, "Calibri")
footer(s, 14)

out = "/workspace/edfip-screening/architecture/EDFIP_Architecture_Dexta.pptx"
prs.save(out)
print("wrote", out)
