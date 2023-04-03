## Hidden Markov Model 

CRF를 이해하기 위한 Naive Bayes의 다음 단계이다.

Markov Property, Markov chain, Markov model 등의 기본 개념부터 하나씩 이해하고, HMM으로 넘어가자


<br>

#### Markov Model 

- Markov Model의 종류

      1. Markov Chain : 상태를 완전히 관찰 가능한 자율 시스템에 사용 
      2. Hidden Markov Model : 상태를 부분적으로 관찰 가능한 자율 시스템에 사용 
      3. Markov Decision Process : 상태를 완전히 관찰 가능한 통제 시스템에 사용 (강화학습)
      4. Partialliy Observable Markov Decision Process : 상태를 부분적으로 관찰 가능한 통제 시스템에 사용 (강화학습)

---

<br>

#### Markov Property

- Markov Property

        N+1 상태는 오직 N의 상태, 혹은 그 이전의 '일정'기간의 상태에만 영향을 받는 것을 Markov Property라고 한다. 

            예를 들어, 동전 던지기는 독립 시행이므로 n 번째의 상태가 앞이든 뒤이든 n+1 번째의 상태에 영향을 주지 않는다.

            반면 1차 Markov chain은 n번 째 상태가 n+1 상태를 결정하는데 영향을 미친다!





