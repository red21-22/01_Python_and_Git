from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from pickle import dump, load
import os

# 파일 경로 설정
filename = "./데이터프레임/data/1_pima.csv"
output_filename = "./데이터프레임/results/finalized_model_with_score.sav"

# 데이터 확인 및 로드
if not os.path.isfile(filename):
    raise FileNotFoundError(f"Data file not found: {filename}")

# 데이터 로드
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(filename, names=names)
array = dataframe.values
X = array[:, 0:8]
Y = array[:, 8]

# 데이터 분할
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, random_state=7)

# 모델 학습
model = LogisticRegression(max_iter=1000)
model.fit(X_train, Y_train)

# 모델 정확도 계산
score = model.score(X_test, Y_test)
print(f"Trained Model Score: {score}")

# 저장 디렉토리 생성
os.makedirs(os.path.dirname(output_filename), exist_ok=True)

# 모델과 스코어 저장
with open(output_filename, 'wb') as file:
    dump({'model': model, 'score': score}, file)

# 저장된 모델과 스코어 로드
with open(output_filename, 'rb') as file:
    loaded_data = load(file)

# 로드된 데이터에서 모델과 스코어 가져오기
loaded_model = loaded_data.get('model', None)
loaded_score = loaded_data.get('score', None)

if loaded_model is None or loaded_score is None:
    raise ValueError("Loaded data is missing 'model' or 'score' keys!")

# 결과 출력
print(f"Loaded Model Score: {loaded_score}")
