# Initial Grok Batches / 首批 Grok 候选项目

[English](#english) | [简体中文](#简体中文) · [Review archive / 审核记录](README.md)

**Review date / 审核日期:** 2026-08-01

## English

Seventeen repository URLs from two Grok result batches were checked against the public inclusion rules. Repository source, root files, README documentation, license metadata, hardware path, AI role, and maintenance state were inspected.

The batches did not include specific X post URLs. No project is described as a recent X share in the catalog until its original post is provided or independently verified.

### Accepted

| Project | Decision evidence |
|---|---|
| [AI Doorbell for Home Assistant](https://github.com/nwkuga/ha-ai-doorbell) | MIT-licensed Home Assistant implementation; a multimodal agent analyzes real doorbell camera snapshots and reference images. |
| [ESP32 AI](https://github.com/slvDev/esp32-ai) | MIT-licensed firmware, training code, wiring instructions, measurements, and an on-device ESP32-S3 demo. |
| [esprec](https://github.com/tig/esprec) | Apache-2.0 ESP32 component and host tool designed for agents to inspect real embedded screens over USB. |
| [Hailo Apps](https://github.com/hailo-ai/hailo-apps) | MIT-licensed current official repository with runnable vision, VLM, LLM, and speech pipelines for Hailo accelerators. It replaces the submitted outdated repository. |
| [Home Generative Agent](https://github.com/goruck/home-generative-agent) | MIT-licensed Home Assistant integration with entity control, automation generation, camera analysis, and local-model support. |
| [mcp2mqtt](https://github.com/mcp2everything/mcp2mqtt) | MIT-licensed MCP-to-MQTT bridge with implementation, configuration, tests, and hardware command examples. |
| [Omi](https://github.com/BasedHardware/omi) | MIT-licensed wearable, firmware, applications, and AI backend for audio and context capture. |
| [Open V Robotics System](https://github.com/vahagnmikayelyan/open-v-robotics-system) | MIT-licensed SBC and microcontroller runtime that routes model tool calls to modular robot hardware. |
| [OpenHome Abilities](https://github.com/openhome-dev/abilities) | MIT-licensed voice-agent plugin system with local abilities for Raspberry Pi DevKit GPIO and sensors. |
| [PicoLM](https://github.com/RightNow-AI/picolm) | MIT-licensed C inference runtime with low-memory board instructions and an offline agent integration path. |

### Deferred or not listed

| Submitted repository | Decision | What would change the decision |
|---|---|---|
| [Codex Light](https://github.com/TanShilongMario/Codex-Light-shortcut) | Deferred: relevant and reproducible, but no license file is present. | Add an explicit open-source license. |
| [Buddie](https://github.com/Buddie-AI/Buddie) | Deferred: PCB, firmware, and application sources are present, but the repository has no license file. | Add a license covering the code and hardware design files. |
| [StackChan](https://github.com/m5stack/StackChan) | Deferred: hardware, firmware, apps, and AI-agent features are documented, but no repository license is present. | Add an explicit license covering the published components. |
| [ESP32-S3 Distributed AI](https://github.com/wladimiravila/esp32s3-distributed-ai) | Deferred: strong implementation and hardware documentation, but no license file is present. | Add an explicit open-source license. |
| [Hailo Raspberry Pi 5 Examples](https://github.com/hailo-ai/hailo-rpi5-examples) | Superseded: its README explicitly marks it outdated and points to the current Hailo Apps repository. | The maintained successor was listed instead. |
| [ESP32 AI Environment Monitoring System](https://github.com/SMD111-git/esp32dht-mqi15-with-fastapi-json-data-transfer) | Not listed: no license; the claimed AI layer is a fixed set of numeric threshold rules in `app/ai.py`. | Add a license and a substantive ML or model-based capability in the core path. |
| [Orca](https://github.com/orca-wm/Orca) | Not listed: no license and no direct hardware integration path in the current repository; it is primarily a model and evaluation release. | Add a license and reproducible robot or device integration code. |
| [OpenHome DevKit](https://github.com/openhome-dev/devkit) | Companion resource only: it contains CAD and enclosure files but no license or AI implementation. | Add a hardware license; it may then qualify as a separately reusable hardware component. |

## 简体中文

本次按照公开收录标准核验了两批 Grok 结果中的 17 个仓库 URL，检查范围包括源代码、根目录文件、README、许可证、硬件路径、AI 作用和维护状态。

两批结果均未提供具体 X Post URL。在获得或独立核验原始帖子前，正式目录不会声称这些项目是“近期 X 分享”。

### 正式收录

| 项目 | 通过依据 |
|---|---|
| [AI Doorbell for Home Assistant](https://github.com/nwkuga/ha-ai-doorbell) | MIT 许可证；Home Assistant 实现使用多模态 Agent 分析真实门铃快照和参考照片。 |
| [ESP32 AI](https://github.com/slvDev/esp32-ai) | MIT 许可证；包含固件、训练代码、接线说明、测量结果和 ESP32-S3 端侧演示。 |
| [esprec](https://github.com/tig/esprec) | Apache-2.0；ESP32 组件与主机工具让 Agent 通过 USB 检查真实嵌入式屏幕。 |
| [Hailo Apps](https://github.com/hailo-ai/hailo-apps) | MIT 许可证；Hailo 当前官方仓库，为硬件加速器提供可运行的视觉、VLM、LLM 和语音管线，并替代已过时的投稿仓库。 |
| [Home Generative Agent](https://github.com/goruck/home-generative-agent) | MIT 许可证；支持实体控制、自动化生成、摄像头分析和本地模型的 Home Assistant 集成。 |
| [mcp2mqtt](https://github.com/mcp2everything/mcp2mqtt) | MIT 许可证；包含 MCP 到 MQTT 的实现、配置、测试和硬件命令示例。 |
| [Omi](https://github.com/BasedHardware/omi) | MIT 许可证；包含可穿戴硬件、固件、应用和音频/上下文处理后端。 |
| [Open V Robotics System](https://github.com/vahagnmikayelyan/open-v-robotics-system) | MIT 许可证；在 SBC 与微控制器间把模型工具调用路由至模块化机器人硬件。 |
| [OpenHome Abilities](https://github.com/openhome-dev/abilities) | MIT 许可证；语音 Agent 插件体系包含访问 Raspberry Pi DevKit GPIO 和传感器的本地 Ability。 |
| [PicoLM](https://github.com/RightNow-AI/picolm) | MIT 许可证；C 推理运行时提供低内存硬件运行说明和离线 Agent 集成路径。 |

### 暂缓或不收录

| 投稿仓库 | 结论 | 重新审核条件 |
|---|---|---|
| [Codex Light](https://github.com/TanShilongMario/Codex-Light-shortcut) | 暂缓：相关且可复现，但没有许可证文件。 | 添加明确的开源许可证。 |
| [Buddie](https://github.com/Buddie-AI/Buddie) | 暂缓：已有 PCB、固件和应用源码，但仓库没有许可证。 | 添加覆盖代码与硬件设计文件的许可证。 |
| [StackChan](https://github.com/m5stack/StackChan) | 暂缓：硬件、固件、应用和 AI Agent 功能明确，但仓库没有许可证。 | 添加覆盖已发布组件的明确许可证。 |
| [ESP32-S3 Distributed AI](https://github.com/wladimiravila/esp32s3-distributed-ai) | 暂缓：实现和硬件说明充分，但没有许可证。 | 添加明确的开源许可证。 |
| [Hailo Raspberry Pi 5 Examples](https://github.com/hailo-ai/hailo-rpi5-examples) | 已被替代：首页明确标记为过时并指向当前的 Hailo Apps。 | 已改为收录仍在维护的后继仓库。 |
| [ESP32 AI Environment Monitoring System](https://github.com/SMD111-git/esp32dht-mqi15-with-fastapi-json-data-transfer) | 不收录：没有许可证；所谓 AI 层实际是 `app/ai.py` 中固定的数值阈值规则。 | 添加许可证，并在核心路径加入实质性的机器学习或模型能力。 |
| [Orca](https://github.com/orca-wm/Orca) | 不收录：没有许可证，当前仓库也没有直接硬件集成路径，主要是模型与评测发布。 | 添加许可证和可复现的机器人或设备集成代码。 |
| [OpenHome DevKit](https://github.com/openhome-dev/devkit) | 仅作为配套资源：包含 CAD 与外壳文件，但没有许可证或 AI 实现。 | 添加硬件许可证后，可重新评估为独立可复用的硬件组件。 |
