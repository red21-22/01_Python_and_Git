# Quiz 1
def add(a,b,c,d):
    sum = a + b + c + d
    return sum

def multiply(a,b,c,d):
    product = a * b * c * d
    return product

sum_result = add(1,2,3,4)
product_result = multiply(1,2,3,4)
print("두 함수의 합: ", sum_result)
print("두 함수의 곱: ", product_result)

# Quiz 2
def odd_or_even(number):
    if number % 2 == 0:
        return "짝수"
    else:
        return "홀수"

print(odd_or_even(3))
print(odd_or_even(16))

#Quiz 3
def average(number):
    total = 0
    

