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

## 3.4. Réduction polynomiale et problèmes NP-complets

### 3.4.1. Définition de la réduction polynomiale
La **réduction polynomiale** est une technique utilisée en théorie de la complexité pour comparer la difficulté des problèmes algorithmiques. Un problème \( A \) est dit **réductible polynomialement** à un problème \( B \) (noté \( A \leq_P B \)) s'il existe une fonction \( f \) calculable en temps polynomial telle que :

\[ x \in A \iff f(x) \in B \]

Cela signifie que si nous savons résoudre \( B \) efficacement, alors nous pouvons également résoudre \( A \) en transformant ses instances en instances de \( B \) via \( f \).

### 3.4.2. Importance de la réduction polynomiale
La réduction polynomiale joue un rôle crucial dans la classification des problèmes en **NP-complets**. Pour montrer qu'un problème est NP-complet, il faut :

1. Montrer qu'il appartient à la classe NP (on peut vérifier une solution en temps polynomial).
2. Montrer qu'un problème déjà connu comme NP-complet peut être réduit polynomialement à ce problème.

Si ces deux conditions sont satisfaites, alors le problème est aussi difficile que tous les autres problèmes NP-complets.

### 3.4.3. Exemples de problèmes NP-complets
Voici quelques problèmes classiques prouvés NP-complets via réduction polynomiale :

- **Problème du voyageur de commerce (TSP) :** Donnée une liste de villes et les distances entre elles, trouver le plus court chemin qui visite chaque ville exactement une fois et revient au point de départ.
- **Problème de la couverture de sommets :** Trouver un sous-ensemble minimal de sommets couvrant toutes les arêtes d'un graphe.
- **Problème de la satisfaction booléenne (SAT) :** Trouver une affectation des variables qui satisfait une formule booléenne donnée.
- **Problème du sac à dos (Knapsack) :** Sélectionner des objets avec une valeur et un poids, de sorte à maximiser la valeur totale sans dépasser une capacité donnée.

### 3.4.4. Conséquences et impact
La notion de réduction polynomiale est essentielle car elle permet d'identifier des problèmes difficiles en pratique. Si un problème est NP-complet, alors sauf si **P = NP**, il n'existe pas d'algorithme en temps polynomial pour le résoudre dans le cas général. 

Cela guide la recherche vers des approches alternatives comme :
- **Heuristiques** : Algorithmes qui donnent des solutions approximatives en un temps raisonnable.
- **Algorithmes d'approximation** : Garantissent une solution proche de l’optimum avec une borne sur l’erreur.
- **Méthodes exactes exponentielles** : Comme la programmation dynamique et le branch-and-bound.

### 3.4.5. Conclusion
La réduction polynomiale est un outil fondamental en informatique théorique. Elle permet d'identifier des problèmes difficiles et de mieux comprendre la structure de la classe NP. Si un jour un algorithme polynomial est découvert pour un problème NP-complet, alors **P = NP**, ce qui révolutionnerait l'informatique et la cryptographie !

# 4. Paradigmes Algorithmiques

Les **paradigmes algorithmiques** sont des stratégies générales utilisées pour concevoir des algorithmes efficaces. Ils permettent de résoudre une large gamme de problèmes en adoptant des approches spécifiques adaptées à la structure du problème. Parmi les paradigmes les plus connus, on retrouve :

- **Diviser pour régner**  
- **Programmation dynamique**  
- **Algorithmes gloutons**  
- **Retour sur trace (Backtracking)**  
- **Recherche locale et heuristiques**  

Nous allons explorer en détail le premier paradigme : **Diviser pour régner**.

---

## 4.1. Diviser pour régner

Le paradigme **Diviser pour régner** (Divide and Conquer) consiste à résoudre un problème en le décomposant en sous-problèmes plus petits, en résolvant ces sous-problèmes de manière récursive, puis en combinant leurs solutions pour obtenir la solution globale.

### Principe général

Un algorithme basé sur **Diviser pour régner** suit généralement trois étapes :

1. **Diviser** : Le problème est divisé en plusieurs sous-problèmes plus petits (généralement de taille équivalente).  
2. **Régner** : Les sous-problèmes sont résolus de manière récursive.  
3. **Combiner** : Les solutions des sous-problèmes sont fusionnées pour obtenir la solution finale.

### Complexité et analyse

Si nous notons :
- **T(n)** : le temps d'exécution de l'algorithme pour un problème de taille **n**,
- **a** : le nombre de sous-problèmes créés à chaque étape,
- **b** : le facteur par lequel la taille des sous-problèmes est réduite,

alors la complexité suit généralement la **récurrence de Master** :

\[
T(n) = aT(n/b) + f(n)
\]

où **f(n)** représente le coût du travail effectué en dehors des appels récursifs (par exemple, la fusion des solutions).

### Exemples d'algorithmes utilisant ce paradigme

- **Tri fusion (Merge Sort)**  
  - Divise le tableau en deux sous-tableaux de tailles égales.
  - Trie récursivement chaque sous-tableau.
  - Fusionne les sous-tableaux triés.
  - Complexité : **O(n log n)**.

- **Tri rapide (Quick Sort)**  
  - Choisit un pivot et partitionne le tableau en deux sous-tableaux.
  - Trie récursivement les sous-tableaux.
  - Complexité moyenne : **O(n log n)** (pire cas **O(n²)**).

- **Recherche dichotomique (Binary Search)**  
  - Divise le tableau en deux parties égales.
  - Vérifie si l'élément recherché est dans la première ou la seconde moitié.
  - Réduit la taille du problème par un facteur **2** à chaque étape.
  - Complexité : **O(log n)**.

- **Algorithme de Strassen (multiplication de matrices)**  
  - Décompose la multiplication de matrices en 7 multiplications de sous-matrices au lieu de 8.
  - Complexité : **O(n^{2.81})**, améliorant l'algorithme naïf **O(n³)**.

---

### Avantages et inconvénients

✅ **Avantages :**  
- Efficace pour les problèmes récursifs.  
- Permet des solutions optimisées avec une complexité logarithmique ou quasi-linéaire.  
- Exploite bien la parallélisation.

❌ **Inconvénients :**  
- Peut entraîner un **coût en mémoire élevé** dû aux appels récursifs et au stockage temporaire des sous-problèmes.  
- Le choix d'une bonne stratégie de division est essentiel pour l'efficacité.  

---

Le paradigme **Diviser pour régner** est une technique puissante utilisée dans de nombreux algorithmes de tri, de recherche et d'optimisation. D'autres paradigmes comme la **programmation dynamique** ou les **algorithmes gloutons** offrent des alternatives selon la nature du problème.

## 4.2. Programmation Dynamique

### 1. Introduction à la Programmation Dynamique

La **programmation dynamique** est une technique d'optimisation qui permet de résoudre des problèmes en les décomposant en sous-problèmes plus petits et en stockant les résultats intermédiaires pour éviter des calculs redondants. Elle est particulièrement utile lorsque les sous-problèmes se répètent dans le processus de résolution.

### 2. Principe Fondamental

Un problème peut être résolu par programmation dynamique si :
- Il possède une **structure optimale** : une solution optimale du problème global est composée de solutions optimales des sous-problèmes.
- Il présente une **redondance des sous-problèmes** : les mêmes sous-problèmes apparaissent plusieurs fois.

### 3. Approches de la Programmation Dynamique

Il existe deux approches principales :

#### a) **Approche Top-Down (Mémoïsation)**
Cette approche repose sur la récursivité avec stockage des résultats des sous-problèmes déjà calculés. Cela évite de recalculer les mêmes sous-problèmes plusieurs fois.

**Exemple : Fibonacci avec mémoïsation**
```python
# Implémentation en Python avec mémoïsation
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

print(fibonacci(10))  # Résultat : 55
```

#### b) **Approche Bottom-Up (Tabulation)**
L'approche bottom-up consiste à résoudre les sous-problèmes en premier, puis à construire progressivement la solution finale.

**Exemple : Fibonacci avec tabulation**
```python
# Implémentation en Python avec tabulation
def fibonacci(n):
    if n <= 1:
        return n
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]

print(fibonacci(10))  # Résultat : 55
```

### 4. Exemples Classiques de Programmation Dynamique

#### a) **Problème du Sac à Dos (0/1 Knapsack)**
Un voleur a un sac d'une certaine capacité et doit choisir des objets avec des valeurs et des poids différents afin d'obtenir la valeur maximale sans dépasser la capacité du sac.

#### b) **Plus Longue Sous-Séquence Commune (LCS - Longest Common Subsequence)**
Ce problème consiste à trouver la plus longue sous-séquence commune entre deux chaînes de caractères.

#### c) **Problème du Rendu de Monnaie**
Trouver le nombre minimal de pièces pour donner une somme spécifique en utilisant des pièces de valeurs données.

### 5. Complexité et Optimisation

L'utilisation de la programmation dynamique permet souvent de réduire la complexité exponentielle à une complexité polynomiale. Cependant, il faut faire attention à la consommation mémoire. Des techniques comme la **programmation dynamique en espace optimisé** permettent de réduire l'utilisation de mémoire en stockant uniquement les résultats nécessaires.

### 6. Conclusion

La programmation dynamique est un outil puissant pour résoudre une large gamme de problèmes en informatique. Bien que son implémentation nécessite une analyse approfondie des sous-problèmes et de la structure optimale, elle permet d'obtenir des solutions efficaces en optimisant les performances computationnelles.

## 4.3. Algorithmes Gloutons

### Définition
Un **algorithme glouton** (ou **greedy algorithm**) est une stratégie algorithmique qui fait des choix successifs en sélectionnant, à chaque étape, l'option qui semble être la meilleure à court terme, sans tenir compte des conséquences futures.

### Principe de fonctionnement
L'approche gloutonne suit généralement ces étapes :
1. **Sélection d’un choix optimal localement** : choisir la meilleure option immédiate disponible.
2. **Vérification de la faisabilité** : s'assurer que le choix respecte les contraintes du problème.
3. **Construction progressive d’une solution** : répéter le processus jusqu'à obtenir une solution complète.

### Conditions d’applicabilité
Un algorithme glouton donne une solution optimale uniquement si le problème satisfait **l’une des deux propriétés suivantes** :
- **Propriété de sous-structure optimale** : une solution optimale du problème global peut être obtenue à partir de solutions optimales de sous-problèmes.
- **Propriété du choix glouton** : un choix optimal local conduit toujours à une solution optimale globale.

Si ces conditions ne sont pas remplies, l’algorithme peut produire une solution sous-optimale.

### Exemples d’algorithmes gloutons

#### 1. **Problème du rendu de monnaie**
L’objectif est de rendre une somme donnée avec le moins de pièces possible. Un algorithme glouton choisit à chaque étape la pièce de plus grande valeur disponible.

**Exemple en euros :**
- Somme à rendre : 63 centimes
- Pièces disponibles : {50, 20, 10, 5, 2, 1} centimes
- Solution gloutonne : 50 + 10 + 2 + 1 (4 pièces)

⚠️ **Attention** : Cet algorithme ne fonctionne pas toujours pour des systèmes monétaires où des combinaisons non triviales donnent un meilleur résultat.

#### 2. **Problème du sac à dos fractionnaire (Knapsack Fractionnaire)**
- Un voleur doit choisir des objets à mettre dans un sac à dos de capacité limitée.
- Chaque objet a un poids et une valeur.
- L’objectif est de maximiser la valeur totale des objets dans le sac.
- Un algorithme glouton prend toujours l’objet ayant **le meilleur rapport valeur/poids** en premier.
- Pour le cas fractionnaire (où l’on peut prendre une partie d’un objet), la solution gloutonne est **optimale**.

#### 3. **Algorithme de Dijkstra**
L’algorithme de Dijkstra, utilisé pour trouver le plus court chemin dans un graphe pondéré, suit une approche gloutonne en choisissant **le sommet ayant la plus petite distance courante**.

#### 4. **Algorithme de Prim**
L’algorithme de Prim construit un **arbre couvrant minimal** en ajoutant à chaque étape l’arête de plus faible poids connectant un nouveau sommet à l’arbre en construction.

### Avantages et inconvénients
✅ **Avantages**
- Facile à comprendre et implémenter.
- Rapide et efficace pour certains problèmes.
- Fonctionne bien lorsque les propriétés optimales sont vérifiées.

❌ **Inconvénients**
- Ne garantit pas toujours une solution optimale.
- Peut nécessiter une preuve formelle pour vérifier sa validité.
- Certains problèmes nécessitent une approche plus avancée comme la programmation dynamique.

### Conclusion
Les algorithmes gloutons sont puissants pour certains types de problèmes mais ne sont pas universellement applicables. Ils sont souvent utilisés lorsque les décisions locales garantissent une solution optimale globale. Lorsqu’ils échouent, il est souvent nécessaire d’avoir recours à des approches comme la **programmation dynamique** ou la **recherche exhaustive**.

## 4.4. Retour sur trace (Backtracking)

### 1. Introduction au Backtracking
Le **retour sur trace** (ou *backtracking*) est une technique algorithmique qui explore toutes les solutions possibles à un problème en construisant une solution incrémentalement. Lorsqu'une branche explorée mène à une impasse, l'algorithme revient en arrière ("backtrack") pour explorer une autre possibilité.

### 2. Principe du Backtracking
Le backtracking suit un schéma récursif où l'on :
1. Construit une solution partielle.
2. Vérifie si elle satisfait les contraintes du problème.
3. Si oui, on poursuit avec l'étape suivante.
4. Si non, on revient en arrière pour essayer une autre possibilité.

Le **backtracking** est particulièrement efficace pour les problèmes combinatoires, où l'on cherche à générer toutes les solutions possibles et à en valider certaines.

### 3. Exemples d'Applications
Le **backtracking** est utilisé dans plusieurs domaines, notamment :
- **Le problème des huit reines** (placer 8 reines sur un échiquier sans qu'elles ne s'attaquent)
- **Le Sudoku** (remplir une grille en respectant les contraintes)
- **Le problème du sac à dos** (optimisation combinatoire)
- **Les labyrinthes** (trouver un chemin dans un graphe)

### 4. Implémentation en Python
Voici un exemple simple du backtracking appliqué au **problème des N reines** :

```python
def est_safe(echiquier, ligne, col, n):
    for i in range(col):
        if echiquier[ligne][i] == 1:
            return False
    for i, j in zip(range(ligne, -1, -1), range(col, -1, -1)):
        if echiquier[i][j] == 1:
            return False
    for i, j in zip(range(ligne, n, 1), range(col, -1, -1)):
        if echiquier[i][j] == 1:
            return False
    return True

def resoudre_n_reines(echiquier, col, n):
    if col >= n:
        return True
    for i in range(n):
        if est_safe(echiquier, i, col, n):
            echiquier[i][col] = 1
            if resoudre_n_reines(echiquier, col + 1, n):
                return True
            echiquier[i][col] = 0  # Backtrack
    return False

def n_reines(n):
    echiquier = [[0] * n for _ in range(n)]
    if not resoudre_n_reines(echiquier, 0, n):
        print("Solution inexistante")
    else:
        for ligne in echiquier:
            print(" ".join(str(x) for x in ligne))

n_reines(8)
```

### 5. Complexité du Backtracking
La complexité du backtracking dépend du problème traité. Dans le pire des cas, il peut explorer toutes les solutions possibles, ce qui donne une complexité exponentielle **O(k^n)** pour un problème combinatoire à **n** étapes et **k** choix possibles à chaque étape.

Cependant, des optimisations comme **la branche et l’élagage (branch and bound)** ou l’**ordre de recherche heuristique** peuvent améliorer l'efficacité.

### 6. Conclusion
Le **backtracking** est une méthode puissante pour résoudre des problèmes combinatoires et de recherche. Bien que souvent coûteux en termes de temps d'exécution, il reste une approche essentielle lorsqu'une solution exacte est requise et que l'exploration exhaustive est envisageable.

## 4.5. Recherche locale et heuristiques

### 4.5.1. Introduction
La **recherche locale** et les **heuristiques** sont des approches permettant de trouver des solutions approximatives à des problèmes d’optimisation difficiles, souvent NP-durs. Contrairement aux méthodes exactes, ces approches ne garantissent pas nécessairement une solution optimale mais fournissent une solution satisfaisante en un temps raisonnable.

---

### 4.5.2. Recherche locale
La recherche locale explore l’espace des solutions en passant d’une solution à une autre par de petites modifications appelées **mouvements**. Elle est efficace pour les problèmes combinatoires comme le **voyageur de commerce** (TSP) ou le **problème de satisfaction de contraintes**.

#### Principes :
- Définition d’un **espace de solutions**.
- Utilisation d’une **fonction de coût** pour évaluer la qualité des solutions.
- Application d’un **mouvement local** pour passer d’une solution à une autre.

#### Exemples d’algorithmes de recherche locale :
1. **Descente de gradient (Hill Climbing)**  
   - À chaque étape, on passe à la meilleure solution voisine.
   - Risque de rester bloqué dans un **optimum local**.

2. **Recuit simulé (Simulated Annealing)**  
   - Inspiré du processus physique de refroidissement des métaux.
   - Introduit une probabilité d’accepter des solutions moins bonnes pour éviter les optima locaux.

3. **Recherche tabou (Tabu Search)**  
   - Maintient une liste des solutions récentes pour éviter de revenir en arrière.
   - Permet d’explorer plus efficacement l’espace des solutions.

---

### 4.5.3. Heuristiques
Les **heuristiques** sont des stratégies permettant de produire rapidement une solution satisfaisante en sacrifiant parfois l’optimalité. Elles sont souvent spécifiques à un problème donné.

#### Types d’heuristiques :
1. **Algorithmes gloutons (Greedy Algorithms)**  
   - Sélectionnent localement la meilleure option sans considération du futur.
   - Exemples : l’algorithme de Prim pour les arbres couvrants, Dijkstra pour les plus courts chemins.

2. **Méthodes basées sur des règles (Rule-based Methods)**  
   - Utilisation de règles heuristiques spécifiques au problème.
   - Exemple : heuristique du plus proche voisin pour le problème du voyageur de commerce.

3. **Algorithmes évolutionnaires et métaheuristiques**  
   - Inspirés des processus biologiques ou physiques.
   - Exemples : algorithmes génétiques, colonies de fourmis, optimisation par essaim de particules.

---

### 4.5.4. Comparaison et Applications
| Méthode                | Avantages                            | Inconvénients                      | Exemples d’application |
|------------------------|------------------------------------|------------------------------------|------------------------|
| Descente de gradient   | Simple, efficace pour certains problèmes | Bloqué dans les optima locaux | Problèmes de clustering, optimisation continue |
| Recuit simulé         | Évite les optima locaux, adaptable | Paramétrage délicat | Problèmes combinatoires |
| Recherche tabou       | Exploration plus large de l’espace | Coût mémoire plus élevé | Planification, ordonnancement |
| Algorithmes gloutons  | Rapide, implémentation simple | Ne donne pas toujours la solution optimale | Graphes, optimisation de réseau |
| Algorithmes évolutionnaires | Bonne exploration globale | Temps de calcul élevé | Machine learning, optimisation multi-objectifs |

---

### 4.5.5. Conclusion
Les algorithmes de **recherche locale** et les **heuristiques** sont essentiels pour résoudre efficacement des problèmes complexes. Bien que ces approches ne garantissent pas toujours l’optimalité, elles sont largement utilisées en intelligence artificielle, en recherche opérationnelle et en optimisation.

---
# 5. Structures de Données et Algorithmes Fondamentaux

## 5.1. Listes, Piles et Files

Les structures de données jouent un rôle crucial dans la conception des algorithmes. Parmi les plus fondamentales, on retrouve les **listes**, **piles** et **files**.

### 5.1.1. Listes
Une **liste** est une structure de données linéaire permettant de stocker une collection d’éléments. On distingue principalement :
- **Liste chaînée** : chaque élément (nœud) contient une valeur et un pointeur vers l’élément suivant.
- **Liste doublement chaînée** : chaque élément contient un pointeur vers l’élément précédent et suivant.
- **Liste circulaire** : le dernier élément pointe vers le premier.

📌 *Avantages* :
- Insertion et suppression rapides (O(1) pour une liste chaînée).
- Pas de taille fixe, contrairement aux tableaux.

📌 *Inconvénients* :
- Accès plus lent aux éléments (O(n) en moyenne).
- Surcharge mémoire due aux pointeurs.

### 5.1.2. Piles (*Stack*)
Une **pile** est une structure de données respectant le principe **LIFO** (*Last In, First Out*), où le dernier élément ajouté est le premier retiré.

**Opérations principales** :
- `push(x)`: ajoute un élément `x` au sommet.
- `pop()`: retire l’élément au sommet.
- `peek()`: consulte l’élément au sommet sans le retirer.

📌 *Applications* :
- Gestion des appels de fonctions (pile d’exécution).
- Annulation d’actions (Ctrl + Z).
- Évaluation d’expressions (notation postfixe).

### 5.1.3. Files (*Queue*)
Une **file** suit le principe **FIFO** (*First In, First Out*), où le premier élément ajouté est le premier retiré.

**Types de files** :
- **File simple** : ajout à l’arrière (*enqueue*), retrait à l’avant (*dequeue*).
- **File double (*Deque*)** : insertion et suppression possibles aux deux extrémités.
- **File de priorité** : les éléments sont extraits selon une priorité et non leur ordre d’arrivée.

📌 *Applications* :
- Gestion des tâches dans les systèmes d’exploitation.
- Algorithmes de parcours en largeur (*BFS*).
- Impression de documents en file d’attente.

---

Dans les sections suivantes, nous explorerons d’autres structures de données avancées comme les **arbres** et les **graphes**, ainsi que leurs algorithmes associés.
## 5.2. Arbres et Graphes

### 5.2.1. Définition et Terminologie

Un **graphe** est une structure composée de **sommets** (ou nœuds) et d'**arêtes** (ou arcs) reliant ces sommets. On distingue plusieurs types de graphes :

- **Graphe orienté** : les arêtes ont une direction.
- **Graphe non orienté** : les arêtes n'ont pas de direction.
- **Graphe pondéré** : chaque arête est associée à un poids.
- **Graphe connexe** : il existe un chemin entre chaque paire de sommets.

Un **arbre** est un cas particulier de graphe :

- C'est un graphe acyclique connexe.
- Un arbre avec \( n \) sommets possède exactement \( n-1 \) arêtes.
- Il possède une hiérarchie avec un sommet racine (dans le cas d'un arbre enraciné).

### 5.2.2. Représentation des Graphes

Il existe plusieurs manières de représenter un graphe en informatique :

1. **Liste d’adjacence** : chaque sommet est associé à une liste de ses voisins.
2. **Matrice d’adjacence** : une matrice \( n \times n \) où la case \( (i, j) \) indique la présence ou l'absence d'une arête entre les sommets \( i \) et \( j \).

Exemple d’une liste d’adjacence pour un graphe non orienté :

```
1 → [2, 3]
2 → [1, 4]
3 → [1, 4]
4 → [2, 3]
```

### 5.2.3. Parcours des Graphes

Les algorithmes de parcours permettent d’explorer un graphe :

- **Parcours en largeur (BFS - Breadth-First Search)** : explore les sommets niveau par niveau.
- **Parcours en profondeur (DFS - Depth-First Search)** : explore les sommets en profondeur avant de revenir en arrière.

#### Implémentation du BFS en Python

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node])
```

### 5.2.4. Applications des Graphes et Arbres

Les arbres et graphes sont utilisés dans de nombreux domaines :

- **Informatique** : modélisation des réseaux, intelligence artificielle.
- **Bioinformatique** : classification phylogénétique.
- **Transport** : planification des itinéraires.
- **Web** : structure des liens entre les pages (PageRank de Google).

## 5.3. Algorithmes de tri (tri fusion, rapide, tas, etc.)

Les algorithmes de tri sont essentiels en informatique, car ils permettent de réorganiser les éléments d'un tableau ou d'une liste selon un ordre donné (croissant ou décroissant). Plusieurs algorithmes existent, chacun ayant ses propres caractéristiques en termes de complexité temporelle et d'usage. Voici les algorithmes les plus utilisés :

### 1. Tri par fusion (Merge Sort)
Le tri par fusion est un algorithme de tri basé sur le paradigme "Diviser pour régner". Il divise récursivement le tableau en sous-tableaux de plus en plus petits jusqu'à obtenir des sous-tableaux de taille 1 (qui sont déjà triés). Ensuite, il fusionne les sous-tableaux triés pour obtenir le tableau final trié.

#### Complexité :
- **Complexité temporelle** : O(n log n)
- **Complexité spatiale** : O(n) (en raison de la mémoire supplémentaire utilisée pour stocker les sous-tableaux)

#### Fonctionnement :
1. Diviser le tableau en deux moitiés.
2. Trier chaque moitié récursivement.
3. Fusionner les deux moitiés triées pour obtenir un tableau trié.

### 2. Tri rapide (Quick Sort)
Le tri rapide est également un algorithme de tri "Diviser pour régner". Il sélectionne un "pivot" dans le tableau, partitionne le tableau en deux sous-tableaux (un avec des éléments plus petits que le pivot et l'autre avec des éléments plus grands) et trie ces sous-tableaux de manière récursive.

#### Complexité :
- **Complexité temporelle moyenne** : O(n log n)
- **Complexité temporelle dans le pire cas** : O(n²) (cela peut être évité en choisissant un bon pivot)
- **Complexité spatiale** : O(log n) en moyenne

#### Fonctionnement :
1. Choisir un pivot dans le tableau.
2. Partitionner le tableau en fonction du pivot (les éléments plus petits que le pivot à gauche et les plus grands à droite).
3. Trier récursivement les sous-tableaux à gauche et à droite du pivot.

### 3. Tri par tas (Heap Sort)
Le tri par tas utilise une structure de données appelée "tas" (ou "heap"). Un tas est un arbre binaire complet qui satisfait à la propriété de tas (le parent est plus grand ou plus petit que ses enfants, selon que l'on utilise un tas maximum ou minimum). Le tri par tas transforme d'abord le tableau en un tas, puis extrait les éléments un à un en ajustant le tas à chaque extraction.

#### Complexité :
- **Complexité temporelle** : O(n log n)
- **Complexité spatiale** : O(1)

#### Fonctionnement :
1. Convertir le tableau en un tas.
2. Extraire l'élément racine du tas (le plus grand ou le plus petit) et le placer à la fin du tableau.
3. Réajuster le tas et répéter jusqu'à ce que tous les éléments soient triés.

### 4. Tri par insertion (Insertion Sort)
Le tri par insertion est un algorithme simple où les éléments sont insérés un à un dans une portion triée du tableau. L'élément actuel est comparé avec les éléments déjà triés et est inséré à la bonne position.

#### Complexité :
- **Complexité temporelle dans le pire cas** : O(n²)
- **Complexité temporelle dans le meilleur cas** : O(n) (lorsque le tableau est déjà trié)
- **Complexité spatiale** : O(1)

#### Fonctionnement :
1. Commencer avec un tableau vide.
2. Parcourir le tableau et insérer chaque élément dans la partie triée du tableau en décalant les éléments nécessaires.

### 5. Tri par sélection (Selection Sort)
Le tri par sélection fonctionne en sélectionnant successivement l'élément le plus petit (ou le plus grand) dans la portion non triée du tableau et en l'échangeant avec l'élément en début de la portion non triée.

#### Complexité :
- **Complexité temporelle** : O(n²)
- **Complexité spatiale** : O(1)

#### Fonctionnement :
1. Trouver l'élément le plus petit dans le tableau non trié.
2. L'échanger avec le premier élément du tableau non trié.
3. Répéter ce processus pour chaque position du tableau.

### 6. Tri Shell (Shell Sort)
Le tri Shell est une amélioration du tri par insertion. Il permet de trier les éléments en utilisant une séquence de pas (gap) et en insérant les éléments dans des sous-listes définies par ces pas. Cela permet d'améliorer les performances par rapport au tri par insertion classique.

#### Complexité :
- **Complexité temporelle** : Varie en fonction de la séquence des pas, mais peut être O(n^(3/2)) ou O(n log² n) dans le meilleur des cas.
- **Complexité spatiale** : O(1)

#### Fonctionnement :
1. Sélectionner une séquence de pas.
2. Trier les éléments en utilisant ces pas, en insérant dans des sous-listes définies par les pas.
3. Réduire progressivement les pas jusqu'à atteindre 1, ce qui revient au tri par insertion classique.

### Conclusion
Les algorithmes de tri sont des outils fondamentaux en informatique, et le choix de l'algorithme dépend du contexte (taille du tableau, structure des données, etc.). Les algorithmes comme le tri fusion et le tri rapide sont largement utilisés en raison de leur efficacité, tandis que des algorithmes comme le tri par insertion et le tri par sélection peuvent être utiles pour de petites tailles de données ou des cas particuliers.

