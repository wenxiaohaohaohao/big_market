# Legacy snapshot before the access--capture axis reset

日期：2026-07-24

状态：`SUPERSEDED`

## 归档原因

本目录保存项目在重新确认研究主轴之前的理论文件。这些文件主要研究：

```text
潜在比较优势
  -> 全国市场进入
  -> 外部平台组织
  -> 本地嵌入式组织
```

其中的固定成本--边际成本阈值推导具有独立参考价值，但该版本删除了
consumer-side access、本地渠道替代和名义/实际地方收入分解，因而不能继续作为
当前过渡性论文的模型合约。

## 使用限制

- 本目录文件不得作为当前项目的研究问题、模型设定或命题状态依据。
- 不从这里向 `paper/main.tex` 直接复制命题或结论。
- 如需重新使用某项推导，必须先说明它如何服务于当前
  `access--capture` 主轴，再写入活动 model contract。
- 当前唯一活动理论合约是：
  `notes/01_theory/model_contract.md`。
- 当前唯一活动命题台账是：
  `notes/01_theory/proposition_ledger.md`。

## 文件说明

| 文件 | 原用途 | 当前处理 |
|---|---|---|
| `NSE_Platform_Local_Organization_Model_Contract_v1.md` | 外部平台与本地组织的六参数阈值模型 | 保留为可选组织选择子模块，不作为全文基准 |
| `model_contract_draft0.md` | 第一版范围约束 | 被活动 contract 取代 |
| `proposition_ledger_draft0.md` | 第一版命题计划 | 被活动命题台账取代 |
| `model_update_plan_2026-07-23.md` | 七模块更新计划 | 其中 access--capture 验收标准被保留，复杂模块计划不再执行 |
| `NSE_project_memo_zh.md` | “独立 NSE 论文”路线备忘录 | 因主从关系倒置而归档 |
| `conversation_note_pre_axis_reset.txt` | 将新稿推向生产--进入--组织选择主轴的旧问答摘录 | 只供追踪主轴偏移原因 |

## 可重新使用的内容

旧 contract 中以下结果可以在完成当前基准模型后作为 lemma 或 extension 重新评估：

1. 外部平台的低固定成本--高边际成本与本地组织的高固定成本--低边际成本选择；
2. 平台进入阈值、本地组织独立盈利阈值和组织切换阈值；
3. 平台效率提高可能降低进入门槛、同时提高本地组织切换门槛；
4. 平台服务支付部分本地化时的支付流会计。

这些结果只有在能够改变地方第一轮收入、名义收入或消费等价实际收入时，才进入
当前论文正文。
