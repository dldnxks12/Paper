## Notation

- Sparse Data ? Spartial Data?
- Coarse ? Fine ? 

#### Spatial data 

    특정 기하학적 위치나 장소를 나타내거나, 특정 데이터 끼리 서로 관계를 가지고 있는 데이터

#### Dense data & Sparse data 

    Dense Data  (밀집 데이터) : 차원/전체 공간에 비해 데이터가 있는 공간이 매우 빽빽하게 차있는 데이터 
    Sparse Data (희소 데이터) : 차원/전체 공간에 비해 데이터가 있는 공간이 매우 협소한 데이터


![image](https://user-images.githubusercontent.com/59076451/129004403-0fc6ca9b-d13f-4cfd-bcbb-01f42b888c24.png)

위 행렬 중 Sparse Matrix(희소 행렬)이다. 보시다 싶이 행렬의 값의 대부분이 0이다.
    
    반대로 Dense Matrix(밀집 행렬)는 행렬 값 중 0이 거의 없다.
   
위 행렬은 2차원이기 때문에 희소 행렬은 2차원 공간에서 데이터가 매우 희소한 상태. 아래 그림과 같다.
    
![image](https://user-images.githubusercontent.com/59076451/129004371-a8b85535-4931-44da-a969-d80f1cbfd42a.png)

만약 차원이 3,4,5, ... 점점 높아지는데 그 때 데이터가 희소하다면 그것은 2차원일 때보다 더 데이터가 희소해진다. 

        즉, 3차원 이상의 Tensor에서 의미 없는 0의 값이 점점 많아진다는 뜻

ML에서는 매우 고차원 데이터를 다루는 경우가 많은데, 그 만큼 데이터가 Sparse해질 확률도 높다.

이 Sparse한 데이터를 가지고 학습할 시 잘 되지 않는다.

    이 때 차원 축소등을 통해 데이터를 Dense하게 만들어 사용한다!
    
        SegNet에서 UnPooling 후 일련의 Conv layer를 통해 Sparse data를 Dense data로 만듦
        
        NIN과 GoogLeNet의 Inception Net에서도 1x1 Conv Layer를 통해 Sparse data를 가지고도 Dense data로 만들어 학습할 수 있음을 보임
    

#### Coarse grained

    data의 분류를 큼직큼직하게 하는 것
    
            dog, cat, horse ...

#### Fine grained

    data의 분류를 세밀하게 하는 것

            big dog, middle dog, small dog ...
