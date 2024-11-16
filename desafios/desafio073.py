times = ('Corinthians','Palmeiras','Santos','Grêmio','Cruzeiro','Flamengo',
         'Vasco','Chapecoense','Atlético','Botafogo','Atlético-PR','Bahia',
         'São Paulo','Fluminense','Sport Recife','EC Vitória','Coritiba',
         'Avaí','Ponte Preta','Atlético-GO')
print('-=' * 20)
print(f'Lista dos times do Brasileirão: {times}')
print('-=' * 20)
print(f'Os 5 primeiros colocados são {times[:5]}')
print('-=' * 20)
print(f'Os 4 últimos colocados são {times[-4:]}')
print('-=' * 20)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 20)
print(f'A Chapecoense está na {times.index("Chapecoense")+1}º posição')