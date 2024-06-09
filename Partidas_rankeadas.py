""" Crie uma função que recebe como parâmetro a quantidade de vitórias e derrotas de um jogador,
depois disso retorne o resultado para uma variável, o saldo de Rankeadas deve ser feito através do calculo (vitórias - derrotas)

Se vitórias for menor do que 10 = Ferro
Se vitórias for entre 11 e 20 = Bronze
Se vitórias for entre 21 e 50 = Prata
Se vitórias for entre 51 e 80 = Ouro
Se vitórias for entre 81 e 90 = Diamante
Se vitórias for entre 91 e 100= Lendário
Se vitórias for maior ou igual a 101 = Imortal

## Saída

Ao final deve se exibir uma mensagem:
"O Herói tem de saldo de **{saldoVitorias}** está no nível de **{nivel}**"
  """


def nivel_rank(vitorias, derrotas):
    nivel_da_rank = float(vitorias) - float(derrotas) 
    return nivel_da_rank


def classificador(vic, losers):
    nivel = nivel_rank(vic, losers)

    if (nivel <= 10):       
        return 'FERRO'

    elif (11 <= nivel <= 20):
        return 'BRONZE'

    elif (21 <= nivel <= 50):
        return 'PRATA'

    elif (51 <= nivel <= 80):
        return 'OURO'

    elif (81 <= nivel <= 90):
        return 'DIAMANTE'
    
    elif (91 <= nivel <= 100):
        return 'LENDARIO'
        
    elif (nivel >= 101):
        return "IMORTAL"
      



vitorias = input('Informe o numero de vitorias do jogador')
derrotas = input('informe o numro de derrotas do jogador')

print("O Herói tem de saldo de {} está no nível de {}".format(nivel_rank(vitorias, derrotas), classificador(vitorias, derrotas)))