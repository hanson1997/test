# EDFIP architecture — final position

**Dexta Synergy Services** · Prepared from Alison’s Fineract–Odoo draft, revised after the Emeraid screening  
**Status:** Proposed architecture (not a discussion sketch)  
**Confidential:** Emeraid / Dexta only

---

## Direct answer

Yes. **Apache Fineract (core banking) + Odoo (operating core) + FastAPI (orchestration / REST) + Flutter (field and customer Android)** can deliver what Emeraid specified in the TOR — including full CRM, VSLA share-out, cooperative shares, PayGo OEM tokens, agency float, institution onboarding, and **branch-scoped staff access**.

Odoo is not thrown away. Odoo remains the product operators live in. Fineract is not the product UI. Fineract is the **core banking** engine so we do not build loans, savings, interest, and the general ledger from scratch.

| Layer | Role | What Emeraid’s people touch |
|---|---|---|
| **Apache Fineract** | Money core — **core banking** | Nobody, except through APIs. System of record for accounts, balances, schedules, postings, GL. |
| **Odoo Community** | Operating core | Staff web: CRM, KYC, institution admin, branches, VSLA, coop shares, PayGo/OEM, agency float, portal. |
| **FastAPI** | EDFIP API and orchestration | Not a third bank. Maps IDs, idempotent money commands, webhooks, offline sync, partner REST. |
| **Flutter** | Field app + customer Android | Offline collections, customer self-service. Talks to FastAPI, not to Fineract tables. |

Mifos X is **not** in this stack. Mifos was the staff/field UI on Fineract. **Odoo + Flutter take that job.**

---

## What we kept from Alison, and what we changed

Alison’s draft is the right engine split and the right integration rules. This final version keeps that, and tightens three things Emeraid already asked about.

**Kept**

- Fineract is the only financial ledger. No parallel trial balance in Odoo.
- FastAPI does not write to Odoo or Fineract tables. It uses their APIs.
- Odoo does not post core banking transactions itself. Money goes FastAPI → Fineract.
- Idempotency, reconciliation, correlation IDs, separate logical databases.
- IPO (input–process–output) as the way we explain each process.

**Changed for the final architecture**

1. **Staff live in Odoo, not behind FastAPI.** Alison’s drawing put FastAPI in front of everything. That would make FastAPI the product. The product is Odoo. FastAPI is the money/channel spine. Staff open Odoo. Flutter, USSD, and partners open FastAPI.
2. **Institution onboarding and the branch access engine are first-class Odoo capabilities**, then mapped to Fineract offices. This is the answer to Emeraid’s onboarding / branch-access question.
3. **Flutter is named.** Field offline app and customer Android replace Mifos mobile apps.
4. **Language:** loans, savings, and GL are **core banking** (Fineract). VSLA share-out, coop shares, PayGo tokens, and agency float stay in Odoo as operating workflows, with naira posted in Fineract.
5. This is the architecture we are proposing. Price and timeline still need a formal re-baseline versus the Odoo-only ₦70m proposal — that change is real, and we say so.

---

## Can this achieve what Emeraid wants?

Yes, if the ownership rules below are kept. Mapping to the TOR domains:

| Emeraid domain | Where it lives | Naira / ledger |
|---|---|---|
| Multi-tenant SaaS, module packs, suspend/restore | Odoo tenant control plane | Fineract tenant created and mapped |
| Clients, members, KYC | Odoo | Fineract client created after approval |
| Full CRM | Odoo | — |
| **Core banking** (loans, savings, GL) | Odoo screens (read/command) | **Fineract** |
| Cooperatives (shares, governance, dividends) | Odoo | Fineract accounts / share accounts |
| VSLA (meetings, share-out ceremony) | Odoo | Fineract postings |
| Green Asset Finance / PayGo + OEM tokens | Odoo (device, OEM, token) | Fineract loan |
| Agency float, tills, commissions | Odoo (float engine, limits) | Fineract GL / float account |
| Payments, collections, USSD | FastAPI + channels | Fineract posting |
| Notifications | Odoo | — |
| Donor / MIS reporting | Reporting layer | Fineract + Odoo, labelled by source |
| Partner APIs | FastAPI OpenAPI | — |
| Field offline + customer Android | Flutter | via FastAPI |
| Customer web | Odoo portal | via Odoo / FastAPI |

We are not building a core banking engine in Python. We are not running Mifos as a second staff UI. We are not dual-writing two general ledgers.

---

## Institution onboarding and branch access

This is the question Emeraid asked. The answer is: **Odoo owns the institution and the branch access engine. Fineract receives a matching office tree so core banking cannot leak across branches.**

### What an “institution” is

One Emeraid-hosted platform. Each MFI, cooperative, VSLA network, NGO, or PayGo operator is a **tenant** (institution). They do not get a separate install. Emeraid super-admin onboards them, turns on the licensed module pack, and can suspend login without deleting data.

### Onboarding sequence

```
1. Emeraid super-admin creates the Institution in Odoo
     name, type, branding, module pack, licence dates
2. Odoo creates the org tree
     Head Office → Branch A, Branch B, …
3. Odoo creates the Institution Admin user
     all branches, admin roles, MFA
4. FastAPI provisions core banking
     Fineract tenant  ↔  Odoo institution
     Fineract office  ↔  each Odoo branch (same hierarchy)
5. Institution Admin creates staff in Odoo
     role + one or more branches
6. FastAPI creates the Fineract user/staff
     office = home branch; restricted to that office tree
7. Staff log into Odoo
     they only see their branch’s customers, loans, tills, groups
```

### Branch access engine (Odoo)

This is a real access model, not a slogan.

- Every staff user belongs to **one institution**.
- Every staff user is assigned **one or more branches**, plus a role (credit, teller, CRM, finance, institution admin).
- Institution admin / finance can be granted **all branches**.
- Odoo **record rules** hide other branches in CRM, KYC, VSLA groups, PayGo assets, agency tills, and operational dashboards.
- Maker-checker and segregation of duties stay on the role, still inside the branch scope.

### Why Fineract still gets offices

Odoo hiding a menu is not enough for core banking. FastAPI and Fineract must enforce the same rule:

| Layer | What it enforces |
|---|---|
| **Odoo UI** | Staff cannot open another branch’s records |
| **FastAPI** | Token carries `institution_id` + `branch_ids`. A Flutter or partner call for another branch is rejected |
| **Fineract** | User/staff is bound to the mapped **office**. Loan, savings, and GL postings cannot land in the wrong office |

That three-layer check is the branch access engine. Odoo is the place it is configured. Fineract is the backstop for money.

### What staff actually do

- **Credit officer, Branch A** — sees Branch A pipeline and portfolio; originates loans that FastAPI opens on Fineract office A.
- **Teller, Branch B** — till and cash movements for Branch B only.
- **Institution finance** — all branches, still one institution; cannot see another tenant.
- **Emeraid super-admin** — onboards/suspends institutions; does not sit in the tenant’s customer book.

---

## Logical architecture

```
Channels
  Staff web ───────────────► Odoo (operating core)
  Flutter field (offline)
  Flutter customer
  USSD / partners / OEM ───► FastAPI (EDFIP API)

Money path (always)
  Odoo or Flutter or USSD
        → FastAPI (idempotency, ID map, tenant/branch scope)
        → Fineract (core banking: post, balance, GL)
        → FastAPI stores confirmed txn id
        → Odoo updates operational status only

Identity
  OIDC (Keycloak or Emeraid-approved) · MFA · tenant + branch claims
```

**Rules that do not move**

1. Fineract is the only core banking ledger.
2. FastAPI never writes Odoo or Fineract tables.
3. Odoo never posts a loan repayment, disbursement, or GL entry itself.
4. Flutter never talks to Fineract or to SQL.
5. One person: `res.partner` ↔ Fineract `clientId`.
6. One org: Odoo branch ↔ Fineract office.
7. Interrupted money commands retry with the same idempotency key. Reconciliation reports unmatched rows; nothing is silently overwritten.

---

## Component responsibilities

### Odoo — operating core

- Tenant (institution) administration, module packs, branding, suspend/restore  
- Branch access engine  
- Customer/member master, KYC evidence, full CRM  
- VSLA cycles and share-out ceremony  
- Cooperative share register, governance, dividend workflow  
- Green-asset registry, installation, OEM token orchestration  
- Agency float, limits, commissions, till UX  
- Notifications, customer portal, operational dashboards  
- May **display** Fineract balances; may not **author** them  

### Apache Fineract — core banking (money core)

- Products, clients (financial reference), savings, loans, schedules  
- Interest, fees, penalties as configured  
- Disbursement, repayment, reversal  
- Balances, transaction history, GL, financial audit references  

Fineract is API-first. We consume the REST API. We do not ship Mifos web or Mifos Android. Any true product gap is a controlled Fineract extension or an approved workflow — not a second ledger in Odoo.

### FastAPI — orchestration, not a bank

- Versioned EDFIP REST/OpenAPI for Flutter, USSD, partners  
- Canonical IDs: Odoo ↔ Fineract  
- Idempotent financial commands  
- Webhook verification (payments, OEM)  
- Offline sync ingest for the field app  
- Command state, retries, dead-letter, reconciliation queue  

### Flutter — field and customer

- Offline-first field app: encrypted local outbox, sync, conflict/duplicate rules  
- Customer Android self-service  
- Device binding and remote revocation  

---

## Critical flows (IPO)

### Institution onboarding

| | |
|---|---|
| **Input** | Institution profile, module pack, branding, Head Office + branches, admin user |
| **Process** | Odoo creates tenant and org tree; FastAPI maps Fineract tenant + offices; admin assigns staff/branches |
| **Output** | Live tenant, matching Fineract offices, staff who can only see their branches |

### Customer onboarding

| | |
|---|---|
| **Input** | Bio-data, IDs, documents, consent, institution + branch |
| **Process** | Odoo KYC and duplicates; FastAPI assigns external customer ID; Fineract client created |
| **Output** | Approved customer, linked Odoo/Fineract IDs, branch-scoped |

### Core banking — loan

| | |
|---|---|
| **Input** | Application, product, amount, tenor, appraisal, branch |
| **Process** | Odoo workflow and limits; FastAPI creates Fineract loan on the mapped office |
| **Output** | Account ID, schedule, audit; Odoo shows confirmed reference |

### Repayment

| | |
|---|---|
| **Input** | Amount, account, channel, event/idempotency ID |
| **Process** | FastAPI posts once to Fineract; Odoo updates status; receipt/notification |
| **Output** | Confirmed txn, balance, receipt, reconciliation row |

### VSLA share-out

| | |
|---|---|
| **Input** | Cycle, attendance, shares, fines, social fund |
| **Process** | Ceremony and rules in Odoo; member-level money commands through FastAPI |
| **Output** | Meeting record in Odoo; Fineract postings; discrepancy case if cash ≠ books |

### PayGo OEM token

| | |
|---|---|
| **Input** | Customer, asset, device, loan, repayment event |
| **Process** | Fineract confirms eligibility; FastAPI calls OEM; Odoo stores token state |
| **Output** | Token, delivery status, device state, exception queue |

### Offline field repayment

| | |
|---|---|
| **Input** | Encrypted local event, device, user, timestamp, unique event ID |
| **Process** | Sync → FastAPI dedupe → Fineract post → Odoo confirmed status |
| **Output** | Accepted, rejected, or pending — no silent loss, no double post |

---

## Deployment (logical)

Same Emeraid-hosted environment as the TOR. Processes stay separate even if they share a host at the start.

- Nginx / TLS edge  
- OIDC provider  
- Odoo  
- Fineract (JVM)  
- FastAPI  
- PostgreSQL with **separate logical databases** (Odoo, Fineract if the chosen Fineract version supports it, integration store)  
- Queue + Redis  
- Monitoring, audit, encrypted backup of all three stores  

Scale-out later does not change ownership: Odoo, Fineract, and FastAPI remain separate systems talking over APIs.

---

## Acceptance evidence (architecture)

- One Fineract posting path for core banking; retry does not double-post  
- Odoo partner, Fineract client, and branch/office IDs traceable  
- Institution A cannot see Institution B (web, Flutter, API, reports, sync)  
- Branch A officer cannot read or post Branch B  
- VSLA share-out and PayGo token only after confirmed Fineract state  
- Offline sync: zero loss, zero duplicate  
- Daily reconciliation: operational projections vs Fineract, unexplained variance = 0 on agreed test data  

---

## Commercial note

This is an architectural change from the submitted Odoo-only foundation. It does **not** throw Odoo away. It does add a JVM core banking service, an integration spine, and reconciliation evidence.

The ₦70,000,000 proposal should be **re-baselined** under change control if Emeraid adopts this stack: Fineract deploy/upgrade skill, integration test load, and dual-runtime operations.

We still do **not** need a team to *build* core banking. We need one person who can run Fineract and consume its API, plus the Odoo/Flutter team we already proposed.

---

## One sentence for Emeraid

> EDFIP is an Odoo operating system — institution onboarding, branch access, CRM, VSLA, cooperatives, PayGo, and agency — with Apache Fineract as the core banking engine and FastAPI as the only path that moves money, so there is one ledger, not two.
