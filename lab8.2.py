import numpy 
import random

M = int(input("Введіть кількість рядків (M): "))
N = int(input("Введіть кількість стовпців (N): "))

A = numpy.random.randint(2, size=(M, N))

print("Початковий масив A:")
print(A)

P = []

for row in A:
    ones_count = numpy.sum(row)  
    if ones_count % 2 == 0:
        P.append(0)  
    else:
        P.append(1)  

A = numpy.column_stack((A, P))

print("Оновлений масив A з доданим стовпцем для парності:")
print(A)
