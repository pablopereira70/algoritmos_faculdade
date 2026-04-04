def main():
    n = int(input('Digite o número de termos: '))

    den = 1
    for i in range(1, n + 1):
        s = den / i
        den += 2
        print(s)


main()