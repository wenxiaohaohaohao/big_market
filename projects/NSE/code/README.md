# Code

本目录只用于 NSE 项目的解析核验、数值示意和构建脚本。当前结构为：

```text
code/
├── theory/
│   └── validate_model.py       # 解析恒等式、有限差分、边界和反例
├── numerical/
│   ├── model.py                # 论文方程和均衡选择
│   └── generate_figures.py     # 三张正文图、机制关闭、政策对照和CSV
└── build_paper.ps1             # XeLaTeX--BibTeX完整构建
```

硬规则：

- 输入不得依赖 EL 子项目的工作文件。
- 输出只能写入本项目的 `figures/`、`output/` 或 `tmp/`。
- numerical illustration 不得称为 calibration，除非参数来源已核实。
- 每张图必须同时输出可追踪的 source-data 文件。

## 环境

- Python 3；
- NumPy；
- SciPy；
- Matplotlib；
- 本机 MiKTeX：
  `D:\application\miktex\miktex\bin\x64`。

当前验证环境使用 Python 3.14、NumPy 2.4.1、SciPy 1.17.0 和
Matplotlib 3.10.8，版本记录在 `code/requirements.txt`。连续收入阈值在固定
组织区间内由 SciPy 的 Brent 方法求根；代码先精确检查 \(G_E,G_L\) 等离散结构
事件。若效应在离散事件处跳跃转正，返回事件本身，不返回依赖网格密度的相邻点。

## 复现命令

在 `projects/NSE` 目录运行：

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r code\requirements.txt
.\.venv\Scripts\python.exe code\theory\validate_model.py
.\.venv\Scripts\python.exe code\numerical\generate_figures.py
.\code\build_paper.ps1
```

输出：

- 正文图：`figures/figure_*.pdf` 和 `figures/figure_*.png`；
- 图形数据：`figures/source_data/*.csv`；
- 干预对照：`figures/source_data/appendix_channel_restriction.csv`；
- 编译论文：`output/NSE_draft.pdf`；
- LaTeX 临时文件：`tmp/latex/`。

构建脚本把 `TEMP` 和 `TMP` 指向 NSE 项目内的 `tmp/`，不把大型临时文件写入
C 盘。
