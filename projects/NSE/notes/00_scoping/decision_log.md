# Decision Log

状态定义：

- `CONFIRMED`：当前项目的冻结决定；
- `PROVISIONAL`：尚待模型推导或作者选择；
- `SUPERSEDED`：保留历史记录，但不得作为当前项目依据。

| 日期 | 决策 | 状态 | 理由 |
|---|---|---|---|
| 2026-07-23 | NSE 与 EL 使用独立主稿、BibTeX、代码、输出和临时目录 | CONFIRMED | 防止两篇论文的模型与证据混淆 |
| 2026-07-23 | 当前稿件定位为完整理论论文 + numerical illustrations | CONFIRMED | 没有原创数据时，以可证明命题和诚实的示意数值练习保证完整性 |
| 2026-07-23 | 核心问题聚焦“潜在比较优势怎样转化为本地生产、组织升级和本地收入” | SUPERSEDED | 该表述将 NSE 中间机制误写成全文研究问题 |
| 2026-07-23 | 第一版不把 NEG 放入核心模型 | CONFIRMED | 避免 home-market effect、迁移和集聚机制改变主问题 |
| 2026-07-23 | 动态组织资本只作为后续扩展 | CONFIRMED | 保持基准模型可解 |
| 2026-07-23 | 文献条目必须经过元数据核实后才进入 `references.bib` | CONFIRMED | 防止候选条目被误当成已核实引用 |
| 2026-07-24 | 全文主问题固定为“平台化 consumer access 为什么不自动转化为 local production and income” | CONFIRMED | 恢复 EL 研究计划的 access--capture 问题 |
| 2026-07-24 | NSE 是内生化 producer response、organization 和 capture 的解释机制，不是新的被解释对象 | CONFIRMED | 防止项目变成一般性 LCA--ACA 论文 |
| 2026-07-24 | consumer-side access 与 producer-side access 同时进入基准模型 | CONFIRMED | 缺少任一方向都不能解释消费者受益与地方收入下降并存 |
| 2026-07-24 | 正文必须能够产生 nominal local income 与 consumption-equivalent income 的不同符号 | CONFIRMED | 这是 EL 与 NSE 连接后的核心可检验结果 |
| 2026-07-24 | 留值率由企业进入、组织选择、所有权和服务所在地的支付流生成 | CONFIRMED | 避免将本地能力简单改名为比较优势或基础设施 |
| 2026-07-24 | EL 的 access--capture 分解进入正文；EL 精确收入传播公式在末端或附录映射 | CONFIRMED | EL 提供问题骨架，但不重复进入生产侧资源约束 |
| 2026-07-24 | `NSE_Platform_Local_Organization_Model_Contract_v1.md` 及相关旧计划进入 legacy | CONFIRMED | 保留有效推导，同时禁止旧主轴干扰活动项目 |
| 2026-07-24 | v1 的 \(M_P,M_{L0},M_X\) 结果仅在改变名义或实际收入阈值时恢复 | SUPERSEDED | v3 已将对应的 \(G_P^0,G_L^0,G_X\) 完整分类放入附录，用于证明三组织区域存在，但不作为正文主命题 |
| 2026-07-24 | facilitating state 只在 P2/P3 完成后作为条件性政策模块 | CONFIRMED | 防止政策模块取代收入机制成为全文中心 |
| 2026-07-24 | NSE 是地方发展侧的结构骨架，不只解释 producer response | CONFIRMED | NSE 同时约束禀赋与产业选择、LCA 的实际实现、组织嵌入、本地产业联系、capture formation 和 facilitating state；2026-07-28 原文审计后不再把 ACA、viability、realization 排成独立阶段 |
| 2026-07-24 | consumer preferences、platform shock 和 EL multiplier 不重新定义为 NSE | CONFIRMED | 保留各模块的理论来源，避免用 NSE 覆盖全文所有机制 |
| 2026-07-24 | 基准模型恢复最小的外部平台--本地嵌入组织选择，但不整体恢复旧三阈值模型 | CONFIRMED | 只内生化 local-service 与 external-payment incidence，不重新改变全文主轴 |
| 2026-07-27 | ACA 使用现实双重相对交付成本单独生成 \(G_A\)，viability 使用零利润条件生成 \(G_E\) | SUPERSEDED | ACA 概念继续严格保留，但 focal-region 模型为求 \(G_A\) 另加的参照地区总成本系统不服务 access--capture 主问题；活动模型只正式求 viable-realization threshold \(G_E\) |
| 2026-07-27 | \(G_L\) 按均衡选择分段定义 | CONFIRMED | \(F>\bar F\) 时由 \(G_X\) 决定；\(F\leq\bar F\) 时平台中间区消失，应由 \(G_L^0\) 决定 |
| 2026-07-27 | 数值基准采用 \(c=0.9,\kappa_g=0.3\) 和 \(\vartheta=0.05,0.50,0.95\) | SUPERSEDED | 新基准删除独立 \(G_A\) 与核心 \(zG\) 交互后重新定参；高参与示例改为 \(\vartheta=0.99\)，使改革路径实际跨过本地嵌入门槛 |
| 2026-07-27 | facilitation 与 protection 数值比较固定为同一本地组织结果 | SUPERSEDED | 比较继续固定同一本地化结果，但外部渠道楔子降为单独的 `external-channel restriction` 例子，不再作为 Proposition 4 或一般 protection 定理 |
| 2026-07-27 | 活动模型不单独构造 ACA 状态变量或 \(G_A\) | SUPERSEDED | 原说明仍把 ACA、viability 和 realization 排成三个不同阶段；2026-07-28 原文审计表明该四级结构并非 Lin--Wang 的理论写法 |
| 2026-07-27 | 基准 producer access 为 \(\mathcal M_0\exp\{(\sigma-1)(\psi z+\gamma G)\}\) | CONFIRMED | \(z\) 与 \(G\) 已分别降低同一 outbound cost；额外 \(zG\) 不是核心命题所需，\(\chi^{ext}>0\) 只在附录扩展 |
| 2026-07-27 | Proposition 4 只证明政府参与提高共享基础设施并跨越结构阈值 | CONFIRMED | 避免把一个特定渠道楔子误写成 NSE 中所有 protection，并避免预设 facilitation 的全面福利优越性 |
| 2026-07-27 | 收入阈值算法直接检查 \(G_E,G_L\) 等离散结构事件 | CONFIRMED | 离散跳跃的经济阈值是事件本身，不能返回依赖网格密度的相邻数值点 |
| 2026-07-28 | LCA--ACA 按 Lin--Wang 原文改为两层关系 | CONFIRMED | LCA 是相对生产成本所预示的潜在专业化；固定与可变交易成本、基础设施和市场条件决定实际生产/出口结构（ACA）。actual entry 是本文的国内市场对应，不另设 realization 状态 |
| 2026-07-28 | viability 只作为进入利润条件的 NSE 解释边界 | CONFIRMED | Lin (2003) 的 viability 属于另一条理论线；本文固定成本含正常回报且无持续选择性保护，因此 \(\max_r\pi_r\geq0\) 与其相容，但不建立独立 viability index、threshold 或 proposition |

## 已完成的模型决定

1. Block B 使用代表性候选产业，不引入企业异质性；
2. 现有固定成本—边际成本排序生成唯一 organizational-embedding threshold，
   不增加能力状态变量；
3. 平台的单位组织成本 \(d_P\) 同时进入利润和支付流；部分本地化由稳健性参数
   \(\lambda\) 单独刻画；
4. EL-compatible 传播分母在支付流闭合后写为
   \(1-\beta-\alpha_M\omega_C(z)\)，不进入生产侧资源约束。
