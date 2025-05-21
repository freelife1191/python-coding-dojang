import math
# https://blog.naver.com/heavencoding/223171171641
# 최소공배수 LCM(Least Common Multiple)
# 두 수의 공통의 배수중 가장 작은 수
# 유클리스 호제법
# 최소공배수를 구할때 최대공약수 구하는 함수를 사용하게 됨

a = 100
b = 84

# 최대공약수
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 최소공배수 = 두 수의 곱 / 최대공약수
def lcm(a, b):
    return a * b // gcd(a, b)

print(f"최대공약수: {gcd(a, b)}")
print(f"최소공배수: {lcm(a, b)}")

print(f"최대공약수: {math.gcd(a, b)}")
print(f"최소공배수: {math.lcm(a, b)}")