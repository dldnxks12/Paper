### A3C `2016`


---
- `A2C / DQN / A3C`


        * A2C
        
            Actor-Critic 알고리즘
                Actor  : PG update 
                Critic : TD update

            Sample correlation 문제 (On policy)-> 복잡한 문제 X
            Policy gradient -> 유연한 학습 O

        * DQN

            PE : Value Function Approximation with Q-Learning 
            PI : Soft greedy policy 

            Replay buffer  -> Sample correlation 해결 (Off policy -> Sample efficient)
            Target Network -> Double sampling issue, Smoothness issue 해결 
            Penelty -> Expensive Memory Capacity, Slow learning speed   
    
        * A3C
            
            Actor-Critic + Multi threading 

            Sample correlation 문제 (On Policy) -> Thread 를 replay buffer 대신 사용 
                -> thread를 사용하므로, replay buffer를 (off policy) 꼭 사용하지 않아도 된다.)

            Add entropy to Objective function J(θ) for better exploration

---

- `Asynchronous RL`

        
            일반적으로 process의 수가 많아질수록 data efficiency, training stability가 줄어든다. 


            * Why does sample efficiency & training stability diminishes as the degree of parellelism increases?

                - Sample efficiency : 

                    Sample efficiency는 제한된 데이터에서 모델이 얼마나 학습을 할 수 있는 지에 대한 능력을 말한다.
                    가진 데이터 내에서 뽑아낼 수 있는 pattern or distribution은 제한적이므로, 
                    어느 수준 이상의 process 수는 불필요하게 된다.

                    또다른 관점에서 보면 Correlated sample이 문제다.
                    각 Worker가 뽑아내는 sample들은 사실상 모두가 다 독립적이지는 않다. 
                    같은 구조의 환경 내에서 무수히 많은 Worker가 sampling을 하게 되면 Sample들의 일정 부분은 비슷한 feature을 갖는다.  
                    즉, Worker의 수를 늘릴수록 이들이 가져오는 Sample들 중 서로 독립적이지 않은 정보의 비중이 점점 커지게 된다.   

                - Tranining stability :

                    Training stability는 학습 과정에서 지속적으로 좋은 solution으로 모델이 수렴해가는 능력을 말한다.
                    학습을 수행하는 Worker가 많아지면, 각각의 Worker가 독립적으로 모델 파라미터를 업데이트한다.
                    
                    여기서 문제가 조금 생기는데, 각각의 Worker가 보는 model update 방향이 다를 수 있다. 
                    즉, 각자가 가져간 데이터를 보고 gradient 계산을 수행하는데, 서로 판단한 업데이트 방향이 다를 수 있다는 말.
                    이게 모델 업데이트에서의 inconsistency로 이어진다.  

                    결과적으로 모델 converge가 느려지거나, 학습 불안정으로 이어진다. 


            * How to solve it?


                1. Increasing batch size -> 각자가 가져가는 data 양을 늘리기
                2. Learning rate tuning 
                3. Implement Synchronize -> 주기적으로 Worker들끼리 동기화 시켜주기 

---

- `A3C`


            
            1. Gorila framework와 같이 asynchronous actor-learner를 사용한다. 
            
               ->  대신 Gorila는 여러 대의 PC, parameter 서버를 사용한 것에 반해, 
                A3C는 한 대의 PC에서 CPU의 mutli thread를 이용해 학습을 수행한다. 


            2. Worker들이 observation을 각자 환경의 각각 다른 부분을 탐험하면서 얻도록 한다.
               또한, 각 Worker마다 다른 exploration method를 적용해서 탐험의 다양성을 높일 수 있다.
                
                -> 시간적으로, worker들이 가져오는 데이터들이 1개의 agent가 가져오는 데이터 보다 uncorrelate하게 한다. (Under on policy)  
                -> data correlation을 끊기 위해 replay buffer를 쓸 필요가 없다. 


            3. Off policy로 학습하지 않아도 되니, 학습이 보다 더 안정적이다. 


---

- `Adding Policy Entropy to Objective function J(θ)`



            A3C paper에서, 목적 함수 J(θ)에 policy의 entropy term을 추가하는게 exploration을 강화한다고 말한다.

                ->  policy의 Entropy는 곧 policy의 불확실성의 정도이다.
                    높은 Entropy를 가진 policy는 agent가 조금 더 random한 action을 할 가능성이 많다는 걸 의미한다.
                    반대로 낮은 Entropy를 가진 policy는 agent가 보다 deterministic하게 행동할 가능성이 많다는 것이다.

            J(θ)에 entropy term을 추가하게 되면서, 학습은 policy가 더 높은 entropy를 갖도록 만든다.
            
                -> 곧 더 exploration을 많이 하도록 장려하는 것.

            Entropy term에 hyperparameter를 추가해서 A3C 모델이 exploration-exploitation trade off 문제를 적절히 조절하게 해준다.
    