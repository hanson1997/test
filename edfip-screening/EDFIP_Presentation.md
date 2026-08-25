# EDFIP — Emeraid Digital Financial Inclusion Platform

**Dexta Synergy Services** · Hanson Eyuren, Lead Developer

Exact slide copy from the presentation (15 slides).  
Present the PowerPoint in the meeting: `EDFIP_Screening_Dexta.pptx`. This file is the same content in Markdown.

---

## Slide 1 / 15 — How we read the assignment

# We understand the product Emeraid is building.

Not a basic microfinance application. A commercialisable, multi-tenant Digital Financial Inclusion Operating System — EDFIP — that Emeraid will own, control, brand and sell to third-party institutions. Every architectural and commercial choice in our proposal follows from that reality.

- Microfinance institutions
- Cooperatives
- VSLA networks
- NGOs and programmes
- Solar / PayGo operators
- Agency banking networks

*Dexta Synergy Services · Hanson Eyuren*

---

## Slide 2 / 15 — What this engagement must protect

# Four commitments that matter to Emeraid.

- **Full CRM** in the first production release — the complete relationship, not a registration screen.
- **Green Asset Finance and PayGo** in the first release, with an Early Operational Release by Month 6.
- Emeraid’s ability to **operate, modify, commercialise and maintain** the platform independently.
- A realistic **12-month delivery plan** with testing and acceptance evidence.

---

## Slide 3 / 15 — First-release scope

# The platform Emeraid specified.

### Operate
- Multi-tenant SaaS Emeraid can sell
- Clients, members and KYC
- Full CRM
- Roles, maker-checker and audit

### Lend and save
- Loan management
- Savings, including esusu / ajo
- Accounting and general ledger
- Cooperatives and VSLA groups

### Differentiate
- Green Asset Finance and PayGo
- Device-linked credit, not cash-only loans
- Agency banking and tellering
- Digital payments and collections

PayGo: repay → unlock solar, freezer, pump via the OEM

### Reach the field
- Offline-first Android field app
- Customer self-service — web and Android
- Notifications — SMS, email, in-app

### Prove and connect
- Dashboards, donor and project reporting
- Partner APIs and integrations
- Data migration and first-tenant setup

*One platform · modules licensed per institution*

---

## Slide 4 / 15 — Multi-tenant Software as a Service

# One control plane. Emeraid onboards. Modules switch on.

### First release
One platform on **Emeraid’s server**. Institutions get a login. No separate install per client.

### What they buy from you
A **module pack** — CRM only, VSLA only, full MFI, or PayGo operator. You turn it on in the super-admin console.

### If a licence lapses
The institution can be **suspended**: access locked, data retained, restored when the licence is current.

*A dedicated database remains available later for a large institution, if required*

---

## Slide 5 / 15 — How Emeraid licences the product

# Same platform. Three different products.

### Hope Microfinance — MFI full suite
Annual licence · all modules

| Module | Licensed |
|---|---|
| CRM | On |
| Loans + savings + GL | On |
| Agency + payments | On |
| PayGo | On |
| VSLA | Off |

### Rivers VSLA Network — Programme pack
CRM + VSLA + reports only

| Module | Licensed |
|---|---|
| CRM | On |
| VSLA meetings + share-out | On |
| Reports / donor | On |
| Loans / agency / PayGo | Off |

### GreenLight Solar — Green operator
PayGo + lending + CRM

| Module | Licensed |
|---|---|
| CRM + clients | On |
| Loans + GL | On |
| PayGo tokens + SMS | On |
| VSLA / cooperative | Off |

*Each institution is licensed only for the modules it needs*

---

## Slide 6 / 15 — Architecture

# One runtime. One database. One ledger.

| Layer | What it is | Why |
|---|---|---|
| Odoo Community 19 | Spine: CRM, general ledger, users, portal, companies | Native where Odoo is already strong |
| Emeraid-owned modules | Loans, savings, VSLA, cooperatives, PayGo, agency | Purpose-built for EDFIP — not available in Odoo as an MFI core |
| FastAPI inside Odoo | Public API, webhooks, mobile sync | Meets the TOR security, versioning and documentation standard |
| Flutter | Field Android app + customer Android app | Encrypted offline store. Odoo’s own app needs a network. |

*Nothing writes to PostgreSQL except through Odoo. Isolation is enforced once.*

---

## Slide 7 / 15 — Implementation approach

# What the foundation provides — and what we build.

### Odoo already gives
- CRM pipeline, activities, campaigns
- Double-entry ledger (posted journals cannot be deleted)
- Users, record rules, customer web portal
- Payment-provider hook, documents, jobs

### We build as Emeraid modules
- Loan engine, PAR, restructuring
- Savings, esusu/ajo, fixed deposits
- VSLA meetings and share-out
- PayGo tokens and OEM connectors
- Agency float, teller, offline sync

*The financial core is custom-built for Emeraid and owned by Emeraid*

---

## Slide 8 / 15 — Odoo · FastAPI · Flutter

# Which tool carries which problem.

| Problem | Tool |
|---|---|
| Sell one platform to many institutions; turn modules on/off | Odoo + custom tenant module |
| Leads, pipeline, campaigns | Odoo CRM |
| Complaints with SLA, client 360 with loans | Custom Odoo |
| Official books of account | Odoo accounting |
| Loans, savings, VSLA, PayGo, agent float | Custom Odoo (Python) |
| Village work with no network | Flutter |
| Paystack, OEMs, USSD, partners talking in | FastAPI |
| Customer balance on the web | Odoo portal |
| Customer balance on a phone | Flutter |

*FastAPI and Flutter never hold a second ledger*

---

## Slide 9 / 15 — Green Asset Finance · Pay-As-You-Go

# Repayment becomes light.

**Customer pays → Days of use earned → OEM connector → Token → SMS / agent / customer app**

### First release
Asset registry, device IDs, one live OEM, eligibility engine, audit trail, ownership transfer when the loan is finished.

### Month 6 — early operational release
Registry, asset-linked loan, first connector, token request, delivery and audit — in a controlled operational environment, ahead of full go-live.

*Connector built against a stub so an OEM delay cannot stall engineering*

---

## Slide 10 / 15 — Field operations

# Works in the field with no network.

- Loan officer, CRM officer, VSLA facilitator, agent — full workflow with **no network**.
- Money is **append-only**. No edited balances on the phone. No silent duplicates.
- Sync slice starts in **Month 2–3**, not at the end. Tests run on every merge.

*Customer self-service: Odoo web portal AND Flutter Android app, both in first release*

---

## Slide 11 / 15 — Twelve months to acceptance

# PayGo is on the clock, not at the end.

| When | What Emeraid can already see |
|---|---|
| Month 1 | Architecture, screens, licence register, server check, OEM checklist |
| Months 2–3 | Tenants, clients, roles, ledger spine, first sync slice |
| Months 4–6 | Loans, savings, teller · **PayGo early operational release** |
| Months 6–8 | Cooperatives, VSLA, full CRM |
| Months 8–11 | Agency, payments, APIs, mobile, security and UAT |
| Month 12 | Migration, go-live, training, handover — then 30 days hypercare |

*Plus 12 months warranty included*

---

## Slide 12 / 15 — Who does the work

# One technical authority. A named delivery team.

### Hanson Eyuren
Lead Developer. Architecture, financial core, API, PayGo, payments, USSD. Single point of accountability. Production Odoo today. Prior: bank USSD portals, compliance / NFIU-style controls, loan portal.

### Dexta Synergy Services
- **Eyuren Alison** — Flutter field + customer apps, offline sync client, QA.
- **Daniel Azu** — project manager, 100% on EDFIP.
- **Rowland Lawson** — security review support.

*Contracting entity: Dexta Synergy Services · RC 7377341*

---

## Slide 13 / 15 — Financial proposal

# ₦70m

Mandatory scope, excluding VAT. ₦75.25m including VAT. 840 person-days. 12 months. Warranty included.

### Inception
10% at accepted D1. Below the 15% ceiling.

### PayGo at Month 6
12% on accepted Deliverable 5 — payment follows a working PayGo release.

### No hosting in the price
Emeraid’s server. We install, harden, hand over.

*Valid 90 days from 13 August 2026*

---

## Slide 14 / 15 — Ownership and handover

# Emeraid owns the platform — and can run it independently.

- Free to **operate, modify, extend, sell, onboard tenants**.
- Source repository is **Emeraid’s from day one**. Independent maintenance after handover.
- No Odoo Enterprise. No paid App Store. Licence register regenerated on every commit.

*Acceptance includes a live restore and a deploy by Emeraid staff*

---

## Slide 15 / 15 — Thank you

# We welcome your questions.

Architecture, PayGo, CRM, delivery capacity, commercial terms, and any collaboration model you wish to explore.

**Hanson Eyuren · 08106248715 · Dexta Synergy Services**
