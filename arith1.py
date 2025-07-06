# 첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.
a, b, c = map(int, input().split())

a1 = (a + b) % c
a2 = ((a%c) + (b%c)) % c
a3 = (a * b) % c
a4 = ((a%c) * (b%c)) % c

print(a1)
print(a2)
print(a3)
print(a3)
print(a4)
