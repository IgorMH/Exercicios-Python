v = []
u = []
v.append(5)
v.append(-1)
v.append(3)
u.append(3)
u.append(2)
u.append(-4)

soma = 0
n = 3

for i in range(3):
    if v[i] > u[i]:
        soma = soma + v[i]
    else:
        soma = soma + u[i]

print(soma)