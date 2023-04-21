## U-net

U-net은 의학 분야에서 이미지 분할 목적으로 제안된 end to end 방식의 FCN 기반 모델이다.

FCN - DeconvNet - SegNet - U-net 순서로 공부하였고, 실제로 이런식으로 발전이 이루어져왔다.

위 모델들은 모두 FCN의 뼈대를 가지고 있으며, Deconv , Segnet, U-net은 모두 Encoder - Decoder 구조를 가지고 있다. 

<br>

#### What's Better?

FCN에서 발전된 U-net은 어떤 부분에서 기존 모델보다 좋은 성능을 보이나?

1. End-to-End 연산 속도 (window method to patch method)
2. Global Conxext 인식과 Localization 간의 trade off를 해결 

<div align=center>
  
![image](https://user-images.githubusercontent.com/59076451/130658323-dbd1653d-bd9b-40a5-89b0-6480ba276aa2.png)
  
</div>  

U-Net은 이미지의 global context 정보를 얻는 Contractring path (Convolution network)

그리고 정확한 Local 정보를 얻는 Expanding path (Deconvolution network)로 구성되어 있다. 

<br>

#### Idea of U-Net

      1. 속도 향상  
      
        Sliding window 대신 Patch 사용 

      2. Trade-off : 
      
        Conv net에서는 이미지 Context를 포착한다. 
        그리고 Deconv net에서는 feature map을 Upsampling한 뒤 Conv layer에서 포착한 context와 결합하여 Localization의 정확도를 높인다.

---

<br>

## Architecture 

#### Contracting Path

    입력 이미지로 부터 Global Context feature를 뽑아 내는 과정 

- 3x3 conv를 2번 씩 반복 (No padding 이기 때문에 이미지 사이즈가 점점 작아진다.)
- Activation fucntion : ReLU
- 2x2 max Pool with stride 2 
- Down-Sampling 할 때마다 Channel을 2배로 늘림 (VGG Architecture와 동일)

#### Expanding Path

    Contracting path로 부터 온 feature에서 더 높은 Resolution의 Segmentation을 얻디 위해 Up-Sampling하는 과정 
    
    즉, Carse Prediction to Dense Prediction

- 2x2 deconv (Up sampling)
- Upsampling후 Sparse data에 대해 3x3 conv를 2번 씩 반복 (Sparse data to Dense data)
- Upsampling 마다 channel을 2배로 줄임
- Activation function : ReLU
- Upsampling된 feature map은 짝을 이루는 Contracting path에서 넘어온 crop된 feature map과 연결됨 (Concatenate)
- 마지막 layer에서 1x1 conv 연산으로 output class matching 

<br>

U-Net은 위의 구조로 총 23개의 layer를 갖는다. 

!주목할 점은 최종 출력 Segmentation map의 크기가 입력 이미지보다 작다는 점이다.

    Conv layer에서 padding은 사용하지 않았기 때문

<br>


#### Coarse Map to Dense Prediction?

FCN에서와 같이 단순히 heap map을 upsampling하여 segmentation을 진행하면 segmentation된 결과가 매우 Coarse하다 (뭉태기)

이를 해결하기 위해서 FCN에서는 Skip Connection을 이용해서 Output Segmentation Map의 Resolution을 높였다.

U-Net에서도 또한 Resolution을 높이기 위해 Up-Samping + Skip Connection 방법을 사용한다. 

<div align=center>
  
![image](https://user-images.githubusercontent.com/59076451/130670684-7162f666-35cb-469f-b399-0ed3113af97d.png)
  
</div>  

위와 같이 계층적인 feature들을 Skip Connection을 통해 서로 결합함으로써 Global Context와 Localization의 trade off를 해결한다.

<br>

#### Overlap-tile

FCN 구조의 특성상 입력으로 들어오는 이미지 크기의 제약이 없다.

따라서 U-net은 만일 굉장히 큰 이미지가 들어왔을 경우 이미지 전체를 모델에 넣어주기보다 작은 크기의 Patch 단위로 살펴보는 방식을 사용한다.

Patch/tile 방법을 쓰면 속도 향상에 있어 이점을 갖는다. 

sliding은 이미지를 중첩해가며 feature를 뽑아내는 반면, Patch 방법은 이미 훑어본 영역은 깔끔히 넘기고 다음 Patch를 탐색하므로 속도 면에서는 일단 월등히 빠르다.

또 하나의 중요한 포인트는 이렇게 작은 단위로 나누어 이미지를 살펴보는 것은 data augmentation의 효과를 낼 수 있다.

데이터의 양이 매우 적은 Biomedical 분야에서 특히 빛을 발한다.

<div align=center>

Patch/tile vs sliding window  
  
![image](https://user-images.githubusercontent.com/59076451/130672529-e5b1e8ee-cb3d-4d4c-8223-3b31428b6a78.png)
  
</div>  


#### Mirror padding

mirror padding은 말 그대로, 이미지의 줄어든 부분을 mirror해서 padding을 처리해주는 것이다.

U-net은 padding을 사용하지 않아 conv layer를 거칠수록 이미지가 작아진다. 또한 출력 결과도 입력이미지와 같지 않다.

Patch 단위로 이미지 Convolution을 수행할 때 Padding을 사용하지 않았기 때문에 단순히 크기가 작아진 것이 아니라, 외곽부분이 잘려나간 형태가 된다. 

<div align=center>

![image](https://user-images.githubusercontent.com/59076451/130673775-bf2217bd-b1e3-4218-802a-4a3b253e0c08.png)

</div>  
  
위 그림과 같이 파란색 영역을 넣어주었지만, 결과적으로 노란색 영역이 나오게된다. 

따라서 이미지 경계 부분 Pixel에 대한 Segmentation을 위해 0이나 임의의 Padding value를 사용하는 대신 이미지 경계 부분의 이미지를 미러링한 Extrapolation 기법을 사용한다. 

<div align=center>  
  
![image](https://user-images.githubusercontent.com/59076451/130674079-b3f15da5-8d57-45d2-a224-718f177bb689.png)

</div>  


    


- 참고 

https://m.blog.naver.com/9709193/221979612209 <br>
https://medium.com/@msmapark2/u-net-%EB%85%BC%EB%AC%B8-%EB%A6%AC%EB%B7%B0-u-net-convolutional-networks-for-biomedical-image-segmentation-456d6901b28a

