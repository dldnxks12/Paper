## Fully Convolutional Networks for Semantic Segmentataion `8 March 2015`

---

### 요약 

1. Semantic Segmentation은 Coarse부터 Fine까지 inference를 통해 모든 픽셀에 대해 Class를 분류하는 것이다. 

2. Semantic Segmentation은 Globally and Locally 각각의 기능을 할 수 있다.

        Globally : What
        Locally  : Where

---

**CNN 구조로 Segmentation를 수행하지 않는 이유**
    
    1. CNN의 경우 입력 이미지의 크기를 멋대로 정할 수 없다.
    
        Convolution 연산은 그 크기가 얼마든 상관없지만, 문제는 FC layer에서 발생한다.

        FC layer는 크기가 고정되어있기 때문에, 입력 이미지의 크기가 들쭉날쭉하면 사용할 수 없다.
        
        
    2. CNN의 FC Layer에서 Spatial information이 사라진다.
    
        기존의 MLP에서 CNN 구조로 넘어가게 된 이유 또한 Spatial data를 최대한 유지하기 위해서이다.
        
        하지만 Segmentation은 Pixel마다 분류를 해주어야하기 때문에 마지막까지 그 위치에 대한 정보를 가지고 가는 것이 중요
        
        따라서 FC layer를 삭제하고, 마지막 단 까지 Convolutional Layer를 붙인 것이 바로 FCN이다.
            
---            
                
**FCN은 CNN의 FC layer를 1x1 Convolution layer로 대체한 구조**

![image](https://user-images.githubusercontent.com/59076451/129008945-81d615cb-2022-475f-877a-a71e345e1309.png)

    기존의 Convolutional Layer Part에서 feature map을 추출한 것을 1 차원 Tensor로 만들지 않는 것을 확인할 수 있다.
    
    대신에 1x1 Conv Layer로 대체되었다. 
    
    위의 결과로 사진 내의 물체가 고양이라는 것, 그리고 그 위치까지 동시에 파악할 수 있다.
    
    이는 1x1 Conv layer의 결과가 아직 2차원 이미지 정보를 담고 있기 때문에 가능한 것이다.

---

**Why 1x1 Conv?**

그렇다면 왜 하필 1x1 Conv를 사용하나?

    보통 Convolution 연산은 관련된 위치 정보상의 특징 or 패턴을 뽑아내기 위해 사용한다.
    
    이 연산을 통과해서 크기를 줄이고, 앞 단의 이미지의 특징만 뽑아낸 feature map을 만들어낸다.
        
    보통의 연산은 (2 x 2) 크기 이상의 Receptive Field를 가지고 수행된다. 그래야 이미지의 크기를 줄이며 특징 추출이 가능하다.
    
    하지만 여러 논문에서 (1 x 1) 크기의 Convolution을 사용한다.
    
        이러한 Convolution은 본래의 기능보다는 차원 축소에 초점을 맞춘 구현이다 !
    
    이는 이미지의 크기는 (1 x 1 )크기 filter를 사용하여 유지하면서, filter의 개수를 이용해서 이미지의 차원을 줄이는 것이다.
    
    즉, 학습해야 하는 파라미터 수를 줄여서 네트워크를 효율적으로 학습시킬 수 있도록 하는 기능도 있다.

1. input 크기와 그에 상응하는 output 크기를 효과적인 추론과 학습과정을 가지고 만들어낼 수 있다.
    
2. FCN 내부에 VGG, AlexNet, GoogLeNet을 전이학습의 용도로 사용함    

---

**Heatmap 과 Upsampling**

위의 구조를 통해 만든 2차원 상의 분류 정보 + 공간 정보를 모두 갖고 있는 이미지를 Upsampling(해상도 복원)해서, 

원래 이미지 해상도에서의 Segmentation을 수행하겠다는 아이디어

- FCN은 CNN과 출력이 다르다.

        어떤 클래스에 대한 분류 점수가 아니라, '2차원 이미지 상의 분류 점수 맵'이 나온다.
        이 맵을 'HeapMap'이라고 한다.
        
![image](https://user-images.githubusercontent.com/59076451/129014015-7b681afa-bc17-49aa-8a99-baa6ae43382b.png)

- HeapMap

        최종 feature map 내의 특정 픽셀이 의미하는 물체가 뭔지에 대한 분류 점수를 feature map에 맞춰서 표현한 Map이다.
        
        위의 사진과 같이 feature map에서 'Tabby Cat'으로 분류된 픽셀과 그 위치를 잘 표현하고 있는 걸 볼 수 있다. 

        HeapMap은 원본 이미지 내 물체의 종류와 그 위치를 대략적으로 알고 있다.
        
        하지만 해상도가 너무 낮아, 정확한 Segmentation이 힘들다. 따라서 Deconvolution연산을 기반으로 Upsampling을 구현한다.
   
---   
   
**Deconvolution**

Deconvolution은 Convolution의 역이라고 생각하면 된다.

32 Stride의 Convolution이 32개의 Pixel을 1개의 feature로 만드는 작업이다.

반면 32 Stride의 Deconvolution은 1개의 feature로 32개의 Pixel을 만들어내는 작업이다.

            논문에서는 1/32 Stride Convolution이라고 표현하기도 했다. 


---

**Skip Connection**

논문에서는 Upsampling을 이용하여 원 이미지의 해상도를 복원하기 위해 Skip Connection 기법을 사용한다.

Skip Connection 기법은 이전의 Pooling layer에서의 출력(예측)을 이용해서 해상도 퀄을 올려보자는 아이디어이다.

전체적으로 Encoding 과정은 VGG와 같으며, 각 Layer를 거치가며 해상도는 1/2로 감소한다.

원본 이미지는 Convolution Network (Conv + Pool)를 거치며 점점 작아지며 결과적으로 HeapMap(feature map)이 된다.

        즉, Heat Map을 구하는 과정에서 해상도가 감소한다!

            하나의 Pixel이 여러 Pixel들의 특징들로 짬뽕됨
            
이를 다시 원래 이미지 크기로 복원하기 위해서 Upsampling을 진행하는데, 해상도를 효율적으로 복원해야한다.
    
        다시 복원하는 과정에서 짬뽕된 feature를 원래 자리로 잘 돌려보내는 것이 관건이다.
    
        이 해상도 복원의 성능을 높이기 위한 방법이 바로 Skip Connection이다!  

![image](https://user-images.githubusercontent.com/59076451/129041356-30734825-1f87-476b-8359-e4d8add5f839.png)

Conv 6, 7은 기존 FC layer를 Conv layer로 바꾼 것이고, x32, x16, x8, x4, x2 들은 Deconvolution의 stride를 의미한다.

feature map이 겹쳐있는 것은 덧셈을 의미한다.

        fcn32 : pool5
        fcn16 : pool5 + pool4 
        fcn 8 : pool5 + pool4 + pool3

Pooling을 반복할수록 지역적인 위치 정보가 사라진다.

따라서 현재 layer에서 Upsampling한 결과와 이와 대응되는 지역 정보를 가지고 있는 Pooling layer에서의 출력 결과를 이용하면 더 정확한 예측이 가능할 것이다!
                
---    
    
**Training**

Cost function : Train 과정에서는 Pixel 단위의 Multi-Class Logistic Loss를 사용한다.

        즉, 각 Pixel 마다 Softmax를 적용했다는 것
        
Optimizer     : SGD with Momentum을 사용        
    

