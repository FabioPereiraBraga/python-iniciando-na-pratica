import getpass

print('\n')
print('*********************************************************************')
print('**************** Fábio Braga - Caixa Eletrônico *********************')
print('*********************************************************************')
print('\n')

account_typed = input('Digite sua conta: ')
password_typed = getpass.getpass('Digite sua senha: '

accounts_list = {
  '0001-02':  {
      'aggency':'0001-02',
      'password':'123456',
      'name':'Fabio Braga',
      'value':0  
    },
   '0002-02':  {
      'aggency':'0002-02',
      'password':'123456',
      'name':'Fulano 2',
      'value':0  
    },
    '0003-02': {
      'aggency':'0003-02',
      'password':'123456',
      'name':'Fulano 3',
      'value':0  
    }
}

if account_typed in accounts_list and password_typed == accounts_list[account_typed]['password']:
   print('Conta Valida')
else: 
   print('Conta invalida!')   
