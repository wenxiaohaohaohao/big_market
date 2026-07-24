# 新结构经济学（NSE）核心文献与变量/参数定义手册

> **用途**：为过渡性 NSE 论文建模时提供可引用的变量定义出处
> **编排**：按新稿六节主题分组，每篇文献标注其核心变量/参数定义
> **日期**：2026-07-23
>
> **2026-07-24 使用边界**：本文件是文献来源和候选变量的 inventory，
> 不是当前模型的变量清单或 model contract。只有同时服务于
> consumer access、comparative-advantage realization、organizational
> embeddedness、local capture、nominal income 或 consumption-equivalent
> income 的对象，才可从本手册进入
> `notes/01_theory/model_contract.md`。旧稿中的 \(q_i\)、多渠道成本、
> 动态组织资本、NEG 和 national welfare 等条目仅表示文献中存在这些概念，
> 不表示它们已被当前论文采用。

---

## 第1节：Introduction & 新结构经济学总论

### 1.1 NSE 总纲性文献

| # | 文献                                                                                                                                                  | 核心变量/参数                                                                                                                                                                                                                                                        |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | **Lin, J.Y. (2011).** "New Structural Economics: A Framework for Rethinking Development." *World Bank Research Observer*, 26(2): 193–221.    | 要素禀赋 endowment:\\(K, L, N\\)（资本、劳动、自然资源）；禀赋结构 endowment structure: \\(K/L\\)；比较优势 comparative advantage；自生能力 viability；最优产业结构 optimal industrial structure；硬/软基础设施 hard/soft infrastructure；交易成本 transaction costs |
| 2 | **Lin, J.Y. (2012).** *New Structural Economics: A Framework for Rethinking Development and Policy.* World Bank Publications.                 | 同上，加上：潜在比较优势 latent comparative advantage；实际比较优势 actual comparative advantage；要素生产成本 factor costs of production；总成本 total costs = factor costs + transaction costs                                                                     |
| 3 | **Lin, J.Y. (2012).** *The Quest for Prosperity: How Developing Economies Can Take Off.* Princeton University Press.                          | 增长甄别与因势利导框架 GIFF (Growth Identification and Facilitation Framework)；后发优势 latecomer advantage                                                                                                                                                         |
| 4 | **Lin, J.Y. (2019).** "New Structural Economics: The Third Generation of Development Economics." *GEGI Working Paper 027*, Boston University. | 结构内生性（structure endogeneity）；要素禀赋结构决定生产结构、基础设施结构、上层制度结构；先行者外部性 first-mover externality                                                                                                                                      |
| 5 | **林毅夫 (2017).** "新结构经济学的理论基础和发展方向." 北京大学国家发展研究院.                                                                  | 要素禀赋结构\\(\rightarrow\\) 比较优势 \\(\rightarrow\\) 最优产业结构；有效的市场 efficient market；有为政府 facilitating state                                                                                                                                      |
| 6 | **林毅夫 (2026).** "新结构经济学的理论内核与创新贡献."                                                                                          | 具有物质第一性的要素禀赋及其结构；生产结构（产业+技术）；基础设施结构；上层制度结构；自生能力定义为"在开放竞争市场中不需外部保护补贴即能获得社会可接受正常利润率的能力"                                                                                              |

### 1.2 自生能力（Viability）核心文献

| # | 文献                                                                                                                                                                                       | 核心变量/参数                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 7 | **Lin, J.Y. (2003).** "Development Strategy, Viability, and Economic Convergence." *Economic Development and Cultural Change*, 51(2): 277–308.                                    | 自生能力 viability：企业\\(V_i = 1\\) 若有自生能力，\\(V_i = 0\\) 若需要保护/补贴；发展战略 strategy（CAF: comparative-advantage-following vs. CAD: comparative-advantage-defying） |
| 8 | **Lin, J.Y. & Tan, G. (1999).** "Policy Burdens, Accountability, and the Soft Budget Constraint." *American Economic Review*, 89(2): 426–31.                                      | 政策性负担 policy burden：战略性负担 strategic burden + 社会性负担 social burden；软预算约束 soft budget constraint                                                                 |
| 9 | **Lin, J.Y. & Zhang, P. (2009).** "Industrial Structure, Appropriate Technology and Economic Growth in Less Developed Countries." *World Bank Policy Research Working Paper* 4905. | 适宜技术 appropriate technology：\\(A_i^* = f(E_i)\\)，即最优技术选择由要素禀赋内生决定；资本密集度 capital intensity：\\(k_j = K_j/L_j\\)；技术前沿 technology frontier            |

### 1.3 比较优势与贸易理论交叉

| #  | 文献                                                                                                                                                                | 核心变量/参数                                                                                                                        |
| -- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| 10 | **Heckscher, E. & Ohlin, B. (1933/1991).** *Heckscher-Ohlin Trade Theory.* MIT Press.                                                                       | 要素禀赋：\\(K, L\\)；要素密集度 factor intensity：\\(a_{Kj}/a_{Lj}\\)；要素价格 w, r；相对比较优势                                  |
| 11 | **Dornbusch, R., Fischer, S. & Samuelson, P.A. (1980).** "Heckscher-Ohlin Trade Theory with a Continuum of Goods." *American Economic Review*, 70: 203-224. | 连续商品 continuum of goods：\\(z \in [0,1]\\) 按资本密集度排序；单位成本：\\(a(z)w + b(z)r\\)；临界商品 cutoff good \\(\tilde{z}\\) |
| 12 | **Deardorff, A.V. (1980).** "The General Validity of the Law of Comparative Advantage." *Journal of Political Economy*, 88(5): 941-57.                      | 自给自足价格 autarky price\\(p_i^a\\)；贸易后世界价格 \\(p_i^w\\)；比较优势链 chain of comparative advantage                         |

---

## 第2节：Model Environment（禀赋结构、行业要素密集度、成本结构）

### 2.1 NSE 基准模型

| #  | 文献                                                                                                                                                                  | 核心变量/参数                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| -- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 13 | **Ju, J., Lin, J.Y. & Wang, Y. (2015).** "Endowment Structures, Industrial Dynamics, and Economic Growth." *Journal of Monetary Economics*, 76(C): 244–263.  | **这是NSE的基准正式模型。** 核心变量：资本禀赋 \\(K_t\\)；劳动 \\(L\\)（常数）；禀赋结构 \\(\kappa_t \equiv K_t/L\\)；行业 \\(j \in [0, \infty)\\) 按资本密集度递增排序；行业资本密集度 \\(\phi(j)\\) 递增函数；行业产出 \\(Y_j(t)\\) 呈 hump-shaped 生命周期；资本门槛 \\(K_j^*\\) 行业出现阈值；工资率 \\(w_t\\)；利率 \\(r_t\\)；CES 生产函数：\\(Y_j = [\alpha_j K_j^{(\sigma-1)/\sigma} + (1-\alpha_j)L_j^{(\sigma-1)/\sigma}]^{\sigma/(\sigma-1)}\\) |
| 14 | **Lin, J.Y. & Wang, Y. (2017).** "Remodeling Structural Change." Chapter for *Oxford Handbook of Structural Transformation*.                                  | 将 Ju-Lin-Wang (2015) 定位为 NSE 基准模型；区分结构less 框架（单部门\\(Y=AK^\alpha H^\beta L^{1-\alpha-\beta}\\)）vs. 结构建模；多个结构维度：endowment structure, industrial structure, financial structure, infrastructure structure                                                                                                                                                                                                                           |
| 15 | **Lin, J.Y., Liu, Z. & Zhang, B. (2023).** "Endowment, Technology Choice, and Industrial Upgrading." *Structural Change and Economic Dynamics*, 65: 364–381. | 技术选择 technology choice：在 CES 生产函数中选择资本/劳动增强系数\\(A_K, A_L\\)；技术前沿 technology frontier：\\(A_K^\theta + A_L^\theta \leq 1\\)；行业 j 的要素密集度：\\(\theta_j\\)；leading industry（市场份额最大的行业）；资本份额 \\(\alpha_j\\) 随时间递增                                                                                                                                                                                            |
| 16 | **Caselli, F. & Coleman, J. (2006).** "The World Technology Frontier." *American Economic Review*, 96(3): 499-522.                                            | 技术前沿\\(A_K^\theta + A_L^\theta = 1\\)；技术采用成本 technology adoption cost                                                                                                                                                                                                                                                                                                                                                                                 |

### 2.2 要素禀赋结构与要素价格

| #  | 文献                                                                                                                                                   | 核心变量/参数                                                                                                                              |
| -- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| 17 | **Acemoglu, D. (2003).** "Labor-and Capital-Augmenting Technical Change." *Journal of the European Economic Association*, 1(1): 1-37.          | 劳动增强型技术进步\\(A_L\\)；资本增强型技术进步 \\(A_K\\)；要素增强系数的边界约束                                                          |
| 18 | **Acemoglu, D. & Guerrieri, V. (2008).** "Capital Deepening and Nonbalanced Economic Growth." *Journal of Political Economy*, 116(3): 467-498. | 资本深化 capital deepening：\\(K/L \uparrow\\)；两部门模型：资本密集部门 vs. 劳动密集部门；部门要素密集度差异 \\(\alpha_1 \neq \alpha_2\\) |
| 19 | **Zuleta, H. (2008).** "Factor Saving Innovations and Factor Income Shares." *Review of Economic Dynamics*, 11(4): 836-851.                    | 要素节约型创新 factor-saving innovation；要素收入份额的变化                                                                                |

### 2.3 禀赋与产业选择

| #  | 文献                                                                                                                                        | 核心变量/参数                                                                                                                                                                    |
| -- | ------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 20 | **Hausmann, R. & Rodrik, D. (2003).** "Economic Development as Self-Discovery." *Journal of Development Economics*, 72(2): 603-633. | 自我发现 self-discovery；现代部门 vs. 传统部门；先行企业 first mover；信息外部性 information externality；模仿成本 imitation cost；先行者利润\\(\pi^F\\)，跟进者利润 \\(\pi^I\\) |
| 21 | **Hausmann, R., Hwang, J. & Rodrik, D. (2007).** "What You Export Matters." *Journal of Economic Growth*, 12(1): 1-25.              | 出口 sophistication：\\(EXPY_i = \sum_j (x_{ij}/X_i) PRODY_j\\)；\\(PRODY_j\\) 产品 j 的收入水平加权平均                                                                         |
| 22 | **Hidalgo, C. & Hausmann, R. (2009).** "The Building Blocks of Economic Complexity." *PNAS*, 106(26): 10570-10575.                  | 经济复杂度 economic complexity index (ECI)；产品空间 product space；能力 capabilities                                                                                            |

---

## 第3节：产业自生能力、比较优势实现与进入门槛

### 3.1 自生能力与产业选择

| #  | 文献                                                                                                                                                                                     | 核心变量/参数                                                                                                                                                                                                           |
| -- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 23 | **Lin, J.Y. (2009).** *Economic Development and Transition: Thought, Strategy, and Viability.* Cambridge University Press.                                                       | 自生能力 viability\\(V\\) 的正式定义；比较优势遵循战略 CAF strategy；违背比较优势战略 CAD strategy；要素相对价格信号的作用                                                                                              |
| 24 | **Lin, J.Y. & Chang, H-J. (2009).** "Should Industrial Policy in Developing Countries Conform to Comparative Advantage or Defy It?" *Development Policy Review*, 27(5): 483-502. | 产业政策的"遵循 vs. 违背"比较优势之争；目标产业 target industry；补贴成本 subsidy cost                                                                                                                                  |
| 25 | **Wang, Y. (2022).** "Market Structure, Factor Endowment, and Technology Adoption." *Research in International Business and Finance*, 63: 101787.                                | 新技术（资本密集型）new capital-intensive technology；先行者垄断 monopoly rent；模仿滞后 imitation lag：新技术在 t+1 期变为公共知识；禀赋结构如何决定垄断利润大小；可能的多重均衡；"资本增加反而延迟技术采用"的非单调性 |
| 26 | **Wang, Y. (2012).** "Market Structure, Factor Endowment and Industrial Upgrading." Working Paper, HKUST.                                                                          | 先行者 first mover；内生市场结构：垄断 vs. 完全竞争；资本门槛\\(\bar{K}\\) 决定工业升级是否发生；效率损失：旧产业存活过久、升级被延迟                                                                                   |

### 3.2 产业选择与结构转型

| #  | 文献                                                                                                                                                                                       | 核心变量/参数                                                                                                            |
| -- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| 27 | **Matsuyama, K. (1992).** "Agricultural Productivity, Comparative Advantage, and Economic Growth." *Journal of Economic Theory*, 58(2): 317-334.                                   | 两部门（农业/制造业）；封闭 vs. 开放经济；农业生产力\\(\theta_A\\)；比较优势在部门选择中的作用                           |
| 28 | **Matsuyama, K. (2009).** "Structural Change in an Interdependent World: A Global View of Manufacturing Decline." *Journal of the European Economic Association*, 7(2-3): 478-486. | 全球视角的结构转型；制造业份额的 hump-shape；各国交互影响                                                                |
| 29 | **Herrendorf, B., Rogerson, R. & Valentinyi, A. (2013).** "Growth and Structural Transformation." in *Handbook of Economic Growth*, Vol. 2.                                        | 三部门结构转型（农业→工业→服务业）；收入效应 income effect vs. 相对价格效应 relative price effect；部门 TFP 增长率差异 |
| 30 | **Ngai, R. & Pissarides, C. (2007).** "Structural Change in a Multisector Model of Growth." *American Economic Review*, 97(1): 429-443.                                            | 多部门模型；部门 TFP 增长率：\\(g_i\\)；CES 偏好：\\(\varepsilon \lessgtr 1\\) 决定部门份额变化方向                      |
| 31 | **Duarte, M. & Restuccia, D. (2010).** "The Role of the Structural Transformation in Aggregate Productivity." *Quarterly Journal of Economics*, 125(1): 129-173.                   | 部门劳动生产率 labor productivity across sectors；结构转型对总体生产率的贡献                                             |

### 3.3 适宜技术与进入

| #  | 文献                                                                                                                              | 核心变量/参数                                                                                                                     |
| -- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| 32 | **Acemoglu, D. & Zilibotti, F. (2001).** "Productivity Differences." *Quarterly Journal of Economics*, 116(2): 563-606.   | 技术-技能匹配 technology-skill mismatch；发达国家技术对发展中国家"不适宜"；行业\\(j\\) 的技能密集度 \\(s_j\\)；技能禀赋 \\(H/L\\) |
| 33 | **Atkinson, A.B. & Stiglitz, J.E. (1969).** "A New View of Technological Change." *Economic Journal*, 79(315): 573-578.   | 本地化技术进步 localized technical change；技术只能在特定要素比例下有效运行                                                       |
| 34 | **Basu, S. & Weil, D. (1998).** "Appropriate Technology and Growth." *Quarterly Journal of Economics*, 113(4): 1025-1054. | 适宜技术 appropriate technology；技术前沿是\\(K/L\\) 的函数；各国因禀赋不同而采用不同技术                                         |

---

## 第4节：异质企业进入、渠道选择与平台中介

### 4.1 异质企业进入

| #  | 文献                                                                                                                                                          | 核心变量/参数                                                                                                                                                                                                                                                        |
| -- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 35 | **Melitz, M.J. (2003).** "The Impact of Trade on Intra-Industry Reallocations and Aggregate Industry Productivity." *Econometrica*, 71(6): 1695-1725. | 企业异质性 productivity\\(\varphi \sim G(\varphi)\\)；固定进入成本 \\(f_E\\)；固定生产成本 \\(f_D\\)；固定出口成本 \\(f_X\\)；冰山贸易成本 \\(\tau\\)；生产率门槛：\\(\varphi^*\\)（国内生产门槛）、\\(\varphi_X^*\\)（出口门槛）；零利润条件 ZCP；自由进入条件 FE |
| 36 | **Melitz, M.J. & Redding, S.J. (2014).** "Heterogeneous Firms and Trade." in *Handbook of International Economics*, Vol. 4.                           | 综合异质企业贸易模型；Pareto 分布：\\(G(\varphi) = 1 - (\varphi_{\min}/\varphi)^k\\)；CES 偏好替代弹性 \\(\sigma\\)；markup：\\(\sigma/(\sigma-1)\\)；企业收入：\\(r(\varphi) = R(P\rho \varphi)^{\sigma-1}\\)                                                       |
| 37 | **Helpman, E., Melitz, M.J. & Yeaple, S.R. (2004).** "Export versus FDI with Heterogeneous Firms." *American Economic Review*, 94(1): 300-316.        | 三种模式排序：国内\\(\prec\\) 出口 \\(\prec\\) FDI；FDI 固定成本 \\(f_I > f_X > f_D\\)；近距效应 proximity vs. 集中效应 concentration                                                                                                                                |
| 38 | **Bernard, A.B., Redding, S.J. & Schott, P.K. (2007).** "Comparative Advantage and Heterogeneous Firms." *Review of Economic Studies*, 74(1): 31-66.  | 行业比较优势 + 企业异质性；行业要素密集度\\(\alpha_j\\)；企业生产率 \\(\varphi\\) 与行业比较优势交互                                                                                                                                                                 |

### 4.2 中介与渠道选择

| #  | 文献                                                                                                                                                                | 核心变量/参数                                                                                                                                                                                                                                       |
| -- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 39 | **Ahn, J.B., Khandelwal, A.K. & Wei, S-J. (2011).** "The Role of Intermediaries in Facilitating Trade." *Journal of International Economics*, 84(1): 73-85. | 中介 intermediation；两种出口模式：直接出口 direct export vs. 间接出口 indirect export（通过中介）；中介全球固定成本\\(F_I\\)；中介边际成本加成 \\(\lambda > 1\\)；三组企业排序：间接出口商 \\(\prec\\) 直接出口商 \\(\prec\\) 不出口；市场份额分解 |
| 40 | **Bernard, A.B., Jensen, J.B., Redding, S.J. & Schott, P.K. (2010).** "Wholesalers and Retailers in US Trade." *American Economic Review*, 100(2): 408-13.  | 批发商/零售商作为贸易中介；中介在贸易中的份额                                                                                                                                                                                                       |
| 41 | **Rauch, J.E. & Watson, J. (2004).** "Network Intermediaries in International Trade." *Journal of Economics & Management Strategy*, 13(1): 69-93.           | 网络中介 network intermediaries；搜索成本 search cost；匹配效率 matching efficiency                                                                                                                                                                 |
| 42 | **Blum, B.S., Claro, S. & Horstmann, I. (2010).** "Facts and Figures on Intermediated Trade." *American Economic Review*, 100(2): 419-23.                   | 中介贸易的实证 facts；中介在贸易中的规模、范围                                                                                                                                                                                                      |

### 4.3 平台经济学

| #  | 文献                                                                                                                                                                 | 核心变量/参数                                                                                                                 |
| -- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| 43 | **Rochet, J-C. & Tirole, J. (2003).** "Platform Competition in Two-Sided Markets." *Journal of the European Economic Association*, 1(4): 990-1029.           | 双边市场 two-sided market；平台 platform；交叉网络外部性 cross-group network externalities；平台收费结构 price structure      |
| 44 | **Armstrong, M. (2006).** "Competition in Two-Sided Markets." *RAND Journal of Economics*, 37(3): 668-691.                                                   | 单归属 single-homing vs. 多归属 multi-homing；平台对买卖双方收取的费用\\(p_B, p_S\\)；交叉外部性参数 \\(\alpha_B, \alpha_S\\) |
| 45 | **Jullien, B. (2011).** "Competition in Multi-Sided Markets: Divide and Conquer." *American Economic Journal: Microeconomics*, 3(4): 186-219.                | 平台分治策略 divide-and-conquer；补贴一方以吸引另一方                                                                         |
| 46 | **Belleflamme, P. & Peitz, M. (2019).** "Platform Competition: Who Benefits from Multihoming?" *International Journal of Industrial Organization*, 64: 1-26. | 多归属对平台竞争的影响；平台佣金率 commission rate                                                                            |

---

## 第5节：均衡下的本地价值捕获

### 5.1 本地乘数与收入传播

| #  | 文献                                                                                                                                                                   | 核心变量/参数                                                                                                                          |
| -- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| 47 | **Moretti, E. (2010).** "Local Multipliers." *American Economic Review*, 100(2): 373-77.                                                                       | 地方乘数 local multiplier；贸易部门 tradable sector；非贸易部门 non-tradable sector；每增加1个贸易部门岗位带来\\(m\\) 个非贸易部门岗位 |
| 48 | **Moretti, E. & Thulin, P. (2013).** "Local Multipliers and Human Capital in the United States and Sweden." *Industrial and Corporate Change*, 22(1): 339-362. | 人力资本强度不同的贸易部门乘数差异；高技能部门乘数 > 低技能部门                                                                        |
| 49 | **van Dijk, J.J. (2018).** "Local Multipliers and the Spatial Diffusion of Economic Shocks." *Journal of Economic Geography*, 18(3): 731-758.                  | 空间扩散 spatial diffusion；地方乘数的地理衰减                                                                                         |
| 50 | **Acemoglu, D., Akcigit, U. & Kerr, W. (2016).** "Networks and the Macroeconomy: An Empirical Exploration." *NBER Macroeconomics Annual*, 30: 273-335.         | 投入产出网络 input-output network；冲击通过生产网络的传播；上游/下游传播                                                               |

### 5.2 价值捕获与空间脱钩

| #  | 文献                                                                                                                                                                                                      | 核心变量/参数                                                                                     |
| -- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| 51 | **Gereffi, G., Humphrey, J. & Sturgeon, T. (2005).** "The Governance of Global Value Chains." *Review of International Political Economy*, 12(1): 78-104.                                         | 全球价值链 GVC governance；五种治理模式；价值链中的权力不对称 power asymmetry；价值在各环节的分配 |
| 52 | **Antràs, P. & Chor, D. (2013).** "Organizing the Global Value Chain." *Econometrica*, 81(6): 2127-2204.                                                                                         | 价值链位置 position in value chain；sequential production；企业对"自制 vs. 外包"的选择            |
| 53 | **Dedrick, J., Kraemer, K.L. & Linden, G. (2010).** "Who Profits from Innovation in Global Value Chains? A Study of the iPod and Notebook PCs." *Industrial and Corporate Change*, 19(1): 81-116. | 价值捕获 value capture；在 iPod/PC 价值链中各参与方的收入分配份额                                 |
| 54 | **Bartik, T.J. (1991).** *Who Benefits from State and Local Economic Development Policies?* W.E. Upjohn Institute.                                                                                | 地方经济发展的受益者；地方乘数中工资、利润、租金的分配                                            |

### 5.3 电商/平台对地方收入的影响

| #  | 文献                                                                                                                                                                                                                                      | 核心变量/参数                                                                                                                    |
| -- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| 55 | **Agrawal, D.R. & Shybalkina, I. (2023).** "Online Shopping Can Redistribute Local Tax Revenue from Urban to Rural America." *Journal of Public Economics*, 219.                                                                  | 电商对地方销售税的空间再分配效应；目的地原则 destination basis vs. 产地原则 origin basis；城市零售中心税收下降，农村辖区税收增加 |
| 56 | **Li, Q., Xie, M. & Tang, Y. (2025).** "Do the E-commerce-induced Business Clusters Increase the Income of Local Rural Households?" *Economic Analysis and Policy*, 86: 1510-1526.                                                | 淘宝村 Taobao villages；DID 方法；结果：淘宝村平均降低本地家庭收入5.3%（商业收入增加但打工工资收入减少更多）；收入不平等加剧     |
| 57 | **Phelps, N.A., Wang, C., Miao, J. & Zhang, J. (2022).** "E-commerce: A Platform for Local Economic Development? Evidence from Taobao Villages in Zhejiang Province, China." *Transactions in Planning and Urban Research*, 1(1). | 淘宝村 vs. OVOP 模型 vs. JA 模型；电商的去中介化 disintermediation；农村就业和收入效应                                           |
| 58 | **刘雨菲 (2026).** "电商发展水平与区域税源背离." *经济学研究前沿*, 9(3).                                                                                                                                                          | 税源背离 tax-source divergence；电商通过资本错配 + 劳动力错配 + 消费模式改变三个渠道加剧税源背离；东部地区加剧、西部地区抑制     |

---

## 第6节：赋能型政府 vs. 保护型政府

### 6.1 有为政府与产业政策

| #  | 文献                                                                                                                                                                                        | 核心变量/参数                                                                                                                                                                                                                      |
| -- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 59 | **Lin, J.Y. & Monga, C. (2011).** "Growth Identification and Facilitation: The Role of the State in the Dynamics of Structural Change." *Development Policy Review*, 29(3): 264-90. | GIFF 六步骤框架：\\(Step\ 1\\) 选择参照国（人均收入高1-2倍、类似禀赋）；\\(Step\ 2\\) 消除现有产业约束；\\(Step\ 3\\) 吸引 FDI 或孵化新企业；\\(Step\ 4\\) 支持自我发现；\\(Step\ 5\\) 经济特区/产业园区；\\(Step\ 6\\) 补偿先行者 |
| 60 | **Rodrik, D. (2004).** "Industrial Policy for the Twenty-First Century." Working Paper, Harvard Kennedy School.                                                                       | 产业政策是"发现过程" discovery process；政府与企业战略协作 strategic collaboration；信息外部性；协调外部性 coordination externality                                                                                                |
| 61 | **Rodríguez-Clare, A. (2005).** "Coordination Failures, Clusters and Microeconomic Interventions." *IADB Working Paper*.                                                           | 协调失败 coordination failure；产业集群 clusters；企业对互补性投入的投资不足；政府协调的角色                                                                                                                                       |
| 62 | **Murphy, K.M., Shleifer, A. & Vishny, R.W. (1989).** "Industrialization and the Big Push." *Journal of Political Economy*, 97(5): 1003-1026.                                       | 大推进 big push；多个部门之间的需求互补 demand complementarity；协调失败导致工业化无法起步；基础设施固定成本                                                                                                                       |
| 63 | **Harrison, A. & Rodríguez-Clare, A. (2010).** "Trade, Foreign Investment, and Industrial Policy for Developing Countries." in *Handbook of Development Economics*, Vol. 5.        | 产业政策三类型：水平政策 horizontal policies、选择性政策 selective policies、功能性政策 functional policies                                                                                                                        |
| 64 | **Aghion, P., Boulanger, J. & Cohen, E. (2011).** "Rethinking Industrial Policy." *Bruegel Policy Brief*, 2011/04.                                                                  | 竞争友好型产业政策 competition-friendly industrial policy；针对部门而非单个企业                                                                                                                                                    |

### 6.2 基础设施与公共品

| #  | 文献                                                                              | 核心变量/参数                                                                                                                                |
| -- | --------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| 65 | **林毅夫 (2013).** "政府如何在市场经济环境下发挥积极有为的作用." 人民日报。 | 潜在比较优势 latent comparative advantage → 需要通过改善软硬基础设施降低交易费用 → 变为实际竞争优势；因势利导 facilitating；增长甄别六步骤 |

### 6.3 保护与赋能的分界

| #  | 文献                                                                                                                                                         | 核心变量/参数                                                                                                                                                                                        |
| -- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 66 | **Pack, H. & Saggi, K. (2006).** "The Case for Industrial Policy: A Critical Survey." *World Bank Research Observer*, 21(2): 267-297.                | 产业政策的市场失灵依据：技术外部性 technological externality、金钱外部性 pecuniary externality、信息外部性 information externality、协调失败 coordination failure；选择性干预 selective intervention |
| 67 | **Stiglitz, J.E. (1996).** "Some Lessons from the East Asian Miracle." *World Bank Research Observer*, 11(2): 151-177.                               | 东亚奇迹中政府角色：市场增进 market-enhancing vs. 市场替代 market-replacing；政府促进储蓄、投资和出口                                                                                                |
| 68 | **Wade, R. (1990).** *Governing the Market: Economic Theory and the Role of Government in East Asian Industrialization.* Princeton University Press. | "引导市场" governing the market；东亚国家产业政策工具；选择性信贷；进口保护                                                                                                                          |

---

## 第7节（可选动态扩展）：组织资本与结构转型缺口

### 7.1 组织资本

| #  | 文献                                                                                                                                                     | 核心变量/参数                                                                                                                                                                        |
| -- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 69 | **Prescott, E.C. & Visscher, M. (1980).** "Organization Capital." *Journal of Political Economy*, 88(3): 446-461.                                | 组织资本 organization capital：企业内提升生产效率的私有信息积累；三类信息：员工特征信息\\(I_1\\)、团队匹配信息 \\(I_2\\)、企业专用培训信息 \\(I_3\\)；不可交易、不出现在资产负债表中 |
| 70 | **Atkeson, A. & Kehoe, P.J. (2005).** "Modeling and Measuring Organization Capital." *Journal of Political Economy*, 113(5): 1026-1053.          | 组织资本作为生产技术的一部分；组织资本积累的测度：\\(z_t\\)；组织资本折旧率 \\(\delta_z\\)；组织资本投资 \\(i_z\\)                                                                   |
| 71 | **Teece, D.J., Pisano, G. & Shuen, A. (1997).** "Dynamic Capabilities and Strategic Management." *Strategic Management Journal*, 18(7): 509-533. | 动态能力 dynamic capabilities：整合、构建和重构内外部能力以应对快速变化环境的能力；路径依赖 path dependency                                                                          |

### 7.2 能力积累与企业升级

| #  | 文献                                                                                                                                                                                             | 核心变量/参数                                                                     |
| -- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------- |
| 72 | **Sutton, J. (2012).** *Competing in Capabilities: The Globalization Process.* Oxford University Press.                                                                                  | 企业能力 capabilities；能力积累 capability accumulation；在全球价值链中升级的条件 |
| 73 | **Aistleitner, M., Gräbner, C. & Hornykewycz, A. (2021).** "Theory and Empirics of Capability Accumulation: Implications for Macroeconomic Modeling." *Research Policy*, 50(6): 104258. | 能力积累 capability accumulation 的宏观建模整合；企业层面 vs. 国家层面的能力差异  |
| 74 | **Evenson, R.E. & Westphal, L.E. (1995).** "Technological Change and Technology Strategy." in *Handbook of Development Economics*, Vol. 3A.                                              | 技术能力 technological capability；企业技术升级的阶段性                           |

---

## 附录A：按变量类别检索快速索引

### A.1 要素禀赋类变量

| 变量名                   | 含义                    | 出处                                   |
| ------------------------ | ----------------------- | -------------------------------------- |
| \\(E_i\\)                | 地区 i 的要素禀赋向量   | Lin (2011)                             |
| \\(K_i, L_i, N_i\\)      | 资本、劳动、自然资源    | Lin (2011, 2012)                       |
| \\(\kappa_t = K_t/L_t\\) | 禀赋结构（资本-劳动比） | Ju, Lin & Wang (2015)                  |
| \\(w_i, r_i\\)           | 工资率、资本租金        | Ju, Lin & Wang (2015); Heckscher-Ohlin |
| \\(H/L\\)                | 技能禀赋                | Acemoglu & Zilibotti (2001)            |

### A.2 产业/行业类变量

| 变量名                  | 含义                            | 出处                                                      |
| ----------------------- | ------------------------------- | --------------------------------------------------------- |
| \\(\theta_j\\)          | 行业 j 的要素密集度参数         | Lin, Liu & Zhang (2023)                                   |
| \\(\alpha_j\\)          | 行业 j 的资本份额               | Ju, Lin & Wang (2015)                                     |
| \\(\phi(j)\\)           | 行业 j 的资本密集度（递增函数） | Ju, Lin & Wang (2015)                                     |
| \\(j \in [0, \infty)\\) | 连续行业，按资本密集度递增排列  | Ju, Lin & Wang (2015); Dornbusch-Fischer-Samuelson (1980) |
| \\(c_{ij}\\)            | 地区 i 行业 j 的单位成本        | 综合 NSE + Heckscher-Ohlin                                |

### A.3 企业进入与选择类变量

| 变量名                         | 含义                      | 出处                                        |
| ------------------------------ | ------------------------- | ------------------------------------------- |
| \\(\varphi, z\\)               | 企业生产率                | Melitz (2003); Ju, Lin & Wang (2015)        |
| \\(f_E\\)                      | 进入的沉没成本            | Melitz (2003)                               |
| \\(f_D\\)                      | 国内生产的固定成本        | Melitz (2003)                               |
| \\(f_X, F_{ij}^r\\)            | 出口/渠道 r 的固定成本    | Melitz (2003); Ahn, Khandelwal & Wei (2011) |
| \\(\varphi^*, z_{ij}^{r*}\\) | 进入/出口的生产率门槛     | Melitz (2003)                               |
| \\(\tau\\)                     | 冰山贸易成本/市场接入成本 | Melitz (2003)                               |
| \\(\lambda\\)                  | 中介边际成本加成          | Ahn, Khandelwal & Wei (2011)                |
| \\(G(\varphi)\\)               | 生产率分布                | Melitz (2003)                               |
| \\(k\\)                        | Pareto 分布形状参数       | Melitz & Redding (2014)                     |
| \\(\sigma\\)                   | 替代弹性                  | Melitz (2003)                               |

### A.4 平台/中介类变量

| 变量名                   | 含义                            | 出处                                           |
| ------------------------ | ------------------------------- | ---------------------------------------------- |
| \\(r \in \{A, D\}\\)     | 渠道选择：代理渠道 vs. 平台直连 | Ahn, Khandelwal & Wei (2011)                   |
| \\(F_I\\)                | 中介全球固定成本                | Ahn, Khandelwal & Wei (2011)                   |
| \\(\phi_r\\)             | 渠道 r 的可变成本/佣金率        | 综合 NSE + Ahn et al. + Rochet & Tirole (2003) |
| \\(p_B, p_S\\)           | 平台对买卖双方收费              | Armstrong (2006)                               |
| \\(\alpha_B, \alpha_S\\) | 交叉网络外部性参数              | Armstrong (2006)                               |

### A.5 政府/政策类变量

| 变量名                   | 含义                  | 出处                                                                          |
| ------------------------ | --------------------- | ----------------------------------------------------------------------------- |
| \\(G_i\\)                | 公共投入/基础设施投资 | Lin (2011, 2012); Murphy, Shleifer & Vishny (1989)                            |
| \\(q_i\\)                | 平台兼容型组织能力    | 综合 NSE + organizational capital 文献                                        |
| \\(a_{i,t}\\)            | 传统代理/渠道资本     | 新变量（需定义，可引用 Prescott & Visscher (1980) 或 Atkeson & Kehoe (2005)） |
| \\(\delta_a, \delta_q\\) | 组织资本折旧率        | Atkeson & Kehoe (2005)                                                        |
| \\(I_{i,t}\\)            | 新能力投资            | Atkeson & Kehoe (2005)                                                        |

### A.6 福利/收入类变量

| 变量名                 | 含义                    | 出处                                                                  |
| ---------------------- | ----------------------- | --------------------------------------------------------------------- |
| \\(I_i\\)              | 地区 i 第一轮本地收入   | 需新建模：\\(I_i = W_i + \Pi_i^{local} + S_i^{local} + T_i^{local}\\) |
| \\(Y_i\\)              | 地区 i 总收入（乘数后） | 需新建模                                                              |
| \\(\rho_i, \omega_i\\) | 本地留值率              | 需在 NSE 均衡中推导                                                   |
| \\(\lambda_i\\)        | 非贸易部门再循环强度    | Moretti (2010)                                                        |
| \\(\widetilde{m}_i\\)  | 有效地方乘数            | 已有（Dong & Hu, EL 短文）                                            |
| \\(m_i\\)              | 标准 Moretti 地方乘数   | Moretti (2010)                                                        |
| \\(W\\)                | 社会福利                | 需区分地方 vs. 全国                                                   |

### A.7 自生能力与比较优势类变量

| 变量名     | 含义                                     | 出处                                 |
| ---------- | ---------------------------------------- | ------------------------------------ |
| \\(V_i\\)  | 企业自生能力（二元或连续）               | Lin (2003)                           |
| latent CA  | 潜在比较优势：要素成本最低但交易成本尚高 | Lin (2011); Lin & Monga (2011)       |
| actual CA  | 实际比较优势：总成本具有市场竞争力       | Lin (2011)                           |
| congruence | 禀赋-产业一致性指数                      | 可在数值分析中构建（不替代理论核心） |

---

## 附录B：待补充文献建议（需进一步检索）

1. **Banerjee, A.V. & Duflo, E. (2005).** "Growth Theory through the Lens of Development Economics." in *Handbook of Economic Growth*. —— 对企业异质性和资源配置的综述。
2. **Hsieh, C-T. & Klenow, P.J. (2009).** "Misallocation and Manufacturing TFP in China and India." *Quarterly Journal of Economics*, 124(4): 1403-1448. —— 资源错配与生产率。
3. **Restuccia, D. & Rogerson, R. (2017).** "The Causes and Costs of Misallocation." *Journal of Economic Perspectives*, 31(3): 151-74. —— 错配综述。
4. **Goldfarb, A. & Tucker, C. (2019).** "Digital Economics." *Journal of Economic Literature*, 57(1): 3-43. —— 数字经济综述（搜索成本降低、数字平台）。
5. **Einav, L., Farronato, C. & Levin, J. (2016).** "Peer-to-Peer Markets." *Annual Review of Economics*, 8: 615-635. —— P2P 市场平台。
6. **Fan, J., Tang, L., Zhu, W. & Zou, B. (2018).** "The Alibaba Effect: Spatial Consumption Inequality and the Welfare Gains from e-Commerce." *Journal of International Economics*, 114: 203-220. —— 电商的空间消费不平等效应。
7. **Couture, V., Faber, B., Gu, Y. & Liu, L. (2021).** "Connecting the Countryside via E-Commerce: Evidence from China." *American Economic Review: Insights*, 3(1): 35-50. —— 中国农村电商的实证。
8. **Brynjolfsson, E., Hu, Y. & Rahman, M.S. (2013).** "Competing in the Age of Omnichannel Retailing." *MIT Sloan Management Review*. —— 全渠道零售竞争。
9. **Khan, M. (2015).** "The Role of Industrial Policy: Lessons from Asia." in *New Perspectives on Industrial Policy*. —— 亚洲产业政策的组织能力视角。
10. **Lee, K. (2013).** *Schumpeterian Analysis of Economic Catch-up.* Cambridge University Press. —— 熊彼特追赶分析。

---

## 使用说明

- **引用优先级**：标注为 "NSE 基准模型" 的 Ju, Lin & Wang (2015) 和 Lin (2011) 是所有 NSE 建模的第一引用来源。
- **变量名**：建议新稿的变量名与 Ju-Lin-Wang (2015) 保持一致（如 \\(K_t, L, \kappa_t, w_t, r_t\\)），以最大化文献连续性。
- **平台和中介变量**：目前 NSE 文献尚未直接定义。建议新稿引用 Ahn-Khandelwal-Wei (2011) 的中介固定成本/加成框架，作为将平台纳入 NSE 模型的桥梁。
- **留值率 \\(\rho_i\\)**：此为你的核心原创变量。建议在新稿中将 \\(\rho_i\\) 定义为均衡结果（工资+利润+服务收入+税收的加权本地份额），并引用 GVC 文献（Gereffi et al. 2005; Dedrick et al. 2010）作为概念支撑。

---

# 附录C：中文 NSE 文献补充（变量构建、指标测度、实证应用）

> **日期**：2026-07-23
> **说明**：此附录专门整理以中文发表的新结构经济学实证研究，重点提取各文献中**变量/指标的构建方法**，供你后续建模和实证设计时直接引用。

---

## C.1 要素禀赋结构测度

### C.1.1 资本-劳动比（CLR）法

| #  | 文献                                                                                                | 变量/指标构建方法                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| -- | --------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| C1 | **林毅夫、付才辉、陈曦 (2025).** 《中国经济的转型升级：新结构经济学方法与应用》               | **要素禀赋比较优势 FCA**：① 用美国制造业数据库计算行业 j 在自由市场状态下的资本劳动比 CLR_j（避免中国数据内生性）；② FCA_jc = CLR_j / Y_c，其中 Y_c 为地区 c 人均产出（人均资本代理变量）；③ 回归方程中同时加入 FCA 一次项和二次项确定数值关系。**技术比较优势 TCA**：TCA_jc = TSI_j / TSI_c，TSI_j 为行业技术复杂度指数（Hausmann et al. 2007 方法），TSI_c 为地区现有技术基础（TSI_j 加权平均）。**生产率比较优势 PCA**：行业劳动生产率与地区全员劳动生产率的比值 |
| C2 | **魏博通、艾清锋 (2022).** "中国省区要素禀赋与制造业发展的协调度评估及对策." 《深圳社会科学》 | **要素禀赋三级指标体系**：人力资源（年末就业人员、劳动年龄人口及占比、人口平均受教育年限）、自然资源（采掘业从业人员占比、采掘业产品销售收入占比）、资本要素（固定资产形成总额、金融业增加值）；用熵权法构建加权综合指数，再用协调度模型测度要素禀赋与制造业发展的匹配度                                                                                                                                                                                                           |
| C3 | **黄允爵、叶德珠 (2023).** "要素禀赋和产业结构的匹配与经济增长." 《中国经济学》               | **要素禀赋-产业结构匹配度指标**：以资本劳动比（K/L）代表要素禀赋结构，产业结构的资本密集度代表产业结构，计算两者的差距（distance）。发现差距与经济增长呈倒 U 型，差距为 0 时为最优匹配点                                                                                                                                                                                                                                                                                           |
| C4 | **王勇、蒋扬天、岳威铮 (2025).** "禀赋结构、适宜技术与结构转型." 《经济研究》                 | **三维要素禀赋**：物质资本 K、高技能劳动力 H、低技能劳动力 L；用投入产出表和微观数据校准；三种效应：投资效应、收入效应、要素相对价格效应对结构转型的定量贡献                                                                                                                                                                                                                                                                                                                       |
| C5 | **Fu, C. (2018).** "最优生产函数理论——从新古典经济学向新结构经济学的范式转换." 《经济评论》 | **禀赋结构的供给与需求原理**：最优生产方式由禀赋结构的相对价格内生决定；以 CD 生产函数为例推导"最优生产函数"                                                                                                                                                                                                                                                                                                                                                                       |

### C.1.2 要素禀赋指数合成法

| C6 | **2003-2018年中国劳动力、资本与森林要素禀赋指数矢量空间数据集** | **县域级要素禀赋指数**：劳动力指数（常住人口、劳动年龄人口、受教育年限、就业结构加权）、资本指数（固定资产投资、金融机构存贷款余额、规上企业资产总额、夜间灯光强度）、森林要素指数（森林覆盖率、林地面积、蓄积量等）；Z-score / 熵值法 / 主成分分析合成 |

---

## C.2 比较优势测度

### C.2.1 比较优势偏离度

| #   | 文献                                                                                                                 | 变量/指标构建方法                                                                                                                                                                                                                        |
| --- | -------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| C7  | **陈斌开、林毅夫 (2013).**                                                                                     | **技术选择指数 TCI**：\\(TCI = \\)（工业部门资本存量 / 工业部门从业人数）/（全国资本存量 / 全国劳动力），反映实际技术选择与禀赋结构的偏离。此指标的构建方式被后续大量中文实证采用                                                  |
| C8  | **吴清扬、姜磊 (2021).** "工业企业自生能力与存活时间：基于新结构经济学视角." 《经济评论》                      | **比较优势偏离度 DS**：\\(DS = tci / tci^* = tci / w\\)，其中 \\(tci\\) 为实际技术选择指数，\\(tci^*\\) 为最优技术选择（不可观测，设为与工资相关）。数据来源：1998-2013 中国工业企业数据库。生存分析表明 DS 越大，企业存活时间越短 |
| C9  | **罗浩、陈仁.** "比较优势、技术选择与自生能力——中国酒店业'高增长低效益'之谜的新结构经济学解释." 《旅游学刊》 | **比较优势偏离度 DC**：构造新指标反映"技术选择是否遵循比较优势"。基础模型中 DC 对产业利润率有显著负向影响，DC 提高一倍则利润率下降约 4.45%-4.49%。以星级饭店平均利润率作为自生能力的代理变量                                       |
| C10 | **郑洁、付才辉、赵秋运 (2019).** "发展战略与环境治理." 《财经研究》                                            | **发展战略偏离比较优势程度**：以国有企业的比重或重工业化程度来衡量一个地区的发展战略是否违背比较优势。工具变量：到威胁区的最近距离、老工业基地数量。机制：违背比较优势 → 企业缺乏自生能力 → 弱化环境约束 + 政府财政赤字恶化      |

### C2.2 显示性比较优势的 NSE 应用

| C11 | **李乾宏 (2022).** "新结构经济学五类产业分类的 RCA 实证分析." ICEMME 2022 | **RCA + NSE 五分类**：用 RCA 指数 > 1 识别比较优势产业，结合全球产业数据（1995-2018），按新结构经济学五类产业（追赶型、领先型、转进型、弯道超车型、战略型）进行跨国比较 |

---

## C.3 产业升级与结构转型测度

### C3.1 产业升级指标

| #   | 文献                                                                                                            | 变量/指标构建方法                                                                                                                                                                    |
| --- | --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| C12 | **干春晖、郑若谷、余典范 (2011).** "中国产业结构变迁对经济增长和波动的影响." 《经济研究》                 | **产业结构合理化**（泰尔指数）和**产业结构高级化**（第三产业/第二产业）双维指标。这是中文实证中最广泛引用的产业结构测度基准                                              |
| C13 | **刘新智、沈方 (2021).** "人力资本积累与产业结构升级的耦合协调研究——以长江经济带为例." 《西南大学学报》 | **产业结构升级三维测度体系**：合理化（泰尔指数、二元对比系数）、高级化（服务业超前系数、技术密集型集约化程度、外贸依存度）、高效化（第二产业投入产出比、第三产业投入产出比）   |
| C14 | **王勇、樊仲琛、李欣泽 (2022).** "禀赋结构、研发创新与产业升级." 《中国工业经济》                         | **相对资本密集度**：产业资本密集度 / 地区制造业整体资本劳动比（禀赋结构）。发现此比值与发明专利申请数份额呈倒 U 型曲线。**发明专利申请数份额**作为产业创新能力的核心指标 |
| C15 | **王勇、陈诗一、朱欢 (2022).** "新结构经济学视角下产业结构的绿色转型：事实、逻辑与展望." 《经济评论》     | **资本密集度 × 污染排放强度 四类产业分类**：劳动密集型且清洁型、劳动密集型且污染密集型、资本密集型且清洁型、资本密集型且污染密集型。用区域-行业-年份数据和企业数据交叉分析    |

### C3.2 产业甄别方法

| C16 | **林毅夫、付才辉团队 (2017).** 《吉林省经济结构转型升级研究报告》（"吉林报告"） | **GIFF（增长甄别与因势利导框架）的地方应用**：基于禀赋结构（劳动力成本比江浙低 30%-50%）甄别潜在比较优势产业（大农业、大健康、现代轻纺、现代装备、新能源新材料 ICT 五大产业集群）。"扬长补短"——长板是已有产业，短板是有潜在比较优势但尚未发展起来的产业 |
| C17 | **李达、张绍文 (2022).** "乡镇'有为政府'产业政策的逻辑与检验." 《热带地理》 | **乡镇层面 GIFF 应用**：自然资源禀赋（土地、气候、海拔）为第一性约束；政策工具少、操作空间小——必须"少花钱多办事"。以云南勐罕镇为例演示甄别流程 |

---

## C.4 有为政府 / 产业政策测度

### C4.1 基础设施与政府干预

| #   | 文献                                                                                                  | 变量/指标构建方法                                                                                                                                                                                                              |
| --- | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| C18 | **林毅夫、文永恒、顾艳伟 (2020).** "国有企业、基础设施与经济增长." 新结构经济学工作论文         | **基础设施投资的正外部性**：上游自然垄断行业中的国有企业投资 → 正外部性 → 带动下游私营经济。实证：国有企业投资增加 → 非国有企业投资和居民消费上升、杠杆率下降                                                         |
| C19 | **张博 (2024).** "技术选择、基础设施与要素约束：林均衡及其政策含义." 新结构经济学工作论文       | **林均衡 (Lin Equilibrium)**：基础设施正外部性 + 技术选择 + 要素禀赋约束的统一一般均衡。由于基础设施的公共品属性 → 市场失灵 → 三种政府矫正机制：庇古-林均衡、科斯-林均衡、瓦尔拉斯-林均衡                              |
| C20 | **Lin, J.Y. & Wang, X. (2023).** "State Enabling and Comparative Advantages." NSE Working Paper | **LCA → ACA 转换条件**：潜在比较优势 (LCA) 转化为实际比较优势 (ACA) 需要国家降低交易成本。物理和制度基础设施投资是转换的充分条件。跨国实证：非洲和拉美 LCA-ACA 差距大，亚洲差距小；出口结构动态变化与基础设施发展正相关 |
| C21 | **林毅夫、王勇、于海潮、张梓桐.** "新结构产业经济学的学科内涵与分析框架."                       | **匹配度指数**：产业 i 与地区禀赋结构的偏离程度指数；随时间增大的为转进型产业，随时间减小的为符合比较优势的产业。**有效市场 × 有为政府结合**的产业政策分析框架                                                    |
| C22 | **林毅夫、向为、余淼杰 (2018).** "区域产业政策与企业生产率." NSE 工作论文                       | **国家级经济开发区**：提供更好的政策环境（更低税收）、正向溢出效应，但园区内集聚效应不显著。征收税率差异（园区内 15% vs. 园区外 33%）                                                                                    |

### C4.2 电商 / 数字平台 + 有为政府

| C23 | **北京大学新结构经济学研究院 (2025).** "新结构经济学视角下的平台经济：一个分析框架." NSE 工作论文 | **平台经济 NSE 框架**：将平台纳入基础设施和制度安排层面分析——平台作为降低交易成本的手段，属于软基础设施范畴；平台对比较优势实现的影响 |
| C24 | **黄雅姿、颜廷武、魏梦升、姜维军 (2026).** "农村电商何以助推县域产业结构升级." 《经济评论》 | **电商示范县政策（DID）**：2010-2022 年 1821 个县数据。**三重作用机制**：拉动居民消费、促进非农产业集聚、加快要素流动速度。**政府规模调节效应**：呈倒 U 型——过大或过小均不利于政策效果。劳务输入大省和基础设施较好地区效果更突出 |
| C25 | **李力行、申广军 (2015).** "经济开发区、地区比较优势与产业结构调整." 《经济学（季刊）》 | **三类比较优势指标**：要素禀赋比较优势（CLR）、技术比较优势、生产率比较优势。发现：要素禀赋比较优势仅在资本流动性较弱地区起作用；技术和生产率比较优势作用范围更广。**开发区-比较优势匹配**对产业结构调整有显著促进效应 |

---

## C.5 自生能力测度

| #   | 文献                                                                                   | 变量/指标构建方法                                                                                                                                  |
| --- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| C26 | **林毅夫 (2002).** "发展战略、自生能力和经济收敛." 《经济学（季刊）》            | **自生能力概念**：企业所在的产业和技术选择与要素禀赋结构决定的比较优势一致，则在开放竞争市场中不需保护补贴即能获得正常利润                   |
| C27 | **林毅夫 (2002).** "自生能力、经济转型与新古典经济学的反思." 《经济研究》        | **自生能力作为微观分析基础**：缺乏自生能力 → 需要政策性负担和补贴 → 软预算约束 → 资源配置效率低下                                         |
| C28 | **姚治国、朱聪浩、杨金朋 (2023).** "上市企业全要素生产率对其自生能力的影响机制." | **自生能力代理变量**：企业财务指标（利润率等）。TFP → 降低生产成本、缓解融资约束 → 提高自生能力。异质性：国企 TFP 对自生能力效果 < 民企    |
| C29 | **郑洁、付才辉、赵秋运 (2019).**                                                 | **自生能力代理变量**：用**国有及国有控股企业比重**作为企业缺乏自生能力的间接衡量（违背比较优势的发展战略 → 国企比例高 → 自生能力弱） |

---

## C.6 新结构经济学专著（可作为变量定义的总纲性引用）

| #   | 文献                                                                                                | 用途                                                                                                                                                                              |
| --- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| C30 | **林毅夫、付才辉 (2019/2022).** 《新结构经济学（上册/下册）》高等教育出版社                   | NSE 标准教科书，所有核心概念（要素禀赋结构、比较优势、自生能力、有效市场、有为政府、五类产业）的系统定义。下册第 15 章为"新结构空间经济学导论"——直接适用于你的县域/区际分析框架 |
| C31 | **林毅夫 (2017).** "新结构经济学的理论基础和发展方向." 北京大学                               | NSE 理论总纲：要素禀赋结构 → 比较优势 → 最优产业结构 → 硬/软基础设施 → 制度结构，完整的四层内生结构框架                                                                       |
| C32 | **付才辉 (2018).** "最优生产函数理论——从新古典经济学向新结构经济学的范式转换." 《经济评论》 | 禀赋结构的供给函数、需求函数、相对价格原理、最优生产方式（比较优势）原理。这是**NSE 生产理论的数学模型奠基**                                                                |
| C33 | **王勇 (2025).** "产业升级中的有效市场与有为政府——新结构经济学视角."                        | 有为政府 vs. 乱为 vs. 不作为的边界界定："有为 = 排除乱为与不作为后的合理履职"；其边界根据场景（发展阶段、禀赋结构、产业特征）而定                                                 |

---

## C.7 变量/指标构建速查详表（精校版，可直接引用）

> **说明**：每行提供从概念到具体公式、数据来源、构建步骤、单位及解释的完整路径。
> 标记 [★] 表示该指标是中文实证中最常用的基准方法，建议优先采用。

---

### 索引 A：产业结构测度（第3节最常用）

| #  | 你要测度的概念           | [★] 推荐指标       | 精确公式                                                                                                                                                             | 数据来源                                                    | 构建步骤                                                                        | 单位/取值范围                                                         | 解释                                                                                                            | 引用出处                                           |
| -- | ------------------------ | ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | ------------------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| A1 | 产业结构合理化           | ★ TL（泰尔指数）   | \\(TL = \sum_{i=1}^{n} \frac{Y_i}{Y} \ln\left(\frac{Y_i/Y}{L_i/L}\right)\\)，其中 \\(Y_i\\) 为第 i 产业增加值，\\(L_i\\) 为第 i 产业就业人数，n 通常取 3（三次产业） | 中国统计年鉴/各省统计年鉴：三次产业增加值、三次产业就业人数 | ① 计算各产业\\(Y_i/Y\\)（产值份额）和 \\(L_i/L\\)（就业份额）；② 代入公式求和 | TL ≥ 0，TL=0 时为完全均衡（Y_i/L_i = Y/L 对所有 i）；TL 越大越不合理 | 衡量要素投入结构与产出结构的耦合程度。古典假设：经济均衡时各产业生产率相等（Y_i/L_i = Y/L），加权对数差即偏离度 | 干春晖、郑若谷、余典范 (2011)，《经济研究》——C12 |
| A2 | 产业结构合理化（逆指标） | RAT（修正泰尔倒数） | \\(RAT = 1 / TL\\)，TL 同上                                                                                                                                          | 同上                                                        | 同上，再取倒数                                                                  | RAT 越大越合理                                                        | 便于回归系数解读（正指标）                                                                                      | 何好俊、彭冲 (2017)；于斌斌                        |
| A3 | 产业结构高级化           | ★ TS               | \\(TS = \text{第三产业增加值} / \text{第二产业增加值}\\)                                                                                                             | 中国统计年鉴：各省三次产业增加值                            | 直接计算比值                                                                    | TS > 0，TS 越大越高级                                                 | 反映"工业型"向"服务型"转型程度；TS > 1 说明服务业体量超过工业                                                   | 干春晖等 (2011)——C12                             |
| A4 | 产业结构高级化（替代）   | 整体升级指数        | \\(\text{Upgrade} = 1 \times s_1 + 2 \times s_2 + 3 \times s_3\\)，其中 \\(s_i\\) 为第 i 产业比重                                                                    | 中国统计年鉴                                                | 加权求和                                                                        | 取值范围 [1, 3]                                                       | 对三次产业赋予递增权重，综合反映升级水平                                                                        | 刘翠花 (2022)                                      |
| A5 | 产业升级多维度           | 三维合成指标        | 合理化（TL 逆指标）+ 高级化（TS）+ 高效化（第二/三产业投入产出比），用熵值法或主成分分析合成                                                                         | 各省统计年鉴 + 投入产出表                                   | ① 分别计算三个维度；② 标准化；③ 加权合成                                     | 标准化后横截面可比                                                    | 更全面地捕捉产业升级                                                                                            | 刘新智、沈方 (2021)——C13                         |

---

### 索引 B：比较优势与要素禀赋结构测度（第2-3节核心）

| #  | 你要测度的概念             | [★] 推荐指标          | 精确公式                                                                                                                                                                                                                                    | 数据来源                                                                              | 构建步骤                                                                                                   | 单位/取值范围                                                          | 解释                                                                                                                       | 引用出处                                                  |
| -- | -------------------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| B1 | 要素禀赋比较优势           | ★ FCA                 | ① 用美国 NBER-CES 制造业数据库计算行业 j 的资本劳动比：\\(CLR_j = K_j / L_j\\)（固定资产总额/从业人数）；② 地区 c 人均产出作为人均资本代理变量：\\(Y_c = GDP_c / L_c\\)；③ \\(FCA_{jc} = CLR_j / Y_c\\)；④ 回归中同时加入一次项和二次项 | 美国：NBER-CES Manufacturing Industry Database；中国：各省统计年鉴 GDP 和就业         | ① 用美方数据算 CLR_j（避免内生性）；② 匹配至中国行业；③ 计算比值；④ 回归确定最优距离                   | FCA ∈ (0, +∞)，越接近 1 比较优势越强                                 | 衡量地区收入水平与行业所需资本劳动比的匹配度。FCA 远小于 1 表示行业太资本密集（违背比较优势），远大于 1 表示行业太劳动密集 | 林毅夫、付才辉、陈曦 (2025)——C1；Song et al. (2011)     |
| B2 | 技术比较优势               | ★ TCA                 | \\(TSI_j = \sum_i \frac{x_{ji}/X_i}{\sum_i x_{ji}/X_i} Y_i\\)（Hausmann et al. 2007）；\\(TSI_c = \sum_j \frac{ov_{jc}}{OV_c} TSI_j\\)；\\(TCA_{jc} = TSI_j / TSI_c\\)                                                                      | UN Comtrade（出口数据）；世界银行 WDI（人均 GDP）；中国工业企业数据库（地区产出份额） | ① 跨国数据计算每个 HS 码产品的 TSI_j；② 汇总到中国行业层面；③ 用地区产出份额加权平均得 TSI_c；④ 取比值 | TCA ∈ (0, +∞)，越接近 1 技术比较优势越强                             | TSI_j 是出口该产品的各国人均 GDP 加权平均，产品复杂度越高 TSI 越大                                                         | 林毅夫等 (2025)——C1；Hausmann, Hwang & Rodrik (2007)    |
| B3 | 生产率比较优势             | PCA                    | \\(PCA_{jc} = LP_j / LP_c\\)，其中 \\(LP_j\\) 为行业 j 全国层面劳动生产率（增加值/从业人数），\\(LP_c\\) 为地区 c 全员劳动生产率                                                                                                            | 中国统计年鉴/工业企业数据库                                                           | 直接计算比值                                                                                               | PCA ∈ (0, +∞)                                                        | 衡量行业发展阶段与地区发展阶段的匹配                                                                                       | 林毅夫等 (2025)——C1                                     |
| B4 | 发展战略偏离比较优势       | ★ TCI（技术选择指数） | \\(TCI_{it} = \frac{AVM_{it} / LM_{it}}{GDP_{it} / L_{it}}\\)，其中 \\(AVM_{it}\\) 为 i 省 t 年工业增加值，\\(LM_{it}\\) 为工业从业人数，\\(GDP_{it}, L_{it}\\) 为全省 GDP 和全部从业人数                                                   | 中国统计年鉴/各省统计年鉴：工业增加值、工业从业人数、全省 GDP、全省就业               | ① 计算工业部门劳动生产率（AVM/LM）；② 计算全省平均劳动生产率（GDP/L）；③ 取比值                         | TCI > 0；TCI 越大 = 发展战略越违背比较优势（过度发展资本密集型重工业） | 分子反映实际工业技术选择，分母反映整体禀赋结构（人均产出=比较优势基准）。TCI 越大说明工业部门资本密集度偏离整体禀赋        | 陈斌开、林毅夫 (2013)，《中国社会科学》——C7；Lin (2003) |
| B5 | 比较优势偏离度（企业层面） | DS                     | \\(DS_i = TCI_i / TCI_i^* = TCI_i / w_i\\)，其中 \\(TCI_i\\) 为企业实际技术选择指数（企业固定资产/从业人数 ÷ 全国平均），\\(TCI_i^*\\) 不可观测，用工资 w 作为代理                                                                         | 中国工业企业数据库（1998-2013）：企业固定资产、从业人数、应付工资                     | ① 用企业层面数据算 TCI_i；② 最优 TCI 不可观测，用企业工资与全国平均的比值代理                            | DS > 0；DS=1 时技术选择与禀赋结构完全匹配                              | DS > 1 → 技术选择了比禀赋结构更资本密集型的方向；DS < 1 → 劳动密集型方向                                                 | 吴清扬、姜磊 (2021)，《经济评论》——C8                   |
| B6 | 要素禀赋-产业结构匹配度    | Dist                   | \\(Dist =                                                                                                                                                                                                                                   | K/L_{\text{endowment}} - K/L_{\text{industry}}                                        | \\)，或取其平方纳入回归                                                                                    | 各省统计年鉴（资本存量估算用永续盘存法 + 固定资产投资）                | ① 用永续盘存法估算各省资本存量 K；② 算 K/L；③ 用行业资本密集度（行业固定资产/从业人数）作为产业 K/L；④ 取差值          | Dist ≥ 0；Dist=0 为最优匹配点                            |

---

### 索引 C：企业自生能力与产业活力测度（第4节）

| #  | 你要测度的概念            | [★] 推荐指标             | 精确公式                                                                                                 | 数据来源                           | 构建步骤                                                            | 单位/取值范围 | 解释                                                                                            | 引用出处                                             |
| -- | ------------------------- | ------------------------- | -------------------------------------------------------------------------------------------------------- | ---------------------------------- | ------------------------------------------------------------------- | ------------- | ----------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| C1 | 自生能力（企业层面-正向） | 存活时间                  | 企业首次出现在数据库中到最后一次出现的年数                                                               | 中国工业企业数据库 1998-2013       | ① 匹配企业 ID 识别进入/退出年份；② 存活时间 = 退出年 - 进入年 + 1 | 年（正整数）  | 缺乏自生能力的企业存活时间更短；中位数约 4 年，仅 25.49% 存活超 10 年                           | 吴清扬、姜磊 (2021)——C8                            |
| C2 | 自生能力（企业层面-正向） | 利润率                    | \\(ROA = \text{净利润} / \text{总资产}\\) 或 \\(ROS = \text{净利润} / \text{营业收入}\\)                 | 中国工业企业数据库或上市公司数据库 | 直接计算比值                                                        | %             | 利润率越高自生能力越强                                                                          | 姚治国等 (2023)——C28；罗浩等——C9                 |
| C3 | 自生能力（地区层面-反向） | ★ 国有及国有控股企业比重 | \\(\text{SOE_share} = \text{国有及国有控股工业企业总产值（或资产）} / \text{全部工业总产值（或资产）}\\) | 中国统计年鉴/各省统计年鉴          | 直接计算比重                                                        | [0, 1]        | SOE 比重越高 = 历史上违背比较优势的赶超战略越严重 = 自生能力越弱                                | 郑洁、付才辉、赵秋运 (2019)，《财经研究》——C10     |
| C4 | 自生能力（地区层面-反向） | 重工业化程度              | 重工业产值（或资产）/ 工业总产值（或资产）                                                               | 各省统计年鉴                       | 直接计算比重                                                        | [0, 1]        | 同上，产业结构越重，说明越偏离劳动力充裕型比较优势                                              | 郑洁等 (2019)——C10                                 |
| C5 | 发展战略偏离工具变量      | IV: 到威胁区的最近距离    | 用 GIS 计算各省省会到冷战/边境威胁区（如苏联边境）的最短球面距离                                         | 地理信息系统 GIS                   | GIS 空间计算                                                        | 公里          | 外生性来源：冷战时期的国防威胁 → 重工业优先布局 → 偏离比较优势，但不直接影响当前环境/经济表现 | 郑洁等 (2019)——C10                                 |
| C6 | 战略偏离工具变量          | IV: 老工业基地数量        | 国务院认定的老工业基地城市数量                                                                           | 国家发改委/国务院文件              | 直接计数                                                            | 整数          | 同上逻辑                                                                                        | 郑洁等 (2019)——C10                                 |
| C7 | 产业相对资本密集度        | RelCap                    | \\(\text{RelCap}_{jc} = \frac{K_j/L_j}{K_c/L_c}\\)（行业 j 资本密集度 / 地区 c 资本劳动比）              | 中国工业企业数据库 + 各省统计年鉴  | 行业 K/L: 行业总固定资产/从业人数；地区 K/L: 资本存量/全部就业      | RelCap > 0    | 与发明专利申请数份额呈倒 U 型——偏离越大创新越少                                               | 王勇、樊仲琛、李欣泽 (2022)，《中国工业经济》——C14 |

---

### 索引 D：有为政府/产业政策/基础设施测度（第6节）

| #  | 你要测度的概念      | [★] 推荐指标        | 精确公式                                                                                                                                                             | 数据来源                                                        | 构建步骤                                                                                          | 单位/取值范围    | 解释                                                                             | 引用出处                                         |
| -- | ------------------- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ---------------- | -------------------------------------------------------------------------------- | ------------------------------------------------ |
| D1 | 开发区政策效果      | 开发区内/外 TFP 差异 | 用 OP 或 LP 方法估计企业 TFP，再比较开发区内外均值差异；DID 设定：\\(\text{TFP}_{it} = \beta_0 + \beta_1 \text{SEZ}_{it} + \gamma X + \varepsilon\\)               | 中国工业企业数据库 + 国家级开发区地理边界 shapefile             | ① OP/LP 法估计 TFP；② 用企业经纬度判断是否在开发区边界内；③ 控制选址内生性（Heckman 两步/PSM） | TFP 对数差       | 开发区内企业 TFP 显著更高（主要通过更低税率渠道而非集聚效应）；有正向溢出效应    | 林毅夫、向为、余淼杰 (2018)——C22               |
| D2 | 开发区-比较优势匹配 | ★ Match             | 交互项：开发区虚拟变量 × 比较优势指标（FCA/TCA/PCA 偏离度倒数）                                                                                                     | 企业数据 + 开发区名单 + 行业比较优势测度                        | ① 识别开发区目标行业；② 计算目标行业与当地比较优势的匹配度；③ 交互项纳入回归                   | —               | 目标行业符合当地比较优势时，开发区效应显著更强                                   | 李力行、申广军 (2015)，《经济学（季刊）》——C25 |
| D3 | 基础设施投资效应    | 基础设施外部性弹性   | 回归：\\(\text{Private_Invest}_{t} = \alpha + \beta \times \text{SOE_Infra_Invest}_{t} + \gamma X + \varepsilon\\)                                                 | 国家统计局宏观经济季度数据（2004-2015）                         | 时间序列回归：上游国企基础设施投资 → 下游私企投资和居民消费                                      | β 系数          | β > 0，国企基础设施投资显著带动私企投资和居民消费                               | 林毅夫、文永恒、顾艳伟 (2020)——C18             |
| D4 | 政府规模调节效应    | GovSize              | 地方一般公共预算支出 / 地区 GDP                                                                                                                                      | 各省统计年鉴                                                    | 直接计算比值                                                                                      | [0, 1]           | 在电商示范县政策效果中呈倒 U 型调节——过大或过小的政府规模都不利                | 黄雅姿等 (2026)——C24                           |
| D5 | 电商/平台政策效果   | DID: 电商示范县      | 识别策略：分批次电商示范县作为 treatment，未入选县为 control；\\(Y_{it} = \beta_0 + \beta_1 \text{Ecommerce}_{it} + \gamma X + \delta_i + \lambda_t + \varepsilon\\) | 商务部电商示范县名单（2014-2021，8批共 1672 县） + 县域统计年鉴 | ① 收集各批次入选时间和县名单；② 构造 staggered DID；③ Bacon 分解处理处理效应异质性             | β_1 系数（ATT） | 三项机制：拉动居民消费、促进非农产业集聚、加快要素流动                           | 黄雅姿、颜廷武等 (2026)——C24                   |
| D6 | 行政审批改革        | 政务服务中心设立     | 各地级市设立行政服务中心的时间作为 quasi-experiment                                                                                                                  | 政府文件/新闻报道（手工收集）                                   | 构造 DID：设立前后对比                                                                            | 0/1 虚拟变量     | 行政审批改革降低制度性交易成本，使资本密集型产业比重下降、产业选择更符合比较优势 | 郭小年、邵宜航 (2021)，《财经研究》              |

---

### 索引 E：空间/区域层面专用指标

| #  | 你要测度的概念            | [★] 推荐指标  | 精确公式                                                                                                                                                                                             | 数据来源                                                   | 构建步骤                                                           | 单位/取值范围               | 解释                                                          | 引用出处                                     |
| -- | ------------------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------ | --------------------------- | ------------------------------------------------------------- | -------------------------------------------- |
| E1 | 区域要素禀赋综合指数      | 熵权法合成指数 | 维度：人力资源（就业人员、劳动年龄人口及占比、受教育年限）、自然资源（采掘业从业人员/销售收入占比）、资本要素（固定资产形成总额、金融业增加值）→ 熵权法赋权合成                                     | 各省统计年鉴                                               | ① 选取指标；② 极差标准化消除量纲；③ 熵权法确定权重；④ 加权求和 | 标准化后 [0, 1]             | 综合反映省级要素禀赋丰裕度                                    | 魏博通、艾清锋 (2022)——C2                  |
| E2 | 要素禀赋-产业协调度       | 耦合协调度     | ① 先构建要素禀赋和制造业发展两套指标体系；② 各自熵权法合成综合指数；③\\(C = 2\sqrt{U_1 U_2}/(U_1+U_2)\\)（耦合度）；④ \\(D = \sqrt{C \times T}, T = \alpha U_1 + \beta U_2\\)（协调度）          | 同上                                                       | ① 分别算两个综合指数\\(U_1, U_2\\)；② 算耦合度 C；③ 算协调度 D  | D ∈ [0, 1]                 | D < 0.4 失调；0.4-0.6 勉强协调；> 0.6 协调                    | 魏博通、艾清锋 (2022)——C2                  |
| E3 | 县域要素禀赋指数          | 三要素合成     | 劳动力指数（常住人口、劳动年龄人口、受教育年限、就业结构加权）+ 资本指数（固定资产投资、金融机构存贷款余额、规上企业资产总额、夜间灯光强度）+ 森林/生态要素指数 → Z-score / 熵值法 / 主成分分析合成 | 中国县域统计年鉴、夜间灯光数据（DMSP/VIIRS）、土地利用数据 | ① 选取指标；② 标准化（Z-score 或 min-max）；③ 赋权合成          | 标准化后横截面可比          | 县级尺度 SHP 格式数据，可做空间自相关分析（Moran's I）        | 全国三项要素禀赋指数数据集 (2003-2018)——C6 |
| E4 | 出口 RCA 与比较优势一致性 | LCA-ACA gap    | ① 按要素禀赋预测某国在某产品上的潜在比较优势 LCA（基于要素密集度匹配）；② 计算实际 RCA（Balassa 1965）：\\(RCA_{cp} = \frac{M_{cp}/\sum_p M_{cp}}{\sum_c M_{cp}/\sum_{c,p} M_{cp}}\\)；③ gap =    | LCA_index - ACA_index                                      |                                                                    | UN Comtrade；要素密集度数据 | ① 预测 LCA 排名；② 计算实际 RCA 排名；③ 取排名差或相关系数 | gap ≥ 0                                     |

---

### 索引 F：GIFF 产业五类分法速查

| #  | 分类名称                        | 定义                                                           | 识别方法                                                    | 政策含义                                             | 出处                                    |
| -- | ------------------------------- | -------------------------------------------------------------- | ----------------------------------------------------------- | ---------------------------------------------------- | --------------------------------------- |
| F1 | 追赶型 (Catching-up)            | 产业的生产技术和产品附加值低于国际前沿，但要素成本具有比较优势 | 该产业 RCA < 1，但本国要素价格与国际对比具有成本优势        | 引进技术、吸引 FDI、跨境并购、建设产业园             | 林毅夫 (2011, 2012)；Lin & Monga (2011) |
| F2 | 领先型 (Leading)                | 产业已处于或接近国际技术前沿，具有 RCA                         | RCA > 1 且技术处于前沿                                      | 加强基础研究、鼓励自主创新、维持优势                 | 同上                                    |
| F3 | 转进型 (Transformation)         | 曾经具有比较优势，但因禀赋结构升级（工资上升）正在失去优势     | RCA 从 > 1 下降至 < 1，比较优势匹配度指数（RelCap）持续上升 | 向微笑曲线两端升级（品牌、研发、渠道），或将生产外迁 | 同上；林毅夫、王勇等                    |
| F4 | 弯道超车型 (Bending/Overtaking) | 新兴产业，技术路线尚未锁定，研发周期短、人力资本需求高         | 属于新技术领域，全球各国位置未定，本国具有人力资本数量优势  | 加大应用研究投入、抢占技术标准、吸引全球人才         | 同上                                    |
| F5 | 战略型 (Strategic)              | 关乎国家安全/国际地位，通常资本密集度极高                      | 国防、航天、新能源、芯片等国家安全相关领域                  | 国家战略性投入基础研究、政府采购、产学研联合         | 同上                                    |

---

### 快速选指标决策树

```
你要测度什么？
│
├─ 地区层面的产业结构
│   ├─ 合理/均衡程度 → A1: 泰尔指数 TL (干春晖2011)
│   └─ 高级化程度 → A3: TS = 第三产业/第二产业
│
├─ 地区/行业的比较优势
│   ├─ 要素禀赋匹配 → B1: FCA = CLR_j(美)/Y_c (林毅夫等2025)
│   ├─ 技术匹配 → B2: TCA = TSI_j / TSI_c
│   ├─ 发展战略偏离（省级面板最常用） → B4: ★ TCI (陈斌开、林毅夫2013)
│   └─ 企业层面偏离 → B5: DS (吴清扬、姜磊2021)
│
├─ 企业的自生能力
│   ├─ 直接正向 → C1: 存活时间 (工企数据库)
│   ├─ 简便代理 → C3: ★ 国企比重 (省级)
│   └─ 创新视角 → C7: 相对资本密集度 vs 发明专利 (王勇等2022)
│
├─ 有为政府/产业政策
│   ├─ 开发区 → D2: ★ 开发区×比较优势交互 (李力行、申广军2015)
│   ├─ 电商平台 → D5: 电商示范县 DID (黄雅姿等2026)
│   ├─ 基础设施 → D3: 国企基础设施投资 spillover (林毅夫等2020)
│   └─ 行政审批 → D6: 政务服务中心 DID (郭小年、邵宜航2021)
│
└─ 综合/空间分析
    ├─ 要素禀赋综合 → E1: 熵权法合成指数 (魏博通2022)
    ├─ 县域尺度 → E3: 劳动力+资本+森林三指数
    └─ 跨国比较优势测度 → E4: LCA-ACA gap (Lin & Wang 2023)
```
