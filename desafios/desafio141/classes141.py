class Aluno:
    def __init__(self, nome, curso, serie):
        self.nome = nome
        self.curso = curso
        self.serie = serie

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class JSON:
    def exportar(self, dados):
        from json import dumps # dumps é usado para converter um objeto Python em uma string JSON

        lista = []
        for item in dados:
            lista.append(item.__dict__)
        texto = dumps(lista, ensure_ascii=False, indent=2) # ensure_ascii=False: permite que os caracteres especiais sejam exibidos corretamente, indent=2: adiciona indentação para melhor legibilidade
        return texto

class XML:
    def exportar(self, dados):
        import xml.etree.ElementTree as ET # ElementTree (ET) é uma biblioteca para criar e manipular documentos XML

        nome = dados[0].__class__.__name__.lower()
        pai = ET.Element("dados") # O elemento pai é o elemento raiz do documento XML, "dados" é o nome do elemento raiz fixo.
        for item in dados:
            filho = ET.SubElement(pai, nome) # O elemento filho é o nome da classe do objeto, em minúsculo. ET.SubElement cria um novo elemento filho dentro do elemento pai.
            for chave, valor in item.__dict__.items():
                neto = ET.SubElement(filho, chave) # O elemento neto é o nome do atributo do objeto. ET.SubElement cria um novo elemento neto dentro do elemento filho.
                neto.text = str(valor) # O texto do elemento neto é o valor do atributo do objeto, convertido para string.
        ET.indent(pai, space="\t") # A função ET.indent adiciona indentação ao documento XML para melhor legibilidade, usando tabulação como espaço de indentação.
        texto = ET.tostring(pai, encoding="unicode", xml_declaration=True)
        return texto

def exportarDados(formato, dados):
    print(formato.exportar(dados))