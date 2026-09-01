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

