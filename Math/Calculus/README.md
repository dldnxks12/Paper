## Taylor Series 

[참고링크](https://darkpgmr.tistory.com/59)

테일러 급수가 무엇이고, 왜 사용하는지 그리고 어디에 사용하는 지 알아보자.
   
<br>   
   
- List 

      1. Taylor Series? 
      2. Taylor series의 사용
      3. Maclaurin Series

---

<br>   


- `Talyor Series`


`Taylor Series는 미지의 함수 f(x)를 다항함수로 근사하는 방법이다.`

    다항함수는 다루기 매우 쉽고 직관적이기 때문에 이로 근사하는 것은 매우 큰 이점을 가져다준다!
    
<div align=center>    
  
![image](https://user-images.githubusercontent.com/59076451/132955967-e3309e46-c696-4e51-9b51-6d4957661ec5.png)
    
</div>  

    Taylor Series에서 주의해야할 것은 좌변 p(x)와 우변 f(x)이 모든 x에 대해 같은 것이 아니라, 'x=a' 근처에서만 성립한다는 것이다.

    즉, x가 x=a 점에서 멀어질 수록 p(x) = f(x)라는 식은 오차가 커진다. 
    
             p(x)는 f(x)를 x=a 부근에서 다항함수로 근사시킨 식이다. 
             
<br> 

    한편, 위의 근사 다항식은 차수가 커질수록 f(x)를 더 잘 근사하게 된다.  
    
    (첫 번째 식에서 근사 차수를 infinite까지 한 것이 f(x)와 같다고 되어있는 것을 보자)
        
    
<br> 

<br> 

`Taylor Series는 결국 f(x)를 x = a 부근에서 f(x)와 동일한 미분계수를 갖는 어떠한 다항함수 ( p(x) )로 근사시키는 방법이다. `

      f(a) = p(a), f'(a) = p'(a), f''(a) = p''(a) , ... 임을 확인할 수 있다. 
      
      위와 같이 p(x)와 f(x)의 x=a에서 미분계수를 일치시키면, 사실 x = a 뿐아니라 해당 주변에서도 어느정도 두 함수가 일치한다! 
     
<br>        
     
경우에 따라서는 Taylor Series를 1차 또는 2차까지만 전개해서 사용하는 경우도 많다.

    물론 차수를 infinite하게 가져가면 오차는 매우매우 작아져 근사에 문제가 없다.
           
    
<div align=center>    
  
![image](https://user-images.githubusercontent.com/59076451/132956316-ee9ce14e-442e-40d6-92eb-91e3ffc18585.png)
  
예를 들어 2차까지만 Taylor 근사를 시킨다면 위와 같이 전개한다.
  
나머지 부분은 `Q(x)`로 놓고 0처럼 생각하여 무시한다.   
  
만약 `우리가 근사하려는 x가 a의 부근이라면` 차수가 낮아도 사실 근사에 오차가 별로 없다고 생각할 수 있다!  
  
</div>  


---

<br>

<br>

- `Taylor Series의 사용`


Taylor Series가 필요한 이유는 쉽게 얘기해서 우리가 모르는 미지의 함수 f(x)를 `다항함수로 바꿔서 쉽게 처리하기 위함`이다.

일반적으로 `문제 또는 모델의 단순화에 사용`한다.

      우리가 잘 모르는 또는 복잡한 함수를 1 ~ 3차 다항함수로 근사하여 사용해서 문제 또는 모델을 굉장히 단순화 시킬 수 있다.    
    
<br>    

`ex)` sin(x2)의 정적분 

    적분을 구하기 어려운 함수의 경우 다음과 같이 Taylor 근사를 통해 함수를 단순화하여 계산할 수 있다.
    
<div align=center>    
  
![image](https://user-images.githubusercontent.com/59076451/132956530-4e38124e-fae4-4102-a0df-6704542d6e75.png)

    위 식에서 sin(x2)의 taylor series는 sin(t)의 t = 0에서의 전개를 한 후, t = x2을 대입하여 얻어진 식이다. 
    
</div>  


---

<br>

<br>

- Maclaurin Series


Taylor Series를 사용한다고 하면 대부분 `x = 0` 부근에서 Taylor Series를 사용하는게 일반적이라고 한다. 

    결과식이 깔끔하기 때문일까? 잘 모르겠다.
    
<br>    
    
`x = 0`에서 전개된 Taylor Series 식을 특별히 `Maclaurin Series` 라고 한다. 










