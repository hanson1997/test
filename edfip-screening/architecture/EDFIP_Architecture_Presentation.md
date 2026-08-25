# EDFIP proposed architecture — slide copy

**Dexta Synergy Services** · Confidential — for Emeraid International Group Ltd

Present the PowerPoint: `EDFIP_Architecture_Dexta.pptx`.  
This file is the same 14 slides in Markdown. It develops the Apache Fineract and Odoo architecture already shared.

---

## Slide 1 / 14 — Proposed architecture

# One platform Emeraid hosts. Institutions are onboarded and licensed.

This walkthrough develops the Apache Fineract and Odoo architecture already shared. It shows how EDFIP operates as multi-tenant software-as-a-service that Emeraid will brand and sell.

---

## Slide 2 / 14 — Software as a service

# Emeraid does not install EDFIP at each institution.

1. **Host** — One platform on Emeraid’s environment.  
2. **Onboard** — Super Administrator creates the institution.  
3. **Licence** — The purchased module pack is switched on.  
4. **Use** — Staff work only in the licensed portion.

If a licence is not current, access can be locked and data retained. A very large institution may later receive a dedicated data store still hosted by Emeraid — not an on-premise install.

---

## Slide 3 / 14 — Configurable packs

# The same platform, sold as different products.

- **Microfinance** — CRM, core banking, agency, field app  
- **Cooperative** — CRM, share register, core banking  
- **VSLA network** — CRM, share-out, core banking  
- **PayGo / green asset** — CRM, device credit, OEM tokens  

Packs are assembled from a catalogue and can be changed during the contract. Unlicensed modules are unavailable in the screens and in the API.

---

## Slide 4 / 14 — Platform

# Four parts. One ledger.

- **Odoo** — Where people work: CRM, KYC, VSLA, cooperatives, PayGo, agency, System Administration.  
- **Apache Fineract** — Core banking: loans, savings, schedules, balances, general ledger. APIs only.  
- **FastAPI** — Channel and money path. Separate process, same environment as Odoo.  
- **Flutter** — Field Android (offline) and customer Android. Calls FastAPI only.

The Mifos user applications are not part of this design. Staff and field users work in Odoo and Flutter.

---

## Slide 5 / 14 — How people enter

# Staff open Odoo. Channels open the API.

- **Odoo** — Institution staff, Emeraid Super Administrators, customer web portal.  
- **FastAPI (`/api`)** — Flutter, USSD, payment providers, OEM callbacks, partner integrations.

Fineract is not a public staff website. When a teller posts a repayment in Odoo, the Odoo server calls FastAPI, which posts to Fineract.

---

## Slide 6 / 14 — How money moves

# Every naira is posted once, in Fineract.

Instruction → FastAPI (identity, licence, branch, idempotency) → Fineract posts and updates the ledger → Odoo shows confirmed status and receipt.

If the network fails after posting, the same key is retried. A second posting is not created.

---

## Slide 7 / 14 — Onboarding an institution

# From licence to a live tenant.

1. Super Administrator creates the institution, branding, and module pack.  
2. Head Office and branches are recorded.  
3. The Institution Administrator is invited.  
4. FastAPI creates the Fineract tenant and an office for each branch.  
5. Institution Administrator assigns staff to roles and branches. Staff log into Odoo.

---

## Slide 8 / 14 — Branch access

# Configured in Odoo. Enforced for money in Fineract.

- **Odoo** — A Garki officer does not see Wuse records.  
- **FastAPI** — A request for another branch is refused.  
- **Fineract** — Postings can only land in the mapped office.

Institution finance may see all branches of their own institution. They cannot see another tenant.

---

## Slide 9 / 14 — Control plane

# System Administration is how Emeraid operates the SaaS.

- **Emeraid Super Administrator** — Institutions, licences, packs, platform connectors, core-banking provisioning.  
- **Institution Administrator** — Their branches, staff, and local branding. They cannot see another institution or Emeraid’s platform credentials.

---

## Slide 10 / 14 — Ownership

# Each domain has one system of record.

- **Odoo** masters tenant, licence, packs, CRM, KYC, VSLA ceremony, PayGo devices, agency operations.  
- **Fineract** masters loans, savings, balances, general ledger.  
- **FastAPI** carries mobile, USSD, payments, and OEM calls, posting money in Fineract.

---

## Slide 11 / 14 — Security

# Controls sit on every path, not only the server.

- **Access** — TLS, OpenID Connect, multi-factor authentication, tenant and branch scope, licence enforcement on the API.  
- **Money** — Fineract is the only ledger. Idempotent posting. Maker-checker. Fineract is not a public staff site.  
- **Operations** — Encryption, NDPR, encrypted field store, audit, backup and restore, software bill of materials, penetration testing.

---

## Slide 12 / 14 — Same environment

# Odoo and FastAPI are neighbours, not one programme.

Nginx (TLS) → `/` to Odoo (staff and System Administration) → `/api` to FastAPI (apps, USSD, partners) → Fineract internal.

Each component keeps its own database. They integrate through APIs.

---

## Slide 13 / 14 — Proposal

# This develops the architecture already discussed.

The 13 August 2026 financial proposal used an Odoo-only foundation for core banking. Using Apache Fineract keeps Odoo as the operating platform and avoids building that engine from scratch.

It changes delivery composition. Effort and commercial terms for the combined stack will be confirmed with Emeraid under change control.

---

## Slide 14 / 14 — Summary

# One platform. Configurable packs. One ledger.

Emeraid hosts EDFIP, onboards institutions, and licenses modules. Staff work in Odoo. Apache Fineract is the core banking engine. FastAPI, beside Odoo, is the path that moves money.
