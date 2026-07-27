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
| \(G_A\) 与 \(G_E\) | 分别由现实双重相对交付成本和零利润条件生成，未把盈利能力当作 ACA |
| \(G_L\) | \(F>\bar F\) 时由 \(G_X\) 决定；中间区消失时改由 \(G_L^0\) 决定 |
| consumer-side 与 producer-side access | 由同一 \(z\) 连接，但使用不同价格/市场接入方程 |
| \(\omega_C\) 与 \(\rho_r\) | 均由支付流生成 |
| \(G_R,G_Y\) 排序 | 全局只声称 \(G_R\leq G_Y\)；同一连续组织区间才声称严格不等式 |
| local income 与 welfare | 正文明确排除 national-welfare 解释 |
| iceberg cost | 使用 \(\tau_O=\bar\tau_Oe^{-(\gamma+\chi z)G}\geq1\)，不变基准项吸收到 \(\mathcal M_0\) |

`code/theory/validate_model.py` 已核验解析导数、有限差分、ACA 边界、三区域存在
条件、低 \(F\) 反例、\(\ell_A=\ell_P\)、\(\ell_P>\ell_A\)、
\(\rho_P=\rho_L\)、\(\chi=0\)、同一本地化结果下的保护政策比较、政府融资一阶
条件以及参数网格中的收入阈值排序。连续阈值由有界网格括定后使用
SciPy 的 Brent 方法求根；离散进入或组织切换仍按均衡边界处理。最终运行结果为：

```text
All analytical, boundary, and finite-difference checks passed.
GA=0.611694, GP=0.330038, GL0=0.652932, GX=0.881716
GR=0.330500, GY=0.835116
State supply: G(0.05)=0.3172, G(0.50)=0.4724, G(0.95)=1.0258
State thresholds: vartheta_A=0.6991, vartheta_E=0.1044,
vartheta_L=0.8928, vartheta_R=0.1063, vartheta_Y=0.8694
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
| Figure 1 | `figures/source_data/figure_1_phase_diagram.csv` | `code/numerical/generate_figures.py` 调用 `model.py` 逐点分类，并单独计算 ACA 指数 | 三个组织状态的参数区域非空；虚线 ACA 边界不等于均衡状态边界 | 只显示标准化参数空间，不表示任何真实地区 |
| Figure 2 | `figures/source_data/figure_2_thresholds.csv` | 同上，逐个 \(c\) 求 \(G_A,G_E,G_L,G_R,G_Y\) | LCA 变弱时五个门槛弱上升；拐点来自 active mode 或状态切换 | 曲线是模型比较静态，不是估计置信区间 |
| Figure 3 | `figures/source_data/figure_3_reform_paths.csv` | 同上，按 \(\vartheta=0.05,0.50,0.95\) 求 \(G(\vartheta)\) 并遍历 \(z\) | 三条路径分别展示进入前、平台依赖和本地嵌入；consumer share 保持共同 | 不识别政策因果效应，也不求最优 \(\vartheta\) |

机制关闭结果位于
`figures/source_data/appendix_mechanism_closures.csv`。同一本地化结果下的
facilitation--protection 对照位于
`figures/source_data/appendix_policy_comparison.csv`。图注、正文解释、附录表格
与 CSV 方向一致。

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
| `code/numerical/generate_figures.py` | `AEA1229B1BF3CC56EBA07460BEE751E0EB3CE3D7B3305E34CF9D3976C7600875` |
| `code/numerical/model.py` | `5DD219CF6E9FB093B9E1AAB000C22045B2AFD543C02B9F0D9E1C5932EDA96C19` |
| `code/theory/validate_model.py` | `C3EB708DF9A0FF733A13708C7480BF97FA3EA02CBF28B0EBCA0D40D0AA68F007` |
| `code/requirements.txt` | `87F086E6165AD9E2C92449573EA54BA7F91AD5397053A06EABB3467CEC51911C` |
| `figure_1_phase_diagram.csv` | `304310BAE917CC7AABCA5B4EE2321DF9E61780A84693B3AB4F271B2AC6EEA100` |
| `figure_2_thresholds.csv` | `65481BD1F703F4818DB3A84BE40DFA4327DD838F5E61DC39D79995C8A0614509` |
| `figure_3_reform_paths.csv` | `90D750B8D79FDB8EEBA7F867D37963B511B0D8E0AAD2C8C804C6FD4F1BE1A8D5` |
| `appendix_mechanism_closures.csv` | `708031E752C68DE24F31F846F7084C5B3ADEA3748168751017731572EFA7FA72` |
| `appendix_policy_comparison.csv` | `A54233276DCE10DA39C2F0F77B3B4CC174BC3F3B505EF5A2FA9A87D6273855BC` |

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
- PDF 共 34 页：正文 21 页、参考文献 1 页、证明与稳健性附录 12 页；
- 最终 PDF SHA256：
  `101E66AE35E17972BF1887CE2A60AA01A8B083FAAEE5954CB943F3B8B076B6AE`；
- 无 undefined citation、undefined reference、overfull box 或内部占位措辞；
- 仅有窄表格中的 underfull box，未造成文字溢出或遮挡；
- 已目视检查首页、命题页、第6节标题页、三图页、结论页、附录首页和政策对照表。
- Figure 1 的密集状态层已局部栅格化，PDF 不再出现矢量色块之间的白色细缝；
  文字、坐标轴和 ACA 边界仍保持矢量。
