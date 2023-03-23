### NoisyNetwork `2018 ICLR`

---

- `Policy space exploration`

        
            기존의 policy space 에서의 exploration인 soft-greedy policy 같은 방법은 단점이 존재한다.

                1. Heuristic한 방법 ----- 행동 선택의 기준이 brute-force style
                2. State-independant한 noise
                    즉, Epsilon의 확률로 랜덤하게 움직이는게 현재 상태와는 전혀 무관

                3. 일반적으로 neural network 기반 모델에서 policy space에서의 exploration은 환경과 더 많이 상호작용해야한다.

            하지만 With NoisyNetwork?

                1. Non-Heuristic
                2. State-dependant한 noise
                    즉, 현재 state에 어느정도 아다리가 맞는 noise를 제공해줌.            


            * Heuristic method for exploration 
            
                이 방법은 state space, action space가 작을 때에 그나마 쓸만하다.
                하지만 space size가 커지면 커질수록 되도 않는 선택을 할 가능성이 커지기 때문에 state-dependant한 noise가 필요


---

- `Noisy Network`


            * Noisy Network?

            Neural Network에 학습이 가능한 noise를 추가
 
                   At high level, Value function을 randomize하는 것 -> one of efficient exploration methods


            *즉, NoisyNetwork는 뉴럴 네트워크의 weight와 bias가 parametric noise로 인해 섭동되는 네트워크.

                이 parametric noise는은 GD로 loss function을 업데이트할 때 자동으로 같이 업데이트된다.

                    즉, 매 업데이트마다 달라지는 noise로 인해 보다 exploration이 다채롭다.

                    [In paper] 'this ensures that the agent always acts according to parameters 
                                that are drawn from the current noise distribution.' 
    

                    NoisyNetwork의 이러한 특성은 기존의 DQN에서 처럼 고정된 탐험 전략이 아니라,
                    어떤 문제를 푸느냐에 따라서 network가 problem-specific하게 exploration 전략을 만들어낸다!
<br>


            * 2 method for injecting noist to network

                두 방법 중에서 Computational cost를 고려해서 선택하면 된다.
                (Gaussian noise를 만들어내는 개수의 차이 -> 만들어 내는 양을 줄여 생성 시간을 줄이고 싶음.)

                1. Independent Gaussian noise (Basic method)
    
                    각 layer마다 pq + q 개의 noise 파라미터 생성
    
                2. Factorized Gaussian noise (Cheapter method)
    
                    각 layer마다 p + q 개의 noise 파라미터 생성
    
    

                
                

            
        


---

