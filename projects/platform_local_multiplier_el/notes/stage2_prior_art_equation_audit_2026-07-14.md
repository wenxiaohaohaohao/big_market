# Stage 2 equation-level prior-art audit

日期：2026-07-14  
对象：当前标量 EL 模型  
审计性质：只读；未修改 main.tex、appendix.tex、references.bib、verify_model.py 或 output/paper.pdf

## 1. 终局结论

**当前 scalar route 的严格结论是 NO-GO。**

这不是因为模型有数学错误。当前推导是正确的。阻断原因是：把模型写成

\[
q(z)=\beta+\alpha\omega(z),\qquad
x(z,G)=B(z)+\omega(z)G,
\]

以后，核心收入系统就是

\[
Y=x+qY,
\qquad
Y=(1-q)^{-1}x.
\]

这一 fixed point、几何级数、first-round incidence 与 induced-round feedback，分别是 SAM/fixed-price multiplier、Miyazawa income multiplier、Type-II regional input-output closure 和 Pennings（2021）局部需求轮次的精确标量形式或嵌套特例。Fan et al.（2018）又已经给出与本文 \(s(z)\) 同构的在线/线下渠道份额及 logistic 响应。因此：

- 不能把“留值率进入每一轮支出”“有效乘数不是只在第一轮乘一次留值率”作为新机制；
- 不能把 CES 渠道份额或 \(s'(z)=(\eta-1)s(1-s)\) 作为新结果；
- 不能用机械两地区 \(\Omega\) 矩阵修复创新性，因为 multiregional Miyazawa、Round（1985）及 Rose–Stevens（1991）已经覆盖跨地区生产、收入形成、收入接收和支出反馈；
- finite sign regions 和 \(s^\dagger<1/2\) 没有在本次核查中找到逐字相同的已发表公式，但它们是“标准 multiplier inverse + 已知 CES/logistic share law”的直接代数结果。仅凭这两个闭式表达，不足以通过严格 EL novelty gate。

有条件继续的最低要求不是重新包装现有定理，而是加入一个非标准、平台特有且内生生成 local capture 的行为或制度机制，并推出不能由更新 Type-II/SAM 系数直接得到的命题。否则应停止当前独立 EL 版本，将理论并回更大的模型—实证项目。

## 2. 分类标准

本审计使用四类判定：

1. **Exact equivalence**：变量重命名或标量化后，方程和反馈结构相同。
2. **Nested special case**：既有模型更一般，当前模型由聚合、固定若干系数或关闭若干维度得到。
3. **Adjacent but distinct**：研究相同对象或机制，但方程或均衡闭合不同。
4. **Unresolved**：只取得官方元数据、摘要或可靠重述，无法从原始全文核实具体方程号；不据此作精确等式声称。

## 3. 当前方程对象

当前 main.tex 的核心对象是：

- 第 172–183 行：CES price index、平台份额及导数；
- 第 187–194 行：\(\omega=(1-s)\rho_A+s\rho_P\)；
- 第 202–231 行：地方收入 fixed point 与解析解；
- 第 249–279 行：\(m_B\)、gross-spending multiplier 及 retention elasticity；
- 第 281–307 行：finite nominal/real-income regions；
- 第 315–350 行：marginal drag 和唯一内部峰值。

关键约化为

\[
Y=B+\omega G+(\beta+\alpha\omega)Y,
\]

所以审计的核心不是文献是否使用同一个符号 \(\omega\)，而是既有文献是否已经包含同一个 first-round vector、feedback coefficient 和 inverse。

## 4. 逐式比较矩阵

| 文献 | 最接近的方程或证据 | 与本文的关系 | 判定 |
|---|---|---|---|
| Pyatt & Round (1979) | 期刊 pp.856–857，eqs. (4),(12)：\(y_n=A_ny_n+x\)、\(y_n=(I-A_n)^{-1}x\)；p.861，eqs. (23)–(27)：\(dy_n=C_ndy_n+dx\)、\(dy_n=(I-C_n)^{-1}dx\) | 令一个 endogenous account、\(C_n=\beta+\alpha\omega\)、\(dx=dB+\omega dG\) | fixed point 与 \(m_B\) 为 exact scalar equivalence；\(\mathcal M_G\) 为 first-round incidence 下的 nested case |
| Miyazawa (1960); Sonis & Hewings (2000) | Sonis–Hewings p.577，eqs. (31)–(33)：\(B=(I-A)^{-1}\)、\(L=VBC\)、\(K=(I-VBC)^{-1}\) | 一户一部门且 \(VBC=\beta+\alpha\omega\) | 当前 multiplier 是 nested scalar special case |
| BEA RIMS II Type II | 官方 Guide pp.2-8、3-1–3-2、5-5–5-6：household column、local purchase/import leakage、bill of goods、Type-II induced spending | \(\omega G\) 是 first-round local incidence；\(\beta+\alpha\omega\) 是标量 household feedback | nested special case；重复支出和进口漏出已建立 |
| Pennings (2021) | Proposition 1，印刷 p.1712：temporary LocalGE 为 \(\alpha/(1-\alpha\omega)\)；p.1713 明写 \(\alpha\omega,(\alpha\omega)^2,\ldots\) | 在 \(\beta=0\) 且把当前反馈系数映射为 home-bias × hand-to-mouth share 后，later-round denominator 相同 | exact recursion equivalence；加入 \(\beta\) 是直接加性扩展 |
| Little & Doeksen (1967/1968) | 1967 公开前身 p.60：比较含进口与无进口的 interdependent coefficients；p.65：income multiplier 为总 direct+indirect income / direct income | 其 leakage coefficient 是两个总乘数之差，不等于本文第一轮 \(\omega\) | 定义 adjacent；“进口漏出降低整个 inverse”是既有机制 |
| Round (1985) | 官方记录确认主题为 regional/world-trade multiplier decomposition；原方程全文受限 | 标量模型显然处于区域矩阵 multiplier 的聚合情形，但不能虚构其原文方程号 | nested 的方向有充分支持；原式编号 unresolved |
| Sonis & Hewings (2000) 两地区模型 | pp.579–580，eqs. (39)–(45)：两地区 block system 与各区 \(K_r\)；pp.581–582，eq. (52)：interrelational income multiplier | 已允许区内、区际生产—消费—收入反馈 | 机械 \(\Omega\) 扩展为 nested special case；两地区路线 NO-GO |
| Rose & Stevens (1991) | 官方摘要明确按 income generation、receipt、spending 三地分类，并只把三者均内生的流纳入闭合区域模型 | 当前单一 \(\omega\) 聚合了这些空间归属；原项目“五个地点”与其高度相邻 | 概念 nested/adjacent；原方程全文受限，exact formula unresolved |
| Atkin, Faber & Gonzalez-Navarro (2018) | 作者稿 p.10，eq. (1)：cost-of-living 与 nominal-income 分解；pp.11–13，eqs. (3)–(6)：Cobb–Douglas/CES stores、market-share price-index result | 本文 \(R=KY/P_M^\alpha\) 和两渠道 CES 是其需求—福利框架的简化版本 | demand/real-income block 为 nested special case；无本文 scalar household fixed point |
| Fan et al. (2018) | p.17，eqs. (5)–(7)：online/offline Fréchet channel choice；在线份额 \(\rho=\tau_E^{-\theta}/\sum_m\tau_m^{-\theta}\)，并给出 log odds；pp.14–19 为多地区 GE | 令 \(\theta=\eta-1\)、\(\log\tau_E=-z+constant\)，即得到本文 logistic \(s(z)\) 与 \(s'(z)=\theta s(1-s)\) | \(s(z)\) share law 为 exact functional equivalence；无 scalar retention multiplier |
| Forman, Ghose & Goldfarb (2009) | 官方文章确认 offline transportation cost、online disutility、online/offline prices共同决定 channel choice；全文方程受限 | 空间渠道替代是明确先例，但未核实与 CES share 的精确同式 | adjacent but distinct；equation-level exactness unresolved |
| Li (2025 working paper) | Theorem 1/eq. (2)：Cobb–Douglas + CES online/BM demand；eqs. (8)–(11)：在线进入、跨地在线份额和本地 BM 份额；eqs. (14)–(16)：地区收入、零售/制造 value added 与市场出清 | 聚合 origin、固定工资/成本和 ownership 后，本文 \(\omega\) 是其多地区 channel/value-added flows 的标量 reduced form | 不是逐字相同公式，但属于 nested scalar aggregation；与原大项目最接近 |
| Couture et al. (2021) | AER: Insights 的实验结果：平台接入降低部分家庭 cost of living，但几乎没有广泛 producer/worker income gains | 已直接展示“消费价格收益与地方收入收益分离”这一经验事实 | empirical adjacent precedent；不是解析 multiplier 模型 |

## 5. 五个核心对象的判定

### 5.1 \(s(z)\) 与 price block

当前

\[
s(z)=\frac{ap_P(z)^{1-\eta}}
{(1-a)p_A^{1-\eta}+ap_P(z)^{1-\eta}},
\qquad
s'(z)=(\eta-1)s(1-s)
\]

是标准 CES expenditure share。AFG 已使用 stores 层的 CES；Fan et al. 更直接地给出在线/线下份额的同构 logit/Fréchet 形式。**判定：nested/exact functional equivalence，不是创新对象。**

### 5.2 \(\omega(z)=(1-s)\rho_A+s\rho_P\)

文献中没有发现完全使用当前符号和两系数线性平均的定理。但是，这只是按渠道支出份额加权的地方收入系数。RIMS II 的 bill-of-goods/local-supply treatment、Li 的 online/BM expenditure shares 与区域 value-added flows，都可以生成同一聚合对象。

**判定：公式表面上 distinct，经济对象是 nested scalar aggregation。** 若 \(\rho_A,\rho_P\) 外生且恒定，\(\omega(z)\) 只是随渠道 composition 更新的 SAM/IO coefficient，不构成新的 feedback state。

### 5.3 收入 fixed point 和 multiplier

\[
Y=B+\omega G+(\beta+\alpha\omega)Y,
\quad
m_B=\frac1{1-\beta-\alpha\omega},
\quad
\mathcal M_G=\frac{\omega}{1-\beta-\alpha\omega}
\]

与 Pyatt–Round 的标量 fixed-price multiplier 精确同构，是 Miyazawa/Sonis–Hewings 的一户一部门特例。Pennings 明确写出 later rounds 和 \(1/(1-\alpha\omega)\)。

**判定：fixed point 与 recursive mechanism 为 exact/nested prior art。** Proposition 1 不能作为论文主创新。

### 5.4 finite thresholds

\[
\frac{Y_1}{Y_0}=\frac{\mathcal B}{\mathcal D},
\qquad
\frac{R_1}{R_0}=\frac{\mathcal B}{\mathcal D\mathcal P^\alpha}
\]

及三个区域没有在所核查来源中找到逐字同式。但是，它们是标准 income inverse 与 Cobb–Douglas real-income index 的直接比值比较。AFG 和 Couture 已分别建立/展示 price gains 与 nominal-income losses 可以分离。

**判定：verbatim priority unresolved；mechanism-level novelty 不成立。** 可以保留为说明性 comparative statics，不能单独承担 EL contribution。

### 5.5 \(s^\dagger<1/2\)

本次没有找到相同闭式峰值：

\[
s^\dagger=
\frac{1}{1+\sqrt{1+\alpha\Delta\rho/
(1-\beta-\alpha\rho_A)}}<\frac12.
\]

它确实比“峰值在中间渗透率”更精确；但它由 Fan-type logistic share derivative \(s(1-s)\) 除以标准 multiplier denominator 后的一阶求导产生。若换成一般 share path，唯一性和低于 \(1/2\) 都不成立。

**判定：exact formula 未找到，CES-specific 且机械；单独不足以通过 novelty gate。**

## 6. 原项目是否因 EL 简化而失去创新

答案是：**是，但更准确地说，简化把潜在的行为与空间机制压缩成了两个外生系数，使剩余模型退化为标准 multiplier accounting。**

原项目有四个较强的研究对象：

1. market access 与 local value capture 的区分；
2. 消费地、生产地、经营地、平台总部/结算地和收入/税收归属地的空间分离；
3. 本地供给能力、组织能力和平台依赖决定 capture 的异质性；
4. 外生 integration/platform shock 与真实工资、利润、就业、税基和卖家来源的因果识别。

当前 EL 删除了生产者响应、企业区位、平台收费与所有权、税收归属、跨地区网络和经验识别，只留下 \(s(z)\)、固定 \(\rho_c\) 与一个 scalar fixed point。因此原项目最有辨识力的“谁创造、谁组织、谁拥有、收入在哪里形成”没有被模型内生化。

但不能简单把全部旧模块搬回去。Rose–Stevens 已研究 generation/receipt/spending 的空间分离，Sonis–Hewings 已有 multiregional income feedback，Li 已有 online/BM、retailer location、value added 和 regional income。**机械恢复五地点矩阵或两地区 \(\Omega\) 仍然不够。** 真正需要的是一个平台特有的选择、契约、所有权或组织机制，以及由它产生的可检验新预测。

## 7. 严格 novelty gate

只有同时满足下列四项，独立 EL 路线才可重新判为 conditional GO：

1. **Primitive gate**：local capture 必须由平台费率、seller/intermediary location、local service requirement、ownership 或 adoption/exit choice 内生生成，不能继续只由固定 \(\rho_A,\rho_P\) 给定。
2. **State gate**：新机制必须增加一个有经济含义的 equilibrium margin，而不是把 \(\omega\) 换成矩阵、函数或重新命名的 IO coefficient。
3. **Theorem gate**：至少一个主命题不能通过对标准 \((I-C)^{-1}\) 更新系数并求导直接得到；应有新的存在性、阈值、非单调性、corner、multiple regimes 或 incidence result。
4. **Prior-art gate**：必须逐式排除 Fan/Li 的渠道与区位机制，以及 Miyazawa/SAM/Type-II/Rose–Stevens 的收入闭合和空间流量机制。

若任一 gate 失败，则 NO-GO 保持。当前版本四项均未通过。

## 8. 对后续研究路线的建议

- **独立 scalar EL**：停止。继续改写 Introduction 或增加引用不能解决问题。
- **机械两地区 \(\Omega\)**：停止。它受 Sonis–Hewings、Round、Rose–Stevens 直接约束。
- **平台特有的最小理论重建**：有条件可行，但必须围绕一个内生 capture mechanism 重新建模；这不是当前稿件的小修。
- **原模型—实证大项目**：仍然值得继续。其潜在贡献应放在平台组织如何改变收入空间归属的可测量机制、外生冲击、异质性和经验识别，而不是宣称发明了 leakage multiplier。

## 9. 主要来源与直接链接

1. Pyatt & Round (1979), official World Bank reprint: https://documents1.worldbank.org/curated/en/317011468179066100/pdf/REP125000Accou0ing0matrix0framework.pdf
2. Miyazawa (1960), official OUP endpoint: https://academic.oup.com/qje/article-pdf/74/1/53/5206190/74-1-53.pdf
3. Sonis & Hewings (2000), DOI: https://doi.org/10.1007/s001680000022 ; author-upload text: https://www.researchgate.net/publication/24053472_LDU-factorization_of_Miyazawa_income_multipliers_in_multiregional_systems
4. BEA RIMS II User Guide: https://www.bea.gov/sites/default/files/methodologies/RIMSII_User_Guide.pdf
5. Pennings (2021), primary copy: https://documents1.worldbank.org/curated/en/559331626071176592/pdf/Cross-Region-Transfer-Multipliers-in-a-Monetary-Union-Evidence-from-Social-Security-and-Stimulus-Payments.pdf
6. Little & Doeksen (1968), official record: https://onlinelibrary.wiley.com/doi/abs/10.2307/1237629 ; open 1967 precursor: https://ageconsearch.umn.edu/record/323544
7. Round (1985), official record: https://academic.oup.com/ej/article-abstract/95/378/383/5190759
8. Rose & Stevens (1991), official record: https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1467-9787.1991.tb00147.x
9. Atkin, Faber & Gonzalez-Navarro, author manuscript: https://ben-faber.com/retail_globalization_AFG.pdf
10. Fan et al. (2018), author manuscript: https://fanjt.weebly.com/uploads/1/9/4/7/19473457/alibabaeffect.pdf
11. Forman, Ghose & Goldfarb (2009), official article: https://pubsonline.informs.org/doi/10.1287/mnsc.1080.0932
12. Li, current working paper: https://elmerli.github.io/ecommerce.pdf
13. Couture et al. (2021), official AEA article: https://www.aeaweb.org/articles?id=10.1257/aeri.20190382

## 10. 证据限制

- Miyazawa (1960)、Round (1985) 和 Rose–Stevens (1991) 的官方完整方程页受访问限制；本审计没有虚构其原文 equation numbers。Miyazawa 的 equation-level 判断由 Sonis–Hewings 对其 formalism 的正式重述支持；Round 和 Rose–Stevens 的精确原式标为 unresolved。
- Forman et al. 的全文方程同样未取得；只把它作为官方确认的空间渠道替代先例，不声称与本文 CES 方程精确等价。
- Li 是持续更新的 working paper。当前核查版本题为 Domestic Trade Shocks and E-Commerce Expansion: Evidence from Amazon's Distribution Facilities，日期为 2025-11-07；投稿前必须重新核对最新版。
- “没有找到逐字相同的 finite threshold 或 peak formula”不是 priority certification。审计结论基于 equation mapping 和机制嵌套关系，而不是仅基于关键词或摘要相似度。
