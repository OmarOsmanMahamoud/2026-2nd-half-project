# 2026 Second Half Project

## Présentation

Ce dépôt regroupe mon principal projet personnel pour la seconde moitié de l'année 2026.

L'objectif est de développer une simulation gravitationnelle du Système solaire qui deviendra progressivement de plus en plus complète, à mesure que j'apprends de nouvelles notions en physique, en analyse numérique et en informatique.

Le projet sera développé en **Python** dans un premier temps afin de valider les idées et les algorithmes, puis réimplémenté en **C++** afin d'améliorer mes compétences en programmation scientifique et de produire une version plus performante.

Je me donne jusqu'au **31 décembre 2026** pour faire évoluer ce projet en ajoutant progressivement de nouvelles fonctionnalités, au rythme de mon apprentissage.

---

# Philosophie du projet

Ce projet n'a pas pour objectif d'être terminé rapidement.

Il est conçu comme un **journal d'apprentissage**.

À chaque nouvelle notion découverte, je tenterai de l'intégrer dans la simulation. L'idée est de documenter non seulement le résultat final, mais également le chemin parcouru pour y parvenir.

---

# Ce que j'ai appris jusqu'à présent

Depuis le **9 juillet 2026**, ce projet m'a déjà conduit à découvrir plusieurs concepts importants.

### Analyse numérique

* Les méthodes **RK2** et **RK4** ne désignent pas une unique méthode, mais une **famille d'intégrateurs**.
* En mettant à jour la vitesse avant la position, la méthode d'Euler devient un **Euler symplectique**, beaucoup plus adapté aux simulations hamiltoniennes à long terme.

Ces points ont été clarifiés grâce aux échanges avec la communauté de **Computational Science Stack Exchange (SciComp)**.

### Algorithmique

En souhaitant accélérer la simulation gravitationnelle à l'aide de l'algorithme de **Barnes–Hut**, j'ai réalisé qu'il me manquait une notion fondamentale en informatique : les **arbres**.

Avant de pouvoir implémenter Barnes–Hut, je vais donc apprendre les structures de données associées :

* arbres ;
* arbres binaires ;
* quadtrees.

Cette découverte fait partie intégrante du projet : chaque difficulté rencontrée devient une occasion d'apprendre un nouveau concept.

---

# Objectifs

Au fil des mois, cette simulation intégrera progressivement de nouvelles fonctionnalités, parmi lesquelles :

* amélioration des intégrateurs numériques ;
* optimisation des performances ;
* implémentation de Barnes–Hut ;
* développement parallèle en Python et en C++ ;
* découverte et utilisation de nouvelles structures de données ;
* amélioration continue de l'architecture du code.

---

# État d'esprit

Je considère ce projet comme une exploration de la physique computationnelle.

L'objectif n'est pas seulement d'obtenir une simulation fonctionnelle, mais aussi de comprendre les méthodes numériques, les algorithmes et les structures de données qui rendent ce type de simulation possible.

Chaque obstacle rencontré représente une nouvelle étape d'apprentissage, qui sera intégrée au projet au fur et à mesure de son évolution.

## État actuel du projet

À l'heure actuelle, seule une première version **Python** de la simulation est disponible. Elle repose sur un algorithme naïf en **O(N²)** utilisant une double boucle pour calculer les interactions gravitationnelles entre le Soleil et les huit planètes du Système solaire.

Cette version constitue une base de travail qui sera progressivement enrichie au fil de l'avancement du projet. Elle sera notamment améliorée sur le plan de la visualisation : les trajectoires actuellement affichées sous forme de graphiques statiques évolueront vers de véritables animations à l'aide de **`matplotlib.animation.FuncAnimation`**, dans le but de développer également ma maîtrise de l'écosystème Python.

La version **C++** du projet sera développée progressivement, à mesure que j'acquerrai les notions d'informatique et les structures de données nécessaires (arbres, quadtrees, etc.). L'objectif n'est pas simplement de traduire le code Python, mais de tirer parti du C++ pour construire une implémentation plus performante et mieux adaptée aux simulations gravitationnelles de grande taille.

Ce dépôt est donc pensé comme un projet évolutif, où chaque nouvelle fonctionnalité, optimisation ou structure de données apprise sera intégrée au fur et à mesure de ma progression en physique computationnelle, en analyse numérique et en informatique.
