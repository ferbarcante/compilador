# constantes 
DIGITS = '0123456789'

# tokens
TT_INT = 'TT_INT'
TT_FLOAT = 'TT_FLOAT'
TT_PLUS = 'TT_PLUS'
TT_MINUS = 'TT_MINUS'
TT_MUL = 'TT_MUL'
TT_DIV = 'TT_DIV'
TT_LPAREN = 'TT_LPAREN'
TT_RPAREN = 'TT_RPAREN'

class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f'Token({self.type}, {self.value})'
    
    
class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
    
    def advance(self): 
        self.pos += 1
        self.current_char = self.text[pos] if self.pos < len(self.text) else None
        
    def generate_tokens(self):
        tokens = []
        
        while self.current_char != None: 
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())
            elif self.current_char == '+':
                tokens.append(Token(TT_PLUS))
                self.advance()
            elif self current_char == '-':
                tokens.append(Token(TT_MINUS))
                self.advance()
            elif self current_char == '*':
                tokens.append(Token(TT_MUL))
                self.advance()
            elif self current_char == '/':
                tokens.append(Token(TT_DIV))
                self.advance()
            else:
                # tratamento de erro
        return tokens
    
    def generate_number(self):
        num_str = ''
        dot_count = 0
        
        while self.current_char != None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1: break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
        
        if dot_count == 0:
            return Token(TT_INT, int(num_str))
        else: 
            return Token(TT_FLOAT, float)  