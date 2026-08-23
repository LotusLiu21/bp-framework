# BP-Framework / 投资人故事线教练

一个基于「BP 要素」PDF 的 WorkBuddy Skill，用于把创业项目的事实材料改写成投资人视角的叙事。

## 直达链接

### 🔌 联机（需联网）
- 仓库主页 / 源文件：https://github.com/LotusLiuXY/bp-framework
- 在 WorkBuddy 中安装后，用「帮我写 BP」「投资人说我故事不够硬」等触发语即可调用

### 💾 不联机（本地，无需网络）
- 将整个 `bp-framework` 目录克隆 / 下载到本地 Skill 目录后即可离线使用：
  - 用户级：`~/.workbuddy/skills/`
  - 项目级：`<project>/.workbuddy/skills/`
- 点击本 README 同级相对链接查看内容：[SKILL.md](./SKILL.md)

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

1. 将整个 `bp-framework` 目录复制到你的 WorkBuddy skills 目录（见上方「不联机」）。
2. 重启 WorkBuddy 或刷新 skills。
3. 触发语：「帮我写 BP」「投资人说我故事不够硬」「诊断我的商业计划书」等。

## 目录结构

本仓库根目录即 Skill 内容（clone 后整个文件夹就是 `bp-framework` Skill）。

```
bp-framework/                ← 仓库根目录（也是 Skill 目录）
├── SKILL.md                       # Skill 入口与触发说明
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

Skill 会按 Timing → Vision → Who&Why → Moat → Scale → Proof Points 的顺序提问，并输出一句话 / 30 秒 / 3 分钟版本的故事。

### 2. 诊断现有 BP

把 BP 内容保存为 `my-bp.md`，然后运行：

```bash
python ~/.workbuddy/skills/bp-framework/scripts/bp_diagnostic.py my-bp.md
```

或直接粘贴 BP 内容给 WorkBuddy，让它用框架做缺口分析。

### 3. 单支柱改写

> 帮我改一下 Moat 这一段，投资人质疑我们没有护城河。

Skill 会调用 `references/cases.md` 中的 NVIDIA CUDA 案例，并输出结构性护城河的叙事句式。

## 内容边界

本 Skill 严格基于原始 PDF，不引入外部框架（SWOT、波特五力等）。

## 许可证

MIT
