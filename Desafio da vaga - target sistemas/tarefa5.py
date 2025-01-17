# Inverte os caracteres de uma string sem usar funções prontas.
def inverte_string(s):
    invertida = ''
    for char in s:
        invertida = char + invertida  # Adiciona cada caractere ao início da nova string.
    return invertida

string_original = "Exemplo de string"
print(f"String original: {string_original}")
print(f"String invertida: {inverte_string(string_original)}")