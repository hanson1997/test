# Exact words — EDFIP presentation (for you only, not on screen)

Expand every abbreviation the first time you say it.

---

## Before you click slide 1

Do **not** say: we rushed; we would have used Fineract; Odoo already does microfinance; consortium is fine.

Do say: we read the Terms of Reference as a product company, not a one-off MFI build.

---

## Slide 1

Thank you for inviting Dexta Synergy Services. I am Hanson Eyuren, Lead Developer.

We understand that Emeraid is not procuring a basic microfinance application. You are procuring a commercialisable, multi-tenant Digital Financial Inclusion Operating System — EDFIP — that Emeraid will completely own, control, brand, and sell to third-party institutions: microfinance institutions, VSLAs, cooperatives, solar and PayGo providers, and agency banking networks.

Every architectural and commercial choice in our proposal follows directly from that reality.

---

## Slide 2 — Four commitments

Four commitments that matter to Emeraid.

One: full CRM in the first production release.

Two: Green Asset Finance and PayGo in the first release, with an Early Operational Release by Month 6.

Three: Emeraid’s ability to operate, modify, commercialise and maintain the platform independently.

Four: a realistic 12-month delivery plan with testing and acceptance evidence.

---

## Slide 3 — The platform specified

This is first-release scope from the Terms of Reference.

Green Asset Finance is still a loan — but it is a loan tied to a physical device, not a plain cash disbursement. The customer is financed for a solar home system, freezer, irrigation pump, mill, e-bike or similar. When they repay, the platform asks the OEM for an activation token that unlocks the device. If they stop paying, entitlement lapses.

Typical PayGo OEMs in Nigeria and comparable markets include Sun King (Greenlight Planet), Lumos, d.light and Arnergy. We do not assume which OEM is first. Emeraid will name that partner.

---

## Slide 4 — How SaaS works

**First release: one platform on Emeraid’s server.** You already provide hosting. An institution does not get a separate install. They get a **tenant** — a login, their logo, their products, their data walled off from every other institution.

Emeraid’s super-admin onboards them — a standard tenant in one working day — and **turns on the modules they licensed**.

What you charge an MFI — monthly, annual, per-module — is **your** commercial decision. The software is built so you can run it as Software as a Service. If a licence lapses, you can suspend access without deleting data.

The **₦70 million** is Emeraid paying us once to **build** the platform, plus twelve months warranty.

---

## Slide 5 — Three products, one platform

Odoo is modular. Same EDFIP. Three licence packs:

1. **Hope Microfinance** — full MFI suite.
2. **Rivers VSLA Network** — CRM, VSLA, donor reports only.
3. **GreenLight Solar** — CRM, loans, PayGo.

PayGo still needs clients, a loan engine, the ledger, and SMS. The sellable unit is a **tenant with a module pack**.

---

## Slide 6 — One ledger

One runtime, one database, one ledger.

Odoo Community 19 is the spine. Emeraid-owned modules are the MFI core. FastAPI sits **inside** Odoo as the API door. Flutter is the phones.

If collaboration with another firm comes up: we can add **capacity**. We will not add a **second book of account**.

---

## Slide 7 — What Odoo provides, and what we build

Odoo already gives CRM, double-entry ledger, users, customer web portal.

The loan engine, savings, VSLA, PayGo and agency banking we build as modules Emeraid owns. That is why twelve months is the right plan.

We have used this method before: USSD portals, bank compliance, a loan portal, and a field agent app that works offline and syncs when data returns.

---

## Slide 8 — Which tool

Walk the table. Flutter for the field. FastAPI for partners, payments and OEMs.

---

## Slide 9 — PayGo

A loan tied to a device. Customer pays. System computes days of use. Connector calls the OEM. Token goes out by SMS, agent app, customer app.

Month 6: early operational release. We need OEM documentation, sandbox or a live-test protocol, and a named technical contact by end of Month 3.

---

## Slide 10 — Offline

Works in the field with no network. Officers append events. They never edit a balance on the phone.

Customer self-service: Odoo web portal **and** Flutter Android app, both in first release.

---

## Slide 11 — Twelve months

Month 6 is PayGo early release, and 12% of the fee. Twelve months protects your acceptance gates.

---

## Slide 12 — Team

Hanson: technical authority. Alison: Flutter and QA. Daniel: project manager, full time. Rowland: security support.

If collaboration is discussed: one architecture, one ledger, one prime contractor.

---

## Slide 13 — Price

Seventy million naira excluding VAT. Seventy-five point two five million including VAT. Ten percent at inception. Twelve percent at Month 6 on PayGo. No hosting in the price.

---

## Slide 14 — Ownership

Operate, modify, extend, sell, onboard tenants. Repository is Emeraid’s from week one. Independent maintenance after handover.

---

## Slide 15

We welcome your questions.

If useful, ask: first OEM, payment gateway, and any collaboration model they wish to explore. Do not fill silence with more slides.
