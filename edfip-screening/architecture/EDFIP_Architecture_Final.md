# EDFIP architecture — final position

**Dexta Synergy Services** · Prepared from Alison’s Fineract–Odoo draft, revised after the Emeraid screening  
**Status:** Proposed architecture  
**Confidential:** Emeraid / Dexta only

**How we sell it:** a commercialisable multi-tenant SaaS platform with a real money engine and a real control plane — not a one-off MFI install, and not core banking built from scratch in Odoo.

---

## Direct answer

Yes. **Apache Fineract (core banking) + Odoo (operating core) + FastAPI (sibling API) + Flutter (field and customer Android)** can deliver what Emeraid specified: full CRM, VSLA share-out, cooperative shares, PayGo OEM tokens, agency float, institution onboarding, branch-scoped staff access, and **sellable module packs**.

Odoo is not thrown away. Odoo is the product operators live in. Fineract is not the product UI. Fineract is the **core banking** engine. FastAPI is not inside Odoo and not in front of staff screens. Mifos X is not in this stack. Odoo + Flutter take the job Mifos used to do (human UI on Fineract).

| Layer | Role | Who touches it |
|---|---|---|
| **Apache Fineract** | Money core — **core banking** | Nobody via a staff UI. API only. Accounts, balances, schedules, GL. |
| **Odoo Community** | Operating core + **System Administration** | Staff web, CRM, KYC, VSLA, shares, PayGo, agency. Emeraid Super Admin onboards tenants. |
| **FastAPI** | Sibling API on the same environment | Flutter, USSD, partners, and Odoo’s server-side money/provisioning calls. |
| **Flutter** | Field + customer Android | Offline collections and self-service. Talks to FastAPI only. |

---

## SaaS multi-tenant — deploy once, onboard, licence

This is the commercial model. It is not optional colour on the diagram.

**Emeraid hosts one platform.** An MFI, cooperative, VSLA network, NGO, or PayGo operator does **not** get a separate EDFIP deployment as the normal product. You do not install Odoo and Fineract in each institution’s server room.

What happens:

1. Emeraid Super Admin creates the institution in **System Administration**.
2. Turns on the **pack they paid for** (configurable: bundle or à la carte).
3. Their staff log in and use **only that portion**.
4. FastAPI **refuses** APIs outside the licence. If the API still works, the licence is fake.
5. **Suspend** locks login and **keeps data**. **Restore** opens it again.

That is SaaS multi-tenant: one codebase, one hosted environment, many tenants, isolation by tenant, differentiation by licence.

**Later exception (still SaaS):** a very large institution may get a dedicated database (or dedicated Fineract tenant store) **on Emeraid’s hosting**. Emeraid still operates it. That is an isolation upgrade, not a different product and not an on-prem install.

### Configurable packs (sellable SKUs)

A pack is not a frozen DVD. Super Admin composes it from the catalogue and can change it later (add PayGo in month 8; turn off agency when the licence ends).

Examples:

- **MFI pack** — CRM + core banking + agency + field app  
- **Cooperative pack** — CRM + shares + core banking  
- **VSLA network pack** — CRM + VSLA share-out + core banking  
- **PayGo / green asset pack** — CRM + GAF/PayGo + OEM tokens + core banking  

Enforcement is in **three places**, or it is not a product:

| Place | What “licensed” means |
|---|---|
| **Odoo** | Menus and records for unlicensed modules are gone |
| **FastAPI** | Those routes return forbidden |
| **Fineract** | Products and offices for that tenant match the pack |

---

## What we kept from Alison, and what we changed

**Kept**

- Fineract is the only financial ledger. No parallel trial balance in Odoo.
- FastAPI does not write to Odoo or Fineract tables. It uses their APIs.
- Odoo does not post core banking transactions itself. Money goes FastAPI → Fineract.
- Idempotency, reconciliation, correlation IDs, separate logical stores.
- IPO as the way we explain each process.
- Security as a first-class design (OIDC/MFA, tenant/branch scope, TLS, webhooks, secrets, pentest, SBOM) — expanded below so it sits on every plane, not only a list at the back.

**Changed**

1. Staff live in **Odoo**, not behind FastAPI.
2. **System Administration** is the seller’s control plane (onboarding, licences, packs, platform config).
3. SaaS is stated plainly: **one host, onboard, licence** — not per-institution deploy.
4. Packs are **configurable and enforced**.
5. Branch access engine in Odoo, mapped to Fineract offices.
6. Flutter is named. Mifos UI is out.
7. Loans, savings, and GL are called **core banking**.
8. FastAPI is a **sibling process** on the same environment.
9. The August ₦70m offer was Odoo-only core banking; this stack is viable and the commercial number is re-estimated under change control (see Commercial note).

---

## TOR domains

| Emeraid domain | Where it lives | Naira / ledger |
|---|---|---|
| Multi-tenant SaaS, packs, suspend/restore | Odoo System Administration | Fineract tenant mapping |
| Clients, members, KYC | Odoo | Fineract client after approval |
| Full CRM | Odoo | — |
| **Core banking** (loans, savings, GL) | Odoo screens | **Fineract** |
| Cooperatives | Odoo register | Fineract accounts |
| VSLA share-out | Odoo ceremony | Fineract postings |
| GAF / PayGo + OEM tokens | Odoo + FastAPI OEM adapter | Fineract loan |
| Agency float | Odoo limits / till UX | Fineract GL |
| Payments, USSD | FastAPI + channels | Fineract posting |
| Notifications | Odoo | — |
| Donor / MIS reporting | Reporting layer | Both, labelled by source |
| Partner APIs | FastAPI OpenAPI | — |
| Field + customer Android | Flutter → FastAPI | Fineract via FastAPI |
| Customer web | Odoo portal | Odoo / FastAPI |

---

## System Administration (control plane)

Odoo app for **Emeraid Super Admins** only. It is how Emeraid sells and operates the platform. It is not the MFI’s CRM.

| Who | App | Job |
|---|---|---|
| **Emeraid Super Admin** | System Administration | Onboard institutions, licences, packs, global connectors, provision Fineract tenants |
| **Institution Admin** | Institution Settings (inside their tenant) | Branches, staff, branch access, local branding — never another institution, never platform SMS keys |

Menus: Institutions · Licences · Module catalogue · System configuration · Provisioning log · Platform operators (few people, MFA, full audit).

Institution form tabs: Identity · Branding · Licence · Modules · Organisation (HO + branches) · First Institution Admin · Provisioning.

Typical day: new institution → pick pack → add branches → invite their admin → **Provision core banking**. Odoo does not write Fineract tables. It asks FastAPI; FastAPI creates the Fineract tenant and offices; status goes Live.

**System configuration** (once for the platform): OIDC, MFA policy, SMS/email defaults, payment gateways FastAPI may call, OEM connectors, session policy, internal URLs. Fineract is not a public staff URL.

System Administration owns *who is on the platform* and *what they paid for*. Fineract still owns *how money calculates*.

---

## Institution onboarding and branch access

**Odoo owns the institution and the branch access engine. Fineract receives a matching office tree so core banking cannot leak across branches.**

```
1. Super Admin creates Institution (pack, branding, licence)
2. Org tree: Head Office → Branch A, Branch B
3. Invite Institution Admin (MFA; no System Administration)
4. FastAPI: Fineract tenant ↔ institution; Fineract office ↔ each branch
5. Institution Admin assigns staff: role + branch(es)
6. FastAPI creates Fineract user/staff locked to that office
7. Staff log into Odoo — only their branch
```

| Layer | Enforcement |
|---|---|
| **Odoo UI** | Record rules; other branches invisible |
| **FastAPI** | Token has `institution_id` + `branch_ids` + **licence flags**; out-of-scope calls rejected |
| **Fineract** | User bound to mapped **office**; postings cannot land in the wrong branch |

- Credit officer, Garki — Garki only.  
- Teller, Wuse — Wuse only.  
- Institution finance — all branches, one institution, never another tenant.  
- Super Admin — control plane only; not in the tenant’s customer book.

---

## Logical architecture

```
Channels
  Staff web ────────────────► Odoo (operating core + System Administration)
  Flutter field (offline)
  Flutter customer
  USSD / partners / OEM ────► FastAPI  (/api on the same Nginx)

Money and provisioning
  Odoo server or Flutter
        → FastAPI (licence, tenant, branch, idempotency, ID map)
        → Fineract (core banking)
        → confirmed txn id stored
        → Odoo operational status only

Identity
  OIDC · MFA · tenant + branch + licence claims
```

**Rules that do not move**

1. One hosted platform. Onboard tenants. Do not deploy a new EDFIP per institution (dedicated store later is still Emeraid-hosted).  
2. Fineract is the only core banking ledger.  
3. FastAPI never writes Odoo or Fineract tables.  
4. Odoo never posts repayment, disbursement, or GL itself.  
5. Flutter never talks to Fineract or SQL.  
6. One person: `res.partner` ↔ Fineract `clientId`.  
7. One org: Odoo branch ↔ Fineract office.  
8. Licence cuts UI **and** API.  
9. Interrupted money commands retry with the same idempotency key. Reconciliation reports unmatched rows.

---

## Components

### Odoo — operating core

System Administration; branch access engine; customer/KYC master; full CRM; VSLA share-out; cooperative shares; PayGo device/OEM workflow; agency float; notifications; portal. May **display** Fineract balances; may not **author** them.

### Apache Fineract — core banking

Products, financial clients, savings, loans, schedules, interest/fees as configured, disbursement, repayment, reversal, balances, GL, financial audit references. REST only. No Mifos web or Android.

### FastAPI — sibling process, same environment

Not an Odoo addon. Not a wall in front of staff screens.

```
Nginx (one Emeraid environment)
  /          → Odoo      staff, System Administration, CRM
  /api       → FastAPI   Flutter, USSD, partners, Odoo server-side calls
  Fineract   → internal only
```

Staff browser → Odoo. Flutter → FastAPI. When Odoo must move money or provision a tenant, the **Odoo server** calls FastAPI. FastAPI calls Fineract (and Odoo APIs for operational status).

Also: versioned OpenAPI, canonical IDs, idempotency, webhook verification, offline sync ingest, retries, reconciliation. It does not calculate interest or hold the GL.

### Flutter

Offline-first field app (encrypted outbox, sync, no silent duplicate). Customer Android. Device binding and remote revocation.

---

## Security — every plane, not a slide

Alison’s draft already required OIDC/MFA, tenant and branch scope, TLS, signed webhooks, secrets, field encryption, idempotency, audit, SBOM, SAST/DAST, pentest, device bind, encrypted offline store, and reconciliation. For a hosted SaaS that sells to institutions, that is the product bar. Security is a rule on every box.

| Plane | What must be true |
|---|---|
| **Edge** | HTTPS only. Rate limits. Fineract not on the public internet. |
| **Identity** | OIDC. MFA for Super Admin, institution admin, finance, approvals. Short-lived tokens. Flutter device revoke. |
| **Tenant** | Institution A cannot read B — web, API, reports, sync, backup restore. |
| **Branch** | Garki cannot post Wuse — Odoo + FastAPI + Fineract office. |
| **Licence** | Unpaid modules: no UI, no API. |
| **Money** | Only FastAPI posts to Fineract. Idempotency. Maker-checker. No dual GL. |
| **Data** | Encryption in transit and at rest. KYC and PayGo secrets. NDPR. |
| **Field** | Encrypted offline outbox. Zero silent double repayment. |
| **Supply chain** | SBOM, licence register, dependency scanning. |
| **Ops** | Immutable audit, SIEM path, DR, tested restore of Odoo + Fineract + integration store. Independent pentest. |

Scale is isolation tests, SLAs, DR, audit, CBN/NDPR as applicable, and pentest — not extra boxes. The structure can carry that. Shipping it is the delivery job.

---

## Critical flows (IPO)

### Tenant onboarding (SaaS)

| | |
|---|---|
| **Input** | Institution profile, configurable pack, branding, HO + branches, admin email, licence dates |
| **Process** | System Administration creates tenant; FastAPI provisions Fineract tenant/offices; licence flags on token |
| **Output** | Live tenant; staff see only licensed modules and their branches |

### Customer onboarding

| | |
|---|---|
| **Input** | Bio-data, IDs, documents, consent, institution + branch |
| **Process** | Odoo KYC and duplicates; FastAPI external customer ID; Fineract client |
| **Output** | Approved customer, linked IDs, branch-scoped |

### Core banking — loan

| | |
|---|---|
| **Input** | Application, product, amount, tenor, appraisal, branch |
| **Process** | Odoo workflow; FastAPI creates Fineract loan on mapped office |
| **Output** | Account ID, schedule; Odoo shows confirmed reference |

### Repayment

| | |
|---|---|
| **Input** | Amount, account, channel, idempotency ID |
| **Process** | FastAPI posts once to Fineract; Odoo status; receipt |
| **Output** | Confirmed txn, balance, reconciliation row |

### VSLA share-out

| | |
|---|---|
| **Input** | Cycle, attendance, shares, fines, social fund |
| **Process** | Ceremony in Odoo; money commands through FastAPI |
| **Output** | Meeting in Odoo; Fineract postings; discrepancy case if needed |

### PayGo OEM token

| | |
|---|---|
| **Input** | Customer, asset, device, loan, repayment event |
| **Process** | Fineract eligibility; FastAPI OEM call; Odoo token state |
| **Output** | Token, delivery status, exception queue |

### Offline field repayment

| | |
|---|---|
| **Input** | Encrypted local event, device, user, unique event ID |
| **Process** | Sync → FastAPI dedupe → Fineract post → Odoo confirmed |
| **Output** | Accepted, rejected, or pending — no silent loss, no double post |

### Licence change

| | |
|---|---|
| **Input** | Add/remove module, new dates, Super Admin action |
| **Process** | Licence record updated; Odoo menus; FastAPI flags; Fineract products aligned |
| **Output** | Institution uses the new pack only; unlicensed APIs forbidden |

---

## Deployment (logical)

Same Emeraid-hosted environment. One platform for all tenants. Odoo and FastAPI are neighbours, not one process.

- Nginx / TLS (`/` → Odoo, `/api` → FastAPI)  
- OIDC  
- Odoo (System Administration + operating apps)  
- FastAPI (own process)  
- Fineract (JVM, internal)  
- PostgreSQL with **separate logical databases** (Odoo; Fineract if the chosen version supports it; integration store). A large tenant may later get a dedicated store, still on this hosting.  
- Queue + Redis  
- Monitoring, audit, encrypted backup of all three stores  

Scale-out does not change ownership: APIs only, one ledger.

---

## Acceptance evidence

- One Fineract posting path; retry does not double-post  
- Institution A cannot see B (web, Flutter, API, reports, sync, restore)  
- Unlicensed module: no Odoo UI **and** FastAPI forbidden  
- Branch A cannot read or post Branch B  
- IDs traceable: partner, Fineract client, branch, office  
- VSLA share-out and PayGo token only after confirmed Fineract state  
- Offline sync: zero loss, zero duplicate  
- Daily reconciliation: unexplained variance = 0 on agreed test data  
- Pentest, SBOM, backup/restore of all stores  

---

## Commercial note — re-baseline the ₦70m

This does **not** mean the architecture is wrong. It does **not** mean a new figure must be invented on the next call.

The 13 August proposal priced **Option E: build core banking inside Odoo**. This architecture is a different job: still build the Odoo product (System Administration, CRM, VSLA, PayGo, Flutter) **and** run Fineract plus FastAPI mapping and reconciliation.

Some “write a loan engine in Odoo” days go away. New integration and dual-runtime ops days appear. Net is unknown until re-estimated. That re-estimate is a revised commercial annex under change control — not a handshake that ₦70m still binds Odoo-only scope.

If asked: *the technical path is this stack; the August figure was for Odoo-only core banking and will be revised formally.* Do not volunteer a replacement price until Fineract version and product mapping are scoped.

We do not need a team to **build** core banking. We need someone who can run Fineract and consume its API, plus the Odoo/Flutter team already proposed.

---

## One sentence for Emeraid

> Emeraid hosts one EDFIP platform, onboards institutions, and sells them configurable packs. Staff work in Odoo — System Administration for Emeraid, CRM, VSLA, cooperatives, PayGo, and agency for the tenant. Apache Fineract is the core banking engine. FastAPI, running beside Odoo, is the only path that moves money, so there is one ledger, not two.
