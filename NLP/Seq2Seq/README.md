### Seq2Seq Learning with Neural Networks


#### Abstract

- DNN을 보완
- 크기가 고정된 입력에 대해서만 데이터를 처리할 수 있었지만, 이제 가변 길이에 대해서도 다룰 수 있게 됨
- 2개의 LSTM을 Encoder 그리고 Decoder 구조로 연결 
- 입력을 Reverse하게 배치해서 넣어주면 더 좋은 성능을 보임

#### Introduction

- 가변 길이의 데이터를 다루기 위해 DNN대신 두 개의 LSTM을 사용
- 문장을 시작과 끝을 구분할 수 있게 하기 위해 SOS, EOS Token을 사용
- RNN은 긴 Sequence에 대해 처리하는 과정에서 Long-term Dependency 문제가 발생하기 때문에, 이를 대신하여 LSTM을 사용하여 Encoder , Decoder를 구성한다.
- 추가적으로 입력과 출력에 서로 다른 LSTM을 사용하고, 4 layer로 구성한다. 또한 입력의 순서를 뒤집어서 입력한다.<br>이는 입력 문장을 뒤집어도 Source와 Target사이의 거리 평균은 동일하게 유지되지만 minimal time lag가 줄어들기 떄문에 성능이 향상된다고 논문에서는 예측한다.

![125725545-347c14a3-f0ce-4756-a75c-f82b70813c12](https://user-images.githubusercontent.com/59076451/126780457-f6e0b9a8-e8ed-48e2-9ca4-fb013084d2d0.png)

#### Experiment

- 모델 학습은 Beam Search Algorithm을 통해 진행한다.
- Sequence를 Forward 방향 보다 Reverse 로 넣는 것이 더 성능이 좋다.
- 문장을 역방향으로 넣을 때, Minimal Time lag가 줄어든다는 결과를 보인다.

![125731919-f7ef77a3-3544-41d7-8789-eef0e0df8f5c](https://user-images.githubusercontent.com/59076451/126780451-eb037ad6-ccbe-4b48-85c8-007d17efc236.png)


