# BP-Framework / 投资人故事线教练

一套把创业项目事实材料改写成投资人视角叙事的框架与工具集，按「BP 要素」结构化输出故事线与证据账本。

## 直达链接

🔌 联机（需联网）

- 根目录直达（单文件）：👉 https://lotusliuxy.github.io/bp-framework/
- 仓库主页：https://github.com/LotusLiuXY/bp-framework

💾 不联机（本地，无需网络）

下载 / 克隆后，点击本 README 同级相对链接查看内容：[SKILL.md](./SKILL.md)；技能本体为本地文件，无需服务器。

> 单文件落地页（内联 CSS/JS，无外部依赖）可直接访问或下载双击打开；同一相对链接在本地与 GitHub 在线查看时均有效。
## 核心公式

> 好故事 = 不可逆趋势 × 非你不可 × 风险递减路径

投资人买单的不是戏剧性，而是「因果压缩与验证节拍」的能力。

## 框架结构

- **三大核心问题**
  1. 为什么一定会发生？（趋势）
  2. 为什么是你？（人选）
  3. 为什么风险会下降？（路径）

- **六支柱框架**
  1. Timing：抓住时代机遇窗口
  2. Vision：清晰且可信的终局
  3. Who & Why：非你不可
  4. Moat：结构性护城河
  5. Scale：规模化路径的可行性
  6. Proof Points：里程碑式验证

- **支撑案例**
  - Coinbase：抓住不可逆拐点（Timing）
  - NVIDIA CUDA：生态护城河（Moat）
  - AWS：从单点到平台（Scale）
  - Amazon / Xiaomi 飞轮：生态扩张

## 安装方式

1. 将整个 `bp-framework` 目录复制到你的 AI 助手技能目录（见上方「不联机」）。
2. 刷新或重启技能加载。
3. 触发语：「帮我写 BP」「投资人说我故事不够硬」「诊断我的商业计划书」等。

## 目录结构

本仓库根目录即技能内容（clone 后整个文件夹就是 `bp-framework` 技能包）。

```
bp-framework/                ← 仓库根目录（也是技能目录）
├── SKILL.md                       # 技能入口与触发说明
├── README.md                      # 本文件
├── LICENSE                        # MIT 许可证
├── references/
│   ├── framework.md               # 完整框架：问题、证据、句式、误区
│   ├── cases.md                   # Coinbase / NVIDIA / AWS / 飞轮案例
│   └── action-checklist.md        # 行动清单与输出格式
├── scripts/
│   └── bp_diagnostic.py           # Markdown BP 覆盖度诊断脚本
└── assets/
    └── bp-outline-template.md     # 六支柱大纲模板
```

## 使用示例

### 1. 从零写 BP

> 帮我用这个框架写一份 BP，项目是做企业级 AI Agent 的。

技能会按 Timing → Vision → Who&Why → Moat → Scale → Proof Points 的顺序提问，并输出一句话 / 30 秒 / 3 分钟版本的故事。

### 2. 诊断现有 BP

把 BP 内容保存为 `my-bp.md`，然后运行：

```bash
python <助手技能目录>/bp-framework/scripts/bp_diagnostic.py my-bp.md
```

或直接粘贴 BP 内容给 AI 助手，让它用框架做缺口分析。

### 3. 单支柱改写

> 帮我改一下 Moat 这一段，投资人质疑我们没有护城河。

技能会调用 `references/cases.md` 中的 NVIDIA CUDA 案例，并输出结构性护城河的叙事句式。

## 内容边界

本框架严格基于原始 PDF，不引入外部框架（SWOT、波特五力等）。

## 许可证

MIT
