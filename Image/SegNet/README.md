### Before SegNet ... UnPooling vs UpSampling

- UnPooling

    Pooling layer에 의해 축소된 이미지를 복원하는 것 
    
    [Unpooling - pytorch](https://pytorch.org/docs/stable/generated/torch.nn.Upsample.html)
           
- UpSamping

    Conv layer의 stride에 의해 축소된 이미지를 복원하는 것 
    
        - transposed sparse matrix 사용해서 복원 (torch.nn.convTrans2d ~)

<div align=center>

![image](https://user-images.githubusercontent.com/59076451/130321124-acdc895f-5bf0-424e-b381-3afd3bf75364.png)
  
fcn에서는 앞 단에서 저장해둔 각 layer의 heap map과 decov한 결과를 합하여 resolution을 높였다.
  
SegNet에서는 Pooling 과정에서 Max Index를 기억하고, 단순히 Un-Pooling과정을 통해 resolution을 높인다.  
  
</div>  

**개인적인 생각으로, Un-Pooling결과로 나온 Sparse한 데이터를 일련의 Conv layer를 통과시켜 Dense한 data의 형태로 바꾸는 것이 아닌가 싶다**


[More Info](https://analysisbugs.tistory.com/104)

--- 

#### UnPooling (Un-maxpooling)의 장점

    boundary delineation(묘사) 측면에서 성능이 좋다. (강한 자극을 받은 Pixel에 대해서 복원을 진행하기 때문에 Edge와 같은 feature가 두드러진 곳을 잘 기억하고 복원한다.)

    upsampling을 위해 deconvolution layer를 사용하지 않기 때문에 별도의 학습 파라미터가 없다.
    
---

### Semantic Segmentation을 위한 SegNet 

SegNet의 구조는 Encoder와 Decoder로 나뉜다.

<div align=center>
  
![image](https://user-images.githubusercontent.com/59076451/130320488-26756245-db48-4d12-a026-81302f347bbd.png)
  
</div>  

- Encoder , Decoder

Encoder는 VGG16의 뒷 단의 FC layer를 제외한 구조를 그대로 사용한다.

        Encodedr의 Conv layer에서 주목할 점은 모두 1x1 filter를 사용한다는 것

        Pooling layer에서 주목할 점은 뒤의 UnPooling하는 과정에서 필요하기에 Pooling 수행 시 해당 Index들을 저장해둔다는 것
    
<div align=center>
  
![image](https://user-images.githubusercontent.com/59076451/130320569-d1f45d3b-dfe9-42ed-ad1b-46f32717f7b4.png)
  
</div>      

Decoder에서는 Upsampling을 수행하여 Coarse한 데이터를 보완한다. (FCN의 Coarse data 부분 참고)

이미지의 Resolution을 높이는 방법으로 FCN 또는 CAE에서와는 다르게  UnPooling을 사용한다. (FCN, CAE에서는 UpSampling Deconvolution 수행)

    FCN과 비슷하지만, UnPooling이후 일반적인 Conv layer를 통과시켜 feature를 뽑아냈다는 특징이 있다.


마지막 layer에서는 k-class softmax를 사용해서 Pixel마다 독립적으로 클래스의 확률을 계산한다. (즉, output은 k개의 Channel으 갖는다.)



    
