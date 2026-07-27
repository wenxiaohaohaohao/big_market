# Core Reference Metadata and Claim Audit

日期：2026-07-28
范围：当前 NSE 理论论文正文实际使用的核心来源

## 1. 审计结论

所有进入 `paper/references.bib` 的 17 个条目均已通过期刊、出版社、官方研究
机构页面、DOI 页面或本地原文首页核对。正文引用键与 BibTeX 条目一一对应：无
dangling citation，也无 orphan reference。`NSE_literature_variable_inventory.md`
继续作为候选文献清单，不直接等同于正文引用清单。

## 2. 核心理论来源

| 文献 | 核实的元数据 | 本文允许承载的论断 | 不允许承载的论断 |
|---|---|---|---|
| Lin (2011), `10.1093/wbro/lkr007` | *World Bank Research Observer* 26(2), 193--221 | 禀赋结构、适宜产业结构、hard/soft infrastructure、facilitating state | 本文具体平台阈值或支付流 |
| Lin (2012), ISBN `9780821389553` | World Bank 专著 | NSE 总体框架、比较优势遵循和基础设施外部性 | 本文的 CES 或组织利润公式 |
| Lin (2003), `10.1086/367535` | *EDCC* 51(2), 277--308 | viability 和违背比较优势的持续保护负担 | LCA--ACA 的具体总成本定义 |
| Ju, Lin and Wang (2015), `10.1016/j.jmoneco.2015.09.006` | *JME* 76, 244--263 | 禀赋驱动产业结构及资本劳动比的正式 NSE 基础 | 本文不复制其无限产业动态模型 |
| Lin and Wang (2023), NSE WP E2023001 | 本地 PDF 与北京大学新结构经济学研究院页面 | LCA 是相对生产成本所预示的潜在专业化；固定和可变交易成本决定产业是否实际生产、出口并形成 ACA；state 可通过基础设施改变 active-industry set | 不把 ACA 改写成独立 total-cost index，也不在 ACA 后再添加独立 realization 状态 |
| Lin and Monga (2010), `10.1596/1813-9450-5313` | World Bank WPS 5313 | 识别 latent-CA industries、解除阻碍 private entry 的信息、协调和基础设施约束，使产业成为 actual comparative advantage；支持必须在政策退出后仍 viable 的边界 | 不支持“任意补贴优于保护”或四阶段 LCA--ACA--viability--realization 链条 |
| Romalis (2004), `10.1257/000282804322970715` | *AER* 94(1), 67--97 | 要素丰裕度和行业要素密集度共同决定生产、贸易结构 | 不用于定义 ACA 或 viability |
| Dixit and Stiglitz (1977) | *AER* 67(3), 297--308 | 标准 CES/垄断竞争需求基准 | 不承担平台或 NSE 机制 |

## 3. 平台、市场接入和组织来源

| 文献 | 本文用途 |
|---|---|
| Ahn, Khandelwal and Wei (2011), `10.1016/j.jinteco.2010.12.003` | 低固定成本、高边际分销成本的中介选择逻辑；本文只借用成本排序，不引入异质企业 |
| Rodríguez-Clare (1996), `10.1016/0304-3878(95)00051-8` | 本地专业化生产者服务、共同固定成本与产业联系的理论解释；本文不复制其完整发展联系模型 |
| Fan et al. (2018), `10.1016/j.jinteco.2018.07.002` | 电商降低固定进入和距离摩擦、改善偏远地区消费接入 |
| Couture et al. (2021), `10.1257/aeri.20190382` | 农村电商主要产生部分消费者生活成本收益，而本地生产者和劳动收入改善有限 |
| Atkin, Faber and Gonzalez-Navarro (2018), `10.1086/695476` | 零售全球化可通过生活成本下降产生消费者福利，同时改变本地商店利润与收入 |
| Faber (2014), `10.1093/restud/rdu010` | 国内贸易成本下降不保证外围工业化，连接大市场可能强化空间不均衡 |
| Donaldson and Hornbeck (2016), `10.1093/qje/qjw002` | producer market access 的标准充分统计量表达 |

## 4. 收入传播来源

| 文献 | 本文用途 |
|---|---|
| Moretti (2010), `10.1257/aer.100.2.373` | 地方收入和就业乘数的区域发展背景 |
| Miller and Blair (2009), ISBN `9780521517133` | household-endogenous input--output/SAM 传播的标准基准 |

本文的精确固定点来自 companion EL 模型的符号映射。正文明确将该固定点称为
conditional local-income propagation，不把乘数本身再次作为 NSE 新贡献。

## 5. 原文论断边界

1. Couture et al. (2021) 支持 access 与 local income 可能分离，不证明平台化在
   所有地区降低收入。
2. Lin and Wang (2023) 支持 LCA--ACA 的交易成本区分和 state enabling 逻辑。
   该文的 ACA 最终体现为实际生产、出口和 RCA；其模型通过基础设施改变固定成本、
   可变交易效率、冰山成本和 active-industry cutoff。它既没有独立 ACA index，也
   没有在 ACA 之后再定义 realization。本文的 \(G_E,G_L,G_R,G_Y\) 均不是该文
   已有结果。
3. Ahn et al. (2011) 支持一种条件性的固定成本--边际成本渠道排序，不意味着所有
   数字平台都具有较高单位成本。
4. Moretti (2010) 和 Miller--Blair (2009) 支持收入传播背景，不支持把 local income
   解释为 national welfare。

## 6. NSE 概念使用审计

本轮原文复核纠正了此前过度形式化的四级表述。

1. **LCA 的术语来源。** Lin (2011)、Lin (2012) 和 Ju--Lin--Wang (2015)
   支撑“禀赋结构决定比较优势和适宜产业结构”的一般 NSE 命题；正文使用的
   LCA--ACA 明确区分主要来自 Lin--Wang (2023)，而不是前三项文献中的一个
   统一数学定义。
2. **LCA 的测量与模型表达。** Lin--Wang 的实证以国家禀赋和产品要素需求之间
   的距离识别 LCA；其理论沿用 Romalis 的要素密集度连续产业模型。本文的
   两地区、两产业双重相对成本
   \(\mathcal C^P_{ij}\) 是为保证 comparative 而非 absolute cost 所作的模型内
   定义，不是 Lin--Wang 原文公式。
3. **ACA 不是独立中间指数。** Lin--Wang 说明 LCA 产业只有在总成本相对较低时
   才能成为 ACA，并在经验上用出口参与和 RCA 表示 ACA。本文因此把
   \(\max_r\pi_r\geq0\) 所产生的实际进入和销售解释为国内市场中的
   LCA-to-ACA realization，不再建立独立 \(G_A\) 或第二套参考地区总成本系统。
4. **viability 不另行建模。** Lin (2003) 的 viability 是 normally managed firm
   在 free, open, competitive market 中无需外部补贴或保护即可获得 socially
   acceptable normal profit 的企业属性。本文的利润条件在固定成本包含正常回报、
   且政府只提供共享基础设施时与其相容，但不是完整的 viability 模型。因此正文
   不再设置 viability index、viability threshold 或独立命题。
5. **本文真正新增的状态。** 外部平台依赖与本地组织嵌入是本文为回答
   platform access--local capture 问题引入的组织选择，不是 NSE 既有术语。其
   文献基础来自 Ahn--Khandelwal--Wei 的成本排序和 Rodríguez-Clare 的本地
   producer-services linkage。

## 7. 最终逐条核实轨迹

核实日期：2026-07-28。下列链接均指向期刊、出版社、作者机构页或官方研究机构；
每一项均核对作者、标题、年份、刊物或工作论文编号及页码/DOI（如适用）。

| BibTeX key | 核实来源 | 结论 |
|---|---|---|
| `AhnKhandelwalWei2011` | [ScienceDirect article page](https://www.sciencedirect.com/science/article/abs/pii/S0022199611000031) | VERIFIED |
| `AtkinFaberGonzalezNavarro2018` | [Benjamin Faber publication page](https://www.ben-faber.com/)；DOI `10.1086/695476` | VERIFIED |
| `CoutureFaberGuLiu2021` | [AEA article page](https://www.aeaweb.org/articles?id=10.1257/aeri.20190382) | VERIFIED |
| `DixitStiglitz1977` | [AEA full article](https://www.aeaweb.org/aer/top20/67.3.297-308.pdf) | VERIFIED |
| `DonaldsonHornbeck2016` | [Oxford Academic issue page](https://academic.oup.com/qje/issue/131/2) | VERIFIED |
| `Faber2014` | [Oxford Academic article page](https://academic.oup.com/restud/article/81/3/1046/1605154) | VERIFIED |
| `FanTangZhuZou2018` | [ScienceDirect article page](https://www.sciencedirect.com/science/article/abs/pii/S0022199618301594) | VERIFIED |
| `JuLinWang2015` | [ScienceDirect article page](https://www.sciencedirect.com/science/article/pii/S0304393215001142) | VERIFIED |
| `Lin2003` | [University of Chicago issue page](https://www.journals.uchicago.edu/toc/edcc/2003/51/2)；DOI `10.1086/367535` | VERIFIED |
| `Lin2011` | [World Bank official article record](https://documents.worldbank.org/en/publication/documents-reports/documentdetail/368751468181776674) | VERIFIED |
| `Lin2012` | [World Bank official book PDF](https://documents1.worldbank.org/curated/en/991771468155733696/pdf/663930PUB0EPI00nomics09780821389553.pdf) | VERIFIED |
| `LinMonga2010` | [World Bank WPS 5313](https://openknowledge.worldbank.org/bitstreams/0e1402d5-e4ef-59a1-aadf-baa42b77f569/download) | VERIFIED |
| `LinWang2023` | [INSE working-paper page](https://www.nse.pku.edu.cn/en/Research/WorkingPaper/d920dcc480d14eab8c0ccf2d4c7ebfa8.htm) | VERIFIED |
| `MillerBlair2009` | [Cambridge front matter](https://assets.cambridge.org/97805215/17133/frontmatter/9780521517133_frontmatter.pdf) | VERIFIED |
| `Moretti2010` | [AEA article page](https://www.aeaweb.org/articles?id=10.1257/aer.100.2.373) | VERIFIED |
| `RodriguezClare1996` | [author-hosted published paper](https://eml.berkeley.edu/~arodeml/Papers/DOL.pdf)；DOI `10.1016/0304-3878(95)00051-8` | VERIFIED |
| `Romalis2004` | [AEA article page](https://www.aeaweb.org/articles?id=10.1257/000282804322970715) | VERIFIED |
