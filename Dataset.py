# importamos las librerías necesarias 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import chardet
import numpy as np


Ds_Pokemon = pd.read_csv("Datos/dataset.csv")
Ds_Pokedex = pd.read_csv("Datos/pokedex.csv")
file_path = "C:\Users\gonra\Downloads\archive.zip\pokemon.csv"
with open(file_path, "rb") as f:
    result = chardet.detect(f.read())
df_Pokemon2 = pd.read_csv(file_path, encoding=result["encoding"], on_bad_lines="skip")
columnas_drop= ["TIPO_1",
                "TIPO_2",
                "PUNTOS_VELOCIDAD",
                "NOMBRE_GENERATIONS",
                "LEGENDARIO"]
Ds_Pokedex2 = Ds_Pokedex.drop(columns=columnas_drop)
columnas_drop2 = [abilities,
                  against_bug,
                  against_dark,
                  against_dragon,
                  against_electric,
                  against_fairy,
                  against_fight,
                  against_fire,
                  against_flying,
                  against_ghost,
                  against_grass,
                  against_ground,
                  against_ice,
                  against_normal,
                  against_poison,
                  against_psychic,
                  against_rock,
                  against_steel,
                  against_water,
                  attack,
                  base_egg_steps,
                  base_happiness,
                  base_total,
                  capture_rate,
                  classfication,
                  defense,
                  experience_growth,
                  height_m,
                  hp,japanese_name,name,percentage_male,pokedex_number,sp_attack,sp_defense,speed,type1,type2,weight_kg,generation,is_legendary
                  
                  
                  
                  ]