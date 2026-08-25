# EDFIP proposed architecture — slide copy

**Dexta Synergy Services** · Confidential — for Emeraid International Group Ltd

Present the PowerPoint: `EDFIP_Architecture_Dexta.pptx`.  
This file is the same 16 slides in Markdown.

---

## Slide 1 / 16 — Proposed architecture

# One platform Emeraid hosts. Institutions are onboarded and licensed.

This document sets out how EDFIP operates as multi-tenant software-as-a-service that Emeraid will host, brand, and sell.

---

## Slide 2 / 16 — Software as a service

# Emeraid does not install EDFIP at each institution.

1. **Host** — One platform on Emeraid’s environment.  
2. **Onboard** — Super Administrator creates the institution.  
3. **Licence** — The purchased module pack is switched on.  
4. **Use** — Staff work only in the licensed portion.

If a licence is not current, access can be locked and data retained, then restored when the licence is current.

---

## Slide 3 / 16 — Configurable packs

# The same platform, sold as different products.

- **Microfinance** — CRM, core banking, agency, field app  
- **Cooperative** — CRM, share register, core banking  
- **VSLA network** — CRM, share-out, core banking  
- **PayGo / green asset** — CRM, device credit, OEM tokens  

Packs are assembled from a catalogue and can be changed during the contract. Unlicensed modules are unavailable in the screens and in the API.

---

## Slide 4 / 16 — Platform

# Four parts. One ledger.

- **Odoo** — Where people work: CRM, KYC, VSLA, cooperatives, PayGo, agency, System Administration.  
- **Apache Fineract** — Core banking: loans, savings, schedules, balances, general ledger. APIs only.  
- **FastAPI** — Channel and money path. Separate process, same environment as Odoo.  
- **Flutter** — Field Android (offline) and customer Android. Calls FastAPI only.

The Mifos user applications are not part of this design. Staff and field users work in Odoo and Flutter.

---

## Slide 5 / 16 — How people enter

# Staff open Odoo. Channels open the API.

- **Odoo** — Institution staff, Emeraid Super Administrators, customer web portal.  
- **FastAPI (`/api`)** — Flutter, USSD, payment providers, OEM callbacks, partner integrations.

Fineract is not a public staff website. Customers use the portal or the customer app. Staff post work on the operating platform; money is confirmed in core banking.

---

## Slide 6 / 16 — How money moves

# Every naira is posted once, in core banking.

Instruction → integration service (who is acting, licence, branch) → core banking posts and updates the ledger → operating platform shows the receipt to staff and, where appropriate, to the customer.

If the network fails after posting, the same instruction is retried. A second posting is not created.

---

## Slide 7 / 16 — Onboarding an institution

# From licence to a live institution.

1. Super Administrator creates the institution, branding, and module pack.  
2. Head Office and branches are recorded. The institution’s administrator is invited.  
3. Core banking is prepared for that institution, with a matching office for each branch.  
4. Staff are given roles and branches. They sign in and see only their institution and those branches.

---

## Slide 8 / 16 — Branch access

# Staff see their branch. Money can only post there.

- **Operating platform** — A Garki officer does not see Wuse customers.  
- **Integration service** — A request for another branch is refused.  
- **Core banking** — Postings can only land in the matching branch.

Institution finance may see all branches of their own institution. They cannot see another institution.

---

## Slide 9 / 16 — Customers

# A customer belongs to the institution, a branch, and an officer.

1. **Record** — Opened at a branch and assigned to an account officer.  
2. **KYC** — Approved on the operating platform.  
3. **Core banking** — The same person is opened at that branch.  
4. **Account** — Savings or loan is created in core banking.

The customer application and portal show only that person’s accounts. Other institutions never see them.

---

## Slide 10 / 16 — Customers

# The record and the accounts are linked. They are not two people.

- **Operating platform** — Name, KYC, documents, CRM, home branch, account officer. What staff use every day.  
- **Core banking** — Savings and loan accounts, balances, repayment schedule, ledger. The money.

One customer number on both sides. The officer sees their portfolio. The customer sees only themselves.

---

## Slide 11 / 16 — Control plane

# System Administration is how Emeraid operates the SaaS.

- **Emeraid Super Administrator** — Institutions, licences, packs, platform connectors, core-banking provisioning.  
- **Institution Administrator** — Their branches, staff, and local branding. They cannot see another institution or Emeraid’s platform credentials.

---

## Slide 12 / 16 — Ownership

# Each domain has one system of record.

- **Operating platform** — institution, licence, packs, CRM, KYC, customer record, branch, account officer, VSLA ceremony, PayGo devices, agency operations.  
- **Core banking** — savings and loan accounts, balances, general ledger.  
- **Integration service** — field app, customer app, USSD, payments, and OEM calls, posting money in core banking.

---

## Slide 13 / 16 — Security

# Controls sit on every path, not only the server.

- **Access** — TLS, OpenID Connect, multi-factor authentication, tenant and branch scope, licence enforcement on the API.  
- **Money** — Fineract is the only ledger. Idempotent posting. Maker-checker. Fineract is not a public staff site.  
- **Operations** — Encryption, NDPR, encrypted field store, audit, backup and restore, software bill of materials, penetration testing.

---

## Slide 14 / 16 — Same environment

# Odoo and FastAPI are neighbours, not one programme.

Nginx (TLS) → `/` to Odoo (staff and System Administration) → `/api` to FastAPI (apps, USSD, partners) → Fineract internal.

Each component keeps its own database. They integrate through APIs.

---

## Slide 15 / 16 — Foundation

# Odoo remains the operating platform. Fineract provides core banking.

The 13 August 2026 financial proposal assumed an Odoo-only foundation for core banking. This architecture uses Apache Fineract for core banking so that Odoo remains the operating platform, rather than building that engine from scratch.

The combined stack changes delivery composition. Effort and commercial terms will be confirmed under the engagement’s change-control process.

---

## Slide 16 / 16 — Summary

# One platform. Configurable packs. One ledger.

Emeraid hosts EDFIP, onboards institutions, and licenses modules. Staff and customers use the operating platform and the apps. Core banking holds the accounts. There is one customer, one set of accounts, and one ledger.
