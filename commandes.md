# Commandes du projet

## 1. Vérifier la version de Python

```bash
python --version
```

## 2. Exécuter le programme

```bash
python main.py
```

## 3. Résultat attendu

Le programme affiche la liste des livres avec leur nombre de pages, puis calcule le nombre total de pages des livres situés aux indices 1 à 3.

## 4. Structure de données utilisée

- Liste Python pour stocker les livres.
- Arbre de segments pour calculer rapidement la somme des pages sur un intervalle.

## 5. Complexité

- Construction de l'arbre : O(n)
- Requête sur un intervalle : O(log n)
