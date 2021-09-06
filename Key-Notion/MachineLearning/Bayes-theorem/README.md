## Bayes theorem for Understanding CRF

DeepLab v2를 공부하는 도중 CRF에 대한 이야기가 나와서 공부하려고 한다.

CRF의 밑단에서는 Naive Bayes과 HMM이 있어 먼저 공부해볼 필요가 있다. 

Naive Bayes를 이해하기 위해서는 다음의 순서대로 차근차근 이해해야한다.

      1. 조건부 확률 
      2. 독립사건
      3. 분할
      4. 베이즈 정리
      
[참고 링크](https://junpyopark.github.io/bayes/)      

---

<br>

#### Bayes theorem 

추론 대상의 사전 확률과 추가적인 정보를 기반으로 사후 확률을 추론하는 통계적 방법을 베이츠 추정이라 한다. 

      어떤 기계의 성능을 평가한다고 해보자.
      
      이 때 기계 몇 대를 무작위로 뽑아 해당 표본으로 얻어진 정보만으로 모수(모든 기계)의 성능을 평가해야 한다.
      하지만 이전에 사용했던 동일한 기계에 대한 정보가 있다면 이를 이용해서 사전 정보를 얻을 수도 있다. 
      
      이런 경우 단순히 표본을 통해 모수를 추정하기보다는 표본 정보와 서전 정보를 같이 사용해서 모수를 추정하는 것이 더 바람직하다
     
---

<br>

#### 조건부 확률 (Conditional Probability)      

조건부 확률은 말 그대로 , 어떤 조건하에서의 사건의 확률을 말한다.

사건 B가 발생했을 때, 사건 A가 발생할 확률은.. 사건 B의 영향을 받아 변화할 수 있다! 

즉, 조건부 확률은 사건 B가 일어났을 때 때 때, 사건 A가 일어날 확률이다.

        예를 들어 오늘 비가 왔을 때, 내일도 비가 올 확률과 같은 것
        
<br>

<div align=center>

수식으로는 다음과 같다.
  
![image](https://user-images.githubusercontent.com/59076451/131610605-97899cf0-3322-4538-982b-2ba22d1529ae.png)
  
</div>  

<br>

비슷하게 사건 A가 일어났을 때 때 때 , 사건 B가 일어날 확률은 다음과 같다.


<br>

<div align=center>
 
![image](https://user-images.githubusercontent.com/59076451/131610711-b7703d0a-f017-4ead-b0f4-6a3d2daee750.png)
  
</div>  

<br>
        
여기서 중요한 것이 있다.

위의 두 식에 간단한 곱셈을 적용해보면 관계가 드러난다!


<br>

<div align=center>

아래 식은 단순해 보이고 별 의미 없어 보이지만 굉~장히 큰 의미를 가진 식이다. 
  
![image](https://user-images.githubusercontent.com/59076451/131610807-c6f754c9-f38c-4241-81a0-3ff02fd1f0c7.png)
    
</div>  

---

<br>

#### 독립 사건

<div align=center>

두 사건이 독립이라면 다음의 식이 성립한다.  
  
![image](https://user-images.githubusercontent.com/59076451/131611170-6267a06b-4836-4a15-ab34-f67bf10c5185.png)
  
</div>

이를 사건이 n개가 있는 경우로 확장시키면 아래와 같이 나타내볼 수 있다. 

<div align=center>
  
![image](https://user-images.githubusercontent.com/59076451/131611553-54baf4da-ee7f-4fe1-9bd7-b07ddd3ed5c6.png)
                       
어떠한 1 <= i_1 ... <= i_k <= n 에 대해서도 위 식을 만족시키면 사건 A1, A2 , ... , An 을 독립인 사건이라고 한다. 

(i_1, ... , i_k 라는 숫자는 1에서 n까지의 숫자중 임의의 k를 뽑은 인덱스)
                           
쉽게 말해서, n개의 사건 중 아무거나 k개 뽑아서 교집합한 확률이 각각 확률의 곱과 같다면 독립이라고 할 수 있다!                                                
                             
</div>  
  
---
  
<br>  
 
#### 분할 (Partition)
  
베이즈 정리를 정확히 이해하려면 먼저 분할이라는 개념을 이해해야한다!
  
K개의 집합 B1, B2 , ... , Bk가 어떤 집합 S의 분할이 되려면 아래의 두 가지 조건을 만족해야 한다.
  
      1. B1, B2, ... Bk는 각각 서로소 여야한다.  

      2. B1, B2, ... Bk 총 K개의 집합을 합집합 하였을 때, 그 집합은 정확히 S가 되어야한다.  
  
위의 두 가지 조건을 모두 만족하면 B1, B2, ... Bk를 그 집합의 **분할**이라고 한다!  
  
<div align=center>
  
집합 A1, A2, A3, A4는 각각 서로소이고, 합집합을 했을 때 전체 집합인 A가 되므로 집합 A의 분할이다 ~  
  
![image](https://user-images.githubusercontent.com/59076451/131612510-776b9d65-775a-44c3-923d-b464f83545dd.png)
  
</div>  

---
  
<br>
  
#### 베이즈 정리 

<div align=center>  
    
![image](https://user-images.githubusercontent.com/59076451/131613629-c266b190-c27f-47eb-b5fb-0f2b48fabcab.png)
  
전체 집합 S의 분할 B1, B2, B3, B4 그리고 전체 집합 S의 부분 집합인 A   
  
</div>  
  
전체 집합에 대한 분할이 4개인 예를 이용해서 베이즈 정리를 이해해보자
  
집합 B1, B2, B3, B4는 어떤 사건인 집합 S의 분할이다. 그럼 모든 S의 부분 집합 S에 대해서는 다음과 같은 식이 성립한다. 
  
<div align=center>
  
![image](https://user-images.githubusercontent.com/59076451/131613861-22380739-1570-46c3-b8bc-8dcf6f56a7de.png)
  
K는 4라고 생각하면 된다. 위 식의 괄호 안에 사건들이 각각 서로소이기 때문에 사건 A가 일어날 확률은 아래와 같이 쓸 수 있다.  
  
![image](https://user-images.githubusercontent.com/59076451/131614046-dd02ec48-33fc-497b-91bf-7da92110e924.png)

사건들이 서로 서로소이기 때문에 확률을 단순히 더하기 해주면 된다!
  
</div>  
  
<br>
  
따라서 어떤 A라는 사건이 일어났을 때 Bk 라는 사건이 일어날 조건부 확률은 다음과 같이 계산할 수 있다!!  
  
<div align=center>  

![image](https://user-images.githubusercontent.com/59076451/131614250-c6183813-49b5-4d36-8ccc-2a1e29bb93f9.png)
       
</div>  
  
위 식의 분모를 자세히 살펴보면 아까 말한 P(A)와 모양이 다른 것을 알 수 있다.
  
하지만 같은 식이다. 왜?? 
  
위의 조건부 독립 식을 다시 살펴보자!  
  
<div align=center>  

![image](https://user-images.githubusercontent.com/59076451/131614046-dd02ec48-33fc-497b-91bf-7da92110e924.png)
    
![image](https://user-images.githubusercontent.com/59076451/131614404-4611f24c-1945-44e8-ab23-4e131a364586.png)  
       
</div>    

  

#### 정리   
  
<div align=center>  

![image](https://user-images.githubusercontent.com/59076451/131614250-c6183813-49b5-4d36-8ccc-2a1e29bb93f9.png)
       
</div>  
  
위에서 다룬 이 식을 **베이즈 정리**라고 한다.  
  
그럼 이 베이즈 정리가 어떤 의미를 갖고 있을까?
  
      사건A가 일어났을 때 때 때, Bk가 일어날 확률을 계산함에 있어서,
      
      이를 거꾸로 Bk가 일어났을 때 때 때 사건 A가 일어날 확률로 표현할 수 있다는 것이다!
  
언뜻 들어서는 이게 무엇이 중요할까 싶다.
  
<br>
  
이는 A가 조건으로 주어졌을 때 B의 확률에 대해 궁금했던 것을,
  
반대로 B가 조건으로 주어졌을 때 A의 확률에 대해 이야기 하는 것으로 바꿔 쓸 수 있다는 것이다.  
  
<br>  
  
베이지안적인 용어로 이야기해보자. 
  
      사전 확률로 부터 사후 확률을 알아내는 것에서, 사후 확률로 부터 사전 확률을 알아낼 수 있게 되었다!
      
      하지만 이는 정확한 표현이 아니며, 
      
      사전 확률을 알고 있었는데.. 새로운 정보를 이용해서 사후 확률로 부터 사전 확률을 업데이트 할 수 있다는 걸 의미한다고 생각한다.
      
      아래의 예시를 보며 이해해보자.
  
---  

<br>
  
#### 예시
  
어떤 주식이 그 날 오를 확률이 θ라고 하자.  
  
이전의 주가 분석 정보들을 통해, θ가 0.4일 확률이 50% θ가 0.6일 확률이 50%임을 발견했다. (사전 확률 또는 사전 정보) 

이를 식으로 표현하면 다음과 같다.
  
<div align=center>  
  
![image](https://user-images.githubusercontent.com/59076451/131616062-a24244e8-89b5-462c-bf8c-a74b1442a241.png)
  
</div>  
  
이제 또 다른 데이터 분석을 통해 θ가 결정된 후 주가가 3일 연속으로 상승할 확률이 θxθxθ 임을 또 발견했다. (우도)

그렇다면 이제 문제다.
  
주가가 3일 연속 상승하였을 때, θ값이 0.6였을 확률은 얼마일까? (주가가 3일 연속 오른 사건을 A라고 하자.)
  
        엥? θ = 0.6 일 확률은 50% 라며? .. 일단 진행해보자!
  
우선 우리가 구해야 하는 확률은 P(θ = 0.6 | A )이며, 이를 베이즈 정리로 다음과 같이 구할 수 있다.   

<div align=center>  
  
![image](https://user-images.githubusercontent.com/59076451/131616300-e67a72bc-6e39-4541-97ed-0fb35ec519ef.png)
  
</div>  
  
여기서 결과적으로 구하게 된 확률인 0.7714 라는 수치가 **사후 확률**이다.  
  
      사후 확률은 추가된 정보로부터 사전 정보를 새롭게 수정한 확률이다.

<br>  
  
우리가 사전에는 θ가 0.6일 확률이 50%. 즉 0.5임을 확인하였으나, 새로운 정보가 추가됨에 따라 이 정보가 0.7714 라는 수치로 변화하였다.
  
**이처럼 베이즈 정리는 새로운 정보에 대해 어떻게 계산을 하고, 또 결과를 도출해 낼 수 있는 지를 알려주는 굉장히 좋은 도구이다.**
    
---
      
<br>
      
#### 용어 정리       

<div align=center>      
      
![image](https://user-images.githubusercontent.com/59076451/131617302-0e7c0699-ae26-4b30-998a-bc5b09a303e2.png)
      
</div>      

            P(A)   : A의 사전 확률      
            P(B)   : B의 사전 확률      
            P(A|B) : 사후 확률      
            P(B|A) : 우도 (Likelihood)  --- 보통 알려져있다고 가정한다. 

      
      
[예시 링크](http://solarisailab.com/archives/2614)
