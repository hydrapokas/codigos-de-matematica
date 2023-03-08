#an = a1 * q**(n - 1)
#n = log[(an/a1), r] + 1
import math
rep = 1
primeiravez = 1
print('Esse programa serve para calcular Progressao Geometrica.')
opc = int(input('Escolha uma opcao:\n1. Descobrir o An(nesimo termo)\n2. Descobrir a razao (q)\n3. Descobrir o n (termo)\n4. Descobrir o a1(primeiro termo)\n5. Soma da P.G\n'))
while rep == 1:
    if primeiravez == 0:
        opc = int(input('\nEscolha uma opcao:\n1. Descobrir o An(nesimo termo)\n2. Descobrir a razao (q)\n3. Descobrir o n (termo)\n4. Descobrir o a1(primeiro termo\n5. Soma da P.G\n'))
    primeiravez = 0    

    match opc:
        case 1:
            a1 = float(input('insira o primeiro termo: '))
            n = int(input('insira o termo que deseja descobrir: '))
            q = float(input('insira a razao?:'))
            print ('an = a1 * q **(n - 1)')
            print (f'an = {a1} * {q} **({n} - 1)')
            an = a1 * q **(n - 1)
            print ('an =',an)
            rep = int(input('deseja reiniciar o programa?\n1. Sim\n2. Nao\n'))

        case 2:
            an = float(input('insira o valor do An: '))
            a1 = float(input('insira o primeiro termo: '))
            n = int(input('digite o termo:'))
            q = (an / a1) ** ((1 / (n-1)))       
            print('R = (an – a1)/(n – 1)')
            print(f'R = ({an} – {a1})/({n} – 1)')
            print('R =',q)
            rep = int(input('deseja reiniciar o programa?\n1. Sim\n2. Nao\n'))

        case 3:
            an = float(input('insira o valor do An: '))
            q = float(input('insira a razao: '))
            a1 = float(input('insira o primeiro termo: '))
            n = math.log((an/a1), q) + 1
            print('n = log[(an/a1), r] + 1')
            print(f'n = log[({an}/{a1}), {q} + 1')
            print('n =',n)
            rep = int(input('deseja reiniciar o programa?\n1. Sim\n2. Nao\n'))

        case 4:
            n = int(input('insira o termo que deseja descobrir: '))
            q = float(input('insira a razao?:'))
            an = float(input('insira o valor do An: '))
            a1 = an / (q**(n - 1))
            print('a1 = an - r*n + r')
            print(f'a1 = {an} - {q}*{n} + {q}')
            print('a1 =',a1)
            rep = int(input('deseja reiniciar o programa?\n1. Sim\n2. Nao\n'))

        case 5:
            q = float(input('insira o valor da razao: '))
            a1 = float(input('insira o primeiro termo: '))
            inf = bool(input('A P.G e infinita?\n1. Sim\n0. Nao\n'))
            if inf and (q < 1 and q > 0) or (q < 0 and q > -1):
                sn = a1 / (1 - q)
                print ('sn = a1 / (1 - q)')
                print (f'sn = {a1} / (1 - {q})')
                print ('Sn =',sn)
                rep = int(input('deseja reiniciar o programa?\n1. Sim\n2. Nao\n'))
            else:
                n = int(input('insira o n: '))
                an = float(input('insira o valor do An: '))
                sn = (a1 * (q**n - 1)) / (q - 1)
                print('Sn = n . (a1 + an)/2')
                print(f'Sn = {n} . ({a1} + {an})/2')
                print('Sn =', sn)
                rep = int(input('deseja reiniciar o programa?\n1. Sim\n2. Nao\n'))