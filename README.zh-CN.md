# Awesome AI Hardware

> 汇集将 AI、大语言模型或 Agent 与真实硬件结合的开源项目。

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Validate](https://github.com/s87343472/awesome-ai-hardware/actions/workflows/validate.yml/badge.svg)](https://github.com/s87343472/awesome-ai-hardware/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

[English](README.md) | **简体中文**

Awesome AI Hardware 是一个经过审核的 **AI × 硬件** 开源项目合集。我们关注真正把大模型、Agent、语音 AI、视觉 AI 或机器学习与智能家居、IoT、可穿戴设备、机器人及边缘设备结合起来的可复现项目。

这里不是新闻流，也不是未经核验的链接堆。每个正式收录项目都必须满足明确的开源、相关性、证据和可复现性要求。

## 目录

- [项目分类](#项目分类)
- [项目列表](#项目列表)
- [收录时间线](#收录时间线)
- [文档索引](#文档索引)
- [收录标准](#收录标准)
- [参与贡献](#参与贡献)
- [数据与透明度](#数据与透明度)
- [免责声明](#免责声明)
- [许可证](#许可证)

## 项目分类

- 智能家居与 IoT
- AI 可穿戴设备
- 语音助手与 AI 伴侣
- 机器人与具身智能
- 边缘 AI 与微控制器
- 硬件控制协议、桥接层与基础设施
- AI 状态可视化与创意硬件

## 项目列表

### 智能家居与 IoT

- [AI Doorbell for Home Assistant](https://github.com/nwkuga/ha-ai-doorbell) — 通过视觉语言模型比较真实门铃快照与已标注参考照片，并在 Home Assistant 与 Telegram 中完成识别和纠正。`MIT` · [流程图](https://github.com/nwkuga/ha-ai-doorbell/blob/main/docs/img/04-flow.svg) · [文档](https://github.com/nwkuga/ha-ai-doorbell/tree/main/docs)
- [Home Generative Agent](https://github.com/goruck/home-generative-agent) — 将 LangGraph Agent 集成到 Home Assistant，用云端或本地模型控制实体、创建自动化、分析摄像头并提供异常提醒。`MIT` · [演示](https://github.com/goruck/home-generative-agent/blob/main/assets/create_automation.gif) · [文档](https://github.com/goruck/home-generative-agent/blob/main/docs/installation.md)

### AI 可穿戴设备

- [Omi](https://github.com/BasedHardware/omi) — 结合开源可穿戴硬件和配套应用，提供实时转写、摘要、行动项提取和个人记忆检索。`MIT` · [文档](https://docs.omi.me/) · [网站](https://omi.me/)

### 语音助手与 AI 伴侣

- [OpenHome Abilities](https://github.com/openhome-dev/abilities) — 为 OpenHome 语音 Agent 提供插件，其中本地 Ability 可运行在 Raspberry Pi DevKit 上并访问 GPIO 与传感器。`MIT` · [文档](https://docs.openhome.com/) · [DevKit 文件](https://github.com/openhome-dev/devkit)

### 机器人与具身智能

- [Open V Robotics System](https://github.com/vahagnmikayelyan/open-v-robotics-system) — 在 SBC 与 Raspberry Pi Pico 之间，通过模块化驱动把受权限控制的 LLM 工具调用路由至电机、摄像头、传感器和其他机器人硬件。`MIT` · [界面](https://github.com/vahagnmikayelyan/open-v-robotics-system/blob/main/docs/images/main%20screen.png) · [文档](https://github.com/vahagnmikayelyan/open-v-robotics-system/tree/main/docs)

### 边缘 AI 与微控制器

- [ESP32 AI](https://github.com/slvDev/esp32-ai) — 在 ESP32-S3 上完全离线运行 2890 万参数语言模型，并将生成文本输出到连接的显示屏。`MIT` · [演示](https://github.com/slvDev/esp32-ai/blob/main/media/esp32-ple-demo.gif) · [实验结果](https://github.com/slvDev/esp32-ai/blob/main/RESULTS.md)
- [Hailo Apps](https://github.com/hailo-ai/hailo-apps) — 为树莓派 5 等平台上的 Hailo 加速器提供可运行的计算机视觉、VLM、LLM 与语音应用。`MIT` · [演示](https://github.com/hailo-ai/hailo-apps/blob/main/doc/images/agentic_ai.gif) · [文档](https://github.com/hailo-ai/hailo-apps/blob/main/doc/README.md)
- [PicoLM](https://github.com/RightNow-AI/picolm) — 通过零依赖 C 推理引擎，在低内存 RISC-V 和树莓派设备上运行量化十亿参数 GGUF 模型。`MIT` · [硬件介绍](https://github.com/RightNow-AI/picolm/blob/main/picolm.jpg) · [技术说明](https://github.com/RightNow-AI/picolm/blob/main/BLOG.md)

### 协议、桥接层与基础设施

- [esprec](https://github.com/tig/esprec) — 通过 ESP32 端组件和 USB 主机工具，让编码 Agent 捕获并检查真实设备屏幕。`Apache-2.0` · [演示](https://github.com/tig/esprec/blob/main/docs/examples/xuss-c-screens.gif) · [Agent 指南](https://github.com/tig/esprec/blob/main/AGENTS.md)
- [mcp2mqtt](https://github.com/mcp2everything/mcp2mqtt) — 把 MCP 工具调用转换成 MQTT 命令，让大模型控制联网灯光、电机和其他设备。`MIT` · [架构图](https://github.com/mcp2everything/mcp2mqtt/blob/main/docs/images/stru_chs.png) · [工作流](https://github.com/mcp2everything/mcp2mqtt/blob/main/docs/images/workflow_chs.png)

通过、暂缓、替代和拒绝项目的完整依据见 [2026-08-01 审核记录](reviews/2026-08-01-initial-batch.md)。

## 收录时间线

可以通过[收录时间线](timeline/README.md)按正式收录月份浏览项目。时间线条目会展示源代码仓库、可用的原始 X Post、简短介绍，以及原始图片、视频、Demo 或文章链接。

正式收录日期不等于项目发布日期，也不一定等于项目被发现的日期。

## 文档索引

[文档总索引](docs/README.md)集中列出贡献指南、审核指南、社区行为准则和安全政策的英文、简体中文版本。

## 收录标准

项目必须同时满足以下条件：

1. 有可公开访问的源代码仓库；
2. AI、LLM 或 Agent 是核心能力，而不是营销标签；
3. 与真实硬件、传感器、执行器或设备有直接交互；
4. 提供足以理解或复现项目的说明；
5. 仓库中有明确的开源许可证；
6. 项目描述和相关声明可以通过公开来源核验。

完整规则请阅读[贡献指南](CONTRIBUTING.zh-CN.md)和[审核指南](docs/REVIEW_GUIDE.zh-CN.md)。

## 参与贡献

- 推荐项目：使用[项目投稿表单](https://github.com/s87343472/awesome-ai-hardware/issues/new?template=project-submission.yml)
- 修正或更新已收录项目：直接提交 Pull Request
- 安全问题：请勿公开披露敏感漏洞，参见[安全政策](SECURITY.zh-CN.md)

被推荐不等于被收录。维护者会在收录前核验源代码仓库、许可证、AI 的实际作用、硬件集成方式、可复现性和来源证据。

## 数据与透明度

正式收录的项目也会保存在 [`data/projects.json`](data/projects.json) 中。自动检查会验证必填字段、分类、收录与核验日期、URL、媒体资源、排序和重复项；审核结论会保留在对应的 Issue 或 Pull Request 中。

## 免责声明

收录仅表示项目在审核时符合本合集的公开标准，不代表维护者对其安全性、隐私性、硬件可靠性或商业适用性作出背书。将项目连接到真实设备前，请自行审查代码、权限、数据流和网络访问。

## 许可证

[MIT](LICENSE) © s87343472 及所有贡献者。
