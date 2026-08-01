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
- [Showcase and Ideas](#showcase-and-ideas)
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

| No. | Name | License | Description | Image / Video | GitHub | X |
|---:|---|---|---|---|---|---|
| 1 | AI Doorbell for Home Assistant | MIT | Uses a vision-language model to recognize and correct people from real doorbell snapshots in Home Assistant and Telegram. | [Image](https://github.com/nwkuga/ha-ai-doorbell/blob/main/docs/img/04-flow.svg) | [Repo](https://github.com/nwkuga/ha-ai-doorbell) | — |
| 2 | Anima | Apache-2.0 | Runs a local agent OS that combines Mi Home device state, memory, and device skills to plan real control actions. | [Image](https://github.com/Fullive-AI/Anima/blob/main/docs/images/bedroom.svg) | [Repo](https://github.com/Fullive-AI/Anima) | [Post](https://x.com/GitHub_Daily/status/2068687909839073743) |
| 3 | Home Generative Agent | MIT | Adds entity control, automation creation, camera analysis, and anomaly alerts to Home Assistant with cloud or local models. | [Video](https://x.com/lindostangel/status/2081732515228995858) | [Repo](https://github.com/goruck/home-generative-agent) | [Post](https://x.com/lindostangel/status/2081732515228995858) |

### AI Wearables

| No. | Name | License | Description | Image / Video | GitHub | X |
|---:|---|---|---|---|---|---|
| 4 | LightMem-Ego | MIT | Turns first-person camera and audio streams from Rokid AI glasses into hierarchical multimodal memory that users can query. | [Image](https://github.com/zjunlp/LightMem-Ego/blob/main/figs/thumbnail.png) | [Repo](https://github.com/zjunlp/LightMem-Ego) | [Post](https://x.com/aigclink/status/2079059418168311813) |
| 5 | Omi | MIT | Combines wearable hardware and companion apps for transcription, summaries, action items, and personal memory retrieval. | [Image](https://x.com/CycleDecoded/status/2082693629953659191/photo/1) | [Repo](https://github.com/BasedHardware/omi) | [Post](https://x.com/CycleDecoded/status/2082693629953659191) |

### Voice Assistants and AI Companions

| No. | Name | License | Description | Image / Video | GitHub | X |
|---:|---|---|---|---|---|---|
| 6 | OpenHome Abilities | MIT | Provides voice-agent plugins, including local abilities that run on Raspberry Pi DevKit hardware and access GPIO and sensors. | — | [Repo](https://github.com/openhome-dev/abilities) | — |

### Robotics and Embodied AI

| No. | Name | License | Description | Image / Video | GitHub | X |
|---:|---|---|---|---|---|---|
| 7 | Cyclo Intelligence | Apache-2.0 | Covers data recording, policy training, inference, and ROBOTIS AI Worker execution with Behavior Tree and VLA hybrid control. | [Video](https://youtu.be/jRcUuwxFk_Y) | [Repo](https://github.com/ROBOTIS-GIT/cyclo_intelligence) | [Post](https://x.com/passionvirus/status/2074051976133046428) |
| 8 | Open V Robotics System | MIT | Routes permissioned LLM tool calls to robot motors, cameras, and sensors across an SBC and Raspberry Pi Pico. | [Image](https://github.com/vahagnmikayelyan/open-v-robotics-system/blob/main/docs/images/main%20screen.png) | [Repo](https://github.com/vahagnmikayelyan/open-v-robotics-system) | — |
| 9 | OpenArm | Apache-2.0 + component licenses | Provides a compliant humanoid arm and open CAD, control, teleoperation, datasets, MuJoCo, and Isaac Lab stacks for physical-AI research. | [Video](https://x.com/lukas_m_ziegler/status/2043595780695457957) | [Repo](https://github.com/enactic/OpenArm) | [Post](https://x.com/lukas_m_ziegler/status/2043595780695457957) |
| 10 | reBot-DevArm | CERN-OHL-W-2.0 | Opens the robotic-arm structure and BOM while connecting ROS, Isaac Sim, LeRobot, and visual-grasping workflows. | [Image](https://x.com/IlirAliu_/status/2040702009720881214/photo/1) | [Repo](https://github.com/Seeed-Projects/reBot-DevArm) | [Post](https://x.com/IlirAliu_/status/2040702009720881214) |

### Edge AI and Microcontrollers

| No. | Name | License | Description | Image / Video | GitHub | X |
|---:|---|---|---|---|---|---|
| 11 | Autonomous Computer | MIT | Provides open BOMs, CAD, assembly material, and build guides for local AI computers with two, four, or eight GPUs. | [Video](https://x.com/dee_hw/status/2065803426429346115) | [Repo](https://github.com/autonomous-ai/autonomous-computer) | [Post](https://x.com/dee_hw/status/2065803429071765819) |
| 12 | ESP32 AI | MIT | Runs a 28.9-million-parameter language model fully offline on an ESP32-S3 and writes generated text to a display. | [Video](https://github.com/slvDev/esp32-ai/blob/main/media/esp32-ple-demo.gif) | [Repo](https://github.com/slvDev/esp32-ai) | [Post](https://x.com/GithubAwesome/status/2081550211990569069) |
| 13 | Hailo Apps | MIT | Provides runnable vision, VLM, LLM, and speech applications for Hailo accelerators on platforms including Raspberry Pi 5. | [Video](https://github.com/hailo-ai/hailo-apps/blob/main/doc/images/agentic_ai.gif) | [Repo](https://github.com/hailo-ai/hailo-apps) | — |
| 14 | PicoLM | MIT | Runs quantized billion-parameter GGUF models through a zero-dependency C engine on low-memory RISC-V and Raspberry Pi devices. | [Image](https://x.com/GitHub_Daily/status/2083183407132254242/photo/1) | [Repo](https://github.com/RightNow-AI/picolm) | [Post](https://x.com/GitHub_Daily/status/2083183407132254242) |

### Protocols, Bridges, and Infrastructure

| No. | Name | License | Description | Image / Video | GitHub | X |
|---:|---|---|---|---|---|---|
| 15 | esprec | Apache-2.0 | Lets coding agents capture and visually validate a real ESP32 screen through an on-device component and USB host tool. | [Video](https://github.com/tig/esprec/blob/main/docs/examples/xuss-c-screens.gif) | [Repo](https://github.com/tig/esprec) | — |
| 16 | mcp2mqtt | MIT | Converts MCP tool calls into MQTT commands so language models can control connected lights, motors, and other devices. | [Image](https://x.com/GitHub_Daily/status/1946721719349055520/photo/1) | [Repo](https://github.com/mcp2everything/mcp2mqtt) | [Post](https://x.com/GitHub_Daily/status/1946721719349055520) |

See the [2026-08-02 extended review](reviews/2026-08-02-extended-showcase-batch.md) and [2026-08-01 initial review](reviews/2026-08-01-initial-batch.md) for accepted, deferred, superseded, and rejected candidates.

## Timeline

Browse the [collection timeline](timeline/README.md) to discover projects by the month they were accepted. Timeline entries include the source repository, original X post when available, a concise introduction, and links to original images, videos, demos, or articles.

The acceptance date is not necessarily the project's publication date or the date it was discovered.

## Showcase and Ideas

Browse [Showcase & Ideas](showcase/README.md) for verified X posts that preserve the creator's thinking, build process, trade-offs, images, and video demonstrations. Entries clearly distinguish project authors and team members from community explainers, and a showcase can remain useful even when its project is deferred or does not qualify for the formal open-source catalog.

## Documentation

The [documentation index](docs/README.md) links every guide in English and Simplified Chinese, including the contributing guide, review guide, showcase archive, Code of Conduct, and security policy.

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
- Recommend an X post with the [showcase submission form](https://github.com/s87343472/awesome-ai-hardware/issues/new?template=showcase-submission.yml).
- Submit a Pull Request to correct or update an existing entry.
- Do not disclose sensitive vulnerabilities publicly; follow the [security policy](SECURITY.md).

A recommendation is not an acceptance. Maintainers verify the source repository, license, role of AI, hardware integration, reproducibility, and supporting evidence before listing a project.

## Data and Transparency

Accepted projects are stored in [`data/projects.json`](data/projects.json), while verified X posts are stored separately in [`data/showcases.json`](data/showcases.json). Automated checks validate required fields, categories, dates, URLs, media resources, author relationships, indexes, sorting, and duplicate entries. Review decisions remain visible in the corresponding Issue, Pull Request, or [review record](reviews/README.md).

## Disclaimer

Inclusion means only that a project met this list's public criteria when it was reviewed. It is not an endorsement of the project's security, privacy, hardware reliability, or commercial suitability. Review the code, permissions, data flows, and network access before connecting any project to a physical device.

## License

[MIT](LICENSE) © s87343472 and contributors.
