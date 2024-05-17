A = 3.0 
B = 2.0 
C = 1.0 

if (A <= B <= C) or (A >= B >= C):
    A *= 2
    B *= 2
    C *= 2
else:
    A = -A
    B = -B
    C = -C

print("New value of A:", A)
print("New value of B:", B)
print("New value of C:", C)
