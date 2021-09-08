## Interpolation

Image를 Decode or Upsampling하는 과정에서 자주 등장하는 Interpolation에 대해서 이해해본다.

주로 Bi-linear Interpolation에 대한 얘기가 많이 나오는데, 이를 포함한 전반적인 Interpolation에 대해 정리해보자. 

우선 내가 궁금해 하는 Bi-Linear Intorpolation은 선형 보간법이라는 개념에 속한다. 

1차, 2차, 3차 선형 보간법 정도가 있다고 생각하면 될 것 같다.

[참고링크](https://darkpgmr.tistory.com/117)

---

<br>

#### 선형 보간법

보간법에는 Interpolation과 extrapolation이 있다. 

- Interpolation

          알려진 지점의 값 사이에 위치한 값을 알려진 값으로부터 추정하는 것 
          
- Extrapolation

          알려진 지점의 값 밖에 위치한 값을 알려진 값으로부터 추정하는 것 (Interpolation에 비해 훨씬 위험한 예측 방법)
          
<div align=center>          
  
![image](https://user-images.githubusercontent.com/59076451/131601481-b5b20d8f-c4a6-4df9-8403-10ac6cd479de.png)
    
</div>

내 관심은 Interpolation이니 extrapolation은 나중에 공부해보자.

<br>

---

#### 1D Linear Interpolation

두 지점을 보간하는 방법은 spline, polynomial 등 여러 가지 방법이 있다고 한다. 그 중 linear interpolation은 

두 지점 사이의 값을 추정할 때 , 그 값을 두 지점과의 직선 거리에 따라 선형적으로 결정하는 방법이다!

<div align=center>          
  
![image](https://user-images.githubusercontent.com/59076451/131601676-3c8f5f65-421b-4554-801c-76e8ddcf9d12.png)
  
아래의 식은 고등과정에서 두 점 사이의 한 점 위치를 구하는 공식이며, 선형 보간법의 한 점을 추정하는 방법과 완전히 동일하다.  

![image](https://user-images.githubusercontent.com/59076451/131601733-e699c2cb-2781-42e3-801e-a3bbe64dd12b.png)

거리의 합이 1이 되도록 정규화하면 위 식은 아래와 같이 정리가능하다. 
  
![image](https://user-images.githubusercontent.com/59076451/131601743-c25a3305-048f-464b-bfa4-4cafb43b4052.png)
 
</div>

#### 2D Linear Interpolation : Bilinear Interpolation

1차원에서의 선형 보간법의 2차원으로의 확장

<div align=center>

Bilinear interpolation은 아래 그림과 같이 네 개의 직사각형의 꼭지점의 값이 주어져있을 때 이로부터 가운데 점 P를 추정하는 방법이다.
  
점 P에서 x축 방향으로 사각형의 변까지의 거리를 w1, w1, 점 P에서 y축 방향으로 사각형의 변까지의 거리를 h1, h2라 하자.

![image](https://user-images.githubusercontent.com/59076451/131602233-a2405c6b-ae24-418b-9c90-83aaf2fccb99.png)

![image](https://user-images.githubusercontent.com/59076451/131602246-a9718cf3-fc00-425f-8886-bd06297a63ea.png)
      
</div>  

점 P는 위와 같은 식으로 구할 수 있으며, 보기에는 굉장히 복잡하지만 실은 다음의 방법으로 구하면 된다.

1. A,B를 보간해서 M을 얻고, 반대쪽에서도 C,D를 보간해서 N을 얻는다.
2. M, N을 보간해서 P를 얻는다. 

<br>

위의 방법은 직사각형의 경우에만 사용할 수 있다. 

임의의 사각형에 대해서는 다음과 같은 방법에 따라 해결할 수 있다.

1. 임의의 사각형 T을 T'으로 워핑(매핑)한다.
2. T'에서 Bilinear 보간을 통해 P'을 구한다.
3. P'을 워핑(매핑)을 통해 다시 P로 복귀시켜 구한다. 

<div align=center>

![image](https://user-images.githubusercontent.com/59076451/131602551-6deaabd9-d437-4b62-82bf-062b6812bfb8.png)
  
</div>  


