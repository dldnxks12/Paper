#### Eligibility trace for POMDP

Memoryless approach for delayed RL 

---

- `N-step TD`


        TD-learning과 Monte Carlo의 쨈뽕

<div align="center">

![img.png](img.png)

![img_1.png](img_1.png)

</div>

---

- `TD(λ) - forward learning`

        N-step TD에서 N 값 찾기 너무 번거로바서 제안 (λ - smoothly changes in 0~1) 
        + Episodic case에서만 사용가능 

        1. λ = 0 : TD(0)                   --- Small variance / Bias 존재
        2. λ = 1 : TD(1) = Monte Carlo     --- Large variance / Bias X
        3. 0 < λ < 1 : TD + Monte Carlo    --- 적당~


<div align="center">

![img_2.png](img_2.png)

</div>

---

- `Eligibility trace - backward learning` 

<div align="center">

![img_3.png](img_3.png)

</div>

---

- `Eligibility trace for POMDP`