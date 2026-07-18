# 2026-07-16 更新前正文快照

本目录保存 2026-07-17 实施 M1--M3 升级之前的论文正文及其最小可复现材料。所有文件均从同一个 Git 悬空树对象中按原始字节恢复，没有覆盖当前工作区文件。

## 快照身份

- Git tree：`44982ee1fbc8e559e5e3b2c8a35668e291eb5680`
- 历史 PDF blob：`29083abae96a861ee5d687052042868fb74ed0ad`
- 历史 PDF SHA-256：`124D2F36FD663885CA67C279C25F92AF8AC9FC0F1168C644F473F0C86646A63D`
- 历史 PDF：11 页，Letter 页面，PDF 内部生成时间为 2026-07-16 22:21:53。
- 版本边界：该版本仍以 CES 渠道需求和更新前的命题结构为正文，并将 `appendix.tex` 直接并入 11 页 `paper.pdf`；它早于 2026-07-17 的一般需求系统与 M1--M3 替换式升级。

## 核心文件核验

| 文件 | Git blob | SHA-256 |
|---|---|---|
| `output/paper.pdf` | `29083abae96a861ee5d687052042868fb74ed0ad` | `124D2F36FD663885CA67C279C25F92AF8AC9FC0F1168C644F473F0C86646A63D` |
| `paper/main.tex` | `19e14e3089773241b517b0e316bf07015d071756` | `413563BB8419739C0D0788986A2925B9A9E0AFBF68E47232DD3577E220E3CAD7` |
| `paper/appendix.tex` | `7beda78f0945d33eed22b6794e09daeefeda56e8` | `E79671921F6B52410C4ACF89996281CDA6F1918FEC62CD41979FA9EB92BCDFFF` |
| `paper/references.bib` | `a5cb7a48059aaab18763b330dc0f2def105d58f9` | `4C0E306EA38C149F457CA3328B0AC9420E8C43A03B74A15023B9B395341D74BF` |
| `figures/mechanism_figure.pdf` | `47ee344352994778a062f15c465699cde598da4a` | `9943881791DB0BBFA00EE1C90C75E54F7EED5DBAB5B04C6F2CCDA190DA3F5884` |
| `code/build_paper.ps1` | `cd3799528cbaa3a507d420a55b620b41733f4755` | `5EE4F6AAFB0A821688ECA04DBC1F2537005587C29771DDAED588C54F04EEAC0F` |
| `code/make_mechanism_figure.py` | `690dfaf9ff37fe6e9ec876a0249cada05ee65960` | `46D5C03C1075CFA28E062406DC6DE37CF7544D952024A2381D703B28314C2493` |
| `code/verify_model.py` | `2ed7f723ad55e9c9d1d89f409e962dc015c67010` | `BBA005B39752B761AA345B4CEEAA1C7FC47FDE160F3BB305CBC6194A027B4430` |

## 使用说明

- 用于查看的便捷副本同时保存在当前项目的 `output/history/paper_pre_M1_M3_2026-07-16.pdf`。
- 本目录是历史记录，请不要直接编辑。若需试编译，先复制整个目录，再运行其中的 `code/build_paper.ps1`，避免改写已核验的历史 PDF。
- 当前正式稿仍位于项目根目录的 `paper/` 与 `output/paper.pdf`，恢复过程没有修改这些文件。
