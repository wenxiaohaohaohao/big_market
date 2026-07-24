# Code

本目录只用于 NSE 项目的解析核验、数值示意和构建脚本。

建议后续按真实内容建立：

```text
code/
├── theory/       # 符号推导和解析条件核验
├── numerical/    # 参数区域、敏感性分析和 source data
└── build_paper.ps1
```

硬规则：

- 输入不得依赖 EL 子项目的工作文件。
- 输出只能写入本项目的 `figures/`、`output/` 或 `tmp/`。
- numerical illustration 不得称为 calibration，除非参数来源已核实。
- 每张图必须同时输出可追踪的 source-data 文件。
