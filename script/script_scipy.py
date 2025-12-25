import scipy.io
import matplotlib.pyplot as plt

# Chargement du fichier
mat = scipy.io.loadmat("MatFileVisualizer/data/Box.mat")

# Récupération des structures
names = mat["name"]
dataInfo = mat["dataInfo"]
data_2 = mat["data_2"]

# Décodage simple (tronqué ou pas, on s'en fiche)
var_names = []
for i, row in enumerate(names):
    try:
        name = "".join(chr(c) for c in row if c != 0)
    except:
        name = f"var_{i}"
    var_names.append(name)

# Listage de toutes les variables
print("Variables détectées :")
for i, v in enumerate(var_names):
    print(f"{i}: {v}")

# Temps (première ligne de data_2)
time = data_2[0, :]

# Affichage automatique 3 à 5 courbes
plt.figure()
count = 0
for var_index in range(1, len(var_names)):  # commence à 1 pour éviter le temps
    if count >= 5:
        break
    try:
        data_row = abs(dataInfo[var_index, 1]) - 1
        values = data_2[data_row, :]
        plt.plot(time, values, label=var_names[var_index])
        count += 1
    except Exception:
        continue

plt.xlabel("Temps (s)")
plt.ylabel("Valeurs")
plt.title("Variables représentatives (SciPy)")
plt.legend()
plt.grid()
plt.show()
