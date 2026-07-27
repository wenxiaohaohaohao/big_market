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
- Figure 3 精确结构事件：
  `figures/source_data/figure_3_transition_events.csv`；
- 干预对照：`figures/source_data/appendix_channel_restriction.csv`；
- 编译论文：`output/NSE_draft.pdf`；
- LaTeX 临时文件：`tmp/latex/`。

构建脚本把 `TEMP` 和 `TMP` 指向 NSE 项目内的 `tmp/`，不把大型临时文件写入
C 盘。

## 图形生成原则

- Figure 1 直接填充解析门槛 \(G_E(c)\) 与 \(G_L(c)\) 之间的区域，不使用
  分类网格或图像插值；
- Figure 2 将结构门槛与收入门槛分为两个共享纵轴的面板，避免
  \(G_E=G_R\) 时曲线完全重合造成误读；
- Figure 3 比较低、中、高三个直接给定的共享基础设施水平；在固定组织状态内
  绘制连续曲线，在进入和组织转换点使用精确 Brent 根、开/实心端点和垂直跳跃
  线；不得用普通折线跨越离散均衡事件；
- Figure 3 的跳跃来自代表性候选产业一次性进入或切换组织，不是网格过疏。
  若要从经济结构上平滑，必须扩展为异质企业分布，而不能对现有结果做 spline；
- 所有 PDF 图保持矢量输出。真实的零约束、kink 和 jump 不作统计平滑。
