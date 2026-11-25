# Importa a função install do módulo rich.traceback, que melhora a exibição de erros e rastreamentos no terminal
from rich.traceback import install

# Ativa o rich traceback: a partir deste ponto, qualquer erro será exibido de forma colorida e detalhada,
# facilitando a identificação do problema, linha do erro e contexto do código
install()

# Função simples que realiza a divisão entre dois números
def divisao(x, y):
    return x / y  # Pode lançar ZeroDivisionError se y for zero

# Tenta dividir 50 por 0, o que gera uma exceção (ZeroDivisionError)
# Com o rich.traceback ativado, o erro será mostrado de forma mais clara e visual
print(divisao(50, 0))