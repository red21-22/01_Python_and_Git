#Quiz 1
def add(a,b,c,d):
    sum = a + b + c + d
    return sum

def multiply(a,b,c,d):
    product = a * b * c * d
    return product

sum_result = add(1,2,3,4)
product_result = multiply(1,2,3,4)
print("4개의 숫자의 합:", sum_result)
print("4개의 숫자의 곱:", product_result)

#Quiz 2
def odd_or_even(number):
    if number % 2 ==0:
        return "짝수"
    else:
        return "홀수"

print(odd_or_even(3))
print(odd_or_even(16))

#Quiz 3
def average(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)

print(average([1,2,3,4,5]))

#Quiz 4
class Game_character:
    def __init__(self, id, gender, job):
        self.id = id
        self.gender = gender
        self.job = job

    def attack(self):
        print("공격!")

#Quiz 5
class real_estate:
    def __init__(self, location, size, building_type, price, year_built):
        self.location = location
        self.size = size
        self.building_type = building_type
        self.price = price
        self.year_built = year_built

    def information(self):
        print(f"위치: {self.location}")
        print(f"평수: {self.size}")
        print(f"건물 종류: {self.building_type}")
        print(f"가격: {self.price}")
        print(f"건축 연도: {self.year_built}")

estate = real_estate("청주", 55, "빌라", 1000000000, 2222)
estate.information()