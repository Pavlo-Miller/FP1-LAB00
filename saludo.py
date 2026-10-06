from datetime import datetime
nombre = input("Introduce tu nombre:")
hora_actual = datetime.now().hour
if hora_actual < 12:
    print(f"Buenos Dias, {nombre}")
elif hora_actual > 12 and hora_actual < 20:
    print(f"Buenas tardes, {nombre}")
elif hora_actual > 20 and hora_actual < 23:
    print(f"Buenas noches, {nombre}")