import getpass
import os 

accounts_list = {
       '0001-02': {
           'aggency':'0001-02',
           'password':'123456',
           'name':'Fabio Braga',
           'value':20,
           'admin': False 
         },
        '0002-02': {
           'aggency':'0002-02',
           'password':'123456',
           'name':'Fulano 2',
           'value':50,
           'admin': False  
         },
         '0003-02': {
           'aggency':'0003-02',
           'password':'123456',
           'name':'Fulano 3',
           'value':130,
           'admin': False  
         },
         '1111-11': {
           'aggency':'1111-11',
           'password':'123456',
           'name':'Admin',
           'value':130,
           'admin': True  
         }
     }
     
money_slips = {
       '20':5,
       '50': 5,
       '100':5
     }

while True:

     print('*********************************************************************')
     print('**************** Fábio Braga - Caixa Eletrônico *********************')
     print('*********************************************************************')
     print('\n')

     account_typed = input('Digite sua conta: ')
     password_typed = getpass.getpass('Digite sua senha: ')
     


     if account_typed in accounts_list and password_typed == accounts_list[account_typed]['password']:
        clear = 'cls' if os.name == 'nt'  else 'clear'
        os.system(clear) # Windowa New Tecnologia

        print('*********************************************************************')
        print('**************** Fábio Braga - Caixa Eletrônico *********************')
        print('*********************************************************************')
        print('\n')
        print('1 - saldo')
        print('2 - Saque')
        if accounts_list[account_typed]['admin']:
           print('10 - incluir celulas')
        option_type = input('escolha uma das opções acima: ')
        if option_type == '1':
           print('Seu saldo e %s' % accounts_list[account_typed]['value'] ) 
        elif option_type == '2':
           valor = input('Digite o valor a ser sacado: '); 

           money_slips_user = { }
           valor_int = int(valor);
 
           if valor_int // 100 > 0 and valor_int // 100 <= money_slips['100']:
              money_slips_user['100'] = valor_int // 100
              valor_int = valor_int - valor_int // 100 * 100  

           if valor_int // 50 > 0 and valor_int // 50 <= money_slips['50']:
              money_slips_user['50'] = valor_int // 50
              valor_int = valor_int - valor_int // 50 * 50 

           if valor_int // 20 > 0 and valor_int // 20 <= money_slips['20']:
              money_slips_user['20'] = valor_int // 20
              valor_int = valor_int - valor_int // 20 * 20        

           if valor_int != 0:
              print('O caixa não tem células disponivel para este valor')
           else:
              for money_list in  money_slips_user:
                  money_slips[money_list]  -=  money_slips_user[money_list]    
              print('Pegue as notas')
              print(money_slips_user)    
           

        elif option_type == '10' and accounts_list[account_typed]['admin'] :
           amount_type     = input('Digite a quantidade de cedula: ')
           money_bill_type = input('Digite a cédula a ser incluída: ')
           
           if money_bill_type in money_slips:
              money_slips[money_bill_type] += int(amount_type)
              print(money_slips)
           else:
               print('Valor informado invalido')   
     else: 
          print('Conta invalida!')   
     
     input('Digite <ENTER> para continuar...') 

     clear = 'cls' if os.name == 'nt'  else 'clear'
     os.system(clear) 
     