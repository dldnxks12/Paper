#### Deconvolution, what is it?

초기에는 CNN을 그대로 사용해서 Segmentation을 진행했다.

Window를 이용해서 모든 픽셀에 대해서 하나씩 차근차근 예측하는 것이다.

예를 들어 아래 그림과 같이 사각형 Window로 그림을 픽셀 하나를 중심으로 가지도록 한 칸씩 이동시킨다.

    If 중심 픽셀이 Cow위에 있다면 Cow, 잔디 위에 있다면 Grass로 분류 또는 예측된다.

    ! Computational cost가 매우 크다 또한 시간도 매우매우 오래 걸린다.
            
![image](https://user-images.githubusercontent.com/59076451/129017757-a225379b-8ddb-4689-b17d-aa8d2585554a.png)            

따라서 픽셀 하나씩 따로 예측하는 것은 매우 비효율적이므로, 한 번에 모든 픽셀의 클래스를 분류하는 방법을 고안한다.            

이 아이디어의 특징은, Conv Network를 통과할 때, padding을 이용해서 입력 이미지 사이즈를 계속 유지시킨다.

그리고 마지막 Layer에서는 FC 과정을 거치지 않고, 바로 C x H x W feature map으로 각각 픽셀 별로 바로 예측을 진행한다.

    물론 이 방법도 문제가 존재한다.

    Conv Net을 입력 사이즈를 계속 유지하면서 통과시키는 것이므로 매개변수 수가 기하급수적으로 증가한다.

    즉, Memory과 Computational Cost가 굉장히 커진다.

![image](https://user-images.githubusercontent.com/59076451/129017800-c4c66e34-5102-4292-b20b-2f2bf0e6a9bc.png)
            

그래서 나온 아이디어가 'Deconvolution'이다. 

    모든 픽셀들을 한 번에 예측하되, 사이즈를 안줄이면 문제들이 발생했지?
    그럼 일단 줄였다가 다시 복원시키자! 
    
![image](https://user-images.githubusercontent.com/59076451/129018598-3a1773ad-9f6d-4c48-8e64-21b433e465fb.png)
    
쉽게 말해서 기존 CNN과 비슷하게 Feature map을 구해내고, 나온 결과를 FC layer 대신 Deconvolution을 통해 입력 사이즈로 복원시킨다.

이 때, 앞서 축소시키는 과정과 대칭이 되도록 하는 것이 좋다.

이를 Upsampling이라고도 한다.

#### Deconvolution, go deeper

Deconvolution (Upsampling)에는 2가지가 있다.

1. Pooling layer를 복원하는 것 
2. Convolutional layer의 stride에 의한 축소를 복원하는 것 


