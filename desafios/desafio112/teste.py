from desafio112.utilidadesCeV.moeda import resumo
from desafio112.utilidadesCeV.dado import leiaDinheiro

preco = leiaDinheiro('Digite um preço: R$ ')
resumo(preco, 20, 12)
