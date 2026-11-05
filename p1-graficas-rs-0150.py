import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fb = ["Facebook", 8833, True, 2006]
twt = ["Twitter", 8575, False, 2008]
ig = ["Instagram", 7575, True, 2010]
wsp = ["Whatsapp", 8828, True, 2009]
tel = ["Telegram", 2992, False, 2010]
lkn = ["Linkedin", 7277, False, 2012]

# Creamos una lista de listas
lista_redes_sociales = [fb, twt, ig, wsp, tel, lkn]

# Crear el DataFrame con pandas (pd) y el argumento columns correcto
df_redes_sociales = pd.DataFrame(
    lista_redes_sociales, 
    columns=["Nombre", "Cantidad", "Es_FB", "Años"]
)
print(df_redes_sociales)
# Guardar en CSV
df_redes_sociales.to_csv("redessociales.csv", index=False)
# Crear grafica de lineas
# Donde x es nombre en el eje horizontal
# Donde Y es Cantidad en el eje vertical
plt.plot(df_redes_sociales["Nombre"],df_redes_sociales["Cantidad"])
plt.title("Grafica Redes sociales 0150")
plt.xlabel("Nombre de la redes sociales")
plt.ylabel("Cantidad de usuarios")
plt.show()
# Creamos una grafica de puntos
plt.scatter(df_redes_sociales["Nombre"],df_redes_sociales["Cantidad"])
plt.show()
# Grafica de barras
plt.bar(df_redes_sociales["Nombre"],df_redes_sociales["Cantidad"])
plt.title("Grafica Redes sociales 0150")
plt.xlabel("Nombre de la redes sociales")
plt.ylabel("Cantidad de usuarios")
plt.show()
# Ordenar las graficas de barras de manera descendente
# De la mas grande a la pequeña
df_rs_ordenar=df_redes_sociales.sort_values("Cantidad",ascending=False)
plt.bar(df_rs_ordenar["Nombre"],df_rs_ordenar["Cantidad"],
        color=["b", "g", "c", "m", "y","r"])
plt.show()
print("Programa realizado por Zavala Medina Alexia Paola | NC = 0150")

# Grafica de pastel

plt.plot(df_redes_sociales["Nombre"],df_redes_sociales["Cantidad"])
plt.pie(df_redes_sociales["Cantidad"],labels=df_redes_sociales["Nombre"])
plt.show()