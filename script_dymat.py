from DyMat import DyMatFile
import matplotlib.pyplot as plt
import numpy as np

# ------------------------------
# Chargement du fichier Dymola
# ------------------------------
filename = "ACDC.mat" 
data = DyMatFile(filename)

# ------------------------------
# Listage de toutes les variables
# ------------------------------
variables = list(data.names())
print("Variables disponibles :")
for i, v in enumerate(variables):
    print(f"{i}: {v}")

# ------------------------------
# Calcul de la dynamique de chaque variable
# ------------------------------
# La dynamique = max(value) - min(value)
dynamic_scores = []
valid_variables = []

for var_name in variables:
    try:
        time, values = data.getVarArray([var_name])
        values = values.flatten()
        if len(values) > 1:  # ignorer les constantes
            score = np.max(values) - np.min(values)
            dynamic_scores.append(score)
            valid_variables.append(var_name)
    except KeyError:
        continue

# ------------------------------
#  Sélection des 5 variables les plus dynamiques
# ------------------------------
top_indices = np.argsort(dynamic_scores)[-5:][::-1]  # 5 plus grandes variations
top_variables = [valid_variables[i] for i in top_indices]

print("\n5 variables les plus dynamiques :")
for v in top_variables:
    print(" -", v)

# ------------------------------
# Traçage des courbes
# ------------------------------
plt.figure(figsize=(10,6))
for var_name in top_variables:
    time, values = data.getVarArray([var_name])
    values = values.flatten()
    plt.plot(time, values, label=var_name)

plt.xlabel("Temps (s)")
plt.ylabel("Valeurs")
plt.title("5 variables les plus dynamiques")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
