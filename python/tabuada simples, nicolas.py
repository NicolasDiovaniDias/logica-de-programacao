while True:
    numero=int(input("numero: "))
    if numero<=0 :
        print("fim")
        break
    for cont in range(1,11):
        print(numero,"x",cont,"=",numero*cont)