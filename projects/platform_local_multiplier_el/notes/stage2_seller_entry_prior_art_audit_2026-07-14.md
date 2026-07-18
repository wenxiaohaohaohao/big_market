# Stage 2：Seller-entry 路线的 equation-level prior-art audit

日期：2026-07-14  
项目：*Platform Intermediation and Local Multipliers*  
审计对象：`local seller entry` 候选路线  
文件边界：本轮只形成这份审计笔记；未修改 `paper/main.tex`、`paper/appendix.tex`、`paper/references.bib`、模型核验代码或编译结果。

## 1. 结论先行

本轮结论不是“seller entry 可以直接加入现有 EL”，而是更严格的两层判定：

1. **只把 seller entry 加入现有标量乘数模型：NO-GO。** Fan et al. (2018) 已经把 online/offline channel、destination income、firm entry、labor demand 和 regional income 放在同一多地区 GE 中；Li (2025, 2025-11-07 版本) 又明确建立了 local online retailer 的进入阈值，让 origin 与 destination income 同时决定进入和贸易。普通的“收入提高进入、进入提高本地收入”不再是空白。
2. **平台租金的空间收取地 × seller entry × 本地再支出反馈：CONDITIONAL-GO，仅进入定理可行性测试。** 本次有界检索没有找到一篇同时联立下列六项的论文：online/offline substitution、local and external orders、platform commission、local/remote order or rent routing、free entry、local-respending kink。尤其没有找到“保持 commission 和消费者端条件相同，仅改变平台租金的收取地，进而改变 seller-entry 的稳定性或阈值”的现成命题。但这是“未在本次检索中发现”，不是 priority 的最终证明。

因此，下一步若继续，主结果必须来自**平台租金空间收取地与 seller entry feedback 的联合**。不能把 fee、entry、market size、multiplicity 或 tipping 中任何一个单独包装成创新。

## 2. 判定口径

本审计采用四类关系：

- **Exact**：已有文献包含相同 primitive、相同内生对象和相同均衡作用。
- **Nested**：已有模型更一般，候选方程可作为其限制情形得到。
- **Adjacent**：已有文献包含其中一个关键 primitive，但缺少本项目的空间收取或再支出闭环。
- **Unresolved**：本次核验的全文与官方记录中没有找到直接对应；这不等于证明不存在。

创新判定分三层，避免把旧乘数文献误用为平台创新的否定证据：

- **Layer A — algebra/accounting ancestry**：SAM、Miyazawa、MRIO 和 ownership-augmented regional IO 已覆盖固定收入系数、跨地区收入流和反复支出。它们只说明 inverse 的代数祖先。
- **Layer B — direct platform/e-commerce primitives**：检查 online/offline choice、commission、seller entry、fulfillment/location 是否已有相同建模。
- **Layer C — joint equilibrium loop and prediction**：检查是否已有“空间租金收取改变进入反馈或稳定边界”的同一命题。只有 Layer B 或 C 的实质重合可以构成这条路线的 NO-GO。

## 3. 检索与核验协议

### 3.1 数据源与日期

检索日期为 2026-07-14。优先使用：期刊官网、AEA、NBER、CEPR、作者主页、大学机构库和作者接受稿。SSRN/arXiv 仅用于尚无正式期刊版或识别最新工作论文；没有以二手综述替代原文方程核验。

### 3.2 主要检索式

检索式包括：

1. `e-commerce seller entry local income platform commission spatial`
2. `local demand seller entry digital platform`
3. `spatial model marketplace commission seller entry regional income`
4. `multi-region platform commission seller entry`
5. `platform fee seller location spatial equilibrium`
6. `platform seller participation entry commission free entry`
7. `e-commerce market access local seller entry fulfillment location`
8. `platform commission local income seller entry region`
9. `absentee ownership platform commission seller entry`
10. `headquarters platform fees regional income e-commerce seller entry`
11. `local ownership digital platform seller entry multiplier`
12. `platform rents headquarters local economy seller entry`
13. `online offline channel free entry regional income`
14. `seller entry e-commerce local multiplier`
15. `platform commission local income seller entry spatial economy`

此外对 Fan et al. (2018)、Li (2025)、Goldmanis et al. (2010)、Anderson and Bedre-Defolie (2024)、Etro (2023) 和 Teh (2022) 直接核对全文方程、均衡定义和相关附录。

### 3.3 纳入与排除

纳入条件：至少满足以下之一：

- 平台或 e-commerce seller 的 endogenous participation/entry/exit；
- online/offline channel choice 与多地区 income 或 market access；
- commission/participation fee 与 seller mass；
- fulfillment/location 与本地 seller outcomes；
- local/absentee ownership 与地方 income multiplier。

排除条件：只研究消费者 adoption、一般数字化、税收规范讨论、广告效果或 seller survival，且没有 entry/空间收入机制者，不进入核心方程比较；其中少数仅作为可观测变量或事实背景保留。

这是面向路线选择的**有界定向审计**，不是 PRISMA 式穷尽综述。搜索工具返回结果会动态变化，未构造虚假的总命中数或排除数。对“没有发现完全相同模型”的陈述均限定于上述检索式、来源和日期。

## 4. 需要接受 prior-art 检验的连续候选

为了避免把当前模型的结论预先写入审计，以下只定义必须被同时解释的最小对象。设外围地区为 $L$，平台总部地区为 $H$，本地活跃 seller 质量或数量为 $n$，平台费率为 $\kappa$。

家庭在 online 与 offline 之间选择，平台渠道的本地与外部订单共同形成 seller gross revenue：

\[
X_{P,L}=s(n,z)\alpha Y_L,
\qquad
\mathcal R_L(n;Y_L,Y_H,z)
=\mathcal R_{LL}(n;Y_L,z)+\mathcal R_{LH}(n;Y_H,z).
\]

seller 支付 commission 后的进入条件为

\[
(1-\kappa)\mathcal R_L(n;Y_L,Y_H,z)-F(n)=0
\quad\text{if }n>0,
\]

并配有适当的无进入不等式。令 \(\ell\in[0,1]\) 表示平台租金在本地被收取并再支出的比例；其余 \(1-\ell\) 流向总部地区。地方收入闭合至少必须区分 seller net receipts 与 platform fee receipts：

\[
Y_L
=B_L+\beta Y_L
+\underbrace{\rho_S(1-\kappa)\mathcal R_{LL}}_{\text{local seller receipts}}
+\underbrace{\ell\kappa X_{P,L}}_{\text{local platform-rent receipt}}
+\text{other local receipts}.
\]

若候选模型使用 piecewise local spending rule，则 kink 必须由可解释的经济约束产生，例如只有本地 seller receipts 与本地收取的平台租金进入下一轮本地消费，而外部 seller/HQ receipts 不进入；不能任意指定一个分段函数来制造阈值。

六项共同闭环是：

1. online/offline substitution；
2. local and external orders；
3. commission；
4. local/remote routing of orders or platform rents；
5. free entry；
6. local-respending kink/feedback。

任何只覆盖其中一至五项的结果，都不能被描述为完整候选的同一命题；但如果主命题只使用已有子模块，它仍然不新。

## 5. 核心文献的 equation-level 比较

### 5.1 Fan et al. (2018)：最重要的多地区进入先例

Fan et al. 把 e-commerce 视为一种消除 destination fixed storefront cost、降低距离摩擦的 trade technology。其模型已经包含：

- online-only 与 online/offline 两种渠道；
- 单个 firm 对 destination $j$ 的 online sales 与 $Y_j$ 成正相关，见 equation (9)；
- 是否设立 physical store 的 productivity cutoff 明确含 destination income $Y_j$，见 equation (10)；
- firm free entry，expected profit 等于 entry labor cost，见 equation (11)；
- labor demand 包含 variable production、physical-store setup 和 firm-entry labor，见 equation (12)；
- labor clearing 与 regional income $Y_i=w_iL_i$，见 equations (13)--(14)。

因此，以下链条已经是 **Nested**：

\[
Y_j\longrightarrow \text{channel profitability/entry}
\longrightarrow \text{labor demand and wage}
\longrightarrow Y_i.
\]

Fan et al. 没有把在线渠道建模为收取 commission 并把平台 rent 送往特定总部地区的独立中介，也没有把相同 fee 在 local/remote receipt 下的地方再支出差异作为 primitive。其缺口位于空间 incidence，而不是 entry 本身。

### 5.2 Li (2025)：最接近的 fulfillment--seller-entry--regional-income 模型

Li 的 2025-11-07 作者版本明确说明模型是 multi-region, multi-sector spatial retail trade model，包含 endogenous online retail entry 和 consumer search。其 Amazon facility 数据同时识别 seller business location 与 fulfillment method。

对本路线最关键的是 Appendix B.4：

- regional retailers 决定是否进入 online retail；
- 进入条件要求向各 destination 销售的 expected revenue 至少覆盖 local entry cost；
- equation (30) 给出 threshold cost，分母包含 destination incomes $Y_n$ 加权的市场机会；
- potential entrant mass 假定与 origin nominal income $Y_m$ 成比例；
- equation (31) 的 bilateral exports 同时受 $Y_m$、$Y_n$、shipping frictions 与 price indices 影响；
- equilibrium market-clearing 是 fixed-point，quantitative decomposition 同时报告 price 与 regional income effects。

因此，

\[
(Y_m,Y_n,\text{facility/trade costs})
\longrightarrow \text{local online entry}
\longrightarrow \text{bilateral sales, employment and regional income}
\]

已是 **Nested/Substantive prior**。Li 没有显式区分 platform commission、平台总部 rent ownership 与 receipt location，也没有以地方收入的逐轮再支出作为进入阈值的独立机制。故“fulfillment 降低进入成本”已知；“remote platform rent receipt 改变 entry feedback”仍未被该文覆盖。

### 5.3 Goldmanis et al. (2010)：e-commerce 与 producer entry/exit

Goldmanis et al. 将 e-commerce 表示为 consumer search cost 的下降。潜在 entrant 支付 sunk entry cost，进入后观察成本；运营利润不能覆盖 fixed cost 的 producer 退出。其 equations (10)--(11) 分别给出 exit cutoff 与 free-entry condition。e-commerce 将份额从高成本企业转向低成本企业并导致高成本企业退出。

这使“e-commerce 改变 seller entry/exit”成为 **Exact primitive**，但该文没有多地区 income、seller origin、platform commission、HQ rent 或 local multiplier。因此它对完整闭环是 **Adjacent**，不是同一模型。

### 5.4 Anderson and Bedre-Defolie (2024)、Etro (2023)、Teh (2022)：commission 与 seller mass

Anderson and Bedre-Defolie 的 hybrid-platform 模型让平台设定 ad valorem seller fee，fringe sellers 进行 free entry；fee 提高 seller effective marginal cost、改变 fringe seller mass 和 variety。其正式发表页也明确说明平台用 fee 控制 third-party entry。

Etro (2023) 研究平台设置 access prices 和 seller-revenue commissions，seller 在 monopolistic competition 下 free entry。commission、profitability elasticity 与 seller entry 的联系是模型中心；该文还讨论 two-sided network effects 下的 entry/tipping 问题。

Teh (2022) 系统分析 platform fee instruments 与 seller competition/entry，明确区分 proportional、per-transaction、participation 和 two-part fees。其综述还指出 Nocke et al. 等模型中 seller-side participation fee 已通过 free-entry condition 决定 seller 数量。

因此，下列结果均不能作为新命题：

- \(\kappa\uparrow\Rightarrow n\downarrow\)；
- fee 存在 no-entry cutoff；
- seller/consumer participation 的正反馈可能带来 tipping；
- platform fee instrument 改变进入和 variety。

这些文献均未区分 seller/consumer 的地区，也未研究 commission receipt 在 local 与 remote headquarters 之间的空间归属，更没有地方再支出 kink。故其对六项闭环中的 commission--free-entry 子系统是 **Exact**，对完整空间闭环是 **Adjacent**。

### 5.5 Allain, Bourreau, and Moraga-González (2026)：最新 entry-fee 风险

2026 年 CEPR paper 比较 agency 与 wholesale models，并允许 platform 向 seller 收取 entry fee。论文给出 entry failure、zero entry fee 和不同 commission instruments 下 price/entry ranking 的条件。这进一步说明“entry fee 导致无进入 corner”及“ad valorem 与 per-unit fee 的 entry ranking”不能独立承担贡献。该文没有地方收入与空间收取地，因此仍是 fee-entry 子系统的直接先例。

### 5.6 Nocke, Peitz, and Stahl (2007)：`platform ownership` 不等于 spatial receipt

该文比较 monopoly、dispersed 和 club-like platform ownership，并研究 ownership 对 entry、trade 与 network effects 的影响。它表明 platform ownership structure 本身已有成熟理论。但其 ownership 指平台治理权和排除权，而不是“平台 rent 最终由哪个地区居民收取并在哪里再消费”。本项目若继续，必须把 **control ownership** 与 **income receipt/residence** 明确区分。

### 5.7 Brown, Fitzgerald, and Weber (2019)：空间收入收取的重要性

Brown et al. 以油气 royalty 为对象，发现 local 与 absentee ownership 会显著改变县域收入及 multiplier；相同生产可以因收入收取地不同产生不同地方结果。这是“generation location 不等于 receipt location”的直接经验先例。

它不包含 digital platform、seller entry、online/offline choice 或 commission。因此它只支持空间 incidence 的经济重要性，不能否定平台联合机制的创新，也不能代替平台模型。

## 6. 六项共同闭环的覆盖矩阵

| 文献 | Online/offline substitution | Local + external orders | Commission | Local/remote routing or receipt | Free entry | Local respending kink | 总体判定 |
|---|---:|---:|---:|---:|---:|---:|---|
| Fan et al. (2018) | 是 | 是，多城市销售 | 否 | 商品跨城；无平台 rent receipt | 是 | 否 | entry--income loop 已嵌套；缺平台 incidence |
| Li (2025) | 是，BM/online | 是，双边贸易 | 否 | seller/facility location；无 HQ rent receipt | 是 | 否 | 最接近；seller-entry route 的主要 prior |
| Goldmanis et al. (2010) | 以 search-cost shock 表示 | 否 | 否 | 否 | 是，含退出 | 否 | e-commerce entry/exit primitive 已知 |
| Anderson & Bedre-Defolie (2024) | marketplace/hybrid | 非空间 | 是 | 否 | 是 | 否 | commission--entry exact prior |
| Etro (2023) | direct/platform extension | 非空间 | 是 | 否 | 是 | 否 | fee--entry/two-sided feedback prior |
| Teh (2022) | 可由 governance applications 表示 | 非空间 | 是，多种费制 | 否 | 是/平台控制 seller mass | 否 | fee instrument 与 seller competition prior |
| Allain et al. (2026) | agency/wholesale | 非空间 | 是，含 entry fee | 否 | 可发生 entry failure | 否 | no-entry/ranking prior |
| Nocke et al. (2007) | 否 | 非空间平台交易 | participation pricing | 治理所有权，不是 receipt location | 是/参与 | 否 | ownership 术语邻近但概念不同 |
| Brown et al. (2019) | 否 | 否 | 否 | 是，local/absentee receipt | 否 | 是，经验 multiplier | 空间收取重要性；非平台 prior |
| 连续候选 | 必须有 | 必须有 | 必须有 | 必须区分 orders 与 rents | 必须有 | 必须由经济约束产生 | 六项联合尚未在本次检索中发现 |

覆盖矩阵的含义不是“把六项全部放进模型就自动新”。真正需要新的是六项联合产生一个已有任何子模块都不能推出的命题。

## 7. 逐对象的 exact/nested/adjacent 判定

| 候选对象或结果 | 最接近先例 | 判定 | 对论文的约束 |
|---|---|---|---|
| Online/offline channel substitution | Fan et al. equations (6)--(10) | Exact/Nested | 只能作环境，不能作贡献 |
| Fixed entry cost 与 productivity/profit cutoff | Fan et al. (11); Li (30); Goldmanis et al. (10)--(11) | Exact | 普通进入阈值不能作贡献 |
| Destination income 提高 seller market opportunity | Fan et al. (9)--(10); Li (30) | Exact | “本地需求促进进入”已知 |
| Origin income 影响 entrant mass | Li Appendix B.4 | Exact | 不能用 origin-income feedback 单独主张新意 |
| Entry 改变 local labor demand/income | Fan et al. (12)--(14); Li market clearing | Nested | 普通 entry--income loop 已被覆盖 |
| Commission 改变 seller entry/variety | Anderson--Bedre-Defolie; Etro; Teh | Exact | fee-entry comparative statics 已知 |
| No-entry corner、fee threshold、generic tipping | Allain et al.; Etro；two-sided platform literature | Exact/Adjacent | 只有空间 rent receipt 产生的新边界才可能保留 |
| Fulfillment facility 改变 seller entry 与跨区销售 | Li | Exact/Nested | facility-access 不能作独立贡献 |
| 固定 local/absentee ownership 改变 multiplier | Brown et al.；Layer A regional multiplier literature | Nested/Adjacent | 只作 incidence benchmark |
| Commission 由 remote HQ 收取且不进入本地再支出 | 本次 direct-platform sources 未建模 | Unresolved | 必须明确 receipt residence，而非只写 platform profit |
| 保持 fee/price 相同，仅改变 rent receipt location，从而移动 entry/stability threshold | 本次检索未找到直接命题 | Unresolved | 最有希望的 hard novelty object |
| `local-respending kink` 使 remote routing 对 entry 产生额外间接效应 | 本次检索未找到直接命题 | Unresolved | kink 必须有 microfoundation，且不可由固定 inverse 单独得到 |

### 7.1 对现有 continuous candidate equations (17)--(23) 的直接判定

现有候选的进入条件是

\[
\mathcal A(z)
=E(z)+\frac{\alpha s(z)B}
{1-\beta-\alpha\rho_A[1-s(z)]}
>
\mathcal C(\tau)
=\frac{F\chi}{\mu(1-\tau)}.
\]

这一条件把 local orders、external orders、commission、remote-seller routing competition 和 free entry 放在同一阈值中，但各组成部分已有直接先例：Fan/Li 已有 income-weighted spatial entry opportunity，Anderson--Bedre-Defolie/Etro/Teh/Allain et al. 已有 fee-adjusted seller entry。故以下结果不能单独承担贡献：

- equation (17) 的 break-even inequality；
- equation (18) 条件于 active set 的收入增量，因为其分母仍是固定 household-closure inverse；
- equation (20) 的 $dz^*/d\tau>0$，因为它是“更高 fee 降低 entry profitability”的 integration-index 重参数化。

真正尚未找到直接先例的是 equations (21)--(23) 的**联合 phase reversal**：

1. entry 之前，online substitution 把原本由 local intermediary 捕获的居民订单路由给 remote sellers，地方收入下降；
2. entry 之后，同一平台把 local 与 external orders 路由给 local sellers，扣除 remote-HQ commission 后形成地方收入；
3. free-entry active set 使收入水平连续，但在进入阈值出现 derivative kink；
4. outward market-access 足够强时，收入对 integration 的斜率由负转正。

在本次全文核验中，没有一篇核心文献同时包含这四步及前述六项共同闭环。因此，现有 continuous candidate 的准确判定是：

```text
equations_17_18_20_as_core = NO_GO
equations_21_23_joint_phase_reversal = CONDITIONAL_GO
```

但这个 CONDITIONAL-GO 仍需通过三个额外检验：

1. **反馈必要性**：必须比较关闭 local respending 后的 threshold 与 slope，证明递归需求反馈移动进入边界或放大 kink；如果 phase reversal 完全由第一轮 local/remote receipts 就能得到，不能把 local multiplier 写成核心创新。
2. **routing microfoundation**：$\theta(n)=n/(n+\chi)$ 必须可解释为 CES/logit contest、曝光或履约分配的简化结果；若它只是为了产生 $[Q-Q_E]_+$ 而指定，审稿风险很高。
3. **组合不等于贡献**：Introduction 必须把新命题准确写成 `entry-induced spatial routing reversal`，而不是把已知的 channel substitution、fee-entry 和 local multiplier 分别列作三项创新。

若上述三项中任一失败，应采用更强的 receipt-location counterfactual：保持 fee、price 与技术不变，只改变 platform commission 在本地或总部被收取的比例，并检验它是否移动 entry threshold。该 counterfactual 是加强路线，不应在现有命题尚未完成必要性分解前自动加入模型。

## 8. Old multiplier literature 能说明什么、不能说明什么

### 已经说明

Layer A 文献足以说明：如果 $n$、routing share、commission incidence 和 ownership 都固定，那么

\[
\mathbf Y=(I-A)^{-1}\mathbf B
\]

及其 spillover、feedback、closed-loop decomposition 是已知结构。把平台 fee 固定拆到一个 HQ account，或把 local seller share 固定写进 $A$，本身不是创新。

### 没有说明

旧文献通常不包含：

- digital platform 的 ad valorem commission；
- seller 对平台 participation/free entry 的最优选择；
- online/offline substitution；
- seller origin 与 fulfillment method；
- platform-rent receipt residence；
- rent receipt location 反过来移动 seller-entry equilibrium boundary 的平台特定预测。

因此，Layer A 只建立代数祖先，**不能单独否定**平台联合机制。否定 seller-entry-only 路线的真正证据来自 Fan、Li、Goldmanis 和直接 platform-entry 文献。

## 9. Hard novelty gate

### 9.1 已经失败的表述

下列任何一种作为主命题均为 NO-GO：

1. market integration 提高 seller entry；
2. platform fee 降低 seller entry；
3. local income 提高 entry，entry 又提高 local income；
4. 更强正反馈可能产生 multiplicity/tipping；
5. fulfillment facility 降低 shipping/entry costs；
6. local ownership 提高地方 multiplier；
7. 把上述已知结果并排放在一个模型里，但没有联合交互项。

### 9.2 继续资格

只有同时满足以下条件，才允许进入正式重写：

1. **Receipt-location counterfactual**：比较相同 $\kappa$、相同消费者价格与相同技术下，platform rent 在 $L$ 或 $H$ 被收取的两个经济体。
2. **Endogenous entry response**：receipt location 通过 $Y_L$ 和订单需求改变 free-entry condition，不能只改变事后会计分配。
3. **Platform-specific non-reducibility**：关键命题必须含 $dn/d\ell$、entry cutoff 或稳定性边界；固定 $n$ 时退化为已知 multiplier benchmark，且主结果消失。
4. **Not generic network tipping**：若出现 multiplicity，必须证明其来源是 spatial rent receipt 与 local respending，而不是普通 buyer--seller network effect。
5. **Kink discipline**：local-respending kink 必须来自明确的收取/支出资格、现金流或 local-input constraint；不能为了制造不连续反应而任意设定。
6. **Observable mapping**：至少映射到 take rate、seller business location、local/external orders、fulfillment method、平台 HQ/owner residence、seller payout 和本地收入/就业。
7. **EL scope**：最终只能保留一个主命题和一个推论；若需要完整多地区定量 GE 才成立，则回到大论文而不是 EL。

### 9.3 最低合格定理

合格定理至少应证明类似以下内容，而不是预设其成立：

> 在保持平台费率、交易技术和消费者端条件不变时，将平台租金从本地收取改为远程总部收取，会通过本地再支出降低 seller-entry cutoff；当反馈足够强时，它还会移动唯一性/低进入均衡的边界。该效应严格大于平台费对 seller after-fee margin 的直接效应，并在固定 seller mass 时消失。

可操作的数学门槛是分解

\[
\frac{dn}{d\kappa}
=\left.\frac{dn}{d\kappa}\right|_{Y_L}
+\frac{\partial n}{\partial Y_L}
\frac{dY_L}{d\kappa},
\]

并证明第二项取决于 rent receipt location $\ell$。若该项只是在标准 inverse 后面乘一个固定系数，或其符号/阈值完全由 Fan/Li 的 market-size channel 给出，则仍不合格。

## 10. 可观测变量与经验映射

即使 EL 保持纯理论，模型 primitive 也应能对应现实变量：

| 理论对象 | 可观测对应 |
|---|---|
| $n$ | active third-party sellers、new revenue-positive entrants、seller exit |
| $\kappa$ | referral fee、commission、advertising/service take rate |
| seller origin | business mailing/registration address、ship-from location |
| local/external orders | origin--destination order or sales shares |
| routing | merchant fulfilled/FBA、facility node、local service share |
| rent receipt $\ell$ | platform entity/HQ/owner residence、local affiliate payout、revenue-sharing rule |
| local respending | local payroll、seller payout、merchant profit、nontradable spending/employment |

Li 的数据已经说明 seller location、fulfillment method 与 facility nodes 是可测对象。Jin and Sun (2026 AEA conference version) 进一步把 potential entrant、explored seller、positive-revenue entrant 与 surviving SMB 分开，提醒理论中的 $n$ 不能无说明地把注册、曝光、正收入和存活混成一个进入概念。

## 11. 来源核验表

| 来源 | 类型与版本 | 核验位置 | 相关性 | 证据边界 |
|---|---|---|---|---|
| [Fan et al. (2018), JIE](https://www.sciencedirect.com/science/article/abs/pii/S0022199618301594)；[作者 PDF](https://fanjt.weebly.com/uploads/1/9/4/7/19473457/alibabaeffect.pdf) | 正式期刊 + 作者全文 | equations (9)--(14), pp. 18--19 | 多地区渠道、entry、income | 无 commission/HQ receipt |
| [Li (2025), author latest PDF](https://elmerli.github.io/ecommerce.pdf) | 作者工作论文，2025-11-07，标注 updated regularly | main model pp. 13--14；Appendix B.4 pp. 45--47, eqs. (30)--(31) | fulfillment、local online entry、regional income | 版本可能更新；无显式 platform-rent receipt |
| [Goldmanis et al. (2010), NBER version](https://www.nber.org/system/files/working_papers/w14166/w14166.pdf) | NBER 作者工作论文；后发表于 *Economic Journal* | exit cutoff/free entry eqs. (10)--(11) | e-commerce、entry/exit | 无空间与平台 fee |
| [Anderson & Bedre-Defolie (2024), RAND](https://onlinelibrary.wiley.com/doi/10.1111/1756-2171.12478) | 正式期刊 | seller pricing/free-entry sections | commission、fringe seller entry | 无地区收入与 receipt residence |
| [Etro (2023), IJIO](https://www.sciencedirect.com/science/article/pii/S0167718722000789)；[作者 PDF](https://flore.unifi.it/retrieve/f99a8fc0-5dcb-4684-983b-4f0300fbdb84/Platform%20competition.pdf) | 正式开放获取期刊 + 机构全文 | seller profit/free-entry system | commission、seller entry、two-sided effects | 无空间 income receipt |
| [Teh (2022), AEJ Micro](https://www.aeaweb.org/articles?id=10.1257/mic.20190307)；[AEA PDF](https://www.aeaweb.org/content/file?id=14890) | 正式期刊 + 官方全文 | related literature and fee-instrument model | platform governance/fee/entry | 无空间闭环 |
| [Allain, Bourreau & Moraga-González (2026), CEPR DP21154](https://cepr.org/publications/dp21154) | 最新 CEPR working paper | abstract/model results | entry fee、entry failure、fee ranking | 尚非正式期刊；无地方收入 |
| [Nocke, Peitz & Stahl (2007), JEEA institutional record](https://ora.ox.ac.uk/objects/uuid%3Ace9dc89a-3606-4c72-a82b-ce67da50c4fb) | 正式期刊 + 作者机构库 | platform ownership model | ownership/governance、entry | ownership 不是收入收取地 |
| [Brown, Fitzgerald & Weber (2019), JAERE](https://www.journals.uchicago.edu/doi/abs/10.1086/705505) | 正式期刊 | abstract and empirical multiplier | local/absentee ownership | 资源 royalty，不含平台/entry |
| [Couture et al. (2021), AER Insights](https://www.aeaweb.org/articles?id=10.1257/aeri.20190382) | 正式期刊 | rural e-commerce experiment | access gains vs limited producer income | 不含结构 entry loop |
| [Jin & Sun (2026), AEA conference PDF](https://www.aeaweb.org/conference/2026/program/paper/aK2THfr2) | AEA conference working paper | entry funnel and platform experiment | entrant measurement、advertising | 不含区域收入 feedback |
| [Deng et al. (2023), Service Science](https://pubsonline.informs.org/doi/10.1287/serv.2023.0324) | 正式期刊 | platform product entry and seller spillover | commission 与 platform/seller entry | 研究 platform product entry，非本地 seller free-entry loop |

经济理论论文不适合套用临床研究的 I--VII 层级。本表改用“正式期刊/官方全文/作者工作论文”的来源等级，并将相关性与证据边界分列，避免把发表层级误当作命题重合程度。

## 12. 风险、边界与停止条件

1. Li 的作者 PDF 标注 `Updated regularly`；投稿前必须重新下载并记录版本日期，不能假设 2025-11-07 版本不变。
2. 本轮没有完成 backward/forward citation network 的穷尽搜索，也没有证明完全相同命题不存在。
3. 部分正式期刊页只提供摘要；方程判断尽量使用作者/机构全文，并在表中标明。
4. generic multiplicity 已存在于 two-sided platform 文献。即使候选模型产生多个均衡，若无法证明是 rent receipt location 导致的边界移动，不构成创新。
5. 若加入 local-respending kink 后唯一新增结果只是分段应用已知 multiplier，则停止该路线。
6. 若定理必须同时加入税收、迁移、住房、平台最优定价和多地区生产才能成立，则不适合 Economics Letters，应并回大论文。

建议设置下一轮停止条件：

- **解析 NO-GO**：无法在连续候选中证明 $\ell$ 改变 entry cutoff、稳定性或 fee effect 的额外项；
- **prior-art NO-GO**：新定理可由 Fan/Li 的 market-size entry channel 与 Anderson--Bedre-Defolie/Etro 的 fee-entry channel直接组合得到；
- **scope NO-GO**：无法在一个主命题、一个推论和约 2,000 词内自足表达；
- **CONDITIONAL-GO**：优先证明 continuous phase reversal 中存在关闭 local respending 即消失的 threshold/kink 项，并完成 routing microfoundation；若做不到，则只有 rent receipt residence 能产生新的 entry/stability threshold 时才继续。两种情况下，固定 seller mass 后的关键结果都必须消失，并能映射到 fee、seller location、routing 与 local payout 数据。

### 12.1 两条候选路线的优先级

1. **第一优先：现有 continuous phase-reversal route。** 先对 equations (21)--(23) 做 local-respending necessity decomposition，并为 routing share 提供最小 microfoundation。这条路线已经有唯一均衡、解析 threshold 和 kink，不需要新增状态变量，最符合 EL 篇幅。
2. **第二优先：spatial rent-receipt counterfactual。** 只有当第一条路线的 phase reversal 在关闭递归反馈后仍完全成立、因而不能把 local multiplier 写成关键机制时，才引入 $\ell$，比较 commission 在 local 与 remote 被收取的两个经济体。这是一项有针对性的加强，不是与第一条路线并行堆叠的新模块。
3. **不推荐同时写入两条。** 同时保留 continuous activation、endogenous receipt localization 和平台最优 fee 会迅速超出 EL 的一个命题范围，也会使 prior-art 定位变得模糊。

## 13. 最终判定

```text
seller_entry_only_route = NO_GO
fee_entry_threshold_route = NO_GO
generic_entry_income_feedback_route = NO_GO
fulfillment_access_entry_route = NO_GO_AS_CORE_CONTRIBUTION
continuous_candidate_eq17_18_20 = NO_GO_AS_CORE
continuous_candidate_eq21_23_phase_reversal = CONDITIONAL_GO
spatial_rent_receipt_x_entry_feedback = OPTIONAL_STRENGTHENING_IF_NEEDED
novelty_certification = NOT_YET
formal_manuscript_rewrite = PAUSED
```

最准确的阶段性表述是：原 EL 的过度简化确实删除了有潜力的空间 incidence 机制，但恢复 seller entry 本身仍不够。可继续检验的唯一窄路线，是把平台 commission 的**空间收取与再支出**变成一个会改变 seller-entry equilibrium 的 primitive，并证明它产生 Fan/Li 与直接 platform-entry 文献中都没有的可证伪结果。
