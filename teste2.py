nome = input('Qual seu nome')
peso = input('Quala seu peso')
idade = input('Qual sua idade')

if peso>idade:
  print('Obeso')
if peso==idade:
  print ('Estavel')
  if peso>idade:
   print('Magro') 
print('Minha situação esta {} {}'.format(peso,idade))
   