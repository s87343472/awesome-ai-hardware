# Grok Hardware Candidate Batch / Grok 硬件候选批次

**Reviewed / 审核日期：** 2026-09-12 · [Review archive / 审核记录首页](README.md)

## English

This batch started from twenty candidates surfaced from X posts. Repository metadata, root license files, README implementation evidence, linked hardware paths, and provided source-post URLs were reviewed. Eight projects were accepted; OpenSQZ/OpenGlass is retained as a deferred showcase because its repository currently has no declared license.

| Candidate | Decision | Evidence and caveat |
|---|---|---|
| Autonomous OS | Listed | Apache-2.0 root license; documented robot declarations, safety gate, hardware abstraction, agent runtimes, and real robot integrations. Subcomponent and model licenses must still be reviewed by deployers. |
| xiaozhi-esp32 | Listed | MIT; implemented voice pipeline, LLM/MCP control, documented ESP32 hardware matrix, peripherals, and device-side control. |
| ESP-Claw | Listed | Apache-2.0; Espressif repository documents its ESP32 agent loop, supported boards, LLM endpoints, skills, and local IoT execution. |
| OpenSQZ/OpenGlass | Deferred showcase | Strong open research artifacts, firmware, CAD/BOM/build docs, and local multimodal design, but no root LICENSE file or recognized GitHub license metadata. |
| Microduck | Listed | Apache-2.0 software repository; documents 15-servo neural-policy control, RK3566 hardware, and PPO/MuJoCo sim-to-real companion code. Hardware-design terms require separate review before reuse. |
| Reachy Mini | Listed | Apache-2.0 SDK; documents actual camera, audio, motors, simulation, and LLM-capable applications. Hardware-design terms require separate review before reuse. |
| LeRobot | Listed | Apache-2.0; real-robot datasets, policies, hardware interface, training and deployment are core implementation paths. |
| SO-ARM101 | Listed | Apache-2.0; printable leader-follower arm, BOM, assembly guides, and LeRobot teleoperation integration. |
| NIGHTRUN | Listed | Root MIT license confirmed despite GitHub's unrecognized metadata; implements offline quantized LLM inference on UEFI PCs and Raspberry Pi 5. |

Candidates such as RuView, Kenzy, ESP-WHO, and OpenCat remain for a later pass because their claims, source evidence, or catalog scope need further evaluation. Product-only, no-repository, or non-AI-core candidates were not added as formal projects.

## 简体中文

本批次从 X 上发现的 20 个候选开始，核验了仓库元数据、根目录许可证、README 实现证据、硬件资料路径和给出的原帖 URL。最终收录 8 个项目；OpenSQZ/OpenGlass 因仓库当前缺少许可证，保留为暂缓 Showcase。

| 候选 | 结论 | 证据与边界 |
|---|---|---|
| Autonomous OS | 收录 | 根许可证 Apache-2.0；记录机器人声明、安全门、硬件抽象、Agent 运行时和真实机器人集成。部署者仍需审查子组件与模型许可证。 |
| xiaozhi-esp32 | 收录 | MIT；实现语音链路、LLM/MCP 控制，且记录 ESP32 硬件矩阵、外设和设备端控制。 |
| ESP-Claw | 收录 | Apache-2.0；乐鑫仓库记录 ESP32 Agent 闭环、支持的开发板、LLM 端点、技能和本地 IoT 执行。 |
| OpenSQZ/OpenGlass | 暂缓 Showcase | 研究资料、固件、CAD/BOM/构建文档和本地多模态设计都很完整，但没有根目录 LICENSE 文件或可识别的 GitHub 许可证元数据。 |
| Microduck | 收录 | 软件仓库 Apache-2.0；记录 15 舵机神经网络策略控制、RK3566 硬件和 PPO/MuJoCo sim-to-real 配套代码。复用硬件设计前需单独审查其条款。 |
| Reachy Mini | 收录 | SDK 为 Apache-2.0；记录真实相机、音频、电机、仿真和支持 LLM 的应用。复用硬件设计前需单独审查其条款。 |
| LeRobot | 收录 | Apache-2.0；真机数据集、策略、硬件接口、训练和部署都是核心实现路径。 |
| SO-ARM101 | 收录 | Apache-2.0；提供可打印主从机械臂、BOM、组装指南和 LeRobot 遥操作集成。 |
| NIGHTRUN | 收录 | 虽 GitHub 元数据未识别，已确认根 LICENSE 为 MIT；在 UEFI PC 与树莓派 5 上实现离线量化 LLM 推理。 |

RuView、Kenzy、ESP-WHO、OpenCat 等候选留待下一轮，因为其声明、源码证据或目录范围仍需进一步评估。仅产品宣传、无仓库或 AI 不为核心的候选没有加入正式项目。
