# NSE：平台化市场接入、比较优势实现与本地价值捕获

这是 `big_market` 下拟呈林毅夫教授审阅的过渡性理论论文子项目。

## 当前冻结的研究问题

> 为什么平台化市场整合能够普遍改善消费者接入，却只有在潜在比较优势能够通过
> 适宜的本地组织和基础设施条件得到实现时，才会转化为本地生产和地方收入？

本文继承 EL 短文的 `market access--local capture` 问题，并建立独立的地方发展
结构模型。NSE 为地方一侧提供理论骨架：它解释禀赋结构、比较优势、软硬基础设施、
企业自生能力、本地组织与产业联系如何共同决定生产和价值捕获，但不替换原研究
问题。

## 理论主从关系

```text
研究对象
  platform integration
  -> consumer access
  -> producer access
  -> local capture
  -> nominal and consumption-equivalent local income

解释机制
  endowments
  -> relative production cost
  -> LCA
  -> hard/soft infrastructure and transaction costs
  -> ACA and viability
  -> entry and organizational choice
  -> local complementary services and linkages
  -> endogenous components of local capture

政策推论
  facilitating state
  -> remove shared infrastructure and coordination constraints
     in LCA-consistent sectors.
```

## 工作题目

中文：

**市场接入何时转化为地方发展？平台化、比较优势实现与本地价值捕获**

英文：

**When Does Market Access Become Local Development? Platform Integration,
Comparative-Advantage Realization, and Local Value Capture**

## 活动项目文件

- `paper/main.tex`：唯一正式 LaTeX 主稿；
- `paper/appendix.tex`：唯一附录；
- `paper/references.bib`：唯一 BibTeX 文献库；
- `notes/00_scoping/project_memo_zh.md`：项目身份和范围；
- `notes/00_scoping/decision_log.md`：冻结决定；
- `notes/01_theory/model_contract.md`：唯一活动模型合约；
- `notes/01_theory/proposition_ledger.md`：唯一活动命题台账。

候选文献清单不是正式 bibliography。只有完成元数据核实的来源才能进入
`references.bib`。

## 与 EL 的边界

| 层面 | 当前 NSE 稿 |
|---|---|
| 研究问题 | 保留 consumer access 与 local capture 的分离 |
| NSE 结构骨架 | 内生化 LCA--ACA、viability、生产者进入、组织嵌入、本地产业联系和 facilitating state |
| 平台模块 | 给出 consumer/producer access 和渠道替代冲击，不被重新解释为 NSE |
| 留值率 | 由均衡支付流生成，不是外生能力指标 |
| EL 作用 | access--capture 基准进入正文；精确传播公式在末端或附录映射 |
| 独立性 | 不读取或写入 EL 的代码和输出，不重复宣称 EL 命题 |

## 第一版核心结果

1. 更强的 LCA 降低本地企业实现 producer-side market access 所需的结构门槛；
2. 组织选择和本地配套服务来源内生决定 production gain 有多少转化为 local capture；
3. 存在平台化提高名义地方收入的能力/基础设施阈值；
4. 消费价格收益使实际收入阈值严格低于名义收入阈值；
5. facilitating investment 与 protection 对 access、entry 和 capture 不等价。

## Legacy 规则

主轴重置前的模型和计划保存在：

`history/legacy_2026-07-24_pre_axis_reset/`

这些文件保留有效推导，但状态为 `SUPERSEDED`，不得作为当前项目依据。旧
\(M_P,M_{L0},M_X\) 组织阈值只有在改变当前收入阈值时才可作为扩展恢复。

## 关于 NEG

第一版不加入完整 New Economic Geography，不建模迁移、内生市场规模、集聚
外部性和累积因果。NEG 仅在边界讨论中说明，因为它不是回答当前 access--capture
问题的必要条件。

## 项目结构

```text
NSE/
├── paper/                  # 唯一正式 LaTeX 主稿、附录和 BibTeX
├── notes/
│   ├── 00_scoping/         # 项目主轴和冻结决定
│   ├── 01_theory/          # 活动模型合约与命题台账
│   └── 02_future_empirics/ # 后续数据验证思路
├── literature/             # 经核实的本地文献材料
├── code/                   # 构建、解析核验和数值示意
├── figures/
├── output/
├── history/                # 标明状态的 legacy 和里程碑
└── README.md
```

## 当前状态

- [x] 固定 access--capture 研究主轴；
- [x] 明确 NSE 是地方发展侧结构骨架，并划清 EL 与平台模块边界；
- [x] 归档偏离主轴的旧 contract；
- [x] 建立活动 Model Contract v2.1 和命题台账；
- [ ] 闭合 Block A 的消费接入与支付流；
- [ ] 推导 P1a 的 producer-entry threshold 与 P1b 的 organizational-embedding threshold；
- [ ] 证明名义和实际收入阈值及严格排序；
- [ ] 在 P2/P3 完成后建立 facilitating-state 模块；
- [ ] 完成 illustrative numerical exercises；
- [ ] 形成可供外部审阅的完整理论稿。
