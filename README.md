<!-- for modelscope yaml info
---
language:
- zh
tags:
- SeaSageAI_InternLM2
- internlm2
frameworks:
- pytorch
tasks:
- text-generation
license: Apache License 2.0
---
-->
# SeaSageAI_InternLM2

<br />
<!-- PROJECT LOGO -->

<p align="center">
  <a href="https://github.com/2001wjh/SeaSageAI_InternLM2/">
    <img src="assets/logo.png" alt="Logo" width="50%">
  </a>


## 📢 介绍

**SeaSageAI —— 海军专家大模型** 是一个能够根据给定的商品特点从激发用户购买意愿角度出发进行商品解说的卖货主播大模型。以其独特的智能魅力，将彻底改变您的购物体验。该模型能深度理解商品特点，以生动、精准的语言为商品量身打造解说词，让每一件商品都焕发出诱人的光彩。无论是细节之处，还是整体效果，都能通过其细腻、独到的解说，激发用户的购买欲望。

模型用 [xtuner](https://github.com/InternLM/xtuner) 在 [InternLM2](https://github.com/InternLM/InternLM) 的基础上指令微调而来，部署集成了 LMDeploy **加速推理**🚀，支持 **ASR 语音生成文字** 🎙️，支持 **RAG 检索增强生成**📚做到可以随时更新说明书指导主播生成文案，支持 **Agent 通过网络查询快递信息** 🌐，还加入带有感情的 **TTS 文字转语音**🔊生成，最后还会**生成主播数字人视频**🦸，让主播不止于文字介绍。

**功能点总结：**

- 📜 军事舰艇相关信息一键生成
- 🚀 KV cache + Turbomind 推理加速
- 📚 RAG 检索增强生成
- 🌐 Agent 借助互联网查询实时军事信息


**开源不易，如果本项目帮到大家，可以右上角帮我点个 star~ ⭐⭐ , 您的 star ⭐是我们最大的鼓励，谢谢各位！**  

## 🎉 NEWS

- [2024.07.17] **项目企划完成**，开始进行相关实验！


## 📌 目录

## 🛠 架构图

![架构图](./assets/SeaSageAI项目架构.png)

## 📺️ 讲解视频

干货满满，欢迎一键三连（疯狂暗示🍺）


## 🖼 演示

**在线体验地址**：


## ⚙ Model Zoo

| 模型                            | 基座             | 数据量           | ModelScope(HF)                                                                          | OpenXLab(HF)                                                                                                                                                            |
| ------------------------------- | ---------------- | ---------------- | --------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| streamer-sales-lelemiao-7b      | interlm2-chat-7b | about 40w Toeken | [ModelScope](https://modelscope.cn/models/HinGwenWoong/streamer-sales-lelemiao-7b)      | [![Open in OpenXLab](https://cdn-static.openxlab.org.cn/header/openxlab_models.svg)](https://openxlab.org.cn/models/detail/HinGwenWong/streamer-sales-lelemiao--7b/)    |
| streamer-sales-lelemiao-7b-4bit | interlm2-chat-7b | about 40w Toeken | [ModelScope](https://modelscope.cn/models/HinGwenWoong/streamer-sales-lelemiao-7b-4bit) | [![Open in OpenXLab](https://cdn-static.openxlab.org.cn/header/openxlab_models.svg)](https://openxlab.org.cn/models/detail/HinGwenWong/streamer-sales-lelemiao-7b-4bit) |



## 🧱 开发计划

- [x] 生成多个产品数据集
- [x] 根据产品生成话术，每个都是5个往来的对话
- [ ] 支持多种角色
  - [x] 乐乐喵——可爱萝莉，
  - [ ] 更多角色正在规划中，敬请期待！
- [x] 模型推理加速
- [x] 接入 RAG 解读产品文档
- [x] 支持上传新商品并生成新 RAG 数据库
- [x] TTS 生成语音
- [x] 数字人
- [x] 接入 Agent，支持订单情况、收货时间等实时信息
- [x] ASR
- [x] 前后端分离解耦
- [ ] 多模态


## 💕 致谢

- [InternLM](https://github.com/InternLM/InternLM)
- [xtuner](https://github.com/InternLM/xtuner)
- [LMDeploy](https://github.com/InternLM/LMDeploy)
- [lagent](https://github.com/InternLM/lagent)

感谢上海人工智能实验室推出的书生·浦语大模型实战营，为我们的项目提供宝贵的技术指导和强大的算力支持。

## 🎫 开源许可证

该项目采用 [Apache License 2.0 开源许可证](https://github.com/PeterH0323/Streamer-Sales/LICENSE) 同时，请遵守所使用的模型与数据集的许可证。

## 🔗 引用

如果本项目对您的工作有所帮助，请使用以下格式引用：

```bibtex
@misc{SeaSageAI_InternLM2,
    title={SeaSageAI_InternLM},
    author={SeaSageAI_InternLM},
    url={https://github.com/wjh2001/SeaSageAI_InternLM},
    year={2024}
}
```
