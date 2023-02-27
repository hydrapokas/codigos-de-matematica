#an = a1 + (n – 1) . r

print('Esse programa serve para calcular Progressao Aritmetica.')
opc = int(input('Escolha uma opcao:\n1. Formula geral\n2. Descobrir a razao\n3. Descobrir o n\n4. Descobrir o a1\n5. Soma da P.A'))
while opc > 0 and opc < 6:
    match opc:
        case 1:
            a1 = float(input('insira o primeiro termo: '))
            n = int(input('insira o termo que deseja descobrir: '))
            r = float(input('insira a razao?:'))
            print ('an = a1 + (n – 1) . r')
            print (f'an = {a1} + ({n} – 1) . {r}')
            an = a1 + (n - 1) * r
            print ('an =',an )
            opc = int(input('deseja reiniciar o programa?\n1. Sim\n2. Nao\n'))
            if opc == 2:
                opc = 0

        case 2:
            an = input('insira o valor do An: ')
            a1 = float(input('insira o primeiro termo: '))
            n = int(input('digite o termo:'))
            r = (an - a1) / (n - 1)        
            print('R = (an – a1)/(n – 1)')
            print(f'R = ({an} – {a1})/({n} – 1)')
            print('R =',r)
            opc = int(input('deseja reiniciar o programa?\n1. Sim\n2. Nao\n'))
            if opc == 2:
                opc = 0

        case 3:
            an = input('insira o valor do An: ')
            r = float(input('insira a razao: '))
            a1 = float(input('insira o primeiro termo: '))
            n = (an + r - a1) / r
            print('n = (an + r - a1) / r')
            print(f'n = ({an} + {r} - {a1}) / {r}')
            print('n =',n)
            opc = int(input('deseja reiniciar o programa?\n1. Sim\n2. Nao\n'))
            if opc == 2:
                opc = 0

        case 4:
            n = int(input('insira o termo que deseja descobrir: '))
            r = float(input('insira a razao?:'))
            an = input('insira o valor do An: ')
            a1 = an - r*n + r
            print('a1 = an - r*n + r')
            print(f'a1 = {an} - {r}*{n} + {r}')
            print('a1 =',a1)
            opc = int(input('deseja reiniciar o programa?\n1. Sim\n2. Nao\n'))
            if opc == 2:
                opc = 0

        case 5:
            n = int(input('insira o termo que deseja descobrir: '))
            a1 = float(input('insira o primeiro termo: '))
            an = input('insira o valor do An: ')
            sn = n * (a1 + an)/2
            print('Sn = n . (a1 + an)/2')
            print(f'Sn = {n} . ({a1} + {an})/2')
            print('Sn =', sn)
            opc = int(input('deseja reiniciar o programa?\n1. Sim\n2. Nao\n'))