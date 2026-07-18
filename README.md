# big_market

`big_market` 是“统一大市场、平台化与地方发展”研究项目的云端总控仓库。

## 当前研究主线

本项目研究全国统一大市场建设与平台化交易扩张背景下，价值创造地与价值捕获地的空间脱钩，以及这种脱钩如何通过本地收入形成、地方留值和有效地方乘数重塑区域发展。

当前优先推进的子项目是：

- `platform_local_multiplier_el`：拟投 *Economics Letters* 的独立理论短文；
- 固定题目：**统一市场、平台化与地方乘数：价值捕获的空间重组**；
- 英文题目：*Market Integration, Platformization, and Local Multipliers:
  The Spatial Reorganization of Value Capture*；
- 核心问题：市场一体化何时主要产生 market-access gain，何时因平台
  中介重组降低 local value capture，以及本地组织能力如何决定平台
  扩张能否转化为本地收入和地方乘数。

## 仓库结构

```text
big_market/
├── materials/
│   └── source_notes/                  # 原始项目材料与参考文献
├── projects/
│   └── platform_local_multiplier_el/
│       ├── paper/                     # 唯一正式 LaTeX 主稿、附录与 BibTeX
│       ├── figures/                   # 论文图形
│       ├── code/                      # 推导核验与示意性数值代码
│       ├── notes/                     # 项目备忘录与推导记录
│       ├── literature/                # 经核实的本地文献
│       ├── output/                    # 编译 PDF 与阶段审阅文件
│       └── README.md
└── README.md
```

正式论文从 `projects/platform_local_multiplier_el/paper/main.tex` 编译。

## 版本原则

- GitHub 仓库是项目文件的唯一云端主版本；
- `paper/main.tex` 是唯一正式主稿，`paper/references.bib` 是唯一文献库；
- `paper/appendix.tex` 只能由 `main.tex` 载入，不单独作为论文版本；
- PDF 是审阅输出，不作为可编辑主稿；
- 网页端、Word 或聊天中的文字均不作为平行主稿，确认后的修改必须写回本地 LaTeX；
- 每个明确成果使用独立提交，重要改动通过分支和 Pull Request 审阅；
- ChatGPT 网页与 App 中的讨论结论，应写回仓库内的 README、备忘录或论文源文件。

## 跨端工作流

| 环境 | 主要用途 | 版本地位 |
|---|---|---|
| 桌面 App 本地仓库 | 编辑 LaTeX/BibTeX、推导公式、写代码、生成图形、编译并检查 PDF | 唯一可编辑论文源 |
| GitHub `big_market` | 版本控制、跨设备同步和协作审阅 | 唯一云端版本库 |
| 网页端 Project/聊天 | 讨论研究问题、文献定位、审阅 PDF、比较版本和决定模型取舍 | 讨论与反馈，不维护平行主稿 |
| Library | 保存少量关键阶段的 Markdown、PDF、代码与附录快照 | 里程碑存档，不是工作副本 |

同一个聊天可在网页端和 App 端延续；同一 Project 中另开聊天时，不依赖聊天记忆作为项目记录。所有会改变研究问题、模型、命题、文献定位或投稿方案的决定，必须写回仓库中的 README、`notes/` 或论文源文件。

Library 只在以下节点更新：

1. 模型设定冻结版；
2. 第一版英文全文；
3. 合作者修改版；
4. 投稿版；
5. 最终代码与附录。

Library 中的文件只用于跨端参考和阶段留档。后续修改始终回到桌面 App 的本地仓库完成，再通过 Git 提交同步；不直接修改 Library、网页端 Word 或 PDF 形成第二份主稿。

## 当前状态

EL 子项目正在按固定题目与核心问题重写方案 A。当前正式模型保留
CES 内部渠道选择和地方收入固定点，并加入本地组织能力对平台交易留值
的影响；主文、附录、解析核验和最终 PDF 必须使用同一模型定义。

