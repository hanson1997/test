# EDFIP proposed architecture

**Emeraid Digital Financial Inclusion Platform**  
Dexta Synergy Services  
Confidential — for Emeraid International Group Ltd

This note develops the Apache Fineract and Odoo architecture already shared for technical clarification. It describes how that design operates as a **multi-tenant software-as-a-service (SaaS) platform** that Emeraid will host, brand, and sell to institutions.

---

## 1. Position

EDFIP is one platform, hosted by Emeraid. Institutions — microfinance institutions, cooperatives, VSLA networks, NGOs, and green-asset / PayGo operators — are **onboarded as tenants**. Each tenant is licensed for the modules it has purchased. Staff work in **Odoo**. **Apache Fineract** is the core banking engine (loans, savings, balances, and the general ledger). A **FastAPI** service, running alongside Odoo in the same environment, is the path that posts money and serves mobile, USSD, and partner connections. **Flutter** provides the field and customer Android applications.

Emeraid does not install a separate copy of EDFIP at each institution as the standard product.

---

## 2. What SaaS means for EDFIP

| Practice | What it means in this design |
|---|---|
| One platform | Emeraid operates a single hosted environment. |
| Onboarding | An Emeraid Super Administrator creates the institution, branding, organisation, and first administrator in **System Administration**. |
| Licensing | The institution receives a **module pack** — a configurable set of capabilities. |
| Use | Institution staff log in and work only in the licensed portion of the platform. |
| Suspension | If a licence is not current, access can be locked while data is retained, and restored when the licence is current. |

Each institution’s data is isolated from every other institution.

---

## 3. Configurable module packs

Packs are how Emeraid sells the same platform as different products. They are assembled from a catalogue (for example CRM, core banking, VSLA, cooperatives, Green Asset Finance / PayGo, agency banking) as a named bundle or as selected modules. A pack can be changed later — for example adding PayGo during the life of a contract.

**Illustrative packs**

- **Microfinance pack** — CRM, core banking, agency banking, field application  
- **Cooperative pack** — CRM, share register, core banking  
- **VSLA network pack** — CRM, VSLA share-out, core banking  
- **PayGo / green-asset pack** — CRM, device-linked credit, OEM token workflow, core banking  

A module that is not licensed must be unavailable in the Odoo screens **and** through the public API. Otherwise the licence would not be effective.

---

## 4. Platform components

| Component | Role |
|---|---|
| **Odoo Community** | Operating system of EDFIP. Staff and Emeraid administrators work here: CRM, KYC, VSLA, cooperatives, PayGo operations, agency float, customer portal, and System Administration. |
| **Apache Fineract** | Core banking engine. Products, savings and loan accounts, schedules, repayments, balances, and the general ledger. Used through its documented APIs. The Mifos user applications are not part of this design. |
| **FastAPI service** | Integration and channel API. Runs as a separate process in the **same Emeraid environment** as Odoo. It is not an Odoo addon, and it is not placed in front of Odoo staff screens. |
| **Flutter** | Offline-capable field Android application and customer Android application. These applications call FastAPI only. |

**How people reach the platform**

- Institution and Emeraid staff open **Odoo**.  
- Field apps, customer apps, USSD, payment providers, and OEM callbacks use **FastAPI** (`/api`).  
- Fineract is not published as a staff website.

When a member of staff posts a repayment in Odoo, the Odoo server calls FastAPI; FastAPI posts to Fineract; Odoo then shows the confirmed result. Staff do not log into Fineract.

---

## 5. System Administration

System Administration is an Odoo application used only by Emeraid Super Administrators. It is the control plane for selling and operating EDFIP. It is not the institution’s day-to-day CRM.

| Role | Where they work | Responsibility |
|---|---|---|
| **Emeraid Super Administrator** | System Administration | Create and suspend institutions, licences, module packs, platform connectors (identity, SMS, payments, OEMs), and core-banking provisioning. |
| **Institution Administrator** | Institution Settings, inside their own tenant | Branches, staff, branch access, and local branding. They cannot see another institution or Emeraid’s platform credentials. |

**System Administration includes**

- Institutions  
- Licences (start and end dates; active, suspended, or expired)  
- Module catalogue and packs  
- Platform configuration  
- Provisioning history (creation of the matching Fineract tenant and offices)  
- A small set of Emeraid platform operators, with multi-factor authentication and a full audit trail  

Provisioning core banking does not write to Fineract databases from Odoo. Odoo requests FastAPI to create the Fineract tenant and offices and stores the confirmed identifiers.

Loan products, interest, and ledger accounts remain configured in Fineract (through controlled EDFIP screens that call FastAPI). System Administration decides **who is on the platform** and **what they are licensed to use**. Fineract decides **how money is calculated**.

---

## 6. Institution onboarding and branch access

Emeraid asked how an institution is onboarded and how staff inside that institution are limited to their branches. Both are configured in Odoo and enforced for money in Fineract.

**Onboarding sequence**

1. The Super Administrator creates the institution (name, type, branding, licence, module pack).  
2. The organisation is recorded: Head Office and branches.  
3. The Institution Administrator is invited (multi-factor authentication; no access to System Administration).  
4. FastAPI creates the Fineract tenant and an office for each branch.  
5. The Institution Administrator creates staff and assigns a role and one or more branches.  
6. FastAPI creates the corresponding Fineract user, bound to that office.  
7. Staff log into Odoo and see only their institution, their licensed modules, and their branches.

**Branch access** is applied in three places:

1. **Odoo** — records outside the assigned branches are not shown.  
2. **FastAPI** — the session carries the institution, branches, and licence; requests outside that scope are refused.  
3. **Fineract** — the user is bound to the mapped office, so loans, savings, and ledger postings cannot be placed in the wrong branch.

---

## 7. How money is posted

There is one core banking ledger: Fineract.

A financial instruction (disbursement, repayment, savings movement, VSLA posting, and similar) is accepted by FastAPI with an idempotency key, posted once in Fineract, and then reflected as status in Odoo. If the network fails after posting, the same key is retried; a second posting is not created. Operational screens may display balances; they do not keep a second set of books.

```
Staff, field app, USSD, or payment webhook
        →  FastAPI (identity, licence, branch, idempotency)
        →  Fineract posts the transaction and updates the ledger
        →  Odoo records the confirmed reference and status
        →  Receipt or notification
```

---

## 8. Data ownership

| Domain | System of record | Notes |
|---|---|---|
| Tenant, licence, module pack | Odoo System Administration | Mapped to a Fineract tenant |
| Branch structure | Odoo | Mapped to Fineract offices |
| Customer identity, KYC evidence, CRM | Odoo | Fineract holds the financial client reference |
| Core banking — loans, savings, general ledger | Fineract | Odoo displays confirmed figures |
| VSLA meetings and share-out ceremony | Odoo | Money movement posted in Fineract |
| Cooperative share register | Odoo | Accounts in Fineract |
| PayGo devices and OEM token workflow | Odoo / FastAPI | Eligibility and loan state in Fineract |
| Agency float operations | Odoo | Float accounts in Fineract |
| Field and customer Android | Flutter via FastAPI | Posting in Fineract |

---

## 9. Security

Security is applied on every layer of a hosted financial platform, not only at the server.

| Layer | Control |
|---|---|
| Network edge | TLS; rate limiting; Fineract not exposed as a public staff site |
| Identity | OpenID Connect; multi-factor authentication for administrators, finance users, and approval roles; short-lived tokens; device registration and revocation for field applications |
| Tenant isolation | One institution cannot read another — through the web, APIs, reports, field synchronisation, or restore |
| Branch isolation | As in section 6 |
| Licence | Unlicensed modules are unavailable in the interface and the API |
| Money path | Only FastAPI posts to Fineract; idempotency; maker-checker for sensitive operations |
| Data | Encryption in transit and at rest; protection of KYC and OEM credentials; NDPR |
| Field applications | Encrypted offline store; no silent duplicate repayment |
| Operations | Audit trail; backup and tested restore of Odoo, Fineract, and the integration store; software bill of materials; vulnerability scanning; independent penetration testing |

---

## 10. Principal processes

**Customer onboarding.** Odoo captures identity, documents, consent, and KYC. After approval, FastAPI creates the linked Fineract client. The customer belongs to an institution and a branch.

**Loan.** Appraisal and approval run in Odoo. FastAPI opens the loan in Fineract on the mapped office. The schedule and account identifier returned by Fineract are what the institution sees.

**Repayment.** Teller, agent, field app, USSD, or payment gateway submits one instruction. Fineract posts it. Odoo shows the confirmed receipt.

**VSLA share-out.** Meeting rules and the ceremony are in Odoo. Member-level money is posted through FastAPI to Fineract.

**PayGo token.** The asset and OEM relationship sit in Odoo. Fineract confirms loan and repayment eligibility. FastAPI calls the OEM. Token delivery is recorded in Odoo.

**Offline field repayment.** The application stores an encrypted event. On synchronisation, FastAPI rejects duplicates and posts once to Fineract.

---

## 11. Deployment

The solution runs on Emeraid’s approved hosting.

- Nginx terminates TLS: staff and System Administration on Odoo; `/api` on FastAPI.  
- Odoo, FastAPI, and Fineract are separate processes.  
- Each keeps its own logical database. Applications do not write to one another’s tables.  
- Identity is provided by an OpenID Connect service agreed at inception.  
- Monitoring, audit, and encrypted backup cover all stores.

Capacity can be increased later without changing these boundaries.

---

## 12. Evidence of a sound design

The architecture is accepted through demonstration, including:

- A single posting path for core banking, with no duplicate when a request is retried  
- Institution isolation across web, mobile, API, reporting, and restore  
- Unlicensed modules unavailable in both the interface and the API  
- Branch-scoped access for staff  
- Traceable identifiers between Odoo and Fineract  
- PayGo and VSLA money movement only after a confirmed Fineract state  
- Offline synchronisation without silent loss or duplication  
- Daily reconciliation on agreed test data  
- Backup, restore, and independent security testing  

---

## 13. Relationship to the 13 August 2026 proposal

The submitted financial proposal was prepared on an Odoo-only foundation for core banking. Using Apache Fineract as the core banking engine **preserves Odoo as the operating platform** and avoids building that engine from scratch. It is a development of the architecture already discussed with Emeraid.

It also changes delivery composition (an additional core banking service, integration, and dual-system operations). Effort and commercial terms for this stack will be confirmed with Emeraid under the engagement’s change-control process.

---

## 14. Summary

Emeraid hosts one EDFIP platform, onboards institutions, and sells configurable module packs. Staff work in Odoo. Apache Fineract is the core banking engine. FastAPI, running beside Odoo, is the path that moves money. There is one ledger, not two.
