n1 =37
n2 = 11
r = 1

while r != 0:
    print('verdadeiro')
    r = n1%n2
    n1 = n2
    n2 = r
   
print(f'valor final {n1}')
