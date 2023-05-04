# importamos las librerías necesarias 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


Ds_Pokemon = pd.read_csv("Datos/dataset.csv")
Ds_Pokedex = pd.read_csv("Datos/pokedex.csv")
columnas_drop= ["TIPO_1",
                "TIPO_2",
                "PUNTOS_VELOCIDAD",
                "NOMBRE_GENERATIONS",
                "LEGENDARIO"]
Ds_Pokedex2 = Ds_Pokedex.drop(columns=columnas_drop)