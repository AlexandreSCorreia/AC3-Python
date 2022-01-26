nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')
salario  =float(input('Qual o seu salario? '))


print('Olá '+ nome +'!')
print(f'Após duas décadas, você estará com {idade + 20} anos')
print(f'Seu salário com 25% de aumento é:', salario * 1.025)