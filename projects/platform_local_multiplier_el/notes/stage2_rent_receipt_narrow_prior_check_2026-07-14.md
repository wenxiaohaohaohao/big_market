# Stage 2：platform commission localization × seller entry 的 narrow direct-prior check

日期：2026-07-14  
项目：*Platform Intermediation and Local Multipliers*  
审计对象：`stage2_spatial_rent_receipt_entry_feasibility_2026-07-14.md` 中拟作为主结果的 receipt-location theorem  
文件边界：本轮只新增本审计笔记；未修改 `paper/main.tex`、`paper/appendix.tex`、`paper/references.bib`、验证代码或编译结果。

## 1. 结论先行

本轮有界、定向检索**没有发现 direct overlap**：没有找到一篇论文同时证明，在平台总 take rate、消费者价格、平台份额、seller net-of-fee margin 与交易技术不变时，仅改变当地交易所产生的平台佣金由本地交易服务节点还是远程总部收取的比例，会通过本地收入再支出移动 local seller 的 free-entry active set，并在唯一阈值处产生连续但不可微的收入与 seller-mass 反应。

更精确的判定是：

```text
bounded_direct_overlap = NOT_FOUND
institutional_local_payout_prior = FOUND
platform_revenue_sharing_and_participation_prior = FOUND
local_vs_absentee_income_multiplier_prior = FOUND
regional_income_and_seller_entry_prior = FOUND
joint_receipt_location_x_respending_x_free_entry_theorem = NOT_FOUND
priority_certification = NOT_ESTABLISHED
route_status = CONDITIONAL_GO
```

这意味着 direct-prior gate 可以暂定通过，但不能据此写 `first paper` 或无条件声称 priority。最大的剩余风险不是某篇同式先例，而是审稿人把结果概括为一个通用链条：

\[
\text{local transfer}
\longrightarrow
\text{local demand}
\longrightarrow
\text{free-entry cutoff}.
\]

因此，论文的贡献必须严格限定为**平台交易合同中的 spatial incidence**：固定总 fee 与买卖双方条件，只改变同一笔 transaction commission 的本地 payout share；并用 no-respending counterfactual 证明，seller-organization effect 在关闭该通道后精确消失。kink 本身是标准 active-set 数学，不能单独作为创新。

## 2. 被检验的精确定理

为避免把不同含义的“revenue sharing”混在一起，本文候选中的 \(\lambda\) 定义为：本地居民平台交易产生的总 commission \(\tau\phi Y\) 中，支付给既有本地 transaction-service node 并成为本地可支配收入的比例。总部取得其余部分：

\[
\underbrace{\lambda\tau\phi Y}_{\text{local transaction-service payout}},
\qquad
\underbrace{(1-\lambda)\tau\phi Y}_{\text{remote-HQ receipt}}.
\]

这里的“buyer-side commission”是指**由本地居民 gross platform expenditure 产生并内含于交易额的 commission**，不一定是另向消费者开列的独立 buyer fee。比较中固定：

\[
(\tau,p,s,E,F,\mu,\chi),
\]

从而 seller payout share \(1-\tau\)、消费者价格、平台份额、外部订单和 routing technology 都不随 \(\lambda\) 改变。

订单池与自由进入满足

\[
Q=E+\phi Y,
\]

\[
n\geq0,
\quad
F-\mu(1-\tau)\frac{Q}{n+\chi}\geq0,
\quad
n\left[F-\mu(1-\tau)\frac{Q}{n+\chi}\right]=0.
\]

地方收入固定点包含 local payout 与进入后的 seller receipts：

\[
Y
=B+c_0Y+\lambda\tau\phi Y
+(1-\tau)[E+\phi Y-Q_E]_+,
\qquad
Q_E=\frac{F\chi}{\mu(1-\tau)}.
\]

待保护的联合预测是：若 \(Q_0(0)<Q_E<Q_0(1)\)，则存在唯一 \(\lambda^*\in(0,1)\)，使本地 seller 在 \(\lambda\leq\lambda^*\) 时不进入、在 \(\lambda>\lambda^*\) 时进入；\(Y\) 与 \(n\) 在阈值处连续，但右导数严格高于左导数。若固定居民平台订单 \(\bar X_P\)，则

\[
Q=E+\bar X_P
\quad\Longrightarrow\quad
n=\left[\frac{\mu(1-\tau)Q}{F}-\chi\right]_+,
\]

所以 \(n\) 对所有 \(\lambda\) 完全不变，而不仅是局部导数为零。

一篇文献只有同时包含以下五项，才被判为 direct overlap：

1. 固定总平台费、消费者条件与 seller margin，只改变 commission receipt allocation；
2. 明确区分本地与远程总部的 commission recipient；
3. 本地 recipient 的收入进入地区再支出或 household-income fixed point；
4. local seller/provider 具有 free-entry active set；
5. receipt share 移动 entry threshold，并产生相应 kink 或 regime switch。

命中一至四项但没有第五项，只能是 adjacent 或 nested prior。

## 3. 检索范围与方法

### 3.1 来源

检索日期为 2026-07-14。优先核验期刊官网、AEA/NBER、INFORMS、OECD、Brill/IFAMR、CEPR、作者或大学机构版本。SSRN 仅用于尚未正式发表或仍在更新的 working paper。商业案例只用于发现检索词，不作为定理重合的证据。

### 3.2 定向检索式

主要检索式包括：

1. `platform revenue sharing local agents seller entry commission`
2. `platform commission local agents e-commerce revenue sharing`
3. `local affiliate platform commission seller entry`
4. `rural e-commerce service station commission operator entry`
5. `platform revenue sharing seller entry economic theory`
6. `platform commission rebate local sellers entry theory`
7. `platform fee allocation local headquarters local income seller entry`
8. `platform rent spatial incidence regional income`
9. `local ownership platform economy regional income`
10. `platform cooperative local multiplier economic model`
11. `global platform local provider revenue sharing entry regional demand`
12. `human intermediaries platform agent wage provider participation`
13. `franchise terminal platform commission local operator economics`
14. `platform transaction reward local service center commission`

另外逐篇反向检查 Couture et al.、Cai et al.、Bhargava et al.、Feldman et al.、Adebola et al.、Fan et al.、Li、Brown et al. 以及 commission--seller-entry 文献的模型对象与结果。检索重点是同一联合定理，不以关键词共现替代方程层级判断。

### 3.3 证据边界

这是为路线选择服务的 bounded direct-prior check，不是 Scopus/Web of Science 的穷尽 systematic review。没有伪造检索总命中数，也没有把“未发现”写成“不存在”。working paper 可能继续更新，尤其需要在投稿前重新核对其最新版本。

## 4. 最接近的文献

### 4.1 Couture et al. (2021)：最直接的制度映射，但没有 entry theorem

Couture, Faber, Gu, and Liu 的 AEA Online Appendix 明确记录：项目在村内设置 e-commerce terminal，terminal manager 协助本地家庭买卖；manager 对每笔经 terminal 完成的交易获得约 3--5% reward，平台还会从潜在 local store operators 中征集申请者。这个事实直接支持“transaction-contingent local payout”不是任意的地区转移。

- **已有对象**：本地 platform terminal、本地交易协助者、按交易额支付的 3--5% reward、local operator selection。
- **缺失对象**：没有在固定总 take rate 下比较 local payout 与 HQ receipt；没有 household-income respending fixed point；申请 terminal operator 不是 local seller free entry；没有 receipt-induced seller threshold 或 kink。
- **判定**：最接近的 institutional analogue，非 direct theoretical overlap。

来源：[AEA article](https://www.aeaweb.org/articles?id=10.1257/aeri.20190382)；[AEA Online Appendix](https://www.aeaweb.org/articles/materials/14082)；[NBER version](https://www.nber.org/papers/w24384)。

### 4.2 Cai et al. (2019)：最接近的 local commission + agent participation 模型

Cai, Wang, Xia, and Wang 研究农村电商服务中心（RESC）的 principal--agent governance。服务中心协助本地居民买卖并按交易量取得 commission；地方政府也对 assisted purchases 和帮助农户线上销售设置奖励。其模型把 e-commerce service provider 支付的 commission 与政府 subsidy 纳入 operator revenue，并以 participation/individual-rationality constraint 分析 operator recruitment、effort 与 center sustainability。

- **已有对象**：本地 e-commerce agent、transaction commission、operator participation/closure、服务中心的激励合同。
- **缺失对象**：进入者是 RESC operator，不是商品 seller mass；没有 local household-income fixed point；没有把同一平台 fee 在 local 与 HQ 之间分配；没有 commission receipt 经再支出移动 seller entry threshold；没有 active-set kink。
- **判定**：closest local-agent contract prior；对本联合定理为 adjacent。

来源：[official journal PDF](https://brill.com/view/journals/ifam/22/3/article-p381_5.pdf)；[AgEcon Search record](https://ageconsearch.umn.edu/record/288077/)。正式期刊版为 *International Food and Agribusiness Management Review* 22(3), 381--396，DOI: 10.22434/IFAMR2018.0088。

### 4.3 Adebola, Arora, and Zhang：最接近的 human-intermediary platform theory

*Sharing Platforms in Emerging Markets: The Role of Human Intermediaries* 建模 booking agents 聚合碎片化的本地需求。平台同时选择 customer price、provider wage 与 agent wage，并研究 agents 对 provider earnings、customer surplus 和 platform profit 的影响。本次检索返回的 SSRN revision metadata 不一致：打开的 record 显示 2025-11-04，搜索索引显示 2026-03-31；因此本笔记把它视为持续更新的 working paper，不据此认定最终版本日期。

- **已有对象**：平台、本地 human intermediary、agent wage、需求聚合、providers 与平台的联合均衡。
- **缺失对象**：agent wage 与 consumer/provider prices 是平台优化变量，并非固定总 fee 下的纯 receipt-location counterfactual；没有 local-vs-HQ income receipt；没有地区 household respending；摘要和可核验模型说明没有 local seller free-entry active set 或 receipt-induced kink。
- **判定**：它阻止本文把“本地人力中介改变平台均衡”写成新意，但不重合于 spatial receipt theorem。

来源：[SSRN working paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4190725)。

### 4.4 Bhargava, Wang, and Zhang (2022)：revenue sharing 改变 producer incentives

Bhargava et al. 研究偏向 small businesses 的 differential revenue-sharing design，分析 producer output、平台利润与 welfare。它是本轮最接近的“platform revenue allocation 改变供给侧行为”先例。

- **已有对象**：平台 revenue-sharing rule、异质 producers、参与/产出激励与 spillovers。
- **缺失对象**：revenue share 在 platform 与 producers 之间分配，不是在 local service recipient 与 remote HQ 之间按 receipt residence 分配；无空间地区、无地方 income-respending loop、无 local seller free-entry threshold 或 kink。
- **判定**：direct platform-revenue-sharing prior；对空间联合定理为 adjacent。

来源：[Management Science](https://pubsonline.informs.org/doi/10.1287/mnsc.2022.4545)，68(11):8249--8260。

### 4.5 Feldman, Frazelle, and Swinney (2023)：固定订单上的 restaurant--platform revenue allocation

该文研究 food-delivery platform 的 percentage commission，并提出平台向餐厅支付 percentage revenue share 加 fixed fee 的协调合同。合同可以灵活分配 restaurant 与 platform 之间的订单收入。

- **已有对象**：transaction commission、restaurant/platform contract、同一订单收入的灵活分配。
- **缺失对象**：没有收取地或 recipient residence；restaurant 是现有经营主体而非本地 seller free-entry mass；无地区再支出与 entry threshold。
- **判定**：contract/revenue-allocation adjacent prior。

来源：[Management Science](https://pubsonline.informs.org/doi/10.1287/mnsc.2022.4390)，69(2):812--823。

### 4.6 Duan, Huang, and Shou (2015)：global platform 与 local provider 分成

*Pricing for Local and Global WiFi Markets* 研究 global WiFi provider 与各地 local provider 的 revenue-sharing agreement。global provider 为使用 local infrastructure 与 local provider 分成，用户随后在 local/global services 间选择。这是“全球平台把当地市场收入的一部分支付给当地服务商”的强制度和理论近邻。其模型中，在给定 global-service price 后，revenue-sharing ratio 不改变用户选择，这一点与本文固定消费者条件的隔离思路尤其接近。

- **已有对象**：global provider、local provider、按市场收入分成、消费者服务选择。
- **缺失对象**：均衡中 price 与 revenue share 由 bargaining 联合决定；share 分配的是合作服务收入而非按 recipient residence 进入 household income；local provider 预先存在；没有地方 household respending，也没有 seller free entry 或 kink。
- **判定**：local/global revenue-sharing adjacent prior，非 direct overlap。

来源：[author/arXiv version](https://arxiv.org/abs/1407.4355)；正式发表于 *IEEE Transactions on Mobile Computing* 14(4)。

### 4.7 OECD (2023)：local ownership 与 local value retention 的政策先例

OECD 的 platform-cooperative 报告明确讨论 conventional platforms 将价值集中并返还给平台 owners，而 local cooperative ownership 有助于把收入、surplus 和投资留在社区并继续在当地循环。

- **已有对象**：platform ownership、local value retention、community circulation。
- **缺失对象**：没有解析模型、固定 fee counterfactual、seller free entry 或 threshold。
- **判定**：政策与制度动机，不能作为理论重合证据。

来源：[OECD publication](https://www.oecd.org/en/publications/empowering-communities-with-platform-cooperatives_c2ddfc9f-en.html)，OECD LEED Paper No. 2023/14。

### 4.8 四组必须承认的模块祖先

以下文献分别覆盖候选定理的单独模块，但没有覆盖 joint prediction：

1. **regional income 与 online seller entry**：Fan et al. (2018) 以及 Li 的 multi-region e-commerce working paper 已使 destination/origin income 影响 online seller entry、sales 与 regional income。因此“local demand promotes entry”不是新结果。
2. **commission 与 seller mass/free entry**：Anderson and Bedre-Defolie、Etro、Teh 以及 Allain, Bourreau, and Moraga-González 已研究 commission/entry fee 对 seller participation、variety 与 no-entry boundary 的作用。因此“fee moves entry cutoff”不是新结果。
3. **local versus absentee receipt**：Brown, Fitzgerald, and Weber (2019) 已说明相同资源收入因 local/absentee ownership 不同而产生不同地方 income multiplier。因此“receipt residence matters”不是新结果。
4. **fixed-coefficient respending**：SAM、Miyazawa、regional IO 与 local-multiplier 文献已覆盖固定收入份额下的重复支出 inverse。因此给定 seller active set 后的 multiplier 不是新结果。

候选可以保留的只可能是四组模块的**交互项**：receipt residence 在固定交易楔子下内生改变 seller active set，并且该组织效应在关闭本地再支出时消失。

## 5. Direct-overlap matrix

| 文献 | 固定总 fee/消费者条件，仅改 receipt allocation | local vs remote commission recipient | local income respending | local seller/provider free entry | receipt-induced threshold/kink | 判定 |
|---|---:|---:|---:|---:|---:|---|
| Couture et al. (2021) | 否，描述项目合同 | 是，本地 terminal reward | 否 | 否，operator application 不是 seller free entry | 否 | 最接近制度事实 |
| Cai et al. (2019) | 否，commission/subsidy 是激励合同 | 是，本地 RESC operator receipt | 否 | 部分：operator IR，不是 seller mass | 否 | local-agent contract adjacent |
| Adebola et al. (2025 WP) | 否，平台内生选 price/wages | 是，本地 booking-agent wage | 否 | 否，provider pool/operations 不是本地 seller free-entry active set | 否 | human-intermediary theory adjacent |
| Bhargava et al. (2022) | 否，改变 producer revenue-sharing design | 否，非空间 producer/platform split | 否 | producer incentives/participation | 否 | platform sharing adjacent |
| Feldman et al. (2023) | 否，合同同时改变 payment terms | 否，非空间 restaurant/platform split | 否 | 否 | 否 | contract adjacent |
| Duan et al. (2015) | 否，price 与 share 联合谈判 | 是，global/local provider split | 否 | 否，local provider 已存在 | 否 | global/local sharing adjacent |
| OECD (2023) | 不适用 | 是，local/community ownership | 叙述性地有 | 否 | 否 | policy motivation |
| Fan et al.; Li | 无 platform commission allocation | 否 | regional GE/income | 是 | income/market-access entry cutoff | entry module nested |
| Platform fee-entry literature | fee 本身改变 seller payoff | 否 | 否 | 是 | fee-induced cutoff | fee-entry module exact |
| Brown et al. (2019) | 同一资源收入比较 ownership | 是，local/absentee receipt | 是，经验 multiplier | 否 | 否 | spatial-incidence module adjacent |
| 当前候选 | **是** | **是** | **是** | **是** | **是** | 五项联合未在本轮发现 |

矩阵说明的是 direct overlap 是否存在，不是“把五项放进同一模型就自然形成高贡献”。五项中的每一项都有清楚祖先；论文必须证明联合机制产生一个不可由固定-coefficient multiplier 或普通 fee-entry comparative statics替代的预测。

## 6. 对创新性的严格判断

### 6.1 已被占据的结果

下列表述不能进入 abstract 或 contribution paragraph：

- 平台可以使用本地 agents 或 service centers；
- local agents 可以按交易获得 commission/reward；
- revenue sharing 会改变 producers/providers 的行为；
- local ownership 或 local receipt 会提高地方 multiplier；
- 更高 local demand 会促进 seller entry；
- fixed cost 会产生 no-entry threshold；
- active-set change 会产生 kink。

### 6.2 尚未发现同一先例的联合结果

可防守的窄贡献是：

> Holding the platform take rate, buyer price, seller payout, platform share, external demand, and routing technology fixed, reallocating a transaction-attributed part of the commission from a remote headquarters to an existing local service node can activate local seller entry through induced local spending. The entry effect disappears when platform expenditure is held fixed.

这里真正有识别力的是三个限制同时成立：

1. **receipt-only**：\(\lambda\) 不改变 seller margin 或消费者 wedge；
2. **organization response**：\(\lambda\) 改变的不只是事后收入核算，而是 seller active set；
3. **mechanism falsification**：固定平台订单后，\(n\) 对所有 \(\lambda\) 完全不变。

kink 只能作为 active-set implication，不应被描述为独立的新数学现象。

### 6.3 仍然存在的 generic-transfer objection

即使 direct overlap 未找到，当前代数仍适用于任何 transaction-proportional local transfer。为避免退化成 generic transfer theorem，正式稿必须：

- 把 \(\lambda\tau\) 唯一解释为 `local transaction-service payout`，不要在 terminal reward、affiliate ownership、equity ownership 与税收返还之间切换；
- 用 Couture 的 terminal-manager reward 与 Cai 的 RESC commission 说明合同对象真实存在；
- 明确服务节点、服务质量、采用率、价格与 routing 在比较中固定；
- 承认若 payout 同时改变 agent effort、adoption、financing 或 fulfillment，则 no-respending proposition 不再是普遍结论；
- 不声称所有平台地方化收入安排都满足该 exclusion restriction。

## 7. 风险评级与路线建议

| 风险 | 评级 | 原因 |
|---|---|---|
| 完全同式 direct prior | 低至中 | 本轮未找到；但没有完成数据库级穷尽检索 |
| 模块拼接/obviousness | 中至高 | local payout、respending、entry threshold 均分别已知 |
| 制度 microfoundation | 中 | Couture/Cai/Adebola 提供现实基础；必须冻结一种合同解释 |
| 数学独立贡献 | 中低 | contraction、complementarity 与 kink 都是标准工具 |
| 经济预测的可证伪性 | 中高 | 固定 take rate 下 local-vs-HQ payout 与 no-respending counterfactual 清楚 |
| Economics Letters 篇幅适配 | 中高 | 若完全替换旧模型，可压缩为一个 Proposition 和一个 Corollary |

**推荐继续这条路线，但以 `conditional novelty` 写作。** 它比原 scalar multiplier 或普通 seller-entry route 更接近原项目中的“交易组织与价值捕获地分离”，也比把 fee、entry 和 local multiplier简单相加更有清楚的控制实验。

正式写作时建议把 primitive 记为

\[
r\equiv\lambda\tau\in[0,\tau],
\]

称为 `local transaction-service payout rate`；\(\lambda=r/\tau\) 只是总 commission 的本地份额。这样可避免与 platform literature 中常用作 seller revenue share 的 \(\lambda\) 混淆，也可直接表达 HQ receipt 为 \(\tau-r\)。

## 8. 最终 gate

本轮只解决 adversarial review 中的 narrow direct-prior 阻断项。判定为：

```text
narrow_direct_prior_gate = PASS_CONDITIONALLY
same_joint_theorem_found = NO
safe_to_claim_first = NO
safe_to_claim_separate_literatures = YES_WITH_CITATIONS
local_agent_as_new_primitive = NO
kink_as_new_result = NO
receipt_location_changes_entry_via_respending = DEFENSIBLE_CANDIDATE
```

正式稿最安全的定位不是“首次研究 local agents”或“首次证明平台引起地方 multiplier”，而是：现有研究分别考察了本地平台 intermediaries、platform revenue-sharing、seller entry 与 local/absentee income incidence；本文隔离一个尚未在本轮检索中发现的联合预测——**同一平台交易楔子的收取地，可以经地方再支出改变本地 seller 的进入边界。**

投稿前仍需做两项更新性检查：重新下载 Li 的最新 working-paper version；重新核对 Adebola, Arora, and Zhang 是否已正式发表或新增 endogenous provider-entry extension。若任一新版本加入 regional income respending 与 receipt-induced entry threshold，应重新启动 direct-overlap gate。
