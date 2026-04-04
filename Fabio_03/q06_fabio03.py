def main():
    for i in range(1, 11):
        escrever_tabuada(i)

  
def escrever_tabuada(n):
    print("----------------------------------------------------------------------------------")
    for i in range(1, 11):
        adi = i + n
        sub = (n + i) - n
        div = (n * i) / n
        mul = i * n
        print(f"{i} + {n} = {adi} | {n + i} - {n} = {sub} | {n * i} / {n} = {div:.2f} | {i} * {n} = {mul}")


main()