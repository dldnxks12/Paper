### Offline RL overview

ref : https://talkingaboutme.tistory.com/entry/RL-Offline-Reinforcement-Learning

---

Offline Reinforcement Learning : 환경과의 상호작용 없이 정해진 배치만큼의 데이터만 가지고 Agent를 학습시키는 방법

즉, `고정된 데이터셋`을 가지고 `최대한으로 Exploitation`을 하겠다.

    - No exploration 
    - No interaction with Environment

---

Exploration 없이 고정된 데이터셋을 이용해서 학습한다는 점에서 `Imitation Learning과 유사`하다.

하지만 Offline RL과는 다음과 같은 차이점이 있다.

    - IL 관련 문제는 optimal하거나 적어도 전문가 급 성능을 내는 데이터가 있다고 가정
        but, offline RL은 suboptimal한 데이터만 다루는 환경을 가정

    - 대부분의 IL 문제는 reward function이 없다. 
        but, offline RL은 reward function을 고려한다.

    - 일부 IL 문제는 전문가와 비전문가를 구분할 수 있는 label이 필요
        but, Offline RL은 이를 고려하지 않는다. 

    - Offline RL은 주로 off policy Deep RL 알고리즘으로 구성. 

결국 Offline RL은 주어진 데이터에 대해 Optimal policy를 찾는 문제.

IL 에서는 전문가의 성능을 넘어서는 결과를 보여주기 어렵지만, Offline RL에서는 이를 해낼 가능성이 있다.




