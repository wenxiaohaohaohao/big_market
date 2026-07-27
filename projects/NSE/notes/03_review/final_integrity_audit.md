# Final Integrity and Reproducibility Audit

日期：2026-07-27
对象：`paper/main.tex`、`paper/appendix.tex`、`paper/references.bib`、三张正文图、
CSV source data 和数值核验代码

## 1. 结论

**项目定义的理论、引用、数值与编译验收：PASS。**

附带一项工具边界：本文没有使用 iThenticate 或 Turnitin。下述原创性检查是公开
网络的特征短语抽查，不能替代投稿前的专业文本重复率检查。

## 2. 理论与内部一致性

| 检查 | 结果 |
|---|---|
| 正文正式命题 | 4 个 |
| 每个命题的证明 | 全部位于 `paper/appendix.tex` |
| LCA、ACA、viability、realization | 定义分离，未用 \(1/c\) 定义比较优势 |
| consumer-side 与 producer-side access | 由同一 \(z\) 连接，但使用不同价格/市场接入方程 |
| \(\omega_C\) 与 \(\rho_r\) | 均由支付流生成 |
| \(G_R,G_Y\) 排序 | 全局只声称 \(G_R\leq G_Y\)；同一连续组织区间才声称严格不等式 |
| local income 与 welfare | 正文明确排除 national-welfare 解释 |
| iceberg cost | 使用 \(\tau_O=\bar\tau_Oe^{-(\gamma+\chi z)G}\geq1\)，不变基准项吸收到 \(\mathcal M_0\) |

`code/theory/validate_model.py` 已核验解析导数、有限差分、三区域存在条件、低
\(F\) 反例、\(\ell_A=\ell_P\)、\(\rho_P=\rho_L\)、\(\chi=0\)、保护政策比较、
政府融资一阶条件以及参数网格中的收入阈值排序。连续阈值由有界网格括定后使用
SciPy 的 Brent 方法求根；离散进入或组织切换仍按均衡边界处理。最终运行结果为：

```text
All analytical, boundary, and finite-difference checks passed.
GP=-0.070176, GL0=0.126129, GX=0.256065
GR=0.046348, GY=0.550487
State supply: G(0.1)=0.3261, G(0.5)=0.4434, G(0.9)=0.7169
```

## 3. 引用与论断

- 16 个 BibTeX 条目全部在期刊、出版社、作者机构或官方研究机构页面重新核实；
- 16 个条目全部被正文引用；
- 无 dangling citation；
- 无 orphan reference；
- 文献允许承载和不允许承载的论断记录在
  `literature/metadata_audit.md`；
- Lin and Wang (2023) 只承担 LCA--ACA 与 state-enabling 理论依据，不承担本文
  的平台阈值；
- Ahn et al. (2011) 只承担固定成本--边际成本的条件性组织排序；
- Couture et al. (2021)、Atkin et al. (2018) 与 Faber (2014) 只承担各自原文
  支持的经验动机，不被扩展为“平台在所有地区降低收入”。

公开网络原创性抽查使用了摘要、理论贡献、组织嵌入、capture drag、facilitation
与 protection 等八个具有辨识度的特征短语，未发现逐字匹配。该结果仅为初步
screening。

## 4. Figure trace

三张图均由标准化参数产生，不使用实际数据，不构成 calibration。

| artifact | source data | transformation | caption claim | limitations |
|---|---|---|---|---|
| Figure 1 | `figures/source_data/figure_1_phase_diagram.csv` | `code/numerical/generate_figures.py` 调用 `model.py` 逐点分类 | 三个组织状态的参数区域非空，且低 \(F\) 时平台中间区可消失 | 只显示标准化参数空间，不表示任何真实地区 |
| Figure 2 | `figures/source_data/figure_2_thresholds.csv` | 同上，逐个 \(c\) 求 \(G_E,G_L,G_R,G_Y\) | LCA 变弱时阈值弱上升；拐点来自组织状态变化 | 曲线是模型比较静态，不是估计置信区间 |
| Figure 3 | `figures/source_data/figure_3_reform_paths.csv` | 同上，按三个 \(\vartheta\) 求 \(G(\vartheta)\) 并遍历 \(z\) | state participation 改变 producer-side 收入路径，不改变基准 consumer platform share | 不识别政策因果效应，也不求最优 \(\vartheta\) |

机制关闭结果位于
`figures/source_data/appendix_mechanism_closures.csv`。图注、正文解释与 CSV
方向一致。

## 5. Numerical-exercise provenance

`experiment_intake_declaration`：

```yaml
status: experiments_declared
type: illustrative numerical exercises
empirical_data: none
calibration_claim: false
```

This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS.

| 文件 | SHA256 |
|---|---|
| `code/numerical/generate_figures.py` | `091EDFEA704888663BA66E8B6F29DC04C750E9198443F58D774033B018201664` |
| `code/numerical/model.py` | `9FA815D13B96F16DD1D180EBB4E2068DBF5100C301A8219CF4567EAB171645E9` |
| `code/theory/validate_model.py` | `381BFB238A8710762C29B42D4D0A74C5FD9B805329DE69F6C35909C3088FB6B2` |
| `code/requirements.txt` | `87F086E6165AD9E2C92449573EA54BA7F91AD5397053A06EABB3467CEC51911C` |
| `figure_1_phase_diagram.csv` | `29D66194A7E0BCF8EC294CDC699C700A81CF653613D46C8EA62DA306D10D8C0D` |
| `figure_2_thresholds.csv` | `22D700325BD34677F4D0A396558623A698CEA1662A1D6E6BF9E89504ED0F04B1` |
| `figure_3_reform_paths.csv` | `39736F9AB730D35810C521954A7AC131E0BFC16FABE3296BD4AF65569886924A` |

## 6. AI research failure-mode check

| failure mode | 结论 | 依据 |
|---|---|---|
| fabricated or mismatched citations | 未发现 | 16 项逐条元数据核实 |
| implementation bug presented as result | 未发现 | 解析式、有限差分和参数网格交叉核验 |
| shortcut reliance | 未发现 | 阈值不是手工写入，全部由模型函数求解 |
| bug-as-insight | 未发现 | 低 \(F\)、反向 payment ordering 和 \(\chi=0\) 均作为反例单独测试 |
| methodology fabrication | 未发现 | 正文明确说明无数据、无 calibration、无 national welfare |
| pipeline frame lock | 未发现 | `el_overlap_audit.md` 固定 EL 主问题与 NSE 解释机制的边界 |
| claim--artifact mismatch | 未发现 | 图、CSV、正文参数和验证输出一致 |

## 7. 编译与版式

- MiKTeX XeLaTeX + BibTeX 构建成功；
- PDF 共 32 页：正文 20 页、参考文献 1 页、证明与稳健性附录 11 页；
- 最终 PDF SHA256：
  `15EA9CD3865FF8C64A60779C4A92E7058BFE20928AAD6C7A925EB98FB81FD260`；
- 无 undefined citation、undefined reference、overfull box 或内部占位措辞；
- 仅有窄表格中的 underfull box，未造成文字溢出或遮挡；
- 已目视检查首页、命题页、三图页、结论页和附录首页。
