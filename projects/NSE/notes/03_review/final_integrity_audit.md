# Final Integrity and Reproducibility Audit

日期：2026-07-28
对象：正文、证明附录、BibTeX、三张正文图、CSV source data、数值核验代码和最终 PDF

## 1. 结论

**项目定义的理论、术语、引用、数值、图文一致性和编译验收：PASS。**

本文没有使用实际数据，也没有使用 iThenticate 或 Turnitin。当前结论不包含经验
识别、数量校准、全国福利评价或专业文本重复率认证。

## 2. 理论与内部一致性

| 检查 | 结果 |
|---|---|
| 正文正式命题 | 4 个 |
| 每个命题的证明 | 全部位于 `paper/appendix.tex` |
| 论文主问题 | platform access--local capture，没有改写为一般 LCA--ACA 论文 |
| LCA | 地区、产业双重相对生产成本；未用 \(1/c\) 定义 |
| ACA | 严格保留为加入现实交易成本后的比较优势概念；不另造 \(G_A\) |
| viability | 覆盖全部实际成本和正常回报，不依赖持续保护或补贴 |
| realization | 企业实际进入、生产和销售的均衡结果 |
| producer access | 从 outbound iceberg cost 推导；基准无 \(zG\) 交互 |
| 组织选择 | 同一企业利润比较内生决定 \(P/L\) |
| \(\omega_C,\rho_r\) | 均由可审计支付流生成 |
| 固定成本 | 只进入利润和组织选择，未在地方收入中重复扣除 |
| \(G_R,G_Y\) | 全局只声称 \(G_R\leq G_Y\)；连续区间内才声称严格排序 |
| facilitating state | 只降低共享基础设施融资楔子，不等同于任意补贴 |
| 收入与福利 | local nominal income 和 consumption-equivalent local income 均非 national welfare |

## 3. 解析和数值核验

使用项目虚拟环境运行：

```powershell
.\.venv\Scripts\python.exe code\theory\validate_model.py
```

验证内容包括解析导数、有限差分、利润排序、\(F>\bar F\) 的三区域条件、
\(F\leq\bar F\) 的反例、支付流边界、收入分母正性、反向渠道支付排序、部分平台
服务本地化、可选正 \(zG\) 互补、政府融资一阶条件、参数网格和阈值排序。

阈值算法先枚举精确结构事件，再在连续组织区间使用 Brent 方法求根；不再把离散
跳跃后的网格邻点误报为阈值。最终输出：

```text
All analytical, boundary, and finite-difference checks passed.
GP=0.210619, GL0=0.718802, GX=1.090996
GR=0.210619, GY=0.555415
State supply: G(0.05)=0.1780, G(0.50)=0.2887, G(0.99)=1.1198
State thresholds: vartheta_E=0.2331, vartheta_L=0.9863,
vartheta_R=0.2331, vartheta_Y=0.8308
```

因此，基准中的 \(G_R=G_E\) 是进入时第一轮生产收入发生离散变化所导致的精确
经济边界，不是网格误差。

## 4. 引用和术语来源

- `references.bib` 共有 17 个条目；
- 正文和附录共引用 17 个不同的 BibTeX key；
- 无 dangling citation 或 orphan reference；
- 每个核心模块的来源和论断边界记录在
  `literature/metadata_audit.md` 与 `notes/01_theory/model_contract.md`；
- Lin--Wang 只承担 LCA、ACA 和 state-enabling 概念，不承担本文的平台阈值；
- Ahn--Khandelwal--Wei 只承担条件性的组织成本排序；
- Rodríguez-Clare 只承担本地专业化生产者服务和产业联系解释；
- Miller--Blair、Moretti 和 EL companion 只承担 conditional income
  propagation，不把 local income 解释为社会福利。

## 5. Figure trace

三张图均由同一模型代码和 standardized illustrative parameters 生成。

| artifact | source data | 正文所表达的结果 | 边界 |
|---|---|---|---|
| Figure 1 | `figure_1_phase_diagram.csv` | 不进入、外部平台、本地嵌入三种均衡区域非空；LCA 越强，进入和嵌入越容易 | 不是地区分类数据 |
| Figure 2 | `figure_2_thresholds.csv` | \(G_E,G_L,G_R,G_Y\) 随相对生产成本变化；\(G_R=G_E\) 的重合被明确解释 | 不是估计值或置信区间 |
| Figure 3 | `figure_3_reform_paths.csv` | 不同政府参与下，共同的消费者平台份额和不同的名义、实际收入水平路径 | 收入按各自 \(z=0\) 标准化，不是政策因果估计 |

附录机制检查位于 `appendix_mechanism_closures.csv`；facilitation 与
external-channel restriction 的条件性比较位于
`appendix_channel_restriction.csv`。Figure 3 CSV 同时保存原始收入、标准化收入和
命题 3 使用的边际效应。

## 6. Numerical-exercise provenance

```yaml
status: experiments_declared
type: illustrative numerical exercises
empirical_data: none
calibration_claim: false
```

| 文件 | SHA256 |
|---|---|
| `code/numerical/generate_figures.py` | `C585148E044BD0351D134A0A75232E4E011A79873F914DB75669FD38C2390264` |
| `code/numerical/model.py` | `06F2067BDC24053A5B6C6871A22B4A78B95C2D7D26560C1D013962F8C34B8D19` |
| `code/theory/validate_model.py` | `95D439338D3AACB51702837375E517F62A2D8915590DA75B5D316581601F4CAA` |
| `code/requirements.txt` | `87F086E6165AD9E2C92449573EA54BA7F91AD5397053A06EABB3467CEC51911C` |
| `figure_1_phase_diagram.csv` | `A38AA7585ECF91E2A7898E87E776B297086B6D58B38784200454D0D494C9C00D` |
| `figure_2_thresholds.csv` | `177608B4CE0D9C2DF96970CA471CD2223CE1677F60577B27E3E835554AE9537C` |
| `figure_3_reform_paths.csv` | `32AAA781851A69FAEDA6393F8B1795D17C7FFF483BD0FE28A397329CEC6BC9C3` |
| `appendix_mechanism_closures.csv` | `64FF45EFE24F6C5091EF7164D8367B741C876E4313D7F95FDA8EDF67CD99A379` |
| `appendix_channel_restriction.csv` | `3BCB824448A8C572948ABBBE853C89E1315C7894759EFE9D14DB55C3078597E8` |

## 7. 编译与视觉检查

- 使用项目 `code/build_paper.ps1` 调用本机 MiKTeX XeLaTeX 和 BibTeX；
- 所有构建中间文件写入项目 `tmp/latex`，正式 PDF 写入 `output/`；
- 最终 PDF 共 34 页：正文 21 页、参考文献和证明/稳健性附录随后排列；
- PDF SHA256：
  `837CE54A09F7A7B173F090656F4F83E593F8D861D6AEA69A76734629CC0460C1`；
- 无 undefined citation、undefined reference、multiply-defined label 或
  overfull box；
- 少量窄表格 underfull box 不造成文字溢出、遮挡或错位；
- 已目视检查第 6 节标题页及三张正文图。Section 6 的编号与标题是标准 LaTeX
  section 版式，先前截图中的蓝框和圆形“1”是 PDF 批注选区，不属于论文排版；
- Figure 3 现展示标准化收入水平路径，而不是以边际效应代替原计划要求的结果。

## 8. 最终限制

该稿已经是完整的纯理论论文，但只回答结构性机制与门槛：

- 不估计中国的参数或政策效应；
- 不求全国最优政府参与；
- 不评价完整 national welfare；
- 不解释长期地区迁移、集聚或生产要素一般均衡。

任何后续经验或定量空间扩展应作为独立项目，不应反向扩大当前活动模型。
