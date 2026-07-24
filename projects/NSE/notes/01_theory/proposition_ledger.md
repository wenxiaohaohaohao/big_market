# Proposition Ledger

日期：2026-07-24

对应合约：`notes/01_theory/model_contract.md`

本台账只记录当前 `access--capture` 主轴下的正式结果。归档 contract 中的组织阈值
不自动继承证明状态。

| ID | 目标结果 | 必要来源 | 关键条件 | 状态 |
|---|---|---|---|---|
| L0 | 平台化提高平台支出份额并降低消费价格指数 | Block A | CES；平台相对价格随 \(z\) 下降 | TO PROVE |
| P1a | 更强 LCA 降低本地企业将平台市场机会转化为实际进入所需的 \(G_E^*\) | Block B | 严格相对成本；viability 和进入条件 | TO DERIVE |
| P1b | 存在最小 organizational-embedding threshold \(G_L^*\) 或 \(M_L^*\)，组织选择改变本地服务收入与外部支付 | Block B | \(P\)--\(L\) 利润差 single crossing；共同支付流表 | TO DERIVE |
| P2 | 存在唯一名义地方收入阈值 \(G_Y^*\) | Blocks A--C | producer 与 linkage gains 对 \(G\) 的净效应单调；capture loss 有界 | TO DERIVE |
| P3 | 存在实际收入阈值 \(G_R^*\)，且 \(G_R^*<G_Y^*\) | Blocks A--C + EL mapping | \(P_M'(z)<0\)；两个阈值均为内部解 | TO DERIVE |
| C1 | 更强 LCA 同时降低 \(G_R^*\) 和 \(G_Y^*\) | P1a--P3 | production 与 organizational embeddedness 的 increasing differences 或等价条件 | TO DERIVE |
| P4 | 赋能与保护对 access、entry 和 capture 的作用不等价 | Policy block | 一个明确公共品或协调失败；政策真实资源成本 | BLOCKED BY P2/P3 |
| E1 | 外部平台效率提高可能降低进入门槛、提高本地组织切换门槛 | Legacy organization module | 高固定成本--低边际成本的本地组织 | LEGACY; OPTIONAL |
| C2 | EL 收入传播放大第一轮收入，但不改变已证明的阈值排序 | EL mapping | 与 companion paper 分母和支付口径一致 | TO VERIFY |

## 当前优先顺序

```text
L0
 -> P1a
 -> minimal P--L organization choice
 -> payment-flow accounting
 -> P1b
 -> P2
 -> P3
 -> C1
 -> P4
 -> optional full E1 extension.
```

## 停止条件

出现以下任一情况时，不继续增加模型模块：

1. Block A 无法产生可单独识别的消费价格收益；
2. Block B 的 producer gain 仍由外生增长率给定；
3. organizational embeddedness 不能改变 local-service 或 external-payment incidence；
4. capture loss 不是支付流结果；
5. \(G_Y^*\) 的存在需要直接假定目标结论；
6. \(G_R^*<G_Y^*\) 不能由价格效应严格推出；
7. 完整恢复 legacy 三阈值后仍不改变 P2 或 P3。

## 完成定义

一个命题只有在以下四项同时完成时才标记为 `PROVED`：

- 正式陈述；
- 参数条件；
- 解析证明；
- 边界和反例检查。
