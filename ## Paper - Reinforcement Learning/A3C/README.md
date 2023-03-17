### A3C `2016`

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

