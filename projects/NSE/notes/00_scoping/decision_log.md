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
| 2026-07-24 | v1 的 \(M_P,M_{L0},M_X\) 结果仅在改变名义或实际收入阈值时恢复 | CONFIRMED | 组织选择是服务于 access--capture 的子机制 |
| 2026-07-24 | facilitating state 只在 P2/P3 完成后作为条件性政策模块 | CONFIRMED | 防止政策模块取代收入机制成为全文中心 |
| 2026-07-24 | NSE 是地方发展侧的结构骨架，不只解释 producer response | CONFIRMED | NSE 同时约束禀赋与产业选择、LCA--ACA、viability、组织嵌入、本地产业联系、capture formation 和 facilitating state |
| 2026-07-24 | consumer preferences、platform shock 和 EL multiplier 不重新定义为 NSE | CONFIRMED | 保留各模块的理论来源，避免用 NSE 覆盖全文所有机制 |
| 2026-07-24 | 基准模型恢复最小的外部平台--本地嵌入组织选择，但不整体恢复旧三阈值模型 | CONFIRMED | 只内生化 local-service 与 external-payment incidence，不重新改变全文主轴 |

## 尚待模型推导决定

1. Block B 是否只需代表性候选企业，还是 P1 必须引入企业异质性；
2. 最小组织选择能否用现有成本项生成唯一 organizational-embedding threshold，
   而不增加新的能力状态变量；
3. 平台技术成本与平台费/支付归属是否必须使用两个参数；
4. EL companion paper 的最终记号和分母如何逐项映射到新稿。
