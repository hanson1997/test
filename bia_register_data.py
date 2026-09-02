"""Technical Department BIA register row data."""

ROWS = [
    {
        "activity": "Requirements & Solution Design",
        "risk": (
            "Incorrect or incomplete requirements and design decisions, "
            "resulting in a solution that does not meet business needs, "
            "is insecure, or does not scale"
        ),
        "r1d": "2 - Minor",
        "d1w": (
            "Proposal/design timeline is now client-visible. Business Development "
            "cannot lock scope or commit dates. Catch-up pressure raises the chance "
            "of an incomplete, insecure, or non-scaling design being signed off."
        ),
        "r1w": "3 - Moderate",
        "client": (
            "Indirect — new and expanding client proposals delayed. No impact on "
            "live production for existing accounts."
        ),
        "overall": "3 - Moderate",
        "mtpd": 336,
        "rto": 48,
        "rpo": "N/A",
    },
    {
        "activity": "Application Development (Coding)",
        "risk": (
            "Bugs, security vulnerabilities, weak access controls, or data "
            "leakage introduced during coding"
        ),
        "r1d": "2 - Minor",
        "d1w": (
            "Sprint/feature work is a week behind. Client-promised development "
            "dates are missed or at risk. Rushing to recover increases defect "
            "and vulnerability risk."
        ),
        "r1w": "3 - Moderate",
        "client": (
            "Active implementation clients see delayed features/fixes. Live "
            "service usually remains up."
        ),
        "overall": "3 - Moderate",
        "mtpd": 336,
        "rto": 48,
        "rpo": "1 business day",
    },
    {
        "activity": "Source Code & Version Control",
        "risk": (
            "Unauthorized or untraceable code changes, loss of code, or "
            "approval of changes without proper segregation of duties"
        ),
        "r1d": "3 - Moderate",
        "d1w": (
            "No trusted source of truth for a week. Local copies diverge, "
            "merges become high-risk, and releases cannot be made safely. "
            "Lost or untraceable changes are a material risk."
        ),
        "r1w": "4 - Major",
        "client": (
            "Client releases freeze. Committed deliveries cannot be shipped "
            "until the repository is restored and reconciled."
        ),
        "overall": "4 - Major",
        "mtpd": 120,
        "rto": 8,
        "rpo": "15 minutes",
    },
    {
        "activity": "Code Review",
        "risk": (
            "Inadequate review allowing defects, vulnerabilities, or "
            "self-approved changes to reach production"
        ),
        "r1d": "2 - Minor",
        "d1w": (
            "Review queue is a week deep. Releases stall, or reviews are skipped "
            "to hit a date — allowing defects, vulnerabilities, or self-approved "
            "changes toward production."
        ),
        "r1w": "3 - Moderate",
        "client": (
            "Indirect — delivery dates slip, or quality/security risk rises if "
            "reviews are bypassed to keep a client date."
        ),
        "overall": "3 - Moderate",
        "mtpd": 336,
        "rto": 48,
        "rpo": "N/A",
    },
    {
        "activity": "Testing & Quality Assurance",
        "risk": (
            "Inadequate test coverage resulting in undetected defects or "
            "untested functionality reaching production"
        ),
        "r1d": "2 - Minor",
        "d1w": (
            "Release confidence is gone. Fixed client go-live dates (often "
            "month-end or quarter-end) force a choice between slipping the date "
            "or shipping untested functionality. Production defects become likely."
        ),
        "r1w": "4 - Major",
        "client": (
            "Go-live and enhancement dates are missed, or delivered with untested "
            "risk so issues surface in the client environment."
        ),
        "overall": "4 - Major",
        "mtpd": 120,
        "rto": 24,
        "rpo": "N/A",
    },
    {
        "activity": "Build Management",
        "risk": (
            "Compromised or inconsistent builds resulting from unauthorized "
            "changes or vulnerable dependencies"
        ),
        "r1d": "2 - Minor",
        "d1w": (
            "No reliable, authorised build can be produced. Releases are blocked "
            "or assembled manually from uncontrolled artefacts, raising the chance "
            "of compromised or inconsistent packages."
        ),
        "r1w": "4 - Major",
        "client": (
            "Planned client releases cannot be built and shipped; delivery dates slip."
        ),
        "overall": "4 - Major",
        "mtpd": 120,
        "rto": 24,
        "rpo": "1 business day",
    },
    {
        "activity": "CI/CD Pipeline Management",
        "risk": (
            "Unauthorized or unapproved deployments resulting from "
            "misconfigured pipelines or bypassed controls"
        ),
        "r1d": "3 - Moderate",
        "d1w": (
            "The automated path to production is down for a week. The team relies "
            "on manual builds/deployments, increasing unauthorised-change and error "
            "risk. Release throughput collapses."
        ),
        "r1w": "4 - Major",
        "client": (
            "Client releases are delayed or delivered via higher-risk manual deployments."
        ),
        "overall": "4 - Major",
        "mtpd": 120,
        "rto": 8,
        "rpo": "1 hour",
    },
    {
        "activity": "Release Deployment (Execution)",
        "risk": (
            "System outages, data corruption, or unauthorized changes from "
            "inadequately tested or controlled deployments"
        ),
        "r1d": "3 - Moderate",
        "d1w": (
            "Client-promised features/fixes remain unshipped for a week. Follow-ups "
            "escalate and dates must be re-planned. If a delayed deployment is then "
            "rushed, outage and data-corruption risk rises."
        ),
        "r1w": "4 - Major",
        "client": (
            "Missed committed delivery; client follow-up and commercial pressure. "
            "Live service usually continues unless the release was a production fix."
        ),
        "overall": "4 - Major",
        "mtpd": 120,
        "rto": 8,
        "rpo": "N/A",
    },
    {
        "activity": "Database & Data Structure Management",
        "risk": (
            "Data loss, corruption, or unauthorized access resulting from "
            "poorly controlled database changes"
        ),
        "r1d": "3 - Moderate",
        "d1w": (
            "Pending schema or data fixes remain unapplied. During month-end/"
            "quarter-end reporting, client data issues persist. Integrity, "
            "access-control, and recovery risk compound."
        ),
        "r1w": "4 - Major",
        "client": (
            "Client operations and financial reporting can be wrong or blocked "
            "if a data/schema issue is open. Highest sensitivity at close."
        ),
        "overall": "4 - Major",
        "mtpd": 72,
        "rto": 4,
        "rpo": "15 minutes",
    },
    {
        "activity": "Third-Party & Dependency Management",
        "risk": (
            "Vulnerable, malicious, or non-compliant dependencies introduced "
            "into the codebase"
        ),
        "r1d": "1 - Insignificant",
        "d1w": (
            "Dependency and licence work is a week behind. A delayed critical "
            "security patch leaves a known exposure open; year-end or anniversary "
            "renewals may lapse."
        ),
        "r1w": "3 - Moderate",
        "client": (
            "No direct service impact unless a vulnerable component is already in "
            "a client-facing system and a patch was pending."
        ),
        "overall": "3 - Moderate",
        "mtpd": 336,
        "rto": 48,
        "rpo": "N/A",
    },
    {
        "activity": "Security & Access Configuration",
        "risk": (
            "Credential compromise, unauthorized access, or unremediated "
            "security vulnerabilities"
        ),
        "r1d": "3 - Moderate",
        "d1w": (
            "Departed staff may still hold access; new staff remain blocked. "
            "Unremediated vulnerabilities and credential issues persist, raising "
            "the chance of unauthorised access."
        ),
        "r1w": "4 - Major",
        "client": (
            "Indirect but serious — stale or excessive access to client systems "
            "and data; new joiners who support clients cannot work."
        ),
        "overall": "4 - Major",
        "mtpd": 120,
        "rto": 24,
        "rpo": "1 business day",
    },
    {
        "activity": "Environment Management",
        "risk": (
            "Production data exposure or misconfiguration resulting from "
            "poorly controlled environments"
        ),
        "r1d": "2 - Minor",
        "d1w": (
            "Test/staging environments remain unavailable or misaligned. The next "
            "release cannot be validated; pressure grows to test in production or "
            "skip testing."
        ),
        "r1w": "3 - Moderate",
        "client": (
            "Next client release delayed. Risk of production-data exposure if "
            "environment controls are bypassed to keep a date."
        ),
        "overall": "3 - Moderate",
        "mtpd": 336,
        "rto": 48,
        "rpo": "1 business day",
    },
    {
        "activity": "Data Handling & ETL",
        "risk": (
            "Data leakage, corruption, or privacy violations during the "
            "movement of data"
        ),
        "r1d": "3 - Moderate",
        "d1w": (
            "Client reports and dashboards are a week stale or wrong. During "
            "month-end/quarter-end close this becomes a client-facing reporting "
            "failure and a possible SLA issue."
        ),
        "r1w": "4 - Major",
        "client": (
            "Clients making financial or operational decisions on outdated or "
            "incorrect data. Acute during close."
        ),
        "overall": "4 - Major",
        "mtpd": 72,
        "rto": 8,
        "rpo": "1 hour",
    },
    {
        "activity": "Production Support & Troubleshooting",
        "risk": (
            "Unauthorized production changes or service disruption from "
            "inadequately controlled support activities"
        ),
        "r1d": "4 - Major",
        "d1w": (
            "Clients cannot get production issues resolved for a week. "
            "Business-critical faults persist, escalations peak, and SLA breach "
            "plus reputational damage are likely; contract risk follows."
        ),
        "r1w": "5 - Critical",
        "client": (
            "Direct — live client operations disrupted without technical support. "
            "Highest exposure for accounts running critical reports at close."
        ),
        "overall": "5 - Critical",
        "mtpd": 72,
        "rto": 4,
        "rpo": "1 hour",
    },
    {
        "activity": "Access & Account Management",
        "risk": (
            "Excessive privileges or unauthorized access resulting from "
            "poorly managed accounts"
        ),
        "r1d": "3 - Moderate",
        "d1w": (
            "Joiner/leaver backlog is a week old. Departed staff retain accounts; "
            "new staff and client-support joiners cannot access systems. "
            "Segregation-of-duties and excessive-privilege risk grows."
        ),
        "r1w": "4 - Major",
        "client": (
            "Indirect — unauthorised access path to client environments; staff "
            "who serve clients cannot log in."
        ),
        "overall": "4 - Major",
        "mtpd": 120,
        "rto": 24,
        "rpo": "1 business day",
    },
    {
        "activity": "Release Management",
        "risk": (
            "Unauthorized or inadequately validated releases reaching production"
        ),
        "r1d": "3 - Moderate",
        "d1w": (
            "Client-communicated release dates are missed and must be re-negotiated. "
            "Coordination is lost — either an unvalidated release reaches production, "
            "or all releases freeze."
        ),
        "r1w": "4 - Major",
        "client": (
            "Missed agreed release date; requires formal client notification and "
            "re-scheduling. Live service usually continues."
        ),
        "overall": "4 - Major",
        "mtpd": 120,
        "rto": 48,
        "rpo": "N/A",
    },
    {
        "activity": "Cloud Infrastructure Management",
        "risk": (
            "Exposed systems, excessive privileges, or unexpected costs from "
            "misconfigured cloud infrastructure"
        ),
        "r1d": "2 - Minor",
        "d1w": (
            "Scaling, security-group, or cost issues remain unaddressed for a week. "
            "Exposure, outage under load, or uncontrolled cloud spend becomes "
            "realistic; production may still be running on an unmanaged footing."
        ),
        "r1w": "4 - Major",
        "client": (
            "Potential service degradation or outage if capacity or security issues "
            "were pending; otherwise no immediate client symptom."
        ),
        "overall": "4 - Major",
        "mtpd": 120,
        "rto": 8,
        "rpo": "1 hour",
    },
    {
        "activity": "Logging & Monitoring",
        "risk": (
            "Insufficient monitoring, sensitive data in logs, or loss of audit evidence"
        ),
        "r1d": "3 - Moderate",
        "d1w": (
            "A week-long observability gap. Incidents are noticed only when a client "
            "reports them, delaying response. Audit/forensic evidence for that window "
            "may be gone."
        ),
        "r1w": "4 - Major",
        "client": (
            "Issues reach the client before the team. Slower incident response and "
            "weaker investigation after the fact."
        ),
        "overall": "4 - Major",
        "mtpd": 120,
        "rto": 8,
        "rpo": "15 minutes",
    },
    {
        "activity": "Incident Management",
        "risk": (
            "Recurrence of incidents resulting from inadequate root-cause "
            "analysis or bypassed change controls"
        ),
        "r1d": "4 - Major",
        "d1w": (
            "Contractual SLA breach; reputational damage; possible contract "
            "termination. Recurring incidents remain unaddressed because root-cause "
            "analysis and controlled recovery never complete."
        ),
        "r1w": "5 - Critical",
        "client": (
            "Direct and severe — prolonged or repeated outage on live client systems; "
            "commercial and relationship failure risk."
        ),
        "overall": "5 - Critical",
        "mtpd": 72,
        "rto": 4,
        "rpo": "15 minutes",
    },
    {
        "activity": "Decommissioning",
        "risk": (
            "Loss of required records or residual access resulting from "
            "incomplete decommissioning"
        ),
        "r1d": "1 - Insignificant",
        "d1w": (
            "Retirement work stays incomplete. Residual access and unnecessary cost "
            "continue on the system being retired; required records may not have "
            "been retained."
        ),
        "r1w": "2 - Minor",
        "client": (
            "Minimal — retired or non-production assets. Residual access is an "
            "internal control issue unless the asset still holds client data."
        ),
        "overall": "2 - Minor",
        "mtpd": 720,
        "rto": 72,
        "rpo": "N/A",
    },
]

# Workshop draft for the DEPENDENCIES section. Personnel are role titles
# until named Primary / Backup owners are confirmed. Systems reuse what
# already appears in the organisation BIA sample (Oracle ERP, ticketing
# portal, VPN) and otherwise stay product-agnostic.
DEPENDENCIES = {
    "Requirements & Solution Design": {
        "upstream": (
            "Business Development client brief and proposal window; "
            "Implementation Functional Unit process knowledge; VPN for client discovery"
        ),
        "downstream": (
            "Implementation Technical Unit (build against the design); "
            "Business Development (proposal commitment and dates)"
        ),
        "systems": "Design/requirements repository; proposal workspace; VPN",
        "data": "Requirements specs; solution design documents; acceptance criteria; client process notes",
        "personnel": "Solutions Architect (Primary) / Functional Lead (Backup)",
        "vendors": "Oracle Corporation (product documentation, where the client estate is Oracle)",
    },
    "Application Development (Coding)": {
        "upstream": (
            "Approved requirements and design; source control availability; "
            "development environment; VPN"
        ),
        "downstream": "Code Review; Testing & QA; Build Management; CI/CD Pipeline",
        "systems": "Development workstations; source control platform; development environment; VPN",
        "data": "Application source; uncommitted local work; coding standards",
        "personnel": "Lead Developer (Primary) / Senior Developer (Backup)",
        "vendors": "Client ERP platform vendor (Oracle where applicable); language/runtime vendor",
    },
    "Source Code & Version Control": {
        "upstream": "Identity/directory so staff can authenticate; network access to the repository",
        "downstream": (
            "Application Development; Code Review; Build Management; CI/CD; "
            "Release Deployment — the whole delivery path"
        ),
        "systems": "Source control platform",
        "data": "Repositories; commit history; branch permissions; merge and approval records",
        "personnel": "Technical Lead (Primary) / Senior Developer (Backup)",
        "vendors": "Source control platform vendor",
    },
    "Code Review": {
        "upstream": "Source control; submitted change requests; coding and security standards",
        "downstream": "Build Management; CI/CD; Release Deployment (unreviewed changes must not ship)",
        "systems": "Source control review workflow",
        "data": "Review comments; approval records; defect and vulnerability findings",
        "personnel": "Technical Lead (Primary) / Senior Developer (Backup)",
        "vendors": "Source control platform vendor",
    },
    "Testing & Quality Assurance": {
        "upstream": (
            "Testable build; requirements/acceptance criteria; test or staging environment; "
            "Implementation Functional Unit business scenarios"
        ),
        "downstream": "Release Management; Release Deployment; client go-live confidence",
        "systems": "Test/staging environment; ticketing portal (defects); VPN",
        "data": "Test cases; test results; defect logs; sign-off records",
        "personnel": "QA Lead (Primary) / Functional Tester (Backup)",
        "vendors": "Hosting/cloud provider (test environments)",
    },
    "Build Management": {
        "upstream": "Approved code in source control; dependency/artefact store; build configuration",
        "downstream": "CI/CD Pipeline; Release Deployment",
        "systems": "Build server; artefact repository; source control",
        "data": "Build definitions; build logs; versioned artefacts; dependency lockfiles",
        "personnel": "DevOps Engineer (Primary) / Technical Lead (Backup)",
        "vendors": "Build and artefact platform vendor",
    },
    "CI/CD Pipeline Management": {
        "upstream": (
            "Build artefacts; pipeline definitions; environment credentials; "
            "change/release approval"
        ),
        "downstream": "Release Deployment; Production Support (what actually lands in production)",
        "systems": "CI/CD platform; source control; target environments",
        "data": "Pipeline configuration; deployment logs; approval-gate records",
        "personnel": "DevOps Engineer (Primary) / Technical Lead (Backup)",
        "vendors": "CI/CD platform vendor",
    },
    "Release Deployment (Execution)": {
        "upstream": (
            "Approved release package; CI/CD or runbook; change approval; "
            "client release window; VPN to production"
        ),
        "downstream": (
            "Business Development (promised dates); client production; "
            "Production Support; Incident Management"
        ),
        "systems": "Deployment tooling; production environment; VPN; ticketing portal (change record)",
        "data": "Release package; deployment runbook; change ticket; rollback plan",
        "personnel": "Release Engineer (Primary) / Technical Lead (Backup)",
        "vendors": "Cloud/hosting provider; Oracle Corporation (where production is Oracle ERP)",
    },
    "Database & Data Structure Management": {
        "upstream": (
            "Approved schema/data change; backup/restore capability; "
            "VPN to the database environment"
        ),
        "downstream": (
            "Data Handling & ETL; application features; client reporting; "
            "Production Support"
        ),
        "systems": "Database platform; admin console; VPN; backup tooling",
        "data": "Schemas; data dictionaries; backup sets; change scripts; access grants",
        "personnel": "Database Administrator (Primary) / Senior Developer (Backup)",
        "vendors": "Database platform vendor; Oracle Corporation (where the estate is Oracle)",
    },
    "Third-Party & Dependency Management": {
        "upstream": "Licence inventory; vendor security advisories; source control (to apply upgrades)",
        "downstream": "Build Management; application security; Release Deployment",
        "systems": "Dependency/licence inventory; source control; artefact repository",
        "data": "Dependency inventory; licence records; vulnerability and patch status",
        "personnel": "Technical Lead (Primary) / DevOps Engineer (Backup)",
        "vendors": "Component and library vendors; Oracle Corporation and other platform vendors",
    },
    "Security & Access Configuration": {
        "upstream": (
            "HR/Admin joiner–mover–leaver notice; identity directory; "
            "approved access request in the ticketing portal"
        ),
        "downstream": (
            "All technical activities that touch production; client data protection; audit"
        ),
        "systems": "Identity directory; VPN; privileged-access consoles; ticketing portal",
        "data": "Access matrices; secrets inventory; vulnerability results; access-review evidence",
        "personnel": "Security Administrator (Primary) / Technical Lead (Backup)",
        "vendors": "Identity and VPN vendor; security-tooling vendor",
    },
    "Environment Management": {
        "upstream": "Cloud/infrastructure capacity; network and VPN; configuration baselines",
        "downstream": "Application Development; Testing & QA; Release Deployment",
        "systems": "Environment/cloud console; configuration management; VPN",
        "data": "Environment inventory; configuration baselines; credentials; data-masking rules",
        "personnel": "DevOps Engineer (Primary) / Technical Lead (Backup)",
        "vendors": "Cloud/hosting provider",
    },
    "Data Handling & ETL": {
        "upstream": (
            "Source system availability (client Oracle ERP / operational databases); "
            "mapping specs; month-end/quarter-end window"
        ),
        "downstream": (
            "Client reports and dashboards; Implementation Functional Unit; "
            "client finance close"
        ),
        "systems": "ETL/integration platform; source and target databases; VPN",
        "data": "Source extracts; transformation mappings; load logs; data-quality exceptions",
        "personnel": "Data Engineer (Primary) / Database Administrator (Backup)",
        "vendors": "Integration/ETL vendor; Oracle Corporation (source ERP)",
    },
    "Production Support & Troubleshooting": {
        "upstream": (
            "Ticketing portal; VPN to client/production; logging and monitoring; "
            "runbooks; client SLA terms"
        ),
        "downstream": "Business Development; client operations; Incident Management",
        "systems": "Ticketing portal; VPN; production systems (Oracle ERP where applicable); monitoring",
        "data": "Ticket history; SLA terms; escalation contacts; diagnostic logs; workaround records",
        "personnel": "Support Lead (Primary) / Senior Developer (Backup)",
        "vendors": "Oracle Corporation (vendor support); cloud/hosting provider",
    },
    "Access & Account Management": {
        "upstream": (
            "HR/Admin starter and leaver notifications; approved access request; "
            "identity directory"
        ),
        "downstream": "New staff productivity; security (stale access); all system owners",
        "systems": "Identity directory; VPN account administration; ticketing portal",
        "data": "Account register; joiner–mover–leaver records; privileged-account list; access-review logs",
        "personnel": "Access Administrator (Primary) / HR/Admin Liaison (Backup)",
        "vendors": "Identity/directory vendor",
    },
    "Release Management": {
        "upstream": (
            "Test sign-off; client-agreed window; Business Development client communication; "
            "change calendar"
        ),
        "downstream": "Release Deployment; Business Development; client stakeholders",
        "systems": "Ticketing portal; release/change calendar",
        "data": "Release plans; client communications; approval records; go-live checklists",
        "personnel": "Release Manager (Primary) / Technical Lead (Backup)",
        "vendors": "Ticketing platform vendor",
    },
    "Cloud Infrastructure Management": {
        "upstream": "Cloud account and billing; network design; security baselines",
        "downstream": "All environments; CI/CD targets; production availability; cost control",
        "systems": "Cloud management console; infrastructure-as-code repository; monitoring",
        "data": "Infrastructure configuration; IAM/privilege maps; cost/usage data; security-group rules",
        "personnel": "Cloud Engineer (Primary) / DevOps Engineer (Backup)",
        "vendors": "Cloud provider",
    },
    "Logging & Monitoring": {
        "upstream": "Application and infrastructure telemetry; log shipper; storage for logs",
        "downstream": "Incident Management; Production Support; audit and forensics",
        "systems": "Monitoring and alerting platform; log store; ticketing portal (alert to ticket)",
        "data": "Logs; alert rules; dashboards; audit trails",
        "personnel": "DevOps Engineer (Primary) / Support Lead (Backup)",
        "vendors": "Monitoring/logging platform vendor",
    },
    "Incident Management": {
        "upstream": (
            "Monitoring alerts; ticketing portal; on-call roster; VPN; "
            "logging; recent change records"
        ),
        "downstream": "Business Development; client operations; live-service recovery",
        "systems": "Ticketing portal; monitoring; VPN; production systems (Oracle ERP where applicable)",
        "data": "Incident tickets; timeline; root-cause records; SLA clock; escalation contacts",
        "personnel": "Incident Manager (Primary) / Support Lead (Backup)",
        "vendors": "Oracle Corporation (if the incident is on Oracle ERP); cloud/hosting provider",
    },
    "Decommissioning": {
        "upstream": (
            "Approved retirement request; HR/Admin (access removal); "
            "backup/archive of required records"
        ),
        "downstream": "Finance (cost stop); Security (residual access); audit (record retention)",
        "systems": "Asset inventory; identity directory; backup/archive store; cloud console",
        "data": "Decommission checklist; retained records; access-removal evidence; disposal certificates",
        "personnel": "Technical Lead (Primary) / Access Administrator (Backup)",
        "vendors": "Cloud/hosting provider (to terminate); records/archive or disposal vendor",
    },
}

# Workshop draft for CURRENT STATE & GAP + STRATEGY & RECOVERY.
# Alternate site/access and cross-training answers are Yes / Partial / No
# with a short note. Cross-training is Partial until a named, trained deputy
# is confirmed — backup roles were designated in the Dependencies draft.
CURRENT_STATE = {
    "Requirements & Solution Design": {
        "spof": "Solutions Architect as the only designer; design pack held in one workspace or one mailbox",
        "safeguards": "Functional Unit design review; shared requirements repository",
        "strategy": "Functional Lead continues from the shared spec; restore documents from the repository backup",
        "alternate": "Yes — VPN / remote",
        "cross_train": "Partial — Functional Lead designated as backup; named trained deputy not confirmed",
    },
    "Application Development (Coding)": {
        "spof": "Lead Developer knowledge of a module; uncommitted code on one workstation",
        "safeguards": "Source control; coding standards; peer review before merge",
        "strategy": "Senior Developer continues from last commit; rebuild the workstation; do not rely on local uncommitted work",
        "alternate": "Yes — VPN / remote; spare workstation",
        "cross_train": "Partial — Senior Developer designated as backup; confirm module-level training",
    },
    "Source Code & Version Control": {
        "spof": "The source control platform itself; sole repository administrator; vendor outage",
        "safeguards": "Access control and segregation of duties on merges; commit history as the audit trail",
        "strategy": "Restore the repository from platform/vendor backup; freeze merges until the last good copy is verified",
        "alternate": "Yes — VPN to the platform; use the vendor’s alternate region if contracted",
        "cross_train": "Partial — Senior Developer designated as deputy administrator",
    },
    "Code Review": {
        "spof": "Technical Lead as the only reviewer (self-approval risk if that person is also the author)",
        "safeguards": "No self-approval; review workflow in source control",
        "strategy": "Senior Developer reviews; if both reviewers are unavailable, freeze merges — do not skip review",
        "alternate": "Yes — VPN / remote",
        "cross_train": "Partial — Senior Developer designated as backup reviewer",
    },
    "Testing & Quality Assurance": {
        "spof": "QA Lead; a single test/staging environment",
        "safeguards": "Written test cases; defect logging in the ticketing portal; Functional Unit business scenarios",
        "strategy": "Functional Tester continues from written cases; restore or rebuild staging from the environment baseline",
        "alternate": "Yes — VPN to test/staging",
        "cross_train": "Partial — Functional Tester designated as backup",
    },
    "Build Management": {
        "spof": "Build server; DevOps Engineer; artefact store",
        "safeguards": "Build definitions in source control; versioned artefacts",
        "strategy": "Rebuild the build host from definitions in source control; Technical Lead runs a known-good build",
        "alternate": "Yes — VPN / remote; rebuild on an alternate host",
        "cross_train": "Partial — Technical Lead designated as backup",
    },
    "CI/CD Pipeline Management": {
        "spof": "CI/CD platform; pipeline administrator; production deploy credentials",
        "safeguards": "Approval gates; pipeline configuration in source control",
        "strategy": "Restore pipelines from source-controlled config; manual deploy only with dual control if the platform is down",
        "alternate": "Yes — VPN / remote; alternate runner if needed",
        "cross_train": "Partial — Technical Lead designated as backup",
    },
    "Release Deployment (Execution)": {
        "spof": "Release Engineer; production VPN path; the production environment itself",
        "safeguards": "Change ticket; rollback plan; avoid month-end, Friday, and pre-holiday deploys",
        "strategy": "Technical Lead executes the runbook; roll back to the previous package; delay any non-urgent release",
        "alternate": "Yes — VPN to production",
        "cross_train": "Partial — Technical Lead designated as backup",
    },
    "Database & Data Structure Management": {
        "spof": "Database Administrator; the database platform; backups stored in only one place",
        "safeguards": "Scripted changes; backup/restore; controlled access grants; VPN",
        "strategy": "Restore from backup; Senior Developer applies scripted changes only; call the platform vendor if the engine is down",
        "alternate": "Yes — VPN; restore onto an alternate host if the primary is lost",
        "cross_train": "Partial — Senior Developer designated for scripted changes, not full DBA cover",
    },
    "Third-Party & Dependency Management": {
        "spof": "Technical Lead as the only person tracking licences and patches; a single artefact registry",
        "safeguards": "Dependency/licence inventory; vendor security advisories",
        "strategy": "DevOps Engineer applies vendor patches from the inventory and lockfiles; rebuild artefacts from the last known-good set",
        "alternate": "Yes — VPN / remote",
        "cross_train": "Partial — DevOps Engineer designated as backup",
    },
    "Security & Access Configuration": {
        "spof": "Security Administrator; identity directory; a single break-glass path",
        "safeguards": "Access requests via ticketing portal; HR joiner–mover–leaver notices; periodic access review",
        "strategy": "Technical Lead uses the documented break-glass admin; restore the directory from backup; HR-driven leaver disable",
        "alternate": "Yes — VPN / admin console",
        "cross_train": "Partial — Technical Lead designated as backup",
    },
    "Environment Management": {
        "spof": "DevOps Engineer; cloud account owner; environment config not stored in source control",
        "safeguards": "Configuration baselines; data-masking rules for non-production",
        "strategy": "Rebuild the environment from the documented baseline (or infrastructure-as-code if present); Technical Lead",
        "alternate": "Yes — cloud console via VPN from any site",
        "cross_train": "Partial — Technical Lead designated as backup",
    },
    "Data Handling & ETL": {
        "spof": "Data Engineer; ETL platform; source Oracle ERP / operational database availability",
        "safeguards": "Mapping specifications; load logs; data-quality exception records; VPN",
        "strategy": "Database Administrator re-runs documented jobs; restore mappings from the repository; delay non-close jobs",
        "alternate": "Yes — VPN to source and target systems",
        "cross_train": "Partial — Database Administrator designated for documented jobs",
    },
    "Production Support & Troubleshooting": {
        "spof": "Support Lead; ticketing portal; VPN to client production; Oracle vendor support hours",
        "safeguards": "Ticket history; SLA terms; runbooks; monitoring; escalation contacts",
        "strategy": "Senior Developer follows runbooks; escalate to Oracle/cloud vendor; use the on-call rota",
        "alternate": "Yes — VPN / remote (client support is remote-capable)",
        "cross_train": "Partial — Senior Developer designated as backup",
    },
    "Access & Account Management": {
        "spof": "Access Administrator; identity directory; HR notice not reaching Technical",
        "safeguards": "Ticketing for access requests; joiner–mover–leaver records; HR/Admin liaison",
        "strategy": "HR/Admin Liaison disables leavers from the documented checklist; restore the directory from backup",
        "alternate": "Yes — VPN / admin console",
        "cross_train": "Partial — HR/Admin Liaison designated for leaver disable; confirm technical training",
    },
    "Release Management": {
        "spof": "Release Manager; release calendar held in one mailbox",
        "safeguards": "Ticketing portal; client communications; test sign-off before a date is committed",
        "strategy": "Technical Lead holds the shared calendar; freeze releases if approvals cannot be evidenced",
        "alternate": "Yes — VPN / remote",
        "cross_train": "Partial — Technical Lead designated as backup",
    },
    "Cloud Infrastructure Management": {
        "spof": "Cloud Engineer; cloud provider outage; root/owner account",
        "safeguards": "IAM / privilege maps; monitoring; infrastructure-as-code repository",
        "strategy": "DevOps Engineer rebuilds from infrastructure-as-code; provider support; documented break-glass account",
        "alternate": "Yes — cloud console from any location; provider region failover if contracted",
        "cross_train": "Partial — DevOps Engineer designated as backup",
    },
    "Logging & Monitoring": {
        "spof": "Monitoring platform; DevOps Engineer; log store",
        "safeguards": "Alert-to-ticket in the ticketing portal; dashboards; log retention",
        "strategy": "Restore the platform from configuration backup; Support Lead uses client tickets as interim detection",
        "alternate": "Yes — VPN / remote to the monitoring console",
        "cross_train": "Partial — Support Lead designated for alert handling",
    },
    "Incident Management": {
        "spof": "Incident Manager; ticketing portal; a single on-call person",
        "safeguards": "Escalation contacts; monitoring alerts; SLA clock; root-cause records",
        "strategy": "Support Lead runs the incident from the runbook; Business Development handles client communications; restore ticketing from the vendor",
        "alternate": "Yes — VPN / remote; the process does not need a second office",
        "cross_train": "Partial — Support Lead designated; confirm incident-command training",
    },
    "Decommissioning": {
        "spof": "Technical Lead; checklist held in one share; residual access if the owner is absent",
        "safeguards": "Decommission checklist; access-removal evidence; HR/Admin for account removal",
        "strategy": "Access Administrator completes access removal and archive; delay any non-urgent retirement",
        "alternate": "Yes — VPN / remote for access and cloud terminate; physical disposal may still need a site",
        "cross_train": "Partial — Access Administrator designated as backup",
    },
}

# Test Result Summary: no practice drill has been run yet, so every
# activity is the same value. Do not attach a date — a date is not a
# prediction that the risk will occur.
TEST_RESULTS = {row["activity"]: "Not yet tested" for row in ROWS}

