# Awesome AI Hardware

> A curated list of open-source projects that connect AI, large language models, or agents with real-world hardware.

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Validate](https://github.com/s87343472/awesome-ai-hardware/actions/workflows/validate.yml/badge.svg)](https://github.com/s87343472/awesome-ai-hardware/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**English** | [简体中文](README.zh-CN.md)

Awesome AI Hardware is a reviewed collection of reproducible projects that bring large language models, agents, speech AI, vision AI, and machine learning into the physical world.

This is not a news feed or an unverified link dump. Every listed project must meet explicit open-source, relevance, evidence, and reproducibility requirements.

## Contents

- [Categories](#categories)
- [Projects](#projects)
- [Timeline](#timeline)
- [Documentation](#documentation)
- [Inclusion Criteria](#inclusion-criteria)
- [Contributing](#contributing)
- [Data and Transparency](#data-and-transparency)
- [Disclaimer](#disclaimer)
- [License](#license)

## Categories

- Smart Home and IoT
- AI Wearables
- Voice Assistants and AI Companions
- Robotics and Embodied AI
- Edge AI and Microcontrollers
- Hardware Protocols, Bridges, and Infrastructure
- AI Status Displays and Creative Hardware

## Projects

### Smart Home and IoT

- [AI Doorbell for Home Assistant](https://github.com/nwkuga/ha-ai-doorbell) — Uses a vision-language model to compare real doorbell snapshots with labeled reference photos and handle corrections through Home Assistant and Telegram. `MIT` · [Flow](https://github.com/nwkuga/ha-ai-doorbell/blob/main/docs/img/04-flow.svg) · [Docs](https://github.com/nwkuga/ha-ai-doorbell/tree/main/docs)
- [Home Generative Agent](https://github.com/goruck/home-generative-agent) — Adds a LangGraph agent to Home Assistant for entity control, automation creation, camera analysis, and anomaly alerts with cloud or local models. `MIT` · [Demo](https://github.com/goruck/home-generative-agent/blob/main/assets/create_automation.gif) · [Docs](https://github.com/goruck/home-generative-agent/blob/main/docs/installation.md)

### AI Wearables

- [Omi](https://github.com/BasedHardware/omi) — Combines open-source wearable hardware and companion apps for real-time transcription, summaries, action items, and personal memory retrieval. `MIT` · [Docs](https://docs.omi.me/) · [Website](https://omi.me/)

### Voice Assistants and AI Companions

- [OpenHome Abilities](https://github.com/openhome-dev/abilities) — Provides plugins for OpenHome voice agents, including local abilities that run on Raspberry Pi DevKit hardware and access GPIO and sensors. `MIT` · [Docs](https://docs.openhome.com/) · [DevKit files](https://github.com/openhome-dev/devkit)

### Robotics and Embodied AI

- [Open V Robotics System](https://github.com/vahagnmikayelyan/open-v-robotics-system) — Routes permissioned LLM tool calls through modular drivers to motors, cameras, sensors, and other robot hardware across an SBC and Raspberry Pi Pico. `MIT` · [Interface](https://github.com/vahagnmikayelyan/open-v-robotics-system/blob/main/docs/images/main%20screen.png) · [Docs](https://github.com/vahagnmikayelyan/open-v-robotics-system/tree/main/docs)

### Edge AI and Microcontrollers

- [ESP32 AI](https://github.com/slvDev/esp32-ai) — Runs a 28.9-million-parameter language model fully offline on an ESP32-S3 and writes generated text to an attached display. `MIT` · [Demo](https://github.com/slvDev/esp32-ai/blob/main/media/esp32-ple-demo.gif) · [Results](https://github.com/slvDev/esp32-ai/blob/main/RESULTS.md)
- [Hailo Apps](https://github.com/hailo-ai/hailo-apps) — Provides runnable computer-vision, VLM, LLM, and speech applications for Hailo accelerators on platforms including Raspberry Pi 5. `MIT` · [Demo](https://github.com/hailo-ai/hailo-apps/blob/main/doc/images/agentic_ai.gif) · [Docs](https://github.com/hailo-ai/hailo-apps/blob/main/doc/README.md)
- [PicoLM](https://github.com/RightNow-AI/picolm) — Runs quantized billion-parameter GGUF models through a zero-dependency C engine on low-memory RISC-V and Raspberry Pi devices. `MIT` · [Hardware overview](https://github.com/RightNow-AI/picolm/blob/main/picolm.jpg) · [Technical notes](https://github.com/RightNow-AI/picolm/blob/main/BLOG.md)

### Protocols, Bridges, and Infrastructure

- [esprec](https://github.com/tig/esprec) — Lets coding agents capture and visually validate a real ESP32 screen through an on-device component and USB host tool. `Apache-2.0` · [Demo](https://github.com/tig/esprec/blob/main/docs/examples/xuss-c-screens.gif) · [Agent guide](https://github.com/tig/esprec/blob/main/AGENTS.md)
- [mcp2mqtt](https://github.com/mcp2everything/mcp2mqtt) — Converts MCP tool calls into MQTT commands so language models can control connected lights, motors, and other devices. `MIT` · [Architecture](https://github.com/mcp2everything/mcp2mqtt/blob/main/docs/images/stru_eng.PNG) · [Workflow](https://github.com/mcp2everything/mcp2mqtt/blob/main/docs/images/workflow_eng.png)

See the [2026-08-01 review record](reviews/2026-08-01-initial-batch.md) for accepted, deferred, superseded, and rejected candidates.

## Timeline

Browse the [collection timeline](timeline/README.md) to discover projects by the month they were accepted. Timeline entries include the source repository, original X post when available, a concise introduction, and links to original images, videos, demos, or articles.

The acceptance date is not necessarily the project's publication date or the date it was discovered.

## Documentation

The [documentation index](docs/README.md) links every guide in English and Simplified Chinese, including the contributing guide, review guide, Code of Conduct, and security policy.

## Inclusion Criteria

A project must meet all of the following requirements:

1. Its source repository is publicly accessible.
2. AI, an LLM, or an agent is a core capability rather than a marketing label.
3. It directly interacts with physical hardware, sensors, actuators, or devices.
4. It includes enough documentation to understand or reproduce the project.
5. Its repository contains an explicit open-source license.
6. Its description and claims can be verified from public sources.

See the [contribution guide](CONTRIBUTING.md) and [review guide](docs/REVIEW_GUIDE.md) for the complete rules. Chinese versions are available from the [documentation index](docs/README.md).

## Contributing

- Recommend a project with the [project submission form](https://github.com/s87343472/awesome-ai-hardware/issues/new?template=project-submission.yml).
- Submit a Pull Request to correct or update an existing entry.
- Do not disclose sensitive vulnerabilities publicly; follow the [security policy](SECURITY.md).

A recommendation is not an acceptance. Maintainers verify the source repository, license, role of AI, hardware integration, reproducibility, and supporting evidence before listing a project.

## Data and Transparency

Accepted entries are also stored in [`data/projects.json`](data/projects.json). Automated checks validate required fields, categories, acceptance and verification dates, URLs, media resources, sorting, and duplicate entries. Review decisions remain visible in the corresponding Issue or Pull Request.

## Disclaimer

Inclusion means only that a project met this list's public criteria when it was reviewed. It is not an endorsement of the project's security, privacy, hardware reliability, or commercial suitability. Review the code, permissions, data flows, and network access before connecting any project to a physical device.

## License

[MIT](LICENSE) © s87343472 and contributors.
