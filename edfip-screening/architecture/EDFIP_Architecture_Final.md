# EDFIP proposed architecture

**Emeraid Digital Financial Inclusion Platform**  
Dexta Synergy Services  
Confidential — for Emeraid International Group Ltd

This document sets out the proposed EDFIP architecture. Apache Fineract is the core banking engine. Odoo is the operating platform. Emeraid hosts, brands, and sells the system to institutions as **multi-tenant software-as-a-service**.

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
- History of preparing core banking for each institution  
- A small set of Emeraid platform operators, with multi-factor authentication and a full audit trail  

Provisioning does not write into core banking tables from Odoo. The operating platform asks the integration service to prepare core banking for that institution and its branches, then stores the confirmed references.

Loan products, interest, and ledger accounts remain in core banking, reached through controlled EDFIP screens. System Administration decides **who is on the platform** and **what they are licensed to use**. Core banking decides **how money is calculated**.

---

## 6. Institution onboarding and branch access

An institution is created in System Administration. Staff inside that institution are limited to the branches they are assigned. Organisation and access are configured on the operating platform (Odoo). Money movement is enforced in core banking (Fineract).

**Bringing an institution live**

1. An Emeraid Super Administrator creates the institution: name, type, branding, licence, and module pack.  
2. Head Office and branches are recorded.  
3. The institution’s own administrator is invited, with multi-factor authentication. That person manages their institution only — not Emeraid’s control of the platform.  
4. Core banking is prepared for that institution, with a branch office that matches each branch on the operating platform.  
5. The institution’s administrator creates staff and assigns each person a role and one or more branches.  
6. Those staff are also recognised in core banking at the matching branch, so they can only post money where they are allowed.  
7. Staff sign in to the operating platform and see only their institution, the modules they are licensed to use, and their branches.

**Branch access** is applied in three places:

1. **Operating platform** — records outside the assigned branches are not shown.  
2. **Integration service** — a session that is not authorised for a branch cannot act on it.  
3. **Core banking** — postings can only land in the matching branch.

---

## 7. Customers of an institution

EDFIP is not only a staff system. Each institution serves **customers** (members, clients, borrowers) — the people who hold savings, loans, and, where licensed, PayGo devices. The pattern is the same as a bank: the person belongs to the institution, is served from a **home branch**, and is assigned an **account officer**. Accounts then sit under that person.

**One person, two kinds of record**

| | Operating platform (Odoo) | Core banking (Fineract) |
|---|---|---|
| **Customer record** | Master: name, contacts, KYC, documents, CRM, complaints, home branch, account officer | A matching customer is opened so accounts can exist |
| **Accounts** | Staff and the customer **see** confirmed balances and status | Master: savings, loans, schedule, balance, ledger |
| **Customer app and portal** | Sign-in and profile | Show that customer’s own accounts; take repayment instructions |

The integration service keeps one customer number on both sides. There is not a second, disconnected customer book.

**How a customer is opened**

1. At a branch, staff capture the person: identity, contact, consent, and KYC. The record is placed in **this institution**, at **this branch**, and assigned to an **account officer**.  
2. KYC and approval are completed on the operating platform.  
3. The integration service opens the same person in core banking, at the same branch, with the same officer.  
4. When a savings account or loan is opened, it is created **in core banking** against that customer. The operating platform shows the confirmed account. The customer sees it on the app or portal.  
5. The account officer sees their portfolio. Other branches of the same institution do not see that customer unless they are authorised. Other institutions never do.  
6. On the customer application or web portal, the person sees **only their own** record and accounts.

A repayment, disbursement, or savings movement is posted against that account in core banking. The operating platform records the confirmed receipt. The officer’s dashboard and the customer’s app both read the same result.

---

## 8. How money is posted

There is one core banking ledger: Fineract.

A financial instruction (disbursement, repayment, savings movement, VSLA posting, and similar) is accepted by the integration service, posted **once** in core banking, and then shown as status on the operating platform. If the network fails after posting, the same instruction is retried; a second posting is not created. Operational screens may display balances; they do not keep a second set of books.

```
Staff, field app, customer app, USSD, or payment
        →  Integration service (who is acting, licence, branch)
        →  Core banking posts the transaction and updates the ledger
        →  Operating platform records the confirmed reference
        →  Receipt to staff and, where appropriate, to the customer
```

---

## 9. Data ownership

| Domain | System of record | Notes |
|---|---|---|
| Tenant, licence, module pack | Odoo System Administration | Mapped to a Fineract tenant |
| Branch structure | Odoo | Mapped to Fineract offices |
| Customer record, KYC, CRM, home branch, account officer | Operating platform (Odoo) | Matching customer in core banking |
| Savings and loan accounts, balances, schedules | Core banking (Fineract) | Operating platform and customer app display confirmed figures |
| VSLA meetings and share-out ceremony | Odoo | Money movement posted in Fineract |
| Cooperative share register | Odoo | Accounts in Fineract |
| PayGo devices and OEM token workflow | Odoo / FastAPI | Eligibility and loan state in Fineract |
| Agency float operations | Odoo | Float accounts in Fineract |
| Field and customer Android | Flutter via FastAPI | Posting in Fineract |

---

## 10. Security

Security is applied on every layer of a hosted financial platform, not only at the server.

| Layer | Control |
|---|---|
| Network edge | TLS; rate limiting; Fineract not exposed as a public staff site |
| Identity | OpenID Connect; multi-factor authentication for administrators, finance users, and approval roles; short-lived tokens; device registration and revocation for field applications |
| Tenant isolation | One institution cannot read another — through the web, APIs, reports, field synchronisation, or restore |
| Branch isolation | As in section 6. Customers are visible in their home branch and to their officer. |
| Licence | Unlicensed modules are unavailable in the interface and the API |
| Money path | Only the integration service posts to core banking; duplicate requests are not posted twice; maker-checker for sensitive operations |
| Data | Encryption in transit and at rest; protection of KYC and OEM credentials; NDPR |
| Field applications | Encrypted offline store; no silent duplicate repayment |
| Operations | Audit trail; backup and tested restore of Odoo, Fineract, and the integration store; software bill of materials; vulnerability scanning; independent penetration testing |

---

## 11. Principal processes

**Customer.** As in section 7: record and officer on the operating platform; accounts in core banking; customer app shows only that person’s accounts.

**Loan.** Appraisal and approval run on the operating platform. The loan is opened in core banking at the customer’s branch. The schedule returned by core banking is what staff and the customer see.

**Repayment.** Teller, account officer, field app, customer app, USSD, or payment gateway submits one instruction. Core banking posts it. The operating platform shows the confirmed receipt.

**VSLA share-out.** Meeting rules and the ceremony are on the operating platform. Member-level money is posted in core banking.

**PayGo token.** The asset sits on the operating platform. Core banking confirms loan and repayment eligibility. The integration service calls the OEM. Token delivery is recorded on the operating platform.

**Offline field repayment.** The field application stores an encrypted event. On synchronisation, duplicates are rejected and core banking is posted once.

---

## 12. Deployment

The solution runs on Emeraid’s approved hosting.

- Nginx terminates TLS: staff and System Administration on Odoo; `/api` on FastAPI.  
- Odoo, FastAPI, and Fineract are separate processes.  
- Each keeps its own logical database. Applications do not write to one another’s tables.  
- Identity is provided by an OpenID Connect service agreed at inception.  
- Monitoring, audit, and encrypted backup cover all stores.

Capacity can be increased later without changing these boundaries.

---

## 13. Evidence of a sound design

The architecture is accepted through demonstration, including:

- A single posting path for core banking, with no duplicate when a request is retried  
- Staff and customers cannot see another institution’s records (web, mobile, API, reporting, and restore)  
- A customer is visible to their branch and account officer; unlicensed modules are unavailable  
- One customer number links the operating platform and core banking  
- The customer application shows only that customer’s accounts  
- PayGo and VSLA money movement only after confirmed core banking state  
- Offline synchronisation without silent loss or duplication  
- Daily reconciliation on agreed test data  
- Backup, restore, and independent security testing  

---

## 14. Foundation for core banking

The 13 August 2026 financial proposal assumed an Odoo-only foundation for core banking. This architecture uses Apache Fineract for core banking so that Odoo remains the operating platform, rather than building that engine from scratch.

The combined stack changes delivery composition: an additional core banking service, integration, and operations across both systems. Effort and commercial terms will be confirmed under the engagement’s change-control process.

---

## 15. Summary

Emeraid hosts one EDFIP platform, onboards institutions, and sells configurable module packs. Staff and customers work through the operating platform and the customer applications. Apache Fineract is the core banking engine. The integration service, running beside Odoo, is the path that moves money. There is one customer, one set of accounts, and one ledger.
