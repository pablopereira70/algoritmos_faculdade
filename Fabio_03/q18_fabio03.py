def main():
    n = int(input('Digite o número de termos: '))

    sub = 0
    for i in range(1, n + 1):
        s = i / (i - sub)
        sub += 1
        print(s)


main()