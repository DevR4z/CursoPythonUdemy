print('Calculadora: ')
operadores = ['+', '-', '*', '/', '**', '%']
sair = False

while sair is False:
        try:
            num1 = input('Numero: ')
            op = input('Operação: ')
            num2 = input('Numero: ')
            num1_float = float(num1)
            num2_float = float(num2)
            print('Resultado: ')
            if op in operadores:
                if op == '+':
                    print("#"*20)
                    print(f'{num1_float} + {num2_float} = {num1_float + num2_float}')
                    print("#"*20)
                elif op == '-':
                    print("#"*20)
                    print(f'{num1_float} - {num2_float} = {num1_float - num2_float}')
                    print("#"*20)
                elif op == '*':
                    print("#"*20)
                    print(f'{num1_float} * {num2_float} = {num1_float * num2_float}')
                    print("#"*20)
                elif op == '/':
                    print("#"*20)
                    print(f'{num1_float} / {num2_float} = {num1_float / num2_float}')
                    print("#"*20)
                elif op == '**':
                    print("#"*20)
                    print(f'{num1_float} ** {num2_float} = {num1_float ** num2_float}')
                    print("#"*20)
                elif op == '%':
                    print("#"*20)
                    print(f'{num1_float} % {num2_float} = {num1_float % num2_float}')
                    print("#"*20)
            else:
                print("#"*20)
                print('Operação inválida!')
                print("#"*20)
            
            sair = input('Deseja sair? (s/n): ').lower().startswith('s')

        except:
            print('Digite um número, depois um operador e depois outro número!')
            sair = input('Deseja sair? (s/n): ').lower().startswith('s')