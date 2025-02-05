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

