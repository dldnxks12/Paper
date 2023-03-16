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
                
<br>

---

- `Apply Neural Network to RL and it's solutions`

        
        data correlation과 non-stationary distribution 문제를 해결하기 위해 replay buffer를 사용한다. 
    
    
        1. data correlation 
    
            - replay buffer에서 random sampling을 통해 순차적 데이터들의 correlation을 부순다.
    
    
        2. non-stationary distribution
    
            - 서로 다른 policy들이 만들어낸 experience들을 써서 학습하므로, 학습하려는 distribution이 smoothing 된다.    
    
            
