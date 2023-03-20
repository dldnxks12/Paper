### D3QN `2016`

---

- `Dueling Network for reducing Variance`


            DQN의 overestimation bias를 없애기 위해 Double DQN이 등장했다.
            D3QN은 Double DQN에서 더 나아가 variance를 줄이고자, dueling architecture를 도입한다. 


---

- `Why variance?`


            Variance를 줄이면 학습 과정이 조금 더 안정적이고 효율적이다. 
            RL Agent는 환경과 상호작용하면서 얻는 total reward를 극대화하도록 학습을 진행한다.
            하지만 trial and error 기반으로 학습하는 과정은 noisy하고 unpredictable하다. 
            이러한 특성이 V, Q의 추정에 큰 variance를 만들어낸다. 

            High Variance는 다음과 같은 문제를 가져온다.

            1. Slow Learning 
                
                -> 랜덤성이 크면, 학습에 유용하지 않은 피드백을 주는 결정을 고를 확률이 많아진다.
                    이는 optimal policy로 converge하는 시간을 길게 만든다.

            2. Instability 

                -> 위와 같은 맥락으로, 유용하지 않은 피드백으로 인해 optimal policy로 가는 수렴과정에 osilation을 유발한다.

---

- `Why PG method have large variance?`


            PG method는 유한한 수의 sample로 stochastic하게 update를 수행하므로, 
            optimal value로 converge하는 과정에 variance가 큰 편이다.
            이는 batch size를 키울수록 이로 인해 발생하는 variance는 줄일 수 있지만, 연산량이 증가한다.


            [이미지 -> naver keep]

---

- `Why Advantage function?`

 
            Advantage function은 Variance를 줄이는데 효과적이다.

                * Advantage function : Q(s, a) - V(s)

            이는 V의 랜덤성을 제어하는데 도움을 주고, 특정 상태에서 특정 행동에 대한 값에 대한 더 정확한 추정에 집중하기 때문이다.

                -> 즉, state의 본질적인 값에 대한 영향을 줄이고, 그 상태에서 특정 행동을 했을 떄의 값에 더 집중한다.

            V는 학습 과정에서 계속 그 값이 바뀌므로 estimated value가 계속 바뀐다.
            하지만 Advantage function은 그 순간의 V의 기댓값에 기준해서 특정 행동을 했을 때 얼마나 더 좋은 지를 이용해서 학습하기 때문에
            계속해서 바뀌는 Value function의 randomness에서 벗어나기에 학습이 조금 더 강건하다.

                Ex) if V = 10 -> V = 15 -> V = 20

                        -> 기댓값이 계속 변화 + High Varince

                    A = V-Q?
                
                        -> A는 zero mean, only focus on difference
                        -> variance는 상대적으로 Low

---

- `D3QN`


            어떤 Action이 더 좋은 지에 집중하기 때문에, 올바른 행동을 식별하는데에 뛰어나다.
            특히, dueling architecture는 어떠한 State가 가치 있는지, 해당 state의 모든 action을 수행해보지 않아도 학습할 수 있다.

                -> V(s)는 Q(s, a)의 평균이므로, 기본 학습 구조(single stream)에서는 모든 action을 수행해봐야지 V를 추정할 수 있다.

                    즉, 하나의 행동 Q(s, a1)을 얻으면 Q(s, a1)에 대해서만 update가 진행된다.  ---- Q(s, a1)를 학습하는 네트워크니까.. 

                    하지만 deuling 구조에서는 특정 state에서 어떠한 action에 대한 Q 값이 업데이트 될 때마다 V와 공유하는 stream이 업데이트 되기 때문에
                    나머지 action에 대한 Q 값도 간접적으로 학습할 수 있다.

                        -> 1개의 stream을 가진 구조에서는 Q(s, a1)만 학습되고, 다른 action에 대한 값은 건들여지지 않는다.
                            반면에 dueling stream은 어떠한 Action을 고르든 update 과정에서 다른 action들의 값들도 같이 만져진다.
                            
                            -> action의 수가 많으면 많을수록 장점이 많아진다.

                    특히 이건 어떤 행동을 하던 action이 환경에 영향을 주지 않을 때의 state들을 학습하는데에 유용한데, 
                    대부분의 state에서 어떤 행동을 하는 것이 좋은 지 추정하는게 불필요하다고 한다. 

                        -> racing 게임에서 당장의 장애물만 잘 피하면 되는 task에서 유용
                            
                            (* but bootstraping을 통한 학습을 사용하는 알고리즘은 모든 state의 값을 추정하는게 중요) 


                + PER을 같이 썼더니 성능이 크게 올랐다고 한다. 


<br>


            또한 Noisy에 대해 강건하게 학습된다.
            특정 state에서는 Q value들의 차이가 Q value의 절대적인 값에 비해 매우 작다. 

                다시 말해, 조금의 noise가 선택되는 action을 바꿀 수 있다는 얘기

            이러한 상황에서는 업데이트할 때 끼는 작은 noise라도 학습 성능을 저하시킬 수 있다.
            
            반면에 Dueling 구조는 Q 값의 절대적인 크기에 해당하는 V(s)와 이들의 상대적인 차이인 Advantage (V-Q)를 분리해서 학습하기 때문에 
            보다 이러한 noise에 강건하게 학습된다. 


    
            
