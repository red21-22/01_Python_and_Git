import pandas as pd
import matplotlib.pyplot as plt  # 이 부분을 한 번 더 확인합니다.
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score

# 파일 불러오기
filename = './데이터프레임/data/1_pima.csv'

# 열 이름 설정
column_names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

# 데이터 읽어오기
data = pd.read_csv(filename, names=column_names)

# 예측을 위한 데이터 나누기
X = data.iloc[:, :-1].values    # 입력 변수 선택 (class 제외)
y = data.iloc[:, -1].values     # 출력 변수인 class 선택

# Min-Max Scaling
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# 데이터 분할 (학습 데이터와 테스트 데이터)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Linear Regression 모델 생성 및 학습
model = LinearRegression()
model.fit(X_train, y_train)

# 학습된 모델을 사용하여 테스트 데이터에 대한 예측 수행
y_pred = model.predict(X_test)
print(y_pred)

# 예측값을 0 또는 1로 변환 (임계값 설정 적용)
y_pred_binary = (y_pred > 0.5).astype(int)
print(y_pred_binary)

# 예측 정확도 계산
accuracy = accuracy_score(y_test, y_pred_binary)

# 결과 출력
print("----------------------------------")
print("Actual Values:", y_test)
print("Predicted Values:", y_pred_binary)
print("----------------------------------")
print("Accuracy:", accuracy)

# 그래프 설정
plt.figure(figsize=(10, 5))

# 실제값과 예측값 시각화
plt.scatter(range(len(y_test)), y_test, color='blue', label='Actual Values', marker='o')
plt.scatter(range(len(y_pred_binary)), y_pred_binary, color='red', label='Predicted Values', marker='x')

plt.title('Comparison of Actual and Predicted Values')
plt.xlabel('Data Index')
plt.ylabel('Class (0 or 1)')
plt.legend()

# 그래프 저장
plt.savefig('./데이터프레임/results/linear_regression.png')
