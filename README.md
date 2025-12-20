
# Documentation : Exploitation des fichiers `.mat` Dymola avec SciPy et DyMat

## 1. Contexte

Dans le cadre de l’analyse de modèles multiphysiques développés avec **Dymola**, nous disposons de fichiers de résultats au format `.mat`. Ces fichiers contiennent :

- La **variable temps** (`time`)
- Les **variables simulées** (tension, courant, température…)
- Les **métadonnées** : noms, descriptions, indices dans les matrices de données

L’objectif était de **lister les variables** et **visualiser les courbes des résultats** avec Python, en utilisant :

- `scipy.io` (SciPy)
- `DyMat` (bibliothèque spécialisée pour Dymola)

---

## 2. Utilisation de SciPy

### Approche

- Chargement du fichier `.mat` avec `scipy.io.loadmat`
- Extraction des matrices `name`, `dataInfo`, `data_1` et `data_2`
- Décodage des noms des variables (int8 → string)
- Tracé des courbes avec matplotlib

### Observations

- Les **noms des variables** sont souvent tronqués ou illisibles, surtout pour les fichiers Dymola générés avec `SaveAsPlotted` ou `SaveAsResult`.
- Les indices dans `dataInfo` sont **fragiles**, et certaines variables peuvent être mal associées à leurs données.
- Les valeurs **peuvent être correctes**, mais il est difficile d’identifier précisément quelle variable correspond à quoi.
- SciPy **ne gère pas automatiquement le temps ni les alias** des variables.
- Résultat : utile pour des tests rapides ou pour des fichiers `.mat` “standards”, mais **non fiable pour des analyses précises**.

---

## 3. Utilisation de DyMat

### Approche

- Chargement du fichier avec `DyMatFile`
- Lister les variables avec `names()`
- Récupération des valeurs et du temps avec `getVarArray()`
- Calcul des variables les plus dynamiques (variation max-min)
- Tracé des courbes avec matplotlib

### Observations

- DyMat **lit correctement les fichiers Dymola**, même ceux compressés ou encodés.
- Les **noms complets des variables** sont conservés (ex : `voltage.v`, `leak.i`).
- Gestion automatique du **temps**, des **alias** et des **variables dépendantes du temps**.
- Permet de sélectionner et visualiser les **variables les plus dynamiques** pour analyser le système.
- Résultat : fiable, robuste et directement exploitable pour **rapport et visualisation industrielle**.

---

## 4. Comparaison SciPy vs DyMat

| Critère                             | SciPy                   | DyMat                |
| ------------------------------------ | ----------------------- | -------------------- |
| Lecture fichiers `.mat`            | Oui, mais brut          | Oui, natif Dymola    |
| Noms variables                       | Tronqués ou illisibles | Corrects et complets |
| Gestion du temps                     | Manuelle                | Automatique          |
| Alias / variables constantes         | Non                     | Oui                  |
| Sélection variables dynamiques      | Manuelle                | Automatique possible |
| Fiabilité pour analyse industrielle | Faible                  | Très fiable         |

---

## 5. Conclusion

- Pour **tous fichiers `.mat` générés par Dymola**, DyMat est l’outil recommandé pour Python.
- SciPy peut être utilisé pour des tests rapides, mais **ne garantit pas l’intégrité des variables et des noms**.
- L’utilisation de DyMat permet de générer des **graphes fiables**, de **sélectionner les variables pertinentes** et d’avoir une **exploitation directe pour un rapport ou un outil de visualisation**.
- Le workflow final recommandé :
  1. Charger le fichier avec DyMat
  2. Lister toutes les variables
  3. Identifier les variables les plus dynamiques
  4. Tracer leurs courbes pour l’analyse ou le rapport
