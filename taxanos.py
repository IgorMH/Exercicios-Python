paisa = 80000
paisb = 200000
total_anos = 0
while paisb > paisa:
    paisa = paisa + ((paisa / 100) * 3)
    paisb = paisb + ((paisa / 100) * 1.5)
    total_anos += 1

print(total_anos)