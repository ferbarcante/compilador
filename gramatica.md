#  Expressão IF

Na nossa linguagem o IF funcionara na seguinte estrutura:
`IF <condição> THEN <expressão>`
Também teremos a possibilidade de usar a palavra chave ELIF e ELSE no final
` IF <condição> THEN <expressão> ELIF <condição> THEN <expressão> ELSE <expressão>`
o if tambem aceita multiplas expressões quando digitado dessa maneira:
`IF <expressao THEN
    <expressao1>
    <expressao2>
    <expressao3>
END
`

Nossa linguagem será capaz de armazenar expressões em variáveis:
` VAR idade = 27`
`VAR preco = IF age >= 18 THEN 40 ELSE 20`

# Expressão FOR
implementação fatorial simples
`VAR result = 1
FOR i = 0 TO 10 THEN result = result * i`

o for tambem aceita multiplas expressões quando digitado dessa maneira:
`FOR i = 0 TO 10 THEN 
    <expressao1>
    <expressao2>
    <expressao3>
END
`
# While 
`WHILE <condition> THEN <expressão>`

# Função 
`FUN <nome>() -> <expressao> `
o fun tambem aceita multiplas expressões quando digitado dessa maneira:

`FUN <nome>()
    <expressao1>
    <expressao2>
    <expressao3>
END
`
# PRINT
`WRITE("hello"); WRITE("world")`