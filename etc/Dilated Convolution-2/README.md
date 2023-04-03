## Dilated Convoluton

#### Dilated Convolution ?

일반적으로 Filter는 가중치가 나란히 붙은 형태로 한 덩어리를 이루고 있다.

<div align=center>

![image](https://user-images.githubusercontent.com/59076451/131523716-9c352479-4769-43a1-b448-41f19d72af53.png)
  
</div>  

Dilated Convolution (팽창된 Convolution)은 위와 같은 Filter 각각의 값을 사방으로 밀어서 팽창시키는 것이다!

    마치 풍선에 점을 찍어놓고 바람을 불어넣는 것과 같은 이미지
    
<div align=center>

![image](https://user-images.githubusercontent.com/59076451/131523944-f2a19ad1-a57f-4592-8ca5-ba037738a209.png)
  
</div>      
    
일반적인 Convolution과 달리 dilated Convolution의 Receptive Field는 D에 따라서 달라진다.

        첫 번째 그림은 D = 1로 , 3x3의 Receptive Field를 갖는 filter이다. 
        두 번째 그림은 D = 2로 , 5x5의 Receptive Field를 갖는 filter이다. 
        세 번째 그림은 D = 3로 , 7x7의 Receptive Field를 갖는 filter이다. 

---

#### Receptive Field

Receptive Field의 크기는 얼마나 많은 문맥 정보를 사용하는가? 를 의미한다. 

<br>

![image](https://user-images.githubusercontent.com/59076451/131524647-90b6eb63-ab82-481e-ae00-71140fdc8ae5.png)

첫 번째 그림은 Input 샘플의 간격이 r = 1 로 공간적으로 붙어있다. 즉, Receptive Field = 3x3 이다.

반면 두 번째 그림은 Input 샘플의 간격이 r = 2로 공간적으로 떨어져있다. 즉, Receptive Field = 5x5 이다.

        두 그림 모두 하나의 Output을 내기 위해 3개의 입력을 사용하는 것은 동일하다.
        하지만 더 많은 공간적인 문맥 정보를 사용할 수 있는 것은 두 번째 그림이다. 
        
        물론 첫 번째가 지역적인 특징은 더 잘 잡아낼 것이다. 하지만 문맥적, 전역적인 정보는 부족하다!
        
<br>

위 그림에서 Sparse feature extraction 그리고 Dense feature extraction에 대해서는 다음과 같이 이해할 수 있다.

작은 Receptive Field보다 큰 Receptive Field를 이용하면 같은 이미지 크기에 대해 더 많은 출력을 낸다. 즉, 출력 이미지의 크기가 더 크다. 

따라서 얻을 수 있는 데이터가 더 많다. 이를 Dense하게 특징을 추출한다고 표현한 것 같다. 

<br>

![image](https://user-images.githubusercontent.com/59076451/131525938-aa29c214-7afa-4d27-a308-9ef5c304599f.png)

<br>

아래쪽 네모의 중앙에 위치한 하나의 pixel 값을 추출하기 위해 Receptive Field가 서로 다른 4개의 Dilated Convolution이 사용된다. 

        일반적인 Conv보다 전역적인, 문맥적인 정보를 더 잘 잡아낼 것이다. 

---

<br>

#### Summary 


정리하자면 Dilated Convoluton은 Pooling을 이용하지 않고서 Receptive Field를 넓힐 수 있다.

      이는 곧, 전체적인 맥락, 문맥 정보를 잘 포착한다는 것을 의미하며 추가적으로 Spatial한 정보를 잃지 않고서 학습을 진행할 수 있음을 시사한다.

<br>

기존의 FCN, SegNet, U-net과 같이 Down - Up 과정을 거치면 Resolution을 효율적으로 복원할 수 없다. ( 해상도가 거칠어진다. )

하지만 Dilated Convolution을 이용하면 공간 정보를 유지한 채 학습을 진행하기 때문에 Resolution을 효율적으로 건져낼 수 있다. 

<br>

<div aling=center>

![image](https://user-images.githubusercontent.com/59076451/131526628-0f8b8ecb-49ff-4d54-93a7-78f522af2229.png)
  
상단의 중간에 껴있는 그림은 Filter이다. (빨간색, 파란색 Feature를 담고 있다.)
  
이를 Dilated 시킨 결과를 하단의 Filter에서 볼 수 있다. (파란색, 파란색 Pixel들이 팽창되어 있다.)  
  
</div>









        
        




    
