# 1. The Role of Algorithms in Computing
## 1.1 Algorithms Exercices
### 1.1.1
Describe your own real-world example that requires sorting.

Trier par ordre de prix des objets a vendre sur Leboncoin

Describe one that requires finding the shortest distance between two points.

Trouver le meilleur chemin pour ce déplacer en voiture

### 1.1.2
Other than speed, what other measures of effciency might you need to consider in a real-world setting?

La consomation d'essences, l'état de la route
### 1.1.3
Select a data structure that you have seen, and discuss its strengths and limitations.


### 1.1.4
How are the shortest-path and traveling-salesperson problems given above similar?

The travelling salesman problem asks the following question: "Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city?

Dans les deux cas on doit trouver le chemin le plus rapide

How are they different?

Ils sont differents puisque la solution a chaque probléme n'est pas forcement la même, la solution du voyageur de commerce n'est pas forcement le chemin le plus court
### 1.1.5
Suggest a real-world problem in which only the best solution will do. 

Calculer le dosage exact d'un médicament en fonction du poids du patient pour éviter un surdosage ou un sous-dosage.

Then come up with one in which "approximately" the best solution is good enough.

Trouver une place de parking dans une ville : on ne cherche pas forcément la meilleure place possible, juste une qui soit suffisamment proche
### 1.1.6
Describe a real-world problem in which sometimes the entire input is available before you need to solve the problem, but other times the input is not entirely available in advance and arrives over time.

Entrée disponible en avance : Planifier un emploi du temps scolaire avant la rentrée, car toutes les matières, les salles et les professeurs sont connus.
Entrée qui arrive au fil du temps : Gérer les commandes d’un service de livraison en temps réel, car de nouvelles commandes arrivent constamment

## 1.2 Algorithms as a technology
### 1.2.1
Give an example of an application that requires algorithmic content at the application level, and discuss the function of the algorithms involved.

Un exemple d'application nécessitant un traitement algorithmique est la planification optimale des zones de pêche pour maximiser la capture tout en minimisant la consommation de carburant.

Rôle des algorithmes :

    Algorithmes d'optimisation de trajet (Dijkstra, A)* : Trouver le chemin le plus court entre le port et les zones de pêche tout en minimisant la consommation de carburant.

    Algorithmes de prédiction (réseaux neuronaux, arbres de décision) : Analyser les données environnementales (température de l'eau, courants, données satellites) pour prédire les zones les plus riches en poissons.

    Algorithmes d'allocation de ressources (Branch and Bound, programmation linéaire) : Gérer la répartition des navires sur les différentes zones de pêche.


### 1.2.2
Suppose that for inputs of size n on a particular computer, insertion sort runs in $8n^2$ steps and merge sort runs in $64nlog(n)$ steps. For which values of n does insertion sort beat merge sort?

On cherche n pour que:

$8n^2 < 64nlog(n)$
<br>
$n < 8log(n)$
<br>
En résolvant numériquement avec ce programme python:

```python
import math
n=1
while True:
    n+=1
    calcul=8*math.log(n,2)
    if n >=calcul:
        print(n)
        print(calcul)
        break

```
Je trouve n = 44


### 1.2.3
What is the smallest value of n such that an algorithm whose running time is $100n^2$ runs faster than an algorithm whose running time is $2^n$ on the same machine?

On cherche le plus petit n pour lequel :$100n^2<2^n$

On peut résoudre le problème en python:

```python

n=1
while True:
    n+=1
    calcul1=100*n**2
    calcul2=2**n
    if calcul1 < calcul2:
        print(n)
        print(calcul1,calcul2)
        break

```
Je trouve n=15


## Problems
### 1.1 Comparison of running times
For each function f(n) and time t in the following table, determine the largest
size n of a problem that can be solved in time t , assuming that the algorithm to
solve the problem takes f(n) microseconds.

|           | 1 second | 1 minute | 1 hour   | 1 month  | 1 year   | 1 century|
| ----------| ---------|--------  |--------  |--------  |--------  |--------  |
| log(n)    |          |          |          |          |          |          | 
| $sqrt(n)$ |          |          |          |          |          |          |
| $n$       |          |          |          |          |          |          |
| $nlog(n)$ |          |          |          |          |          |          |
| $n^2$     |          |          |          |          |          |          |
| $n^3$     |          |          |          |          |          |          |
| $2^n$     |          |          |          |          |          |          |
| $n!$      |          |          |          |          |          |          |


#### 1. $f(n)= log(n)$

On cherche n pour lequel: $log(n) \le T$ , avec T en microseconds et log en base 2

$n \le 2^T$

On résout pour chaque cas du tableau:

#### $sqrt(n)$ 

On cherche n pour lequel: $sqrt(n) \le T$ , avec T en microseconds et log en base 2

$n \le T^2$

On résout pour chaque cas du tableau:

#### $n$ 

On cherche n pour lequel: $n \le T$ , avec T en microseconds et log en base 2

$n \le T$

On résout pour chaque cas du tableau:


#### $nlog(n)$ 

On cherche n pour lequel: $nlog(n) \le T$ , avec T en microseconds et log en base 2

On résout pour chaque cas du tableau:











