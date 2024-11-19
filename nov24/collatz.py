def collatz(numero: int) -> int:
    """
    Funzione per calcolare la coniettura Collatz, definita:

    """
    if numero % 2 == 0:
        return (numero // 2)
    else:
        return (numero * 3 + 1)

 collatz_number = int(input("valore: "))

 counter = 0
 while collatz_number > 1:
         counter = counter + 1
         collatz_number = collatz(collatz_number)
         print(f"Numero: {collatz_number} - numero di calcolo: {counter}")
