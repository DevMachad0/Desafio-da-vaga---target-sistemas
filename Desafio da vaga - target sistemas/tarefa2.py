# Gera a sequência de Fibonacci até um valor dado e verifica se um número pertence a ela.
def fibonacci_sequence(n):
    a, b = 0, 1
    sequence = [a, b]
    while b < n:
        a, b = b, a + b
        sequence.append(b)
    return sequence

# Verifica se um número faz parte da sequência gerada.
def is_fibonacci_number(num):
    sequence = fibonacci_sequence(num)
    return num in sequence, sequence

number = 21  # Informe o número desejado
belongs, sequence = is_fibonacci_number(number)
print(f"Sequência de Fibonacci: {sequence}")
if belongs:
    print(f"O número {number} pertence à sequência de Fibonacci.")
else:
    print(f"O número {number} não pertence à sequência de Fibonacci.")
