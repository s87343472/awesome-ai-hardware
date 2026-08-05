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
- [展示与灵感](#展示与灵感)
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

| 序号 | 名称 | 许可证 | 介绍 | 图片/视频 | GitHub | X |
|---:|---|---|---|---|---|---|
| 1 | AI Doorbell for Home Assistant | MIT | 使用视觉语言模型识别真实门铃快照中的人物，并通过 Home Assistant 与 Telegram 完成纠正。 | [图片](https://github.com/nwkuga/ha-ai-doorbell/blob/main/docs/img/04-flow.svg) | [仓库](https://github.com/nwkuga/ha-ai-doorbell) | — |
| 2 | Anima | Apache-2.0 | 在本地运行 Agent OS，结合米家设备状态、长期记忆和设备技能规划真实控制动作。 | [图片](https://github.com/Fullive-AI/Anima/blob/main/docs/images/bedroom.svg) | [仓库](https://github.com/Fullive-AI/Anima) | [帖子](https://x.com/GitHub_Daily/status/2068687909839073743) |
| 3 | Home Generative Agent | MIT | 为 Home Assistant 提供实体控制、自动化创建、摄像头分析和异常提醒，支持云端或本地模型。 | [视频](https://x.com/lindostangel/status/2081732515228995858) | [仓库](https://github.com/goruck/home-generative-agent) | [帖子](https://x.com/lindostangel/status/2081732515228995858) |

### AI 可穿戴设备

| 序号 | 名称 | 许可证 | 介绍 | 图片/视频 | GitHub | X |
|---:|---|---|---|---|---|---|
| 4 | LightMem-Ego | MIT | 把 Rokid AI 眼镜的第一视角摄像头与音频流组织成可查询的分层多模态记忆。 | [图片](https://github.com/zjunlp/LightMem-Ego/blob/main/figs/thumbnail.png) | [仓库](https://github.com/zjunlp/LightMem-Ego) | [帖子](https://x.com/aigclink/status/2079059418168311813) |
| 5 | Omi | MIT | 结合可穿戴硬件和配套应用，提供转写、摘要、行动项提取和个人记忆检索。 | [图片](https://x.com/CycleDecoded/status/2082693629953659191/photo/1) | [仓库](https://github.com/BasedHardware/omi) | [帖子](https://x.com/CycleDecoded/status/2082693629953659191) |

### 语音助手与 AI 伴侣

| 序号 | 名称 | 许可证 | 介绍 | 图片/视频 | GitHub | X |
|---:|---|---|---|---|---|---|
| 6 | OpenHome Abilities | MIT | 为语音 Agent 提供插件，本地 Ability 可运行在 Raspberry Pi DevKit 上并访问 GPIO 与传感器。 | — | [仓库](https://github.com/openhome-dev/abilities) | — |

### 机器人与具身智能

| 序号 | 名称 | 许可证 | 介绍 | 图片/视频 | GitHub | X |
|---:|---|---|---|---|---|---|
| 7 | Cyclo Intelligence | Apache-2.0 | 覆盖 ROBOTIS AI Worker 数据采集、策略训练、推理和真机执行，支持 Behavior Tree 与 VLA 混合控制。 | [视频](https://youtu.be/jRcUuwxFk_Y) | [仓库](https://github.com/ROBOTIS-GIT/cyclo_intelligence) | [帖子](https://x.com/passionvirus/status/2074051976133046428) |
| 8 | Open V Robotics System | MIT | 在 SBC 与 Raspberry Pi Pico 之间，把受权限控制的 LLM 工具调用路由至电机、摄像头和传感器。 | [图片](https://github.com/vahagnmikayelyan/open-v-robotics-system/blob/main/docs/images/main%20screen.png) | [仓库](https://github.com/vahagnmikayelyan/open-v-robotics-system) | — |
| 9 | OpenArm | Apache-2.0 + 组件许可证 | 提供顺应性人形机械臂及开放 CAD、控制、遥操作、数据集、MuJoCo 与 Isaac Lab 物理 AI 栈。 | [视频](https://x.com/lukas_m_ziegler/status/2043595780695457957) | [仓库](https://github.com/enactic/OpenArm) | [帖子](https://x.com/lukas_m_ziegler/status/2043595780695457957) |
| 10 | reBot-DevArm | CERN-OHL-W-2.0 | 开放机械臂结构和 BOM，并连接 ROS、Isaac Sim、LeRobot 与视觉抓取工作流。 | [图片](https://x.com/IlirAliu_/status/2040702009720881214/photo/1) | [仓库](https://github.com/Seeed-Projects/reBot-DevArm) | [帖子](https://x.com/IlirAliu_/status/2040702009720881214) |

### 边缘 AI 与微控制器

| 序号 | 名称 | 许可证 | 介绍 | 图片/视频 | GitHub | X |
|---:|---|---|---|---|---|---|
| 11 | Autonomous Computer | MIT | 提供 2、4、8 GPU 本地 AI 电脑的开放 BOM、CAD、装配资料和完整构建指南。 | [视频](https://x.com/dee_hw/status/2065803426429346115) | [仓库](https://github.com/autonomous-ai/autonomous-computer) | [帖子](https://x.com/dee_hw/status/2065803429071765819) |
| 12 | ESP32 AI | MIT | 在 ESP32-S3 上完全离线运行 2890 万参数语言模型，并将生成文本输出到显示屏。 | [视频](https://github.com/slvDev/esp32-ai/blob/main/media/esp32-ple-demo.gif) | [仓库](https://github.com/slvDev/esp32-ai) | [帖子](https://x.com/GithubAwesome/status/2081550211990569069) |
| 13 | Hailo Apps | MIT | 为树莓派 5 等平台上的 Hailo 加速器提供可运行的视觉、VLM、LLM 与语音应用。 | [视频](https://github.com/hailo-ai/hailo-apps/blob/main/doc/images/agentic_ai.gif) | [仓库](https://github.com/hailo-ai/hailo-apps) | — |
| 14 | PicoLM | MIT | 通过零依赖 C 推理引擎，在低内存 RISC-V 和树莓派设备上运行量化十亿参数 GGUF 模型。 | [图片](https://x.com/GitHub_Daily/status/2083183407132254242/photo/1) | [仓库](https://github.com/RightNow-AI/picolm) | [帖子](https://x.com/GitHub_Daily/status/2083183407132254242) |

### 协议、桥接层与基础设施

| 序号 | 名称 | 许可证 | 介绍 | 图片/视频 | GitHub | X |
|---:|---|---|---|---|---|---|
| 15 | esprec | Apache-2.0 | 通过 ESP32 端组件和 USB 主机工具，让编码 Agent 捕获并检查真实设备屏幕。 | [视频](https://github.com/tig/esprec/blob/main/docs/examples/xuss-c-screens.gif) | [仓库](https://github.com/tig/esprec) | — |
| 16 | mcp2mqtt | MIT | 把 MCP 工具调用转换成 MQTT 命令，让大模型控制联网灯光、电机和其他设备。 | [图片](https://x.com/GitHub_Daily/status/1946721719349055520/photo/1) | [仓库](https://github.com/mcp2everything/mcp2mqtt) | [帖子](https://x.com/GitHub_Daily/status/1946721719349055520) |

### AI 状态可视化与创意硬件

| 序号 | 名称 | 许可证 | 介绍 | 图片/视频 | GitHub | X |
|---:|---|---|---|---|---|---|
| 17 | findphone † | 未声明许可证（维护者例外） | 由 Claude 协助制作的 macOS 蓝牙 RSSI 寻机工具，通过仪表和声音反馈引导用户找到附近手机。 | [视频](https://x.com/un1c0rnioz/status/2084686552299634805) | [仓库](https://github.com/ben-z/findphone) | [帖子](https://x.com/un1c0rnioz/status/2084686552299634805) |

† 维护者批准的例外：AI 用于制作过程而非运行时，且仓库没有声明许可证。详见[审核记录](reviews/2026-08-05-findphone-showcase.md)。

通过、暂缓、替代和拒绝项目的完整依据见 [2026-08-02 扩展审核](reviews/2026-08-02-extended-showcase-batch.md)和 [2026-08-01 初始审核](reviews/2026-08-01-initial-batch.md)。

## 收录时间线

可以通过[收录时间线](timeline/README.md)按正式收录月份浏览项目。时间线条目会展示源代码仓库、可用的原始 X Post、简短介绍，以及原始图片、视频、Demo 或文章链接。

正式收录日期不等于项目发布日期，也不一定等于项目被发现的日期。

## 展示与灵感

通过 [Showcase & Ideas / 展示与灵感](showcase/README.md) 浏览已核验的 X Post，了解创作者的想法、制作过程、取舍、图片与视频演示。每个条目都会区分项目作者、项目团队和社区解读；即使项目暂缓收录或不符合正式开源目录门槛，有价值的思路仍可留在 Showcase 中。

## 文档索引

[文档总索引](docs/README.md)集中列出贡献指南、审核指南、Showcase、社区行为准则和安全政策的英文、简体中文版本。

## 收录标准

项目通常必须同时满足以下条件：

1. 有可公开访问的源代码仓库；
2. AI、LLM 或 Agent 是核心能力，而不是营销标签；
3. 与真实硬件、传感器、执行器或设备有直接交互；
4. 提供足以理解或复现项目的说明；
5. 仓库中有明确的开源许可证；
6. 项目描述和相关声明可以通过公开来源核验。

当项目具有特殊的教学价值或制作故事价值时，维护者可作出少量、有记录的例外批准。例外会在项目目录和审核记录中明确标注，不改变普通投稿的收录标准。

完整规则请阅读[贡献指南](CONTRIBUTING.zh-CN.md)和[审核指南](docs/REVIEW_GUIDE.zh-CN.md)。

## 参与贡献

- 推荐项目：使用[项目投稿表单](https://github.com/s87343472/awesome-ai-hardware/issues/new?template=project-submission.yml)
- 推荐 X Post：使用 [Showcase 投稿表单](https://github.com/s87343472/awesome-ai-hardware/issues/new?template=showcase-submission.yml)
- 修正或更新已收录项目：直接提交 Pull Request
- 安全问题：请勿公开披露敏感漏洞，参见[安全政策](SECURITY.zh-CN.md)

被推荐不等于被收录。维护者会在收录前核验源代码仓库、许可证、AI 的实际作用、硬件集成方式、可复现性和来源证据。

## 数据与透明度

正式项目保存在 [`data/projects.json`](data/projects.json)，核验后的 X Post 则单独保存在 [`data/showcases.json`](data/showcases.json)。自动检查会验证必填字段、分类、日期、URL、媒体资源、作者关系、索引、排序和重复项；审核结论会保留在对应的 Issue、Pull Request 或[审核记录](reviews/README.md)中。

## 免责声明

收录仅表示项目在审核时符合本合集的公开标准，不代表维护者对其安全性、隐私性、硬件可靠性或商业适用性作出背书。将项目连接到真实设备前，请自行审查代码、权限、数据流和网络访问。

## 许可证

[MIT](LICENSE) © s87343472 及所有贡献者。
