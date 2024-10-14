def fibonacci_sequence(num):
    fib_sequence = [0, 1]
    while fib_sequence[-1] < num:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    return fib_sequence

def check_fibonacci(num):
    fib_sequence = fibonacci_sequence(num)
    if num in fib_sequence:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} NÃO pertence à sequência de Fibonacci."

try:
    user_input = int(input("Digite um número: "))
    resultado = check_fibonacci(user_input)
    print(resultado)
except ValueError:
    print("Por favor, insira um número válido.")
