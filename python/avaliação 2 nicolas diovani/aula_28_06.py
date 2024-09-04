def escolha():
    continua=["S","N"]
    graus=input("qual voce deseja converter?\n1)-celcius-fahrenheit\n2)-fahrenheit-celcius")
    if graus=="1":
        while True:
            while True:
                try:
                    c=float(input("digite temperatura em celcius: "))
                    break
                except:
                    print("digite certo!!!")
            def fahrenheit(Celcius):
                fahrenheit= (Celcius*9/5)+32
                return fahrenheit
            print(round(fahrenheit(c),2))
            break
    elif graus=="2":
        while True:
            while True:
                try:
                    f=float(input("digite a temperatura em fahrenheit: "))
                    break
                except:
                    print("digite certo!!!")

            def celcius(Fahrenheit):
                celcius= (Fahrenheit-32)/1.8
                return celcius
            print(round(celcius(f),2))
            break
    cont="x"
    while cont not in continua:
        cont=input("Continua [S/N]?").upper()
        if cont=='N':
            break
        if cont=='S':
            escolha()
escolha()