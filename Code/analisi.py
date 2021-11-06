import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import scipy.stats
import seaborn as sns

# Funcio per a llegir dades en format csv
def load_dataset(path):
    dataset = pd.read_csv(path, header=0, delimiter=',')
    return dataset


#Establir els titols de cada grafica
title_x = []
file = open("../titols_columnes.txt",'r')
for linea in file:
    title_x.append(linea)
file.close()
title_x = np.array(title_x)
title_y = np.array(["Popularity"])

#Carregar dades de la BDD
dataset = load_dataset("../BDD/q1.csv","../BDD/q2.csv","../BDD/q3.csv","../BDD/q4.csv")
data = dataset.values