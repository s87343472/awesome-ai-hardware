# Contributing Guide

**English** | [简体中文](CONTRIBUTING.zh-CN.md) · [Documentation index](docs/README.md)

Thank you for helping maintain Awesome AI Hardware. A submission should give other people enough public evidence to verify that a project genuinely combines AI with hardware and decide whether it is worth exploring.

## Quick submission

Open a project submission Issue and provide:

- GitHub repository URL
- One-sentence description
- The specific role of AI
- The specific role of hardware
- Open-source license
- Original post, demo, or documentation URL, when available
- Original image, video, demo, or article URLs, when available
- Suggested category and tags

Submit one project per Issue. Project authors may submit their own work but must disclose the relationship.

## Mandatory requirements

Every requirement below must be satisfied.

### 1. Accessible implementation

A public source repository must contain an actual implementation, not only a product page, screenshots, a waitlist, or prebuilt binaries.

### 2. AI is a core capability

The repository must demonstrate at least one of the following in its core execution path: an LLM, VLM, speech model, generative model, machine-learning inference, or autonomous agent. Ordinary rules, remote control, keyword detection, or simply putting “AI” in the title is not enough.

### 3. Direct relationship with physical hardware

The project must read sensor or device data, control actuators or devices, run on edge hardware, or provide buildable hardware designs. Pure chatbots, desktop-only applications, and projects that only generate Home Assistant text without a device integration path are out of scope.

### 4. Reproducibility evidence

At least two of the following must be available: architecture documentation, a supported-hardware list, and installation or build instructions. A concept video or one-off demo may remain a candidate but cannot be formally accepted.

### 5. Explicit open-source license

The source repository must include an explicit license file. Publicly visible source without a license is not legally reusable open source.

### 6. Verifiable information

Descriptions must be supported by the repository, official documentation, or an accessible original post. A claim that a project was “recently shared on X” requires the specific post URL; search results and secondhand summaries are not substitutes.

## Out of scope

- Software-only agents, prompt collections, or model lists
- Ordinary IoT or Arduino projects without a core AI capability
- Closed-source products represented only by crowdfunding, store, marketing, or demo pages
- Mirrors, duplicate forks, suspected plagiarism, or unclear provenance
- Malware, device-security bypasses, or projects with obvious privacy abuse
- Dead or archived projects without usable documentation
- Paid placement or submissions offering benefits in exchange for inclusion

## Categories

Each project has exactly one primary category:

| ID | Category | Typical projects |
|---|---|---|
| `smart-home-iot` | Smart Home and IoT | Lighting, doorbells, home automation, MQTT |
| `wearables` | AI Wearables | Badges, headphones, glasses, personal assistants |
| `voice-companions` | Voice Assistants and AI Companions | Desktop companions, persistent voice terminals |
| `robotics` | Robotics and Embodied AI | Mobile robots, robot arms, character robots |
| `edge-ai` | Edge AI and Microcontrollers | MCUs, SBCs, local inference |
| `protocols-infrastructure` | Protocols and Infrastructure | MCP, MQTT, device bridges, SDKs |
| `creative-hardware` | Status Displays and Creative Hardware | AI status lights, installations, novel interfaces |

Multiple tags may be added when useful, but only one category may be primary.

## Review process

1. **Triage:** Check links, required fields, and obvious duplicates.
2. **Verification:** Verify the license, role of AI, role of hardware, and reproduction materials.
3. **Decision:** Accept, request information, defer, or reject.
4. **Merge:** Update `data/projects.json`, the relevant README section, and the monthly timeline.
5. **Maintenance:** Periodically revisit dead links, archived status, and material changes.

Typical status labels are `candidate`, `needs-info`, `needs-verification`, `accepted`, `rejected`, and `archived`.

See the [review guide](docs/REVIEW_GUIDE.md) for the detailed decision process.

## Pull Request requirements

- Keep each PR focused on one project or one kind of maintenance change.
- Avoid promotional language, inflated metrics, and unverifiable opinions.
- Describe factually what the AI does and what the hardware is.
- Add a new project to the structured data, the README, and `timeline/YYYY/MM.md`.
- Use `YYYY-MM-DD` dates.
- Run `python scripts/validate_projects.py` before submitting.

## Showcase submissions

Showcase & Ideas preserves useful X posts even when the related project is not formally listed. A showcase submission must provide:

- the canonical X status URL;
- the linked GitHub repository or product page, when one exists;
- whether the poster is the project author, a project-team member, or a community explainer;
- the visible media type and a direct link to the original media context;
- a factual English and Chinese summary of the idea, process, trade-off, or demonstration.

Showcases are grouped by the post's publication month, not the discovery or submission date. Do not infer an author relationship from enthusiastic language, and do not describe a community post as an original announcement. Media must remain on the original X, YouTube, or project-hosted page.

Run `python scripts/validate_showcases.py` before submitting a showcase change.

## Ordering and fairness

Projects are ordered alphabetically within each category. Stars, funding, brand relationships, and popularity on X do not determine inclusion or ranking. Maintainers, contributors, and authors must disclose relevant relationships.

## Date and media fields

- `added_at`: the date a maintainer formally accepts the project; this is the only date used to group timeline entries.
- `discovered_at`: the optional date on which the project was submitted or discovered; it does not replace `added_at`.
- `last_verified`: the date on which the project's information was most recently verified.
- `source_url`: the original X post, blog post, or project announcement rather than a search-results page.
- `resources`: original image, video, demo, article, or documentation links, preferably published by the author or project.

Do not download, copy, or rehost X images or videos without clear permission. Link to the original post; directly embed only repository-owned or appropriately licensed media.

## Removal and appeals

A project may be flagged or removed when its repository disappears, its license is withdrawn, its description is materially misleading, it presents a serious safety or privacy concern, or it no longer fits the scope. Authors may provide new evidence and request another review in the relevant Issue. The same public criteria apply to an appeal.
