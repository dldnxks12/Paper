## Hidden Markov Model

      Markov Chain은 모든 State에 대해 관찰이 가능한 시스템이다.
      
          * 1차 Markov Chain은 모든 State를 다 볼 필요는 없고, 그 이전 State만 들여다 볼 수 있으면 된다 
          * 2차 Markov Chain은 모든 State를 다 볼 필요는 없고, 그 전과 전전 State만 들여다 볼 수 있으면 된다 !
      
      하지만 Hidden Markov Model은 모든 State가 아니라, 그 중 일부 State만 들여다 볼 수 있을 때 사용하는 모델이다!
      
[참고 링크 1](https://sanghyu.tistory.com/17)      
      
<br>

- Hidden Markov Model


      Hidden은 Markov Chain에서의 State가 숨겨져있다는 것을 의미한다

        1차 Markov Chain을 예로 들어보자.

        우리가 다음 State를 예측하고 싶어서 지금의 State를 들여다보아야하는데, 이 State들이 일부 숨겨져 있는 것이다..
    
