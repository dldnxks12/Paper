### Rich feature hierarchies for accurate object detection and semantic segmentation `22 Oct 2014`

`2 - Stage detector의 시초인 R-CNN에 대한 논문 `

`CNN`과 `Region Proposal method`를 결합시킨 모델이며, `R-CNN` 이라고 명명

<br>

<br>

#### `Abstract`

- 해당 논문의 방법으로 지난 2012년의 최고 성능에 비해 mAP 지표로 30% 이상의 성능 향상을 이뤄냈으며, 두 가지 방법에 초점을 맞추었다.  

      1.localize와 segmentation을 위해 bottom-up 방식의 region proposal 방법을 CNN에 결합시켰다. 
      2.Labeling된 data의 부족을 해결하기 위해 auxiliary task로 supervised fine-tuning을 진행한 후 ,
        domain-specific한 dataset으로 fine-tuning을 진행하였다.

<br>
      
- Overfeat 모델과 비교 진행하며 발전시킨 알고리즘이며, Overfeat 모델 보다 성능이 뛰어나다.    

      Overfeat : CNN 구조를 사용하며 Sliding-Window 방법으로 detection을 수행하는 모델이며 R-CNN 비슷한 컨셉
    
---

<br>

<br>

#### `Introduction `

- 이 논문은 CNN을 사용해서 object detection 성능을 극적으로 높인 최초의 논문이다.

      이전에는 HOG 또는 SIFT와 같은 느리고 복잡한 알고리즘을 통해 Object detection을 수행했다.

<br>

- 두 가지에 초점을 맞추어 알고리즘을 발전시켰다.

      1. Deep Network를 이용하여 Localization을 수행하는 방법
      2. 작은 양의 Annotated detection data를 이용하여 High-Capacity 모델을 학습시키는 방법

<br>

- sliding-window detector와 비슷하게 우리도 sliding-window를 사용하려고 했다.

      sliding-window detector은 제한된 수의 물체만 감지하고, 고해상도를 유지하기 위해 2개의 Conv layer와 1개의 pool layer만 사용한다. 
      R-CNN은 5개의 Conv Layer와 Pool layer, 그리고 더 큰 Receptive Field와 Stride를 사용하기에 해당 방법은 부적합하다. 
      
<br>      
      
- sliding-window 대신 `recognition using regions` 방법을 사용한다.

      test에서 하나의 입력 이미지에 대해 2000개의 region을 뽑아냈고, 이를 SVM을 이용해서 모두 분류했다.

<br>

- 부족한 데이터를 처리하는 방법

      Supervised pre-training on a large auxiliary dataset 이후 작은 dataset에 대해 domain-specific fine-tuning 수행

---

<br>

<br>

#### `Object detection with R-CNN`

- 3개의 모듈로 구성된 모델이다.

      1. Module for Generating Category-indepenent region proposals
      2. Module for a large CNN 
      3. Moudle for classifying regions with SVM 

<br>

<div align=center>

![image](https://user-images.githubusercontent.com/59076451/133906285-9988e59f-8796-4ceb-b451-6f06d83b206e.png)
  
</div>  

<br>

- `Region proposals`

      objectness, selective search, category-indepent object proposals, .. 등의 방법 중 selective search 방법 사용 
      
      
      


