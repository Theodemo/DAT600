import matplotlib.pyplot as plt
import numpy as np

class SortedMethods:
    def __init__(self, number_of_elements, visualization):
        self.arr = np.random.randint(1, 100, number_of_elements)
        self.steps = 0
        self.visualization = visualization

    def insertionSort(self):
        '''
        Tri par insertion
        
        Algorithme:
        1. Parcourir le tableau de la gauche vers la droite
        2. Pour chaque élément, le comparer avec les éléments précédents
        3. Si l'élément est plus petit, le déplacer vers la gauche
        4. Répéter les étapes 2 et 3 jusqu'à ce que l'élément soit à sa place

        return: list, tableau trié
        '''
        if self.visualization:
            fig, ax = plt.subplots()
        self.steps = 0
        for i in range(1, len(self.arr)):
            key = self.arr[i]
            j = i - 1
            
            while j >= 0 and key < self.arr[j]:
                self.arr[j + 1] = self.arr[j]
                j -= 1
                self.steps += 1  
                if self.visualization:
                    self._update_plot(ax)

            self.arr[j + 1] = key
            self.steps += 1  
            if self.visualization:
                self._update_plot(ax)

        if self.visualization:
            plt.show()
    def mergeSort(self, arr=None, left=0, right=None, ax=None):
        '''
        Tri fusion
        
        Algorithme:
        1. Diviser le tableau en deux parties
        2. Trier les deux parties récursivement
        3. Fusionner les deux parties triées
        4. Répéter les étapes 1 à 3 jusqu'à ce que le tableau soit trié

        param arr: list, tableau à trier
        param left: int, index de début du tableau
        param right: int, index de fin du tableau
        param ax: matplotlib.axes.Axes, objet pour afficher les étapes de tri

        return: list, tableau trié
        '''

        if arr is None:
            arr = self.arr
        if right is None:
            right = len(arr) - 1
            if self.visualization:
                fig, ax = plt.subplots()
        
        if left < right:
            mid = (left + right) // 2
            self.mergeSort(arr, left, mid, ax)
            self.mergeSort(arr, mid + 1, right, ax)
            self.merge(arr, left, mid, right, ax)
        
        if left == 0 and right == len(arr) - 1:
            if self.visualization:
                plt.show()

    def merge(self, arr, left, mid, right, ax):
        '''
        Fusion de deux tableaux triés
        
        param arr: list, tableau à trier
        param left: int, index de début du tableau
        param mid: int, index du milieu du tableau
        param right: int, index de fin du tableau
        param ax: matplotlib.axes.Axes, objet pour afficher les étapes de tri       
        '''
        left_half = arr[left:mid + 1]
        right_half = arr[mid + 1:right + 1]
        
        i = j = 0
        k = left
        
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
            self.steps += 1
            if self.visualization:
                ax.clear()
                ax.bar(range(len(self.arr)), self.arr, color='blue')
                ax.set_title(f"Étape {self.steps}")
                plt.pause(1*10**-3)
        
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
            self.steps += 1
            if self.visualization:
                ax.clear()
                ax.bar(range(len(self.arr)), self.arr, color='blue')
                ax.set_title(f"Étape {self.steps}")
                plt.pause(1*10**-3)
        
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
            self.steps += 1
            if self.visualization:
                ax.clear()
                ax.bar(range(len(self.arr)), self.arr, color='blue')
                ax.set_title(f"Étape {self.steps}")
                plt.pause(1*10**-3)

    def heapSort(self):
        '''
        Tri par tas
        
        Algorithme:
        1. Créer un tas max
        2. Extraire l'élément racine (le plus grand) et le placer à la fin
        3. Répéter les étapes 1 et 2 jusqu'à ce que le tas soit vide
        
        return: list, tableau trié
        '''
        if self.visualization:
            fig, ax = plt.subplots()
        n = len(self.arr)
        for i in range(n // 2 - 1, -1, -1):
            # Appel de heapify avec ax seulement si la visualisation est activée
            self.heapify(n, i, ax if self.visualization else None)
        for i in range(n - 1, 0, -1):
            self.arr[i], self.arr[0] = self.arr[0], self.arr[i]
            self.steps += 1
            if self.visualization:
                self._update_plot(ax)
            self.heapify(i, 0, ax if self.visualization else None)
        if self.visualization:
            plt.show()

    def heapify(self, n, i, ax=None):
        '''
        Créer un tas max
        
        param n: int, taille du tas
        param i: int, index du noeud racine
        param ax: matplotlib.axes.Axes, objet pour afficher les étapes de tri
        
        return: None
        '''
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.arr[left] > self.arr[largest]:
            largest = left
        if right < n and self.arr[right] > self.arr[largest]:
            largest = right
        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.steps += 1
            if ax is not None:  # Mise à jour du graphique seulement si ax est défini
                self._update_plot(ax)
            self.heapify(n, largest, ax)


    def quickSort(self, low=0, high=None, ax=None):
        '''
        Tri rapide
        
        Algorithme:
        1. Choisir un élément comme pivot
        2. Placer tous les éléments plus petits que le pivot à gauche et les éléments plus grands à droite
        3. Trier les deux parties récursivement
        
        param low: int, index de début du tableau
        param high: int, index de fin du tableau
        param ax: matplotlib.axes.Axes, objet pour afficher les étapes de tri

        return: list, tableau trié
        '''

        if high is None:
            high = len(self.arr) - 1
            if self.visualization:
                fig, ax = plt.subplots()
        
        if low < high:
            pi = self.partition(low, high, ax)
            self.quickSort(low, pi - 1, ax)
            self.quickSort(pi + 1, high, ax)
        
        if low == 0 and high == len(self.arr) - 1:
            if self.visualization:
                plt.show()

    def partition(self, low, high, ax):
        '''
        Partitionnement du tableau
        
        param low: int, index de début du tableau
        param high: int, index de fin du tableau
        param ax: matplotlib.axes.Axes, objet pour afficher les étapes de tri
        
        return: int, index du pivot
        '''
        pivot = self.arr[high]
        i = low - 1
        for j in range(low, high):
            if self.arr[j] < pivot:
                i += 1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
                self.steps += 1
                if self.visualization:
                    self._update_plot(ax)

        self.arr[i + 1], self.arr[high] = self.arr[high], self.arr[i + 1]
        self.steps += 1
        if self.visualization:
            self._update_plot(ax)
        
        return i + 1

    def printArray(self):
        print("Tableau trié:", " ".join(map(str, self.arr)))

    def plotComplexity(self, sort_method, sizes, theoretical_complexity,save_path=None):
        '''
        Tracer la complexité expérimentale et théorique du temps d'exécution

        param sort_method: fonction, méthode de tri
        param sizes: list, tailles de tableau à tester
        param theoretical_complexity: fonction, complexité théorique en fonction de n

        return: None
        '''
        previous_visualization = self.visualization
        self.visualization = False  # Désactiver la visualisation pour ne pas ralentir la complexité
        step_counts = []

        for size in sizes:
            self.arr = np.random.randint(1, 100, size)
            self.steps = 0
            sort_method()
            step_counts.append(self.steps)

        self.visualization = previous_visualization  # Restaurer la visualisation

        # Calculer la complexité théorique
        theoretical_steps = [theoretical_complexity(n) for n in sizes]

        plt.figure()
        plt.plot(sizes, step_counts, marker='o', linestyle='-', color='r', label="Complexité mesurée")
        plt.plot(sizes, theoretical_steps, marker='x', linestyle='--', color='b', label="Complexité théorique")
        plt.xlabel("Taille d'entrée (n)")
        plt.ylabel("Nombre d'étapes")
        plt.title(f"Complexité du {sort_method.__name__}")
        plt.legend()
        plt.grid()
        if save_path:
            plt.savefig(save_path)

        plt.show()

    def _update_plot(self, ax):
        '''
        Mise à jour du graphique pour la visualisation
        
        param ax: matplotlib.axes.Axes, objet pour afficher les étapes de tri
        '''
        ax.clear()
        ax.bar(range(len(self.arr)), self.arr, color='blue')
        ax.set_title(f"Étape {self.steps}")
        plt.pause(1 * 10**-3)


# Exemples de fonctions pour la complexité théorique
def complexity_insertion_sort(n):
    return n**2  # Θ(n^2)

def complexity_merge_sort(n):
    return n * np.log2(n)  # Θ(n log n)

def complexity_heap_sort(n):
    return n * np.log2(n)  # O(n log n)

def complexity_quick_sort(n):
    return n**2  # Θ(n^2) dans le pire cas

if __name__ == "__main__":
    ob = SortedMethods(100, visualization=True)
    #ob.insertionSort()
    #ob.printArray()
    #ob.mergeSort()
    #ob.printArray()
    #ob.heapSort()
    #ob.printArray()
    #ob.quickSort()
    #ob.printArray()
    sizes = [10, 20,30,40, 50,60,70,80]
    ob.plotComplexity(ob.heapSort, sizes,complexity_heap_sort,"complexity_heap_sort")
    ob.plotComplexity(ob.insertionSort, sizes,complexity_insertion_sort,"complexity_insertion_sort")
    ob.plotComplexity(ob.mergeSort, sizes,complexity_merge_sort,"complexity_merge_sort")
    ob.plotComplexity(ob.quickSort, sizes,complexity_quick_sort,"complexity_quick_sort")
