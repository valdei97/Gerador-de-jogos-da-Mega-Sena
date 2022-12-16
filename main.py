#Gerador de jogos da Mega Sena simples
import random
qtd = int (input('Quantos jogos você quer: '))
for j in range(0, qtd):
  jogo = sorted(random.sample(range(1,60), 6))
  print(f'{j+1}º jogo: {jogo}')
              