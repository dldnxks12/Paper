## Dilated Convolution 

DeepLab Model을 공부하는 도중 가장 먼저 dilated Convolution과 CRF에 대한 내용이 눈에 띄었다.

CRF에 대한 내용은 조금 뒤로 미루고, 먼저 dilated Convolution에 대해서 공부해본다.

---

<br>

#### Receptive Field

먼저 Receptive Field다.

      Receptive Field란 Filter가 입력 이미지를 한 번에 보는 영역이다. 

      Filter를 통해 이미지의 전체적인 Feature를 잡아내기 위해서 Receptive Field는 크면 클수록 좋다.
      
<br>      
      
하지만 Filter의 크기를 키우면 그 만큼 연산량이 증가한다. 또한 Overfitting의 우려도 있다고 한다.

기존의 CNN에서는 Receptive Field와 연산량 사이의 Trade off 문제를 Pooling을 통해 해결했다.

      입력 이미지를 pooling을 통해 작게 하면, filter는 그 크기가 그대로기 때문에 상대적으로 Receptive Field는 점점 커진다.

<br>
      
하지만 Pooling을 수행하면 Feature의 손실을 피할 수 없다. 결국 버리는 데이터가 생기기 때문이다.

**이를 해결하기 위해 나타난 것이 dilated convolution이다!**

---

<br>

#### dilated convolution

<br>

<div align=center>

dilated Convolution ?
  
![image](https://user-images.githubusercontent.com/59076451/131513108-a805705a-1d20-461a-9476-520c5339cc71.png)
  
</div>  

      dilated convolution은 filter 내부에 zero padding을 추가해서 강제적으로 Receptive Field를 넓히는 방법이다.

이 dilated convolution으로 poolig을 수행하지 않고도 Receptive Field의 크기를 크게 가져갈 수 있기 때문에 Spatial 정보의 손실이 적다.

즉, Pooling을 하지 않아 공간적 특징을 유지하는 특성이 더 많다! 때문에 Segmentation에 사용하기 좋다.

또한 대부분의 Weight가 0이기 때문에 연산의 효율도 좋다. 


<div align=center>

![image](https://user-images.githubusercontent.com/59076451/131514935-68a27814-1160-42cb-a180-2dac2e5de1d2.png)
    
</div>  


위 그림을 보면 downsampling(pooling) - conv - upsampling(or unpooling) 하는 것과 dilated conv 하는 것의 차이를 볼 수 있다.
  
확실히 공간적 정보의 손실이 있는 것(Pooling)을 Upsampling하면 Resolution이 떨어진다.  

<br>
  
반면에 dilated Conv를 보자. 
  
Receptive Field를 크게 가져가며 convolution을 하면 공간적인 정보를 유지하면서(정보 손실을 최소화하면서) Resolution이 좋은 출력을 얻을 수 있다. 



---




