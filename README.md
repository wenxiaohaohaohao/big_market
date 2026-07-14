# big_market

`big_market` 是“统一大市场、平台化与地方发展”研究项目的云端总控仓库。

## 当前研究主线

本项目研究全国统一大市场建设与平台化交易扩张背景下，价值创造地与价值捕获地的空间脱钩，以及这种脱钩如何通过本地收入形成、地方留值和有效地方乘数重塑区域发展。

当前优先推进的子项目是：

- `platform_local_multiplier_el`：拟投 *Economics Letters* 的独立理论短文；
- 暂定题目：*Platform Intermediation and Local Multipliers*；
- 核心机制：内生渠道替代、递归空间漏出与消费等价实际收入的符号反转。

## 仓库结构

```text
big_market/
├── materials/
│   └── source_notes/                  # 原始项目材料与参考文献
├── projects/
│   └── platform_local_multiplier_el/
│       ├── notes/                     # 项目备忘录与推导记录
│       └── output/                    # 供审阅的 PDF 等阶段成果
└── README.md
```

后续正式论文源文件、图形和复现代码将分别加入该子项目的 `paper/`、`figures/` 与 `code/` 目录。

## 版本原则

- GitHub 仓库是项目文件的唯一云端主版本；
- 正式论文源文件优先使用 LaTeX/BibTeX；
- PDF 是审阅输出，不作为可编辑主稿；
- 每个明确成果使用独立提交，重要改动通过分支和 Pull Request 审阅；
- ChatGPT 网页与 App 中的讨论结论，应写回仓库内的 README、备忘录或论文源文件。

## 当前状态

仓库已完成首次材料归档。下一步是冻结 EL 短文的最小模型、建立 LaTeX 稿件骨架，并完成首周文献查重。

