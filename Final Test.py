import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 데이터 생성
data = {
    'temperature': np.random.uniform(15, 45, 1000),
    'humidity': np.random.uniform(10, 90, 1000),
    'wind_speed': np.random.uniform(0, 20, 1000),
    'soil_moisture': np.random.uniform(5, 50, 1000),
    'fire_risk': np.random.choice([0, 1], 1000, p=[0.8, 0.2])
}

df = pd.DataFrame(data)

# 특징 변수와 목표 변수 분리
X = df[['temperature', 'humidity', 'wind_speed', 'soil_moisture']]
y = df['fire_risk']

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 랜덤 포레스트 모델 학습
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 기본 평가
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print("=== 모델 평가 결과 ===")
print(f"정확도: {accuracy:.2f}")
print("\n분류 리포트:")
print(classification_report(y_test, predictions))
print("\n혼동 행렬:")
print(confusion_matrix(y_test, predictions))

# KFold 교차 검증
kf = KFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=kf, scoring='accuracy')
print("\n=== KFold 교차 검증 결과 ===")
print(f"5-Fold 정확도 점수: {scores}")
print(f"평균 정확도: {scores.mean():.2f}")
