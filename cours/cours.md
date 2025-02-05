# 1. Introduction aux Algorithmes

## 1.1 Définition et Importance des Algorithmes

Un **algorithme** est une suite finie d'instructions bien définies permettant de résoudre un problème ou d'accomplir une tâche. Il peut être exprimé sous différentes formes : langage naturel, pseudo-code, diagramme de flux ou langage de programmation.

### **Importance des Algorithmes**
- **Efficacité** : Permet de résoudre des problèmes complexes en un temps raisonnable.
- **Optimisation** : Réduction du temps d'exécution et de la consommation des ressources.
- **Automatisation** : Exécution répétée et fiable sans intervention humaine.
- **Universalité** : Application dans divers domaines (informatique, mathématiques, physique, etc.).

## 1.2 Historique et Évolution

### **Les Premiers Algorithmes**
- **Antiquité** : Algorithme d'Euclide (~300 av. J.-C.) pour le calcul du PGCD.
- **Moyen Âge** : Al-Khwârizmî (~IXe siècle), dont le nom a donné naissance au terme "algorithme".
- **XVIIe - XIXe siècle** : Développement des mathématiques algorithmiques (Newton, Gauss, etc.).

### **Ère Moderne**
- **1936** : Alan Turing propose la machine de Turing, modèle abstrait du calcul.
- **1940-1950** : Développement des premiers ordinateurs et langages de programmation.
- **1970-1980** : Apparition des concepts de complexité algorithmique et classification des problèmes.
- **1990 - Aujourd'hui** : Avancées en intelligence artificielle, algorithmes distribués et quantiques.

## 1.3 Notion d’Efficacité et d’Optimalité

### **Efficacité d'un Algorithme**
L'efficacité d'un algorithme est mesurée en fonction de :
- **Complexité en temps** : Nombre d'opérations nécessaires pour exécuter l'algorithme.
- **Complexité en espace** : Quantité de mémoire utilisée.

### **Optimalité**
Un algorithme est **optimal** s'il résout un problème en un minimum de ressources possibles (temps et espace). On évalue l'optimalité grâce aux bornes inférieures connues du problème.

### **Exemple : Tri de Tableaux**
- **Tri par sélection** : O(n²) en temps, peu optimal pour les grandes données.
- **Tri fusion** : O(n log n), plus efficace pour de grandes entrées.

L’étude de ces notions est essentielle pour concevoir des solutions informatiques performantes et adaptées aux besoins réels.

# 2. Modèles de Calcul

Les modèles de calcul sont des abstractions mathématiques permettant de formaliser la notion de calcul et de comprendre les limites de ce qui peut être calculé par une machine. Parmi ces modèles, la **Machine de Turing** occupe une place centrale.

## 2.1. Machine de Turing

La **Machine de Turing** est un modèle de calcul théorique proposé par **Alan Turing** en 1936. Elle joue un rôle fondamental dans la théorie de la calculabilité et la complexité des algorithmes.

### 2.1.1. Définition

Une machine de Turing est définie comme une séquence de composants suivants :

- **Un ruban infini** divisé en cases contenant des symboles.
- **Une tête de lecture/écriture**, capable de lire et d'écrire des symboles sur le ruban.
- **Un ensemble d'états internes** parmi lesquels un état initial et des états d'acceptation ou de rejet.
- **Une table de transition**, dictant les actions à entreprendre en fonction de l'état courant et du symbole lu.

### 2.1.2. Fonctionnement

Le fonctionnement de la machine de Turing repose sur les étapes suivantes :

1. La tête lit un symbole sur le ruban.
2. En fonction de l'état courant et du symbole lu, la machine :
   - Modifie le symbole courant (ou le laisse inchangé).
   - Déplace la tête vers la gauche ou la droite.
   - Change d'état interne.
3. Le processus se poursuit jusqu'à atteindre un état d'acceptation ou de rejet.

### 2.1.3. Importance et Applications

- **Théorie de la calculabilité** : La machine de Turing permet de définir ce qui est **calculable** et ce qui ne l'est pas.
- **Complexité algorithmique** : Elle sert de base à l'étude des classes de complexité (P, NP, etc.).
- **Langages formels** : Elle est utilisée pour modéliser les langages récursivement énumérables.
- **Informatique théorique** : De nombreux modèles modernes de calcul découlent des concepts de la machine de Turing.

### 2.1.4. Variantes de la Machine de Turing

- **Machine de Turing multi-rubans** : Utilise plusieurs rubans pour augmenter l'efficacité.
- **Machine de Turing non déterministe** : Peut effectuer plusieurs transitions simultanément.
- **Machine de Turing universelle** : Capable de simuler toute autre machine de Turing, fondement des ordinateurs modernes.

---

La machine de Turing constitue un outil essentiel pour comprendre les fondements de l'informatique et les limites du calcul. Elle reste une référence incontournable en théorie des algorithmes.
## 2.2. Automates et langages formels

### 2.2.1. Introduction aux langages formels
Un **langage formel** est un ensemble de chaînes de caractères construites à partir d'un alphabet donné. L'étude des langages formels est fondamentale en informatique théorique, notamment pour la compilation et la reconnaissance de motifs.

### 2.2.2. Les Alphabets, Mots et Langages
- **Alphabet (\(\Sigma\))** : Un ensemble fini de symboles.
- **Mot** : Une suite finie de symboles appartenant à un alphabet.
- **Langage** : Un sous-ensemble de l’ensemble de tous les mots possibles sur un alphabet donné (\(\Sigma^*\)).

Exemple :
Si \(\Sigma = \{a, b\}\), alors quelques mots possibles sont \("a"\), \("b"\), \("ab"\), \("ba"\), etc.

### 2.2.3. Classes de Langages
Les langages sont classés selon la **hiérarchie de Chomsky** :
1. **Langages réguliers** (Reconnaissables par des automates finis)
2. **Langages contextuels** (Reconnaissables par des automates à pile)
3. **Langages sensibles au contexte**
4. **Langages récursivement énumérables** (Reconnaissables par une machine de Turing)

### 2.2.4. Automates Finis
Un **automate fini** est un modèle mathématique permettant de représenter des systèmes à états finis. Il est défini par un quintuplet \( (Q, \Sigma, \delta, q_0, F) \) où :
- \(Q\) : Ensemble fini d’états
- \(\Sigma\) : Alphabet d’entrée
- \(\delta\) : Fonction de transition \( Q \times \Sigma \to Q \)
- \(q_0\) : État initial
- \(F\) : Ensemble d’états acceptants

Il existe deux types d’automates :
- **Automates finis déterministes (DFA)** : Une seule transition possible par symbole.
- **Automates finis non déterministes (NFA)** : Plusieurs transitions possibles.

Exemple de DFA :
```
      a       b
  --> (q0) --- a ---> (q1)
```

### 2.2.5. Expressions Régulières et Automates Finis
Les **expressions régulières** sont utilisées pour décrire les langages réguliers. Par exemple :
- \(a^*b\) représente des mots contenant zéro ou plusieurs \("a"\) suivis d’un \("b"\).

### 2.2.6. Automates à Pile et Langages Contextuels
Un **automate à pile** est une extension d’un automate fini qui possède une mémoire sous forme de **pile**. Il permet de reconnaître les langages contextuels définis par une **grammaire hors-contexte**.

Exemple de langage hors-contexte :
- \(L = \{a^n b^n | n \geq 0\}\), qui ne peut pas être reconnu par un automate fini, mais l’est par un automate à pile.

### 2.2.7. Machines de Turing et Langages Récursivement Énumérables
Une **machine de Turing** est un modèle plus puissant capable de reconnaître des langages plus complexes. Elle est définie par :
- Une bande infinie pour la mémoire
- Une tête de lecture/écriture
- Un ensemble fini d’états et une fonction de transition

Les machines de Turing sont essentielles pour définir la **décidabilité** et la **calculabilité** en informatique.

### 2.2.8. Applications des Automates et Langages Formels
- **Compilateurs** : Analyse lexicale et syntaxique
- **Moteurs de recherche** : Traitement des requêtes
- **Sécurité informatique** : Détection de patterns malveillants
- **Traitement du langage naturel** : Reconnaissance de la syntaxe


## 2.3. Modèle RAM (Random Access Machine)

Le **modèle RAM (Random Access Machine)** est un modèle abstrait de calcul utilisé pour analyser la complexité des algorithmes en considérant un ordinateur idéal disposant d'une mémoire infinie et d'un processeur exécutant des instructions élémentaires en temps constant.

### 2.3.1. Définition du Modèle RAM
Le modèle RAM repose sur plusieurs hypothèses simplificatrices :
- La machine dispose d’une **mémoire infinie** divisée en cellules accessibles par adresse.
- Chaque cellule peut contenir un entier ou une valeur de taille fixe.
- Les **opérations élémentaires** (addition, soustraction, multiplication, accès mémoire, etc.) s’exécutent en **temps constant**.
- Il n'y a pas de **gestion de cache**, de **hiérarchie mémoire** ou de **parallélisme**.

### 2.3.2. Structure d’un Programme RAM
Un programme dans le modèle RAM est constitué d'une **suite d’instructions**, similaires aux instructions d’un processeur classique :
- **Opérations arithmétiques** : addition, soustraction, multiplication, division.
- **Accès mémoire** : lecture et écriture en mémoire par adresse.
- **Instructions de contrôle** : conditions, boucles, branchements.
- **Opérations logiques** : ET, OU, NON.

### 2.3.3. Comparaison avec d’Autres Modèles
| Modèle | Avantages | Inconvénients |
|--------|----------|--------------|
| **RAM** | Simple et intuitif pour l’analyse de complexité | Ne prend pas en compte les contraintes matérielles réelles |
| **Machine de Turing** | Théorique et universellement applicable | Peu pratique pour l’analyse d’algorithmes réels |
| **Modèle de calcul parallèle** | Permet d’étudier les architectures modernes | Plus complexe que le modèle RAM |

### 2.3.4. Limites et Critiques
Bien que largement utilisé en analyse algorithmique, le modèle RAM présente plusieurs **limitations** :
- **Supposition irréaliste** d’un temps d’exécution constant pour toutes les opérations.
- **Ignorance des contraintes matérielles**, comme la hiérarchie de mémoire (cache, RAM, disque).
- **Absence de parallélisme**, alors que la majorité des processeurs modernes sont multicœurs.

### 2.3.5. Utilisation en Analyse de Complexité
Malgré ses limitations, le modèle RAM reste un outil fondamental pour :
- **Analyser la complexité des algorithmes** indépendamment du matériel.
- **Établir des bornes de performance** en utilisant les notations asymptotiques (O, Ω, Θ).
- **Comparer différents algorithmes** dans un cadre standardisé.

### 2.3.6. Conclusion
Le **modèle RAM** est un cadre simplifié mais puissant pour l’analyse algorithmique. Il permet de comprendre et comparer les performances des algorithmes sans se soucier des détails matériels. Toutefois, dans des contextes pratiques, des modèles plus avancés peuvent être nécessaires pour une analyse plus fine.

# 3. Analyse de la Complexité des Algorithmes

L'analyse de la complexité des algorithmes permet d'évaluer leurs performances en fonction de la taille de l'entrée. Elle est essentielle pour comparer différentes solutions à un même problème et choisir l'algorithme le plus efficace. 

## 3.1. Notations asymptotiques (O, Ω, Θ)

Les notations asymptotiques permettent de caractériser le comportement d'un algorithme lorsqu'il est appliqué à des entrées de grande taille. Elles définissent des bornes sur le temps d'exécution ou l'utilisation de la mémoire.

### **3.1.1. Notation O (O grand) : borne supérieure**
La notation **O (big-O)** donne une borne supérieure sur la croissance d'une fonction. Elle représente le pire cas d'exécution d'un algorithme.

- Forme mathématique :
  $$ f(n) = O(g(n)) \text{ si et seulement si } \exists c > 0, \exists n_0 > 0, \forall n \geq n_0, \quad f(n) \leq c \cdot g(n) $$
- Exemple :
  - Si un algorithme s'exécute en **f(n) = 3n² + 2n + 5**, alors **f(n) = O(n²)** car il existe une constante c telle que **f(n) ≤ c ⋅ n²** pour des valeurs suffisantes de n.

### **3.1.2. Notation Ω (Oméga) : borne inférieure**
La notation **Ω (Omega)** donne une borne inférieure sur la croissance d'une fonction. Elle représente le meilleur cas d'exécution d'un algorithme.

- Forme mathématique :
  $$ f(n) = Ω(g(n)) \text{ si et seulement si } \exists c > 0, \exists n_0 > 0, \forall n \geq n_0, \quad f(n) \geq c \cdot g(n) $$
- Exemple :
  - Pour **f(n) = 5n + 10**, on peut dire que **f(n) = Ω(n)** car il existe une constante c telle que **f(n) ≥ c ⋅ n**.

### **3.1.3. Notation Θ (Thêta) : borne serrée**
La notation **Θ (Theta)** donne une borne asymptotique **exacte** sur la croissance d'une fonction. Un algorithme est **Θ(g(n))** si et seulement si il est à la fois **O(g(n))** et **Ω(g(n))**.

- Forme mathématique :
  $$ f(n) = Θ(g(n)) \text{ si et seulement si } \exists c_1, c_2 > 0, \exists n_0 > 0, \forall n \geq n_0, \quad c_1 \cdot g(n) \leq f(n) \leq c_2 \cdot g(n) $$
- Exemple :
  - Pour **f(n) = 4n² + 3n + 7**, on peut dire que **f(n) = Θ(n²)** car il existe des constantes c1 et c2 telles que **c1 ⋅ n² ≤ f(n) ≤ c2 ⋅ n²**.

### **3.1.4. Relation entre O, Ω et Θ**

- **O(g(n))** : Donne une borne **supérieure**
- **Ω(g(n))** : Donne une borne **inférieure**
- **Θ(g(n))** : Donne une borne **exacte** (si une fonction est à la fois O et Ω de la même fonction g(n))

Exemple visuel de relation entre ces notations :

```
 O(n²)      Θ(n²)      Ω(n²)
  |---------|---------|
      Croissance de f(n)
```

En pratique, on utilise surtout **O(n)** pour exprimer la complexité d'un algorithme, car elle donne une estimation du pire cas.

## 3.2. Complexité en temps et en espace

### 3.2.1. Définition de la Complexité
La complexité d’un algorithme mesure les ressources qu’il consomme en fonction de la taille de l’entrée. Les deux principales mesures de complexité sont :

- **Complexité en temps** : mesure le nombre d’opérations élémentaires exécutées.
- **Complexité en espace** : mesure la quantité de mémoire utilisée.

### 3.2.2. Complexité en Temps

#### Notation asymptotique
Pour analyser la complexité en temps, on utilise des notations asymptotiques :

- **O(f(n))** : Bornes supérieures (croissance maximale)
- **Ω(f(n))** : Bornes inférieures (croissance minimale)
- **Θ(f(n))** : Encadrement serré (croissance exacte)

#### Types de complexités courantes
| Complexité | Notation | Exemple |
|------------|----------|----------------|
| Constante  | O(1)     | Accès à un élément dans un tableau |
| Logarithmique | O(log n) | Recherche dichotomique |
| Linéaire   | O(n)     | Parcours d’un tableau |
| Quadratique | O(n²)   | Algorithme de tri par insertion |
| Exponentielle | O(2ⁿ) | Algorithme de backtracking |

### 3.2.3. Complexité en Espace
La complexité en espace représente la quantité de mémoire utilisée par un algorithme en fonction de la taille de l’entrée.

#### Mémoire utilisée
Elle se décompose en :
- **Espace fixe** : mémoire utilisée indépendamment de l’entrée (variables, constantes, code du programme).
- **Espace variable** : mémoire dépendant de l’entrée (tableaux, structures de données dynamiques).

#### Exemples
| Algorithme | Complexité en espace |
|------------|--------------------|
| Recherche linéaire | O(1) |
| Tri fusion | O(n) |
| Algorithmes récursifs | O(n) à O(n²) selon le stockage de l’appel récursif |

### 3.2.4. Relation entre Complexité en Temps et en Espace
Il existe souvent un compromis entre l’espace et le temps. Par exemple, utiliser une table de hachage (O(1) en temps) peut nécessiter plus de mémoire qu’une recherche linéaire (O(n) en temps mais O(1) en mémoire).

### 3.2.5. Optimisation de la Complexité
- **Optimisation en temps** : Algorithmes efficaces (ex: tri fusion au lieu de tri bulle)
- **Optimisation en espace** : Structures de données adaptées (ex: utilisation d’arbres équilibrés au lieu de matrices pleines)

---

Cette section fournit un aperçu de la complexité en temps et en espace et souligne l’importance d’une analyse approfondie pour choisir l’algorithme le plus adapté.

## 3.3. Classes de complexité (P, NP, NP-complet, NP-dur)

### 3.3.1. Introduction aux Classes de Complexité
La théorie de la complexité vise à classer les problèmes informatiques en fonction de la quantité de ressources (temps et espace) nécessaires pour les résoudre. Parmi ces classifications, les classes **P**, **NP**, **NP-complet** et **NP-dur** sont fondamentales en informatique théorique.

---

### 3.3.2. Classe P (Polynomial Time)
La classe **P** regroupe les problèmes qui peuvent être résolus par un algorithme déterministe en **temps polynomial**.

- Un algorithme est dit **polynomial** s'il existe un entier **k** tel que le temps d'exécution soit **O(n^k)**, où **n** est la taille de l'entrée.
- Ces problèmes sont considérés comme **traitables efficacement**.

**Exemples de problèmes dans P :**
- Tri d'un tableau (**Tri Fusion, Tri Rapide**) → **O(n log n)**
- Recherche du plus court chemin dans un graphe pondéré (**Dijkstra**) → **O(n^2)** ou **O(m + n log n)** avec tas de Fibonacci

---

### 3.3.3. Classe NP (Nondeterministic Polynomial Time)
La classe **NP** contient les problèmes pour lesquels une **solution peut être vérifiée en temps polynomial** par un algorithme déterministe.

- Un problème appartient à **NP** si, étant donné une solution candidate, nous pouvons la vérifier en **O(n^k)**.
- Un algorithme non-déterministe pourrait résoudre ces problèmes en **temps polynomial** en utilisant la **devinette** d’une solution correcte.

**Exemples de problèmes dans NP :**
- **Problème du Voyageur de Commerce (TSP)** : vérifier si un circuit d’un coût donné existe prend un temps polynomial.
- **Problème de la Satisfiabilité Booléenne (SAT)** : vérifier si une affectation satisfait une formule booléenne est faisable en temps polynomial.

---

### 3.3.4. Problèmes NP-complets (NP-C)
Un problème est **NP-complet** s’il est **à la fois dans NP et NP-dur**.

- Il s’agit des problèmes les plus difficiles de **NP**.
- Si un algorithme polynomial était trouvé pour un problème NP-complet, alors **P = NP** (ce qui reste une question ouverte en informatique théorique).

**Méthode pour prouver qu’un problème est NP-complet :**
1. Montrer qu'il est dans **NP** (vérification en temps polynomial possible).
2. Faire une **réduction polynomiale** depuis un problème NP-complet connu.

**Exemples de problèmes NP-complets :**
- **SAT (Satisfiabilité Booléenne)** (le premier problème prouvé NP-complet, théorème de Cook).
- **Problème du Sac à Dos** (optimisation combinatoire).
- **Problème du Voyageur de Commerce (TSP, version décisionnelle)**.

---

### 3.3.5. Problèmes NP-durs (NP-Hard)
Un problème est **NP-dur** s’il est **au moins aussi difficile** que les problèmes de **NP**, mais il **n'a pas nécessairement besoin d'appartenir à NP**.

- Ces problèmes peuvent être **plus difficiles** que NP-complets.
- Ils peuvent ne pas avoir de solutions vérifiables en temps polynomial.
- Certains peuvent même être **indécidables**.

**Exemples de problèmes NP-durs :**
- **Problème du Voyageur de Commerce (TSP, version optimisation)**.
- **Problème d’optimisation du Sac à Dos**.
- **Résolution générale des jeux vidéo (ex: Échecs, Go, Sudoku avec une grille infinie)**.

---

### 3.3.6. Schéma Résumé des Relations entre P, NP, NP-complet et NP-dur
```
      P ⊆ NP
      NP-complet ⊆ NP
      NP-dur ⊇ NP-complet
```
- Tous les problèmes de **P** sont dans **NP**.
- Les **problèmes NP-complets** sont les plus difficiles de **NP**.
- Les **problèmes NP-durs** peuvent être **hors de NP**, car ils ne nécessitent pas d’avoir une solution vérifiable en temps polynomial.

---

### 3.3.7. Conclusion
L’étude de ces classes de complexité est cruciale pour comprendre la difficulté intrinsèque des problèmes et déterminer s’ils sont solubles efficacement. La question **P = NP** reste l’un des plus grands mystères en mathématiques et en informatique théorique.
