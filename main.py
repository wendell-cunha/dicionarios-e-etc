mais_vendidos = {'tecno':'iphone', 'refri': 'consul', 'mouse': 'multi'}
vendas_tecn = {'iphone':4000, 'samsung': 3000, 'ps5': 2000}

print('Vendemos {} ipads'.format(vendas_tecn.get('ps5')))

vendas_tecn['tablet'] = 5000


if 'dell' in vendas_tecn:
  print(vendas_tecn)
else:
  vendas_tecn['dell'] = 21000
  print(vendas_tecn)
  
for x in vendas_tecn:
  print(x)
  print(vendas_tecn[x])
  