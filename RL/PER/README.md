### PER `2016`

---
- `Why Prioritize experiences in replay memory?`

        
        Replay memory에서 experience를 uniform하게 뽑는 건 그 데이터의 중요도를 전혀 반영하지 못한다.

        RL agent는 특정 경험에서 더 많이 배울 수 있다는 게 PER의 Key idea이다.
        즉, 중요한 경험은 더 많이 가져가서 correction해야한다.


        이 방법의 성능을 직관적으로 알 수 있을 때는 reward가 아주 드물게 주어질 때이다.
        
        대부분의 reward가 0이고, 딱 특정 목표를 달성했을 시에만 1의 reward를 받을 경우가 있다.
        이런 경우, reward를 얻게 되는 것과 관련한 경험은 그렇지 않는 무수히 많은 경험들 사이에 숨어있고,
        uniform하게 memory에서 뽑아낼 경우 이 경험이 뽑힐 확률이나 빈도는 매우매우 적을 수 있다.

            (Reward-Relevant experience may hidden in a mass of highly redundant failure or useless cases)
        

---

- `Prioritizing with TD-error`


        PER은 TD Error를 근거로 더 중요한 experience를 선별하고, 더 효율적으로 학습한다.

            -> Reward에 noise가 많이 껴있는 환경에는 좀 안좋다..

        하지만 이렇게 experience들 간의 우선순위를 만들어 학습하게 되면 두 가지 문제가 발생된다.

            1. Loss of diversity -> stochastic prioritization으로 해결 
            2. Bias -> Weighted important sampling으로 해결

        Priority Heap data structure로 data sorting, sampling 시간 최소화

---
- `Greedy Prioritization`


        Prioritize하는 방법 중 가장 먼저 생각할 수 있는 방법이다.

            -> Replay memory에서 가장 TD error가 큰 놈을 빼서 학습하는 방법

        당연히 문제가 여럿있다.

        1. 낮은 TD Error를 가진 experience는 진짜 드물게 아니면 아예 한 번도 뽑히지 않을 것
        2. 아주 작은 subset에만 집중하게 된다. 
            -> 특히 neural network의 경우 error가 아주 천천히 줄어든다.
            -> 처음에 TD Error가 큰 놈들 순서대로 뽑히니까 이 순서가 바뀔때까지 그놈들만 주구장창 업데이트한다.

        3. Sensitive to noise spiking 

        위 세가지 문제로 인해서, Greedy 방법은 Noise에 robust하지 못하고, experience의 다양성을 가져가지 못한다.

            -> Overfitting 유발

---
- `Stochastic Prioritization`


        위의 issue를 해결하기 위해서 Greedy Prioritization과 Uniform sampling을 적절히 섞는다.

            [P[i] 이미지]

        α는 얼마나 priorize할 건지를 결정한다. 

            -> α = 1일 때는 pure uniform sampling이 된다.

        paper에서 제안한 p(i)를 정의하는 방법은 두 가지이다.

        1. proportional : p(i) = |δ(i)| +  ε, where δ : TD error 
        2. rank-based   : p(i) = 1 / rank(i), where rank(i) : rank of transition i

            rank-based 방법이 outliar에 더 강건하기 때문에 robust하다고 한다.

---
- `Bias in prioritized replay`


        Stochastic update로 기댓값을 추정하는 건 근본적으로 변하지 않는 같은 분포에 대해서 수행된다.

            즉, E[X]를 sampling을 통해 stochastic하게 추정할 때, 이 Random variable X의 분포가 fixed!

        Prioritized replay는 통제할 수 없는 방식으로 이 분포가 바뀐다.

            안그래도 policy update로 인해서 계속 바뀌는 분포를 replay buffer로 smoothing해서 어느정도 잡아냈는데
            Prioritized replay는 buffer 내부의 경험들을 골고루 뽑지 않으니, 분포를 smoothing하지 못하게 한다. 

        따라서 이 추정치가 수렴하는 값이 바뀐다. -> bias 발생

        이 문제를 해결하기 위해서 Important-sampling weight를 사용한단다.


---
- `Anealing the bias`

        
        강화학습에서는 학습 결과가 수렴해갈수록 unbiased update가 매우 중요하다. 

            학습 초반에는 어느정도의 bias와 variance가 있는 것이 exploration 관점에서 이점은 있다고 한다.

        그래서 학습 초반에는 β = 0으로 두고 학습이 수렴해가면서 점점 β = 1로 anealing한다.
        β = 1로 될 경우, non-uniform 확률이 완전히 상쇄되어 uniform sampling으로 바뀐다.

            uniform sampling에서의 bias는 없다고(무시해도 된다고) 생각한단다.



---
`PER - discrete? continuous?`




        PER은 continuous action space보다 discrete action space에서 보다 더 유용하다.
    
        discrete action에 대해 우선순위를 정의하는게 더 쉽다. 
        반대로 continuous action에 대해서는 보다 어렵다.


---

`PER - high dimensional space?`




        PER을 high dimensional space에 적용할 때 몇가지 문제가 있다.

        1. Computional cost if calculating priorities.

            -> many possible actions and each actions need to be calculated for comparing TD errors.

        2. PER relies on the magnitude of the TD Error.

            -> high dimensional action space에서 TD error가 noisy할 수 있다. 이 경우, 우선순위 계산이 부정확할 수 있고, 
               곧 학습에 악영향을 준다.

        3. High dimensional action space는 replay buffer 내부에 경험들의 다양성을 유지하기 어렵게 한다.

            -> agent는 정책에 따라 action space의 아주 작은 집합을 explore하고, buffer 내부의 경험들은 bias가 있다.
               high dimensional space에서는 매우 다양한 space를 탐험해야하는데, buffer의 크기는 제한적이다.
               따라서 buffer 내부에 다양한 경험들이 쌓이기 보다는, subspace의 경험들로 가득차는 경우가 많을 것이다. (deque 구조라면)
               

        
