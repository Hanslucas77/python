class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def error(self):
        raise Exception("Caractere inválido.")

    def advance(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            elif self.current_char.isdigit():
                return ('NUMERO', self.integer())
            elif self.current_char.isalpha():
                return self.id_or_keyword()
            elif self.current_char == ';':
                self.advance()
                return (';', ';')
            elif self.current_char == '+':
                self.advance()
                return ('+', '+')
            elif self.current_char == '-':
                self.advance()
                return ('-', '-')
            elif self.current_char == '*':
                self.advance()
                return ('*', '*')
            elif self.current_char == '/':
                self.advance()
                return ('/', '/')
            elif self.current_char == '^':
                self.advance()
                return ('^', '^')
            elif self.current_char == '(':
                self.advance()
                return ('(', '(')
            elif self.current_char == ')':
                self.advance()
                return (')', ')')
            elif self.current_char == '>':
                self.advance()
                return ('>', '>')
            elif self.current_char == ',':
                self.advance()
                return (',', ',')
            elif self.current_char == '{':
                self.advance()
                return ('{', '{')
            elif self.current_char == '}':
                self.advance()
                return ('}', '}')
            elif self.current_char == '=':
                self.advance()
                return ('=', '=')
            else:
                self.error()
        return ('EOF', None)

    def id_or_keyword(self):
        result = ''
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()
        if result in ['int', 'real', 'while', 'if', 'else']:
            return (result, result)
        return ('ID', result)


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.index = -1
        self.advance()

    def advance(self):
        self.index += 1
        if self.index < len(self.tokens):
            self.current_token = self.tokens[self.index]
        else:
            self.current_token = ('EOF', None)

    def match(self, token_type):
        if self.current_token[0] == token_type:
            self.advance()
        else:
            raise SyntaxError(f"Erro de sintaxe: esperava '{token_type}', obteve '{self.current_token[0]}'")

    def programa(self):
        self.declaracoes()
        self.comandos()

    def declaracoes(self):
        while self.current_token[0] in ['int', 'real']:
            self.declaracao()
            self.match(';')

    def declaracao(self):
        self.match(self.current_token[0])  # tipo
        self.lista_variaveis()

    def lista_variaveis(self):
        self.match('ID')
        while self.current_token[0] == ',':
            self.match(',')
            self.match('ID')

    def comandos(self):
        while self.current_token[0] != 'EOF' and self.current_token[0] != '}':
            if self.current_token[0] == 'ID':
                self.atribuicao()
            elif self.current_token[0] == 'while':
                self.repeticao()
            elif self.current_token[0] == 'if':
                self.fluxo_controle()
            else:
                raise SyntaxError(f"Erro de sintaxe: token inesperado '{self.current_token[0]}'")

    def atribuicao(self):
        self.match('ID')
        self.match('=')
        self.expressao()
        self.match(';')

    def repeticao(self):
        self.match('while')
        self.match('(')
        self.expressao_relacional()
        self.match(')')
        self.match('{')
        self.comandos()
        self.match('}')

    def fluxo_controle(self):
        self.match('if')
        self.match('(')
        self.expressao_relacional()
        self.match(')')
        self.match('{')
        self.comandos()
        self.match('}')
        if self.current_token[0] == 'else':
            self.match('else')
            self.match('{')
            self.comandos()
            self.match('}')

    def expressao(self):
        self.termo()
        while self.current_token[0] in ['+', '-', '*', '/']:
            self.match(self.current_token[0])
            self.termo()

    def termo(self):
        self.fator()
        while self.current_token[0] == '^':
            self.match('^')
            self.fator()

    def fator(self):
        if self.current_token[0] == 'ID' or self.current_token[0] == 'NUMERO':
            self.match(self.current_token[0])
        elif self.current_token[0] == '(':
            self.match('(')
            self.expressao()
            self.match(')')
        else:
            raise SyntaxError("Erro de sintaxe: fator esperado")

    def expressao_relacional(self):
        self.expressao()
        self.advance()
        self.expressao()


text = "int x; int y; while (a > b) { x = x + y; }"
lexer = Lexer(text)
tokens = []
while True:
    token = lexer.get_next_token()
    if token[0] == 'EOF':
        break
    tokens.append(token)

try:
    parser = Parser(tokens)
    parser.programa()
    print("Análise sintática bem-sucedida!")
except SyntaxError as e:
    print(f"Erro de sintaxe: {e}")
