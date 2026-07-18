# Independent regional-domain and literature review

Date: 2026-07-14  
Role: local multipliers, ownership/leakage, and retail/e-commerce spatial incidence  
Individual recommendation: **major revision**  
Confidence: high on conceptual assessment and identified antecedents; moderate on exhaustive priority

## Dimension Scores

### D1

dimension_id: D1  
score: warn  
finding: The model is coherent as a short-run benchmark, but fixed channel coefficients are applied to every induced round, making average and marginal local-income shares identical and invariant to capacity, wages, ownership, and spending composition. Each rho_c should be interpreted as a marginal reduced-form local-income coefficient. The restriction epsilon greater than or equal to zero also excludes adverse production-side base-income responses. See main.tex lines 105--145 and 196--350.

External comparisons: [Pennings (2021)](https://www.aeaweb.org/articles?id=10.1257%2Faer.20190240) gives a closely related treatment of recurring local-demand rounds and first-round incidence. [Faber (2014)](https://academic.oup.com/restud/article/81/3/1046/1605154) shows that lower domestic trade costs can harm peripheral production.

### D2

dimension_id: D2  
score: warn  
finding: The manuscript accurately describes its cited e-commerce and ownership evidence, but omits closer analytical antecedents. Recursive consumption feedback, leakage-adjusted multipliers, and the distinction between gross spending and initial local income are established. The defensible increment is CES price-induced channel substitution combined with channel-specific local-income coefficients, finite sign regions, and the below-one-half marginal peak.

Closest verified sources:

- [Pennings (2021)](https://www.aeaweb.org/articles?id=10.1257%2Faer.20190240): recurring local-demand rounds and first-round incidence.
- [Miyazawa (1960)](https://academic.oup.com/qje/article-pdf/74/1/53/5206190/74-1-53.pdf): household consumption feedback in an open-economy multiplier.
- [Little and Doeksen (1968)](https://academic.oup.com/ajae/article/50/4/921/116505): import leakage in regional input-output multipliers.
- [Forman, Ghose, and Goldfarb (2009)](https://pubsonline.informs.org/doi/abs/10.1287/mnsc.1080.0932): spatial online/offline channel substitution.

The equation-level overlap with Li's working paper was not fully resolved; categorical priority claims should be qualified.

### D3

dimension_id: D3  
score: pass  
finding: Within the stated closure, the paper correctly distinguishes B from G, first-round retention from recursive propagation, nominal income from the consumption index, and that index from social welfare. The word retention may still invite confusion unless it is consistently defined as a marginal local-income coefficient.

### D4

dimension_id: D4  
score: warn  
finding: The retail/regional bridge is substantive but underdeveloped because the coefficients are not mapped to seller location, platform margins, warehouses, logistics, local taxes, factor ownership, or purchase geography. It is unclear which observed margins identify platform price, expenditure share, and the channel-income differential.

Useful mappings include [Brown et al. (2019)](https://www.journals.uchicago.edu/doi/full/10.1086/705505), [Forman et al. (2009)](https://pubsonline.informs.org/doi/abs/10.1287/mnsc.1080.0932), [Dolfen et al. (2023)](https://www.aeaweb.org/articles?id=10.1257%2Fmac.20210049), and [Chun et al. (2023)](https://www.sciencedirect.com/science/article/pii/S0094119023000645).

### D5

dimension_id: D5  
score: pass  
finding: The manuscript is concise, orderly, and suitable in form for an Economics Letters theory note. The presentational concern is the breadth of the priority claim relative to the nine-entry bibliography.

## Failure Condition Checks

F1  
fired: false  
derivation: No mandatory dimension is block.

F2  
fired: false  
derivation: This reviewer meets the reviewer-level predicate through D1 and D2, but panel majority is deferred.

F3  
fired: false  
derivation: D4 is warn, not block.

F0  
fired: false  
derivation: This review fails the all-mandatory-pass predicate because D1 and D2 are warn.

## Review Body

### Strongest domain contribution

The strongest contribution is not recurring leakage. It is the parsimonious combination of price-induced CES substitution, channel-specific marginal local-income coefficients, endogenous variation in the propagation coefficient, finite nominal/real-income regions, and a unique marginal peak below one half. No checked source contained this exact combination, but that conclusion is not an exhaustive novelty certification.

### Literature-position verdict

The paper should acknowledge that consumption feedback and leakage-adjusted multipliers are established. Moretti is principally an employment-multiplier antecedent and Chodorow-Reich a geographic fiscal-output-multiplier reference; Pennings is a closer algebraic benchmark. The contribution should be narrowed to the endogenous channel-share mechanism and its comparative statics.

### Interpretation of rho_c

A retail dollar can create local wages, locally owned profit, taxes, logistics income, and payments to local suppliers, while leaking through imports, external sellers, platform fees, and absentee ownership. A single channel coefficient compresses these flows and is repeatedly applied at the margin. It should be called a marginal local-income coefficient and accompanied by an inclusion/exclusion list.

### Required revisions

1. Rebuild the novelty paragraph around Pennings, Miyazawa, and Little--Doeksen.
2. Narrow the contribution to endogenous CES channel composition, finite sign regions, and the below-one-half peak.
3. Define rho_c as a marginal local-income coefficient and map its accounting components.
4. Permit epsilon to be any real number, or justify why a nonnegative base-income response is the intended benchmark.
5. Add a short empirical mapping for prices, expenditure shares, and the channel-income differential.
6. Qualify the comparison with Li until an equation-level audit is documented.
7. Flag in the main text that the appendix extends finite thresholds to positive G.

The paper need not add platform pricing, endogenous ownership, entry, relocation, and full welfare simultaneously. It needs sharper positioning and interpretation.

## Editorial Decision

editorial_decision=major_revision
