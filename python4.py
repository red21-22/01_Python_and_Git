# Quiz 1
one = input("인사를 하세요")
if one == "안녕하세요" :
    print("반갑습니다")
else:
    print("인사를 먼저 하세요")

# Quiz 2
two = int(input("값을 입력하세요"))
num: int = 100 + two
if num >= 150:
    print(num)
else:
    print("값이 부족합니다")

#Quiz 3
number = [100,200,300]
result = []

for a in number :
    b = a * 1.1
    result.append(b)
print(result)

#Quiz 4
numbers = [3, 100, 23, 33, 72, 94]
results = []

for a in numbers:
    if a % 3 == 0:
        results.append(a)

print(results)

#Quiz 5
num = 1
while num <= 1000:
    print(num)
    num = num + 1

#Quiz 6
num = 1
sum = 0
while num <= 100:
    if num%2 != 0:
        sum += num
    num += 1
print(sum)