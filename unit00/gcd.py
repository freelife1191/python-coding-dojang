# 최대공약수 GCD(Greatest Common Divisor)
# 공통으로 나누어지는 수 즉 약수중에 가장 쿤 수

a = 10
b = 12

for i in range(min(a, b), 0, -1):
    if a % i == 0 and b % i == 0:
        print(i)
        break

# 유클리드 호제법
# x, y라는 두수가 있을 때 x를 y로 나눈 나머지인 r이 있다고 한다면
# x, y의 최대공약수는 y와 r의 최대공약수와 같다
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a