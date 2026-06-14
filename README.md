# Nandael (NND)

Bem-vindo à documentação oficial da Nandael, uma linguagem de programação focada em simplicidade, clareza e poder de expressão. Na Nandael, quase todas as estruturas de controle são expressões, o que significa que elas produzem valores que podem ser armazenados diretamente em variáveis.

Abaixo, você encontrará o guia definitivo de uso da linguagem e a especificação da gramática.

## Variáveis e Atribuições

A declaração de variáveis é feita através da palavra-chave VAR. Por ser uma linguagem baseada em expressões, você pode atribuir valores estáticos ou o resultado de blocos inteiros de código.


    # Atribuição simples
    VAR idade = 27

    # Atribuição a partir de uma expressão condicional
    VAR preco = IF idade >= 18 THEN 40 ELSE 20


## Estruturas Condicionais (IF, ELIF, ELSE)

O IF suporta duas abordagens de sintaxe: Inline (linha única) e Multilinha (bloco).

### Sintaxe Inline

Ideal para avaliações rápidas. Não exige a palavra-chave END.



    IF x > 10 THEN PRINT("Maior") ELIF x == 10 THEN PRINT("Igual") ELSE PRINT("Menor")


### Sintaxe Multilinha (Blocos)

Usado para executar múltiplas instruções. Exige a palavra-chave END para fechar o escopo.


    IF idade >= 18 THEN
        PRINT("Maior de idade")
        VAR status = "Liberado"
    ELIF idade == 17 THEN
        PRINT("Quase lá")
    ELSE
        PRINT("Menor de idade")
    END


## Laços de Repetição (FOR e WHILE)

As estruturas de repetição da Nandael também suportam modos inline e multilinha, além de permitirem o uso das palavras-chave BREAK e CONTINUE.

### O Laço FOR

Itera sobre uma sequência de números. Você pode opcionalmente definir um passo com a palavra-chave STEP.

#### Inline (Exemplo de Fatorial):
    


    VAR result = 1
    FOR i = 1 TO 10 THEN result = result * i


#### Multilinha:



    FOR i = 0 TO 10 STEP 2 THEN 
        PRINT("Número par:")
        PRINT(i)
    END


### O Laço WHILE

Executa um bloco de código repetidamente enquanto a condição for verdadeira.



    VAR contador = 0
    WHILE contador < 10 THEN
        PRINT(contador)
        VAR contador = contador + 1
    END


## Funções (FUN)

Funções são declaradas com a palavra-chave FUN e podem ser nomeadas ou anônimas.

### Funções Inline (Expressão de Retorno)

Usam a seta -> para retornar o valor avaliado na mesma linha, sem necessidade de END ou RETURN.

    FUN soma(a, b) -> a + b

### Funções Multilinha

Quando há lógica complexa, o corpo da função é escrito em várias linhas, finalizado por END e retornando valores através de RETURN.

    FUN saudacao(nome)
        VAR mensagem = "Olá, " + nome
        PRINT(mensagem)
        RETURN mensagem
    END

## Entrada e Saída

A Nandael possui funções nativas (built-ins) para interação com o usuário:

- PRINT(valor): Exibe informações no terminal. É possível colocar múltiplas instruções na mesma linha separando com ponto e vírgula ;.

` PRINT("hello"); PRINT("world") 

# Especificação da Gramática (EBNF)
Para desenvolvedores interessados em entender a árvore de análise sintática (AST) e o parser da Nandael, segue a especificação técnica:
    
    statements  : NEWLINE* statement (NEWLINE+ statement)* NEWLINE*
    
    statement   : KEYWORD:RETURN expr?
                | KEYWORD:CONTINUE
                | KEYWORD:BREAK
                | expr
    
    expr        : KEYWORD:VAR IDENTIFIER EQ expr
                | comp-expr ((KEYWORD:AND|KEYWORD:OR) comp-expr)*
    
    comp-expr   : NOT comp-expr
                | arith-expr ((EE|LT|GT|LTE|GTE) arith-expr)*
    
    arith-expr  : term ((PLUS|MINUS) term)*
    term        : factor ((MUL|DIV) factor)*
    factor      : (PLUS|MINUS) factor | power
    power       : call (POW factor)*
    call        : atom (LPAREN (expr (COMMA expr)*)? RPAREN)?
    
    atom        : INT | FLOAT | STRING | IDENTIFIER
                | LPAREN expr RPAREN
                | list-expr
                | if-expr | for-expr | while-expr | func-def
    
    list-expr   : LSQUARE (expr (COMMA expr)*)? RSQUARE
    
    if-expr     : KEYWORD:IF expr KEYWORD:THEN
                  (statement if-expr-b | if-expr-c?)
                | (NEWLINE statements KEYWORD:END | if-expr-b | if-expr-c)
    
    if-expr-b   : KEYWORD:ELIF expr KEYWORD:THEN
                  (statement if-expr-b | if-expr-c?)
                | (NEWLINE statements KEYWORD:END | if-expr-b | if-expr-c)
    
    if-expr-c   : KEYWORD:ELSE statement
                | (NEWLINE statements KEYWORD:END)
    
    for-expr    : KEYWORD:FOR IDENTIFIER EQ expr KEYWORD:TO expr 
                  (KEYWORD:STEP expr)? KEYWORD:THEN statement
                | (NEWLINE statements KEYWORD:END)
    
    while-expr  : KEYWORD:WHILE expr KEYWORD:THEN statement
                | (NEWLINE statements KEYWORD:END)
    
    func-def    : KEYWORD:FUN IDENTIFIER? 
                  LPAREN (IDENTIFIER (COMMA IDENTIFIER)*)? RPAREN
                  (ARROW expr)
                | (NEWLINE statements KEYWORD:END)
     
`
