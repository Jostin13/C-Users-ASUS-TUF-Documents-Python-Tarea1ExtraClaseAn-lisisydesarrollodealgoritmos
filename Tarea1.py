if __name__ == '__main__':
    llamada = int()
    print("Ingrese los Minutos de su Llamada : ")
    llamada = int(input())
    if (llamada<=5):
        print("COSTO POR LLAMADA ES : ",llamada*0.9)
    else:
        print("COSTO POR LLAMADA ES : ",(5*0.9)+((llamada-5)*1.1))
        