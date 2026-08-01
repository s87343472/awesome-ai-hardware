# Review Guide

**English** | [简体中文](REVIEW_GUIDE.zh-CN.md) · [Documentation index](README.md)

This guide is for maintainers and community reviewers. Another reviewer should be able to reproduce a decision from the cited public information.

## 1. Gate checks

All six answers must be “yes” before a project can be formally accepted:

- [ ] The GitHub repository is accessible and contains actual source code.
- [ ] AI or ML is part of the project's core execution path.
- [ ] The project directly interacts with physical hardware or provides hardware designs.
- [ ] Sufficient build, installation, or architecture documentation exists.
- [ ] An explicit open-source license exists.
- [ ] The description and provenance can be verified from public pages.

Use `needs-info` when information is missing and `needs-verification` when evidence exists but has not been checked. Do not lower the gate to increase the number of entries.

## 2. Evidence record

Record the following in the Issue or PR:

| Check | Where to look |
|---|---|
| Role of AI | README, dependencies, model configuration, core code path |
| Role of hardware | BOM, schematics, firmware, device compatibility, communication code |
| License | Root LICENSE/COPYING file and repository metadata |
| Reproducibility | Installation, wiring, build, configuration, and demo instructions |
| Provenance | Original GitHub repository, official documentation, original X or blog post |
| Media | Original images, videos, demos, or articles published by the author or project |
| Activity | Recent commits, Issues, archive flag, and deprecation notices |

Do not use a third-party summary as the only evidence for a project's capabilities.

Confirm that `added_at` is the maintainer's local date of formal acceptance, not the post date, repository creation date, or Grok discovery date. Automated validation allows a one-day UTC offset so contributors east or west of the CI runner are not rejected at midnight. Link media to its original source and do not copy unlicensed material.

## 3. Quality signals

After passing the gates, a project should preferably have at least two of these signals:

- Clear architecture or data-flow documentation
- An explicit supported-hardware list or BOM
- Actionable installation or build instructions
- A demo video, images, or test results
- Basic security and privacy documentation
- Maintenance activity within the last 24 months

Use these signals to determine whether more information is needed. Do not substitute star counts for quality.

## 4. Description style

A good description answers two questions: What does the AI do? What does the hardware do?

Recommended:

> Converts natural-language instructions into MQTT messages through MCP to control lights, motors, and other IoT devices.

Not recommended:

> A revolutionary next-generation intelligent hardware platform with an amazing experience.

Do not include volatile or unverifiable claims about star counts, rankings, performance, prices, or recent popularity.

## 5. Security and privacy

For projects involving always-on microphones, cameras, door locks, home automation, or remote execution, note the principal permissions and data flow in the review record. Inclusion is not a security audit. Defer projects with unresolved severe risks and contact their authors privately.

## 6. Decision template

```text
Decision: Accept / Needs information / Defer / Reject
Role of AI:
Role of hardware:
License:
Reproduction evidence:
Provenance evidence:
Security/privacy notes:
Review date: YYYY-MM-DD
```
