n1, n2, n3 = input().split()
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
p1, p2, p3 = input().split()
p1 = float(p1)
p2 = float(p2)
p3 = float(p3)
media_final = (n1 * p1 + n2 * p2 + n3 * p3)/(p1 + p2 + p3)
print(f'{media_final:.6f}')