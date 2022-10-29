import time

def main():
    tiempo = time.localtime()
    horaActual = tiempo.tm_hour
    minutoActual = tiempo.tm_min
    if horaActual > 19:
        print("Hora de ir a casa")
    else:
        print ("Quedan {} horas y {} minutos para irnos a casa".format(18- int(horaActual), 59-int(minutoActual)))

if __name__ == "__main__":
    main()