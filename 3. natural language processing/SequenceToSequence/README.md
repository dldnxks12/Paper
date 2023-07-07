### Sequence to Sequennce Learning with Neural Networks

---

#### Why not DNN? Why LSTM?
               
    DNN? labeling된 큰 데이터셋만 있으면 성능이 좋은데, 시계열 데이터는 잘 못다룬다.
    So, multi-layer LSTM 사용하는 방법을 제시
      -- 1. Input sequence를 LSTM으로 인코딩 
      -- 2. latent feature 추출 
      -- 3. LSTM으로 다시 디코딩 

      즉, 2개의 LSTM을 Encoder, Decoder 구조로 연결 

    - 긴 시계열 데이터도 문제없다. 
    - Input sequence를 뒤집어 넣은게 성능이 좋아졌다, time-lag 관련 

---

    DNN은 input - output의 dimension이 고정되어있다.
    그래서 질문-대답과 같은 sequence to sequence의 domain-independant하게 문제를 다룰 수 없다.
    이 문제를 여러개의 LSTM을 이용해서 해결할 수 있다. 
      - 즉, 입력과 출력 길이가 달라져도 문제없다.
    
    *Oh? How?

    1. 1개의 LSTM을 이용해서 Input sequence를 fixed-dimenstion의 vector로 바꾼다.
    2. 하나의 LSTM은 더 사용해서 이 fixed-dimension vector에서 model output을 낸다.

<div align = center>
  
![125725545-347c14a3-f0ce-4756-a75c-f82b70813c12](https://user-images.githubusercontent.com/59076451/126780457-f6e0b9a8-e8ed-48e2-9ca4-fb013084d2d0.png)

</div>    

---
    
#### Then why LSTM to LSTM? Why not just RNN or LSTM?


        RNN과 LSTM을 단독으로 쓸 때는 입력과 출력 차원을 알고 있어야한다.
        즉, 가변 길이 데이터에 대해서는 좀 어렵다.

        간단한 방법은 RNN 하나를 써써 입력 데이터를 fixed-size 벡터로 만드는 것.
        그리고 이걸 다시 다른 RNN을 통해 출력을 내는 것.

        But, 긴 입력 데이터에서는 RNN x -> LSTM이 성능 더 좋아 이걸로 선택.


---

#### Summary 

    1. 가변 길이의 데이터를 다루기 위해 DNN대신 두 개의 LSTM을 사용
    2. 문장을 시작과 끝을 구분할 수 있게 하기 위해 SOS, EOS Token을 사용
    3. RNN은 긴 Sequence에 대해 Long-term Dependency 문제 발생, So LSTM을 사용해서 Encoder + Decoder 설계
      - Encoder에서 입력받은 문장의 Latent Vector를 Decoder로 넘겨주는 과정

    # Design tips
    1. 입력과 출력에 서로 다른 LSTM을 사용
    2. shallow LSTM <<< deep LSTM! --- 4 layer로 구성
    3. Input sequence 뒤집어서 입력한다.
      -입력 문장을 뒤집어도 Source와 Target사이의 거리 평균은 동일하게 유지되지만 minimal time lag가 줄어들기 때문에 성능이 향상된다.

---




