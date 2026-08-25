# EDFIP presentation and architecture

Confidential. For the Emeraid meeting only.

## Screening deck

- **Present this:** `EDFIP_Screening_Dexta.pptx`
- **Same slides as Markdown:** `EDFIP_Presentation.md` (open in Cursor, GitHub, or Google Docs)
- Optional words (your phone only): `SPEAKER_NOTES.md`
- Optional browser version: `index.html`

## Architecture (post-screening)

Revised from Alison’s Fineract–Odoo draft after alignment: SaaS = one Emeraid-hosted platform, onboard institutions, sell configurable packs (not a separate deploy per customer). Odoo is the operating core and System Administration control plane. Fineract is core banking. FastAPI is a sibling API on the same environment. Flutter is field/customer Android. Security is required on every plane.

- **Walk through / send:** `architecture/EDFIP_Architecture_Final.md`
- **Diagrams:** `architecture/index.html`

Do not host these files on a public URL.
