# Exact words — EDFIP screening

Expand every abbreviation the first time you say it.

---

## Before you click slide 1

Do **not** say: we rushed; we would have used Fineract; Odoo already does microfinance; consortium is fine.

Do say: we read the Terms of Reference as a product company, not a one-off MFI build.

---

## Slide 1 — You are not buying a microfinance app

Thank you for shortlisting Dexta Synergy Services. I am Hanson Eyuren, Lead Developer, and Emeraid’s single technical point of contact.

You are not buying a microfinance app. You are building a product company. We are here to put the operating system underneath it.

Twelve minutes on what you are buying, how you will sell it, how we build it. Then we want the points from your assessment.

---

## Slide 2 — Commercial operating system

EDFIP — Emeraid Digital Financial Inclusion Platform — is a multi-tenant operating system Emeraid will own, brand, price, and sell to:

- MFIs — Microfinance Institutions
- cooperatives
- VSLA networks — Village Savings and Loan Associations
- NGOs — Non-Governmental Organisations
- DFIs — Development Finance Institutions
- green-asset operators

If we only talk features, we miss why you wrote the TOR — Terms of Reference.

---

## Slide 3 — Two deal-breakers

The TOR is explicit. If either of these slips to phase two, the bid is non-responsive.

One: full CRM — Customer Relationship Management. Leads, visits, complaints, campaigns. Not a registration screen.

Two: Green Asset Finance and PayGo — Pay-As-You-Go. The customer pays, the solar home system, freezer, or pump unlocks. Plus an early operational slice before full go-live.

Evaluation weights: PayGo fifteen points, CRM fifteen, architecture fifteen.

Also mandatory: Android field app with real offline, and customer self-service on both web and Android.

---

## Slide 4 — How SaaS actually works *(they will lean in)*

This is the question: do we deploy on every client’s server, or one cloud Emeraid controls?

**First release: one platform on Emeraid’s server.** You already provide hosting. An institution does not get a separate install. They get a **tenant** — a login, their logo, their products, their data walled off from every other institution.

Emeraid’s super-admin onboards them — TOR says a standard tenant in one working day — and **turns on the modules they licensed**.

**Buying, for your customers, can be recurring.** The platform stores plan, module set, user limits, billing status. If they stop paying you, you **suspend** the tenant: login locked, data kept, switch back on when the licence is current. That is not a wipe.

What you charge an MFI — monthly, annual, per-module — is **your** commercial decision. The software is built so you can run it as Software as a Service.

The **₦70 million** is different. That is Emeraid paying **us** once, to **build** the platform, plus twelve months warranty. Automated invoices from EDFIP to your tenants is extra — ₦1.4 million — because the TOR marked that Desirable.

Later, if a very large client demands their own database, we can export that tenant. That is an escape hatch, not day one. Day one is one control plane.

---

## Slide 5 — Three products, one platform *(mind-blow slide)*

Odoo is modular. That matches TOR MT-04.

Same EDFIP. Three licences:

1. **Hope Microfinance** — full MFI suite. CRM, loans, savings, general ledger, agency, payments, PayGo. VSLA off.
2. **Rivers VSLA Network** — only CRM, VSLA meetings and share-out, donor reports. They should not pay for agency banking.
3. **GreenLight Solar** — CRM, loans, ledger, PayGo tokens and SMS. No VSLA.

Be precise, because they will test you: **PayGo is not a satellite with zero dependencies.** A green operator still needs clients, a loan engine, the ledger, and SMS. The sellable unit is a **tenant with a module pack**, not fourteen disconnected apps.

That is how you licence just what a company needs, and still stay scalable: new institution = configuration, not a new deployment project.

---

## Slide 6 — One ledger

One runtime, one database, one ledger.

Odoo Community 19 is the spine. Emeraid-owned modules are the MFI core. FastAPI sits **inside** Odoo as the API door — Odoo’s built-in XML-RPC does not meet your security and documentation rules. Flutter is the phones.

Nothing writes to PostgreSQL except through Odoo. Tenant isolation is enforced once, including mobile sync.

If collaboration with another shortlisted firm comes up: we can add **capacity**. We will not add a **second book of account**.

---

## Slide 7 — Odoo is not magic

We would rather be believed on the hard parts.

Odoo already gives CRM, double-entry ledger, users, customer web portal.

Odoo does **not** give loans, savings, VSLA, PayGo, or agency float. Those we build as modules Emeraid owns. About one hundred mandatory items. That is why twelve months, not nine.

We have used this method before: USSD portals, bank compliance and internal control, fraud and NFIU-style case and alert work, a loan portal, and a field agent app that works offline and syncs when data returns. That proves **method**. It does not mean EDFIP already exists.

---

## Slide 8 — Which tool

Walk the table. Stop on Flutter: Odoo’s own mobile app needs a network. The village does not. Stop on FastAPI: partners, Paystack, OEMs, USSD.

Why not Fineract as the foundation? Strong loans. **Zero CRM** — and CRM is fifteen points. Thin Java/Fineract talent in Nigeria for handover. A Fineract-plus-Odoo hybrid is two ledgers. Daily zero-variance between sub-ledger and general ledger dies on that seam. We chose the stack this named team can leave you with.

---

## Slide 9 — PayGo

A loan tied to a device. Customer pays. System computes days of use. Connector calls the OEM — Original Equipment Manufacturer. Token goes out by SMS, agent app, customer app.

If the OEM API is down: authorised staff type a token from the OEM portal, flagged as manual, maker-checker, full audit.

New OEM: new small module. No change to core.

Month 6: early operational release — registry, asset-linked loan, first connector, token request, delivery, audit. Not final acceptance. Proof this is not a phase-two slide.

We need from you by end of Month 3: API docs **with error codes**, sandbox or a live-test protocol, named OEM technical contact.

---

## Slide 10 — Offline

The meeting under the tree still counts.

Officers append events. They never edit a balance on the phone. Unique ID on every capture so a retry cannot post twice.

Sync starts Months 2–3, not at the end.

Customer self-service: Odoo web portal **and** Flutter Android app, both in first release.

---

## Slide 11 — Twelve months

Finger on Month 6. That is PayGo early release, and 12% of the fee.

We declined nine months. Compressing your acceptance gates — financial correctness pack, penetration test, zero-loss sync, migration sign-off — would weaken them.

---

## Slide 12 — Team

Hanson is **one** technical authority, not four full-time engineers.

Alison: Flutter and QA, including the offline field loan app.

Daniel: project manager, full time on this.

Rowland: security second pair of eyes.

About 3.36 full-time equivalents, which matches 840 person-days over twelve months. If you award, we can add engineers **under this architecture**.

Consortium: bounded extra capacity, one ledger, one prime contractor. We will not merge cores on this call.

---

## Slide 13 — Price

Seventy million naira excluding VAT. Seventy-five point two five million including VAT.

Ten percent at inception — below your fifteen percent cap.

Twelve percent at Month 6 on PayGo — we get paid when you can see tokens.

No hosting in the price.

Five assumptions we already priced: Flutter for the customer app; your Appendix E server size; one OEM; one payment gateway, Paystack until you name one; automated tenant invoicing extra.

---

## Slide 14 — You end free

Operate, modify, extend, sell, onboard tenants, replace us.

Git is Emeraid’s from week one.

No Odoo Enterprise. No paid App Store. Licence register on every commit. CI fails the build if an AGPL module enters the graph.

At acceptance your staff deploy a release from the runbook without us on the call.

---

## Slide 15 — Stop

We would like your assessment points.

Then ask, if they have not said:

- Who is in the room on your side?
- Have you named the first OEM and the payment gateway?
- Is this conversation scored under Section 44, or is it a new stage?
- If collaboration is live: who would be prime, and who would own the general ledger?

Do not fill silence with more slides.
