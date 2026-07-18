# Independent analytical-methodology review

Date: 2026-07-14  
Role: pure-theory algebra, equilibrium, and boundary audit  
Individual recommendation: **accept**  
Confidence: high

## Dimension Scores

### D1

dimension_id: D1  
score: pass  
finding: Every central derivation reproduces from the stated primitives. CES duality, interiority, the income fixed point, contraction, multiplier identities, finite thresholds, marginal effects, and the unique peak are correct on their stated domains.

### D2

dimension_id: D2  
score: pass  
finding: The manuscript consistently distinguishes CES substitution, first-round incidence, recursive propagation, nominal income, and indirect consumption value. It does not call the real-income index full welfare.

### D3

dimension_id: D3  
score: pass  
finding: The complete chain is p_P to s to omega to D to Y and R. All sign and threshold results carry the restrictions G=0 and rho_A greater than rho_P where required; the appendix separates the general-G extension.

### D4

dimension_id: D4  
score: pass  
finding: The formal objects are translated sufficiently into local-multiplier and spatial-incidence terms, with explicit scope limits.

### D5

dimension_id: D5  
score: pass  
finding: Definitions precede use, notation is stable, and the appendix follows the theorem order, permitting exact verification.

## Failure Condition Checks

F1  
fired: false  
derivation: D1--D3 are pass.

F2  
fired: false  
derivation: This reviewer has no mandatory warning; panel majority is deferred.

F3  
fired: false  
derivation: D4 is pass.

F0  
fired: false  
derivation: This reviewer satisfies all mandatory dimensions; panel unanimity is deferred.

## Review Body

### Independent algebra audit

Let Q equal (1-a) times p_A to power (1-eta), plus a times p_P to power (1-eta). CES duality yields the reported retail price index, Hicksian demands, and the platform expenditure share s. Because the log platform price falls one-for-one with z:

- d log P_M / dz = -s;
- ds / dz = (eta-1)s(1-s);
- omega = rho_A - Delta-rho times s;
- d omega / dz = -Delta-rho times (eta-1)s(1-s).

The income operator has slope q = beta + alpha omega, bounded above by alpha + beta, which is strictly below one. It is therefore a contraction on nonnegative income. The unique positive solution is:

Y = (B + omega G) / D, where D = 1 - beta - alpha omega.

The two multipliers are m_B = 1/D and M_G = omega/D. Their comparison is exact:

m_0 omega - M_G = alpha omega(1-omega) / [(1-alpha-beta)(1-beta-alpha omega)].

It is nonnegative and equals zero exactly at omega equal to zero or one. The retention elasticity is (1-beta)/D, which exceeds one for positive omega, and M_G is strictly convex in omega.

For G=0, the reported finite ratios for Y and R imply the three strict sign regions. Under a lower-retention platform channel, the real-income threshold is strictly below the nominal-income threshold. Therefore nominal income cannot rise while real income falls. Both equality cases are correct.

For marginal changes:

- d log Y / dz = epsilon - Lambda(s);
- d log R / dz = epsilon + alpha s - Lambda(s).

Writing d_A = 1-beta-alpha rho_A and b = alpha Delta-rho, maximization reduces to f(s) = s(1-s)/(d_A+bs). The derivative numerator decreases strictly from positive to negative and has exactly one root:

s-dagger = 1 / [1 + square-root(1+b/d_A)], which is below one half.

Because finite z maps bijectively to an interior share, this root is attainable and is the global CES maximum.

### Theorem verdicts

- Lemma 1: valid, including interiority and the access derivatives.
- Lemma 2: valid; the contraction is global and the positive intercept gives a positive fixed point.
- Proposition 1: valid, including equality cases, elasticity, geometric series, and convexity.
- Proposition 2: valid, including threshold order, equality cases, and exclusion of a fourth sign pattern.
- Corollary 1: valid; the derivative crosses zero exactly once.
- General G greater than zero: valid; the appendix correctly differentiates the numerator and denominator and preserves finite-threshold ordering.

### Boundary audit

- Finite z and positive CES weights imply 0 < s < 1.
- Finite-z omega equal to zero requires both channel coefficients zero; omega equal to one requires both one.
- Equal coefficients make omega constant; reverse ordering makes omega rise with z.
- The alpha to zero, beta to zero, eta to one, and eta to infinity statements are correct.
- At equal prices in the perfect-substitutes limit, choices are nonunique and the CES sequence selects share a.
- When alpha + beta = 1, only the income fixed point can be continued; the maintained household interiority condition no longer applies.

### Reproducibility

Static inspection of verify_model.py found a fixed random seed, 2,000 draws, finite-threshold checks, retention and CES boundary checks, and general-G derivative checks. The reviewer did not execute it and makes no runtime claim.

### Minor corrections

1. State explicitly that the alpha + beta = 1 discussion continues only the income fixed point.
2. Add a code-availability sentence for verify_model.py and its deterministic seed.
3. If multiplier convexity is a reported result, state it in Proposition 1 rather than only in the appendix.
4. Clarify the feasibility condition for the lower finite-threshold equality.

## Editorial Decision

editorial_decision=accept
