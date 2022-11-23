print('start')

print('import ...')
import math
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime as dt
from tkinter import *
print('import klaar')

# Constanten
m_Aarde = 5.972e24                  # Massa Zon
r_Aarde = 6.371e6                   # Straal van de aarde
ds = 1000                           # stapjes van 1 kilometer

# Ariana 5 raket
m_Raket = 710e3                     # Massa van de Ariana 5 raket
d_Raket = 4.5                       # Diameter Ariana 5 raket
m_O2 = 130e3                        # 130 ton zuurstof
m_H2 = 26e3                         # 26 ton waterstof
DraagraketPrecentage = 0.9          # Draagraketten leveren 90% van het start vermogen
F_max_Start = 10.6e6                # Maximale kracht opgewekt bij de start: 10.600 kN
   



def standaard_data_van_bestand(bestandsnaam):
    data = pd.read_excel(bestandsnaam, decimal=',', usecols=["Hoogte km", "LuchtPercentage", "Luchtdruk mBar", "Luchtdichtheid kg/m3", "T kelvin"])
    Standaard_Tabel = pd.DataFrame(data, columns=["Hoogte km", "LuchtPercentage", "Luchtdruk mBar", "Luchtdichtheid kg/m3", "T kelvin"])
    Standaard_Tabel["Hoogte m"] = Standaard_Tabel["Hoogte km"]*1000
    Standaard_Tabel['F'] = F_max_Start
    return Standaard_Tabel

def test(Standaard_Tabel):
    # print(Standaard_Tabel['Hoogte m'], Standaard_Tabel['F'])
    plt.scatter(Standaard_Tabel['Hoogte km'], Standaard_Tabel['Luchtdruk mBar'])
    plt.show()

def main():
    bestandsnaam = 'Standaard_tabel.xlsx'
    Standaard_Tabel = standaard_data_van_bestand(bestandsnaam)
    test(Standaard_Tabel)

if __name__ == '__main__':
    print("running main")
    main()
