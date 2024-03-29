### Deep Q-Network `2013`

---

- `DQN`

    
        - 처음으로 High dimensional, law sensory input을 바로 사용해서 학습한 알고리즘
    
            -> 기존에 High dimension data에서 잘되었던 RL은 사람이 직접 뽑아낸 feature로 구성된 linear function으로 해결했다.
                ( V(s) = w1x1 + w2x2 + ... ) 
    
                - 사람이 어떻게 feature를 뽑아내는지에 따라 성능이 천차만별
                - 하지만 현재, Neural Network가 이 feature를 뽑는데 아주 똘똘하다.
    
                    -> high dimensioanl feature를 Neural Network를 통해 뽑아보자. 
    
        - Non-Linear FA (CNN) + TD(Q Learning) + Off policy
    
            -> 이론적으로 아직 Convergence 보장 안되지만, 실험적으로는 모두 다 잘됬다.
                ( Linear FA + TD(Q Learning)  + Off policy = may diverge )
                ( Linear FA + GTD(Q Learning) + Off policy = converge ) 
    
            -> Off policy
                - experience를 만들어 내는 policy : behavior policy
                - replay buffer에 있는 experience들로 학습하는 policy : target policy 
        

        - Target Network  

            -> Double Sampling issue OK
            -> Smoothness issue OK

<br>

---

- `Apply Neural Network to RL and it's problems`

    
        High dimensional data에서 feature를 잘 뽑아낸다니, RL에 적용하지 않는게 더 이상하다. 
        하지만 여기에는 몇 가지 문제가 있다.
    
        1. Neural Network는 고정된 분포를 학습하는 모델이다. 
    
            - 하지만 RL은 Policy를 Update하고 Q 값을 평가하는 Iteration으로 Optimal value로 Convergence하는 학습 방식을 취한다.
                -> 즉, Neural Network이 학습하는 분포가 매 Iteration 마다 달라진다. 
                
                    PE -> PI -> PE -> PI -> ...
                
    
        2. Neural Network input data들은 모두 independant 함을 가정한다. 
    
            - 하지만 RL의 state sequence들은 서로 강한 correlation이 존재한다. 
                (전자렌지 돌리기 : 손을 올린다 -> 버튼을 누른다 -> 타이머를 돌린다 -> 시작 버튼을 누른다 ...)
                (correlation은 학습 variance를 높이는 문제가 있다.)
    
    
        3. 대부분의 성공적인 Deep Neural Network는 많은 양의 labeling된 훈련 데이터가 있다.
    
            - RL은 sparse하고, delay 되고, 심지어 noise도 껴있는 reward를 통해 학습해야한다.
                

        4. Problems in updating function approximator

            - Double sampling issue & Smoothness issue 
<br>

---

- `Apply Neural Network to RL and it's solutions`

        
        data correlation과 non-stationary distribution 문제를 해결하기 위해 replay buffer를 사용한다. 
    
    
        1. data correlation 
    
            - replay buffer에서 random sampling을 통해 순차적 데이터들의 correlation을 부순다.
    
    
        2. non-stationary distribution
    
            - 서로 다른 policy들이 만들어낸 experience들을 써서 학습하므로, 학습하려는 distribution이 smoothing 된다.    
    
            
<br>

---

- `Double Sampling issue`

        Value function approximation 

        J(W) = E[ (Vπ(s) - Vw(s))**2 ]

        하지만 보통 Vπ(s)를 모르기 때문에, MC or TD방법으로 대체한다.

        MC : J(W) = E[ (Gt - Vw(s))**2 ]
        TD : J(W) = E[ (R + r*Vw(s') - Vw(s))**2 ]

<br>

<div align="center">

`Objective function of value function approximation`

![img.png](img.png)


        이제 이에 대한 Gradient를 계산해서 W를 업데이트한다.

            W = W - a*∇J(W)

![img_1.png](img_1.png)


        하지만 위 식을 풀어 보면, 두 개의 Expectation의 곱을 포함하게 된다. 



![img_2.png](img_2.png)

</div>


<br>

        이게 왜 문제가 될까?

        X와 Y가 독립일 때, E[X]E[Y] = E[XY] 가 성립한다.

<div align="center">

![img_3.png](img_3.png)

</div>

        Sampling을 통해 위 식에서 unbiased stochastic approximation을 얻으려면,
        우리는 s' ∼ p(·|s, a) and a ∼ π(s)를 따르는 분포에서 두 개의 독립적인 샘플을 뽑아야한다.
        
            -> E[X]의 sample을 X, E[Y]의 sample을 Y라고 할 때, E[X]E[Y]의 sample이 X*Y 임이 보장될까?
               만약 독립이라면 E[X]E[Y] = E[XY]이기에 E[X]E[Y]의 sample이 X*Y 임이 보장된다.
               따라서, 독립이 아니라면 bias가 생긴다.

        실제로, 같은 state에서 두 개의 독립적인 Sample을 뽑기는 상당히 어렵거나 비효율적이다.
        이 double sampling issue 때문에, 일반적으로 gradient algorithm이나 bellman error의 loss function으로 value function을 구하는게 어렵다. 

<br>

---
- `Double Sampling issue & Smoothness issue in DQN and it's solution`

        DQN은 Q-Learning을 베이스로 Q function을 업데이트한다.

<div align="center">

`Without target network`

![img_4.png](img_4.png)

</div>

        Target Network를 도입하지 않았을 경우 두 가지 문제가 발생한다.

        1. Double Sampling issue 
        2. Smoothness issue : Objective function 내부에 max operation은 미분이 불가

<div align="center">

`With target network`

![img_5.png](img_5.png)

</div>

        Target Network를 도입하였을 경우, 

        1. Gradient 계산 시 Expectation이 1개만 생긴다 -> Double sampling issue X
        2. ~ max(Q_target) - Q의 미분에서 target network는 무관하기에 미분이 가능해진다. -> Smoothness issue X


<div align="center">

![img_6.png](img_6.png)

![img_7.png](img_7.png)

</div>