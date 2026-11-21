# Changes from version 1.6 to version 1.9

Version 1.9 is dated 21 November 2026 (45 pages; v1.6 had 40). Versions 1.7 and 1.8 were not
posted to this repository separately. Their changes are listed here with those of 1.9, attributed
as in the paper's acknowledgement. Section and theorem numbers refer to v1.9.

## Title and scope

- **Title.** v1.6: *Christol's conjecture for non-resonant globally bounded ${}_3F_2(a_1,a_2,a_3;b,1)$
  series*. v1.9: *Christol's conjecture for non-resonant globally bounded hypergeometric series of
  height two*.
- **Theorem A** now covers ${}_nF_{n-1}(a_1,\dots,a_n;b_1,\dots,b_{n-2},m;x)$ for every order
  $n\ge3$ and every positive integer $m$, under (NR): all $a_i$, $b_j$, $a_i-b_j$ non-integral.
  Repetitions within the upper list, or within the non-integral lower list, are allowed. v1.6
  treated only $n=3$, $m=1$. The theorem also states that $F_m$ is globally bounded if and only if
  $F_1$ is.
- **Corollary C** (complete rank-three statement) now allows lower parameters in
  $\mathbb{Q}\setminus\mathbb{Z}_{\le0}$, i.e. any positive integers, not just $1$.

## v1.7: arbitrary rank and positive integral lower parameter

- **Proposition 3.1** (two Hodge levels ⇔ global boundedness) is proved in arbitrary rank with a
  multiplicity-safe step function $D_k(t)$, the reflection identity
  $D_{-k}(1-t)=2-D_k(t^-)$, and the equal-block endpoint inequalities (3.2) for Fedorov's
  $\rho(l)$. It now also gives the multiplicity bound (each class occurs at most twice). The old
  rank-three ordering table becomes **Corollary 3.2**.
- **Lemma 2.6** (local monodromy at 0) records the full minimal polynomial of $T_0$ and the rank of
  $T_0^d-1$, which can exceed one in higher rank. The proof uses only the distinguished size-two
  Jordan block at eigenvalue 1, not a rank-one variation.
- **Section 4** (weight one) works over the full cyclotomic CM field $\mathbb{Q}(\zeta_N)$
  uniformly. The trace-field refinement (**Lemma 9.1**) is restricted to rank three, and a new
  remark explains why: for $a=(\frac14,\frac14,\frac34,\frac34)$, $b=(\frac12,\frac12)$ the trace
  field is $\mathbb{Q}$.
- **Example 9.3** (new): ${}_4F_3(\frac14,\frac14,\frac34,\frac34;\frac12,\frac12,1;x)$, a
  rank-four case with two monodromy blocks, $\operatorname{rank}(T_0^2-1)=2$.
- **Section 8** (new), *Positive integral lower parameters*: an explicit inverse contiguity
  operator (Proposition 8.1),
  $F_m=\frac{q}{R(-q)}\big[x^{-1}\theta B(\theta)-S_q(\theta)\big]F_{m-1}$ with $q=m-1$,
  replacing the earlier sketch. Proposition 8.2 shows that this operator preserves global
  boundedness and two-variable algebraic diagonals.
- **Appendix B** gains "Higher-order checks in version 1.7" (`tools/verify_extension.py`: 1,220
  contiguity coefficients in ranks 3–5 with $m=2,3,4,7,12$; 2,000 parameter multisets in ranks
  3–6, 47 of them globally bounded), and a "Scope of the source checks" subsection listing
  which primary texts were inspected and at which versions.
- **Imported-results table** expanded (v1.7–v1.8; the paper does not say which of these
  versions added each item): Stacks Project tags, Catanese (integral Lefschetz),
  Silverberg–Zarhin (semistability criterion), Milne's étale notes (Riemann existence), Ehresmann
  (Bourbaki version). Proposition 6.2 Step 1 now explains the comparison between algebraic and
  topological monodromy via torsion covers. Lemma 6.6 gives a self-contained annulus argument.
  Proposition 7.1 derives the local dualizing generator $du/u$ by hypersurface adjunction.

## v1.8: the septic period made explicit

- New paragraph after Corollary B, *A genus-three period for the septic series*: with
  $x=64/s^{14}$, a marked family $C_s$ (equation (1.5)) whose fibre at $s=0$ is
  $v^2=u^7-1$. For $s\ne0$ it is a smooth plane quartic, with an explicit holomorphic differential
  $\eta_s$ and $S_7(64/s^{14})=K\int_{\gamma_s}\eta_s$. Its class satisfies the original
  hypergeometric operator under Gauss–Manin.
- **Example 9.4** now links $S_7$'s abelian threefolds with multiplication by
  $\mathbb{Q}(\sqrt{-7})$ to these marked Jacobians, and notes descent of the generic curve to a
  plane quartic over $\mathbb{Q}(x)$.
- New reference: Cartier–Miller project, *An algebraic genus-three normal form for the septic
  hypergeometric period*, companion note v1.1 (checked through $s^{100}$ for the period matrix
  and $s^{102}$ for the operator; second implementation with Claude Opus 5.5).

## v1.9: arbitrary positive integral lower parameters in Corollary C

- **Corollary C, Case 1** (both lower parameters positive integers) is proved with algebraic
  Hadamard factors $A_{a,m}(x)=\sum_k (a)_k/(m)_k\,x^k$, shown algebraic by the recursion
  $A_{a,m}=\frac{m-1}{a-1}\cdot\frac{A_{a-1,m-1}-1}{x}$. Case 2 is now Theorem A with $n=3$.
- **Remark 9.6** (new), *Maximal height*: for any $n$ and positive integers $m_1,\dots,m_{n-1}$,
  ${}_nF_{n-1}(a;m;x)=A_{a_1,m_1}\star\cdots\star A_{a_n,m_n}$, so
  $\mathrm{hg}=\mathrm{dg}=n$ and $n+1$ rational variables are optimal.
- Abstract, plain-language summary, organization, concluding remarks and acknowledgement were
  updated to match.

## Repository status

The v1.7 verification script is in `supplementary/tools/verify_extension.py`, and the v1.8
septic companion note v1.1 is in `supplementary/septic_companion/` (original bundle in
`releases/`). Both were rerun when they were deposited; see `RERUN_LOG_2026-11-21.md`.
