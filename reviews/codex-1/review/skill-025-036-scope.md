# Scope and safety review: skill-025–036

Reviewed the 12 batch definitions and available examples against their inputs, with targeted checks for security, weapons, biology and ambiguous labels. All 480 IDs are present in the original order; each row has the expected four fields. This is a draft scope review, not a primary-source or release approval. No draft, canonical file or other run was edited.

## Safety spot checks

- Security and access: IT security architecture/documentation, Kenna, Sentinel, intrusion detection, Nexpose, malware analysis, ATT&CK, PCI DSS, JAFAN and JCAVS are explanatory or defensive. Examples illustrate governance, monitoring or authorized assessment; they provide no payloads, attack steps, repro instructions, exploitation, access bypass or automation against targets. The PPTP example recognizes an old configuration rather than recommending or implementing it.
- Weapons: Police baton is defined as a regulated-context impact weapon without tactics, use instructions or a use example. Military standards is about procurement/specification review; no weapon system or operational instruction is described.
- Biology: mammalian cell culture, molecular docking/modelling, protein characterization and structure prediction are broad descriptions. Examples do not identify pathogens, sequences, lab conditions, protocols or orders. Preserve that abstraction in later review.

## Sense flags for authoritative review

| Batch | Label | What to verify before canonical use |
|---|---|---|
| 025 | JAFAN; JDesktop Network Components; JsUnit | JAFAN is a family label rather than a named revision; confirm the owning authority and document scope. Verify the exact JDesktop project and its focus; don't promote the current generic description to a product claim. JsUnit names several historical projects. |
| 025 | Jive Software; Joint Commission standards | Distinguish the company from its collaboration product, and the accreditor's standard families from a specific applicable standard. |
| 026 | Know Your Third Party (KY3P) | Could be a product or generic third-party due diligence; do not attach product-specific aliases without evidence. |
| 027 | LiveData; Logic diagrams | The library hint supports Android Jetpack LiveData but doesn't uniquely establish it. Determine whether diagrams refer to circuit logic or decision modeling. |
| 028 | Microchipping; Meter Operation Code of Practice Agreement | Microchipping could mean an implanted identifier or refer informally to chip manufacture; the draft assumes the former. Confirm the agreement's exact legal title and jurisdiction before using it as authority. |
| 029 | Microsoft Teams live events; MicroStrategy Desktop; MODO | Verify the specific product edition or feature branding if needed. Don't assume current availability or an alias to newer offerings. |
| 030 | Motor control algorithms; MRI Software | Retain the distinction between electric-motor control and biological motor control, and between the real-estate software brand and magnetic resonance imaging software. |
| 031 | npm; Observability | Confirm whether npm is the CLI or the package-distribution ecosystem; the context suggests software observability, not the control-theory term. |
| 032 | ON1; OpenTok; Oracle Cloud; Oracle Application Framework | Confirm featured product vs family/branding, especially broad Oracle Cloud vs OCI. Distinguish OA Framework from Oracle Application Development Framework. |
| 033 | Patient transfer; package.json | The former can describe physical movement or interfacility transfer of care; package.json is a manifest file, not a tool. |
| 034 | Periscope; Physical modelling synthesis; Plant Design Management System | Streaming platform vs optical instrument or Periscope Data; audio synthesis vs generic simulation; named PDMS product vs generic plant-design systems. |
| 035 | PLINK; Polycom | PLINK here means genetics software, not PuTTY Plink. Polycom could be the company, a product family or a specific device. |
| 036 | Production support; Program optimization; Prosecutor's management information system | Confirm software operations vs manufacturing, code performance vs program effectiveness, and generic prosecutorial case management vs the historical PROMIS product. |
