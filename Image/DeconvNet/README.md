## DeConvNet for Semantic Segmentation

  DeConvNet은 Convolution Network와 Deconvolution Network로 구성되어 있다.
  
  사실 SegNet, U-Net과 비슷한 Encoder Decoder 구조라고 생각해도 된다. 
  
  DeConvNet, SegNet, U-Net 모두 FCN에서 시작된 모델이다.
  
  ---
  
  #### Why DeConvNet?

  DeConvNet은 FCN의 문제점을 보완하기 위해 등장한 모델이다. 

  FCN은 Receptive field가 고정되어있어서, 모델이 하나의 Scale의 이미지만 다룰 수 있다. 
  
  즉, Receptive field 보다 작거나 큰 객체는 잘못 labeling되거나, 잘게 쪼개지는 문제가 발생한다. 
  
      1. 큰 객체가 작은 객체 여러 개로 쪼개지거나
      2. 작은 객체는 무식되거나 배경으로 인식될 수 있다.
      
      이 문제를 해결하기 위해 Coarse data의 Resolution을 높이는 Skip Connection 기법을 사용했지만 근본적으로 문제를 해결하지는 못함       

<div align=center>

![image](https://user-images.githubusercontent.com/59076451/130635553-9cac87a4-33c1-4ba8-971e-70333f6ea9ea.png)

</div>

---

#### DeConvNet

<div align=center>

![image](https://user-images.githubusercontent.com/59076451/130645127-02a9e9c8-3130-40a5-a81e-5acea562679e.png)
  
</div>

DeConvNet은 conv network, deconv network로 구성된다. 

convolution part는 입력 이미지에서 feature를 추출하고, deconvolution part는 convolution이 추출한 특징에서 segmentation을 진행한다. 

convolution part에서는 VGG-16과 같은 모양이고 마지막 fc layer를 제거해서 사용한다. 

    주의할 점은 fc layer를 모두 제거하는 것이 아니라, 3개의 fc layer 중에서 1개만 제거하는 것
    
    fc layer를 모두 제거해서 사용한 것은 SegNet이다.
    
즉, Conv Net - fc layer -fc layer - DeConv Net 의 구조를 하고 있다. 

---

#### Deconvolution Part

Deconvolution Part에서는 Convolution을 통해 줄어든 이미지를 다시 복원하는 과정이다.

이에 UnPooling과 Deconvolution 연산을 수행한다.

    UnPooling은 Pooling을 통해 줄어든 것을 복원하는 연산이고, Deconvolution은 Convolution의 Stride에 의해 줄어든 것을 복원하는 연산이다.
    
---    
    
#### Image Reconstruction 


Convolution과 Pooling으로 인해 줄어든 이미지를 다시 복원하는 방법으로는 위에서 언급한 것과 같이 Deconv와 Unpooling이 있다. 

이 둘의 차이는 아래 그림과 같다.

<div align=center>
  
![image](https://user-images.githubusercontent.com/59076451/130649256-d98e5538-309f-49a5-b439-d8ffe3c63b4d.png)
    
</div>  

UnPooling 

    Unpooling의 경우 여러 가지 Type이 있지만, 주로 Pooling시 해당 Index를 기억해두고, Unpooling 과정에서 기억해둔 Index에 대해 값을 복원시킨다.

    값이 복원된 결과는 0으로 된 빈 공간이 많은데, 이런 경우 data가 sparse해서 학습에 어려움이 있다. 

    이 문제를 해결하기 위한 방안으로 Unpooling 후 일련의 Conv 연산을 통해 Dense한 Data로 만들어주는 방법이 있다. 

Deconvolution 

    Deconvolution의 경우 Sparse Transposed matrix를 사용하여 stride로 인해 줄어든 Image를 복원한다. 자세한 사항은 Deconvolution 글을 참고 

---

#### Visualize Deconvolution 


<div align=center>    
  
![image](https://user-images.githubusercontent.com/59076451/130651193-4f5ba9f0-f6ce-45ca-8b53-42da5d92a7fe.png)

</div>  

Deconvolution Network의 수행 결과를 찬찬히 뜯어보자

위 그림은 deconv network의 layer들을 시각화한 그림이다. 

(b) 그림은 deconv net으로 들어가는 이미지이다. 

(c) 그림을 (b) 그림과 비교해보면, 객체가 여러 조각으로 나눠어 크게 퍼진 것 같은 느낌을 받는다.

이 그림의 결과는 Unpooling이며 크기를 2배로 키우고, 이전 Pooling과정에서 저장해둔 Index에 맞게 복원한 결과이다. 

따라서 해당 Index에 맞게 feature들이 산개되있는 것을 볼 수 있다. 이 sparse한 이미지를 일련의 Conv layer를 거쳐 (d)의 이미지를 얻는다.

(d) 이미지로부터 Unpooling을 통해 (e) 이미지를 얻는다. (b) -> (c)와 같은 개념으로 feature들이 가장 두드러지는 feature를 갖고 고르게 산개된다.

결과적으로 (j)를 보면 feature들이 잘 복원된 것을 확인할 수 있다. 
    
---

#### FCN vs DeConv

<div align=center>

![image](https://user-images.githubusercontent.com/59076451/130652662-1f78870c-affb-4e5a-a4dd-09c1947c3972.png)


DeConv architecture  
  
![image](https://user-images.githubusercontent.com/59076451/130654129-964ce570-8c2f-4aa1-b947-fe3d4d0a319f.png)
    
</div>  



