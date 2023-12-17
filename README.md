# DataMining

## Requirement 
__Library__
```
* sklearn
* joblib
* numpy
* pandas
* tensorflow
* matplotlib
```

__Dataset__  
* This repo. utilizes public data from the KMA and NGII
* https://kosis.kr
*  https://www.ngii.go.kr/kor/contents/view.do?sq=701&board_code=contents_data
* directory hierarchy:
```
Project
|--- data
|          |--- 2023_mt.csv
|          |--- autumn_day.csv
|          |--- classification.csv
|          |--- total.csv
|          |--- (*each mountains).csv
|
|--- Classification
|          |--- classification.ipynb
|            (needs classification.csv)
|--- Prediction
|          |--- prediction_all.ipynb
|            (needs total.csv, 2023_mt.csv for model 2)
|          |--- predition_bukhan.ipynb
|          |--- ...
|              (prediction for each mountains
|                needs (*each mountains).csv, autumn_day.csv, 2023_mt.csv)
|--- Visualization
|          |--- visualization.ipynb
|                (needs (*each mountains.csv, total.csv)
|--- Models
|          |--- logistic.pkl
|          |--- bukhan.pkl 
|          |--- ...
|--- Main
|          |--- model1.py
|          |--- model2.py


Then, call --data_path='../data'
```

## Explanation for codes
기상 변수(8월과 9월의 평균기온, 월 총 강수량, 일사량)과 측정 위치(5개의 산)의 위도, 경도, 산의 높이를 이용해 해당 지역의 단풍 시작일을 예측하는 모델

* Model1 : 입력 값에 대해 어떤 산에 대한 정보인지 분류 + 해당 산의 입력값에 대한 단풍 시작일 예측을 각각 진행하여 결합
* Model2 : 산에 대한 지리적 정보(고정 변수) 또한 입력 값에 포함 시켜 산의 분류 과정 없이 해당 입력에 대한 단풍 시작일 예측


### Code Structure
* Main
    * model1.py, model2.py
    * 단풍 시작일 예측 코드 실행
* Classification
    * classification.ipynb
        * 입력된 기상 변수에 대해 어떤 산에 대한 정보인지 분류
        * 이를 통해 logistic.pkl 생성
* Prediction
    * prediction_all.ipynb
        * 산의 지리정보(위도, 경도, 높이)까지 입력하여 단풍 시작일 예측
    * prediction_(*mountain).ipynb
        * 기상 변수를 이용한 각 산 별 단풍 시작일 예측
        * 이를 통해 (*mountain).pkl 생성
* Visualization
    * visualization.ipynb
        * 변수에 대한 상관 관계 및 변화 시각화
* data
    * 모델 구현을 위해 사용된 데이터셋


## Results
![image](https://github.com/soo811/datamining/assets/91643983/d49dcb37-ef93-4bb0-b79d-d272eac5ba35)

> **_2023년도 단풍 시작일에 대해 모델 1과 모델 2를 사용한 결과와 실제 단풍 시작일과의 차이를 비교해 보니 모델1은 실제와 평균 4일, 모델2는 평균 2일 정도의 차이가 나타났다._**


## License
```
Copyright (c) 2023 Jisoo Shin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

