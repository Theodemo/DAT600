import time
import matplotlib.pyplot as plt
import numpy as np

class SortedMethods:
    def __init__(self, arr):
        self.arr = arr
        self.steps = 0

    def insertionSort(self):
        fig, ax = plt.subplots()
        self.steps = 0
        for i in range(1, len(self.arr)):
            key = self.arr[i]
            j = i - 1
            
            while j >= 0 and key < self.arr[j]:
                self.arr[j + 1] = self.arr[j]
                j -= 1
                self.steps += 1  # Comptage des comparaisons et déplacements
                
                ax.clear()
                ax.bar(range(len(self.arr)), self.arr, color='blue')
                ax.set_title(f"Step {self.steps}")
                plt.pause(0.5)
            
            self.arr[j + 1] = key
            self.steps += 1  # Pour l'insertion du key
            
            ax.clear()
            ax.bar(range(len(self.arr)), self.arr, color='blue')
            ax.set_title(f"Étape {self.steps}")
            plt.pause(0.5)
        plt.show()

    def mergeSort(self, arr=None, left=0, right=None, ax=None):
        if arr is None:
            arr = self.arr
        if right is None:
            right = len(arr) - 1
            fig, ax = plt.subplots()
        
        if left < right:
            mid = (left + right) // 2
            self.mergeSort(arr, left, mid, ax)
            self.mergeSort(arr, mid + 1, right, ax)
            self.merge(arr, left, mid, right, ax)
        
        if left == 0 and right == len(arr) - 1:
            plt.show()

    def merge(self, arr, left, mid, right, ax):
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
            ax.clear()
            ax.bar(range(len(self.arr)), self.arr, color='blue')
            ax.set_title(f"Étape {self.steps}")
            plt.pause(0.5)
        
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
            self.steps += 1
            ax.clear()
            ax.bar(range(len(self.arr)), self.arr, color='blue')
            ax.set_title(f"Étape {self.steps}")
            plt.pause(0.5)
        
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
            self.steps += 1
            ax.clear()
            ax.bar(range(len(self.arr)), self.arr, color='blue')
            ax.set_title(f"Étape {self.steps}")
            plt.pause(0.5)

    def heapSort(self):
        def heapify(arr, n, i, ax):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            
            if left < n and arr[left] > arr[largest]:
                largest = left
            
            if right < n and arr[right] > arr[largest]:
                largest = right
            
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                self.steps += 1
                ax.clear()
                ax.bar(range(len(arr)), arr, color='blue')
                ax.set_title(f"Étape {self.steps}")
                plt.pause(0.5)
                heapify(arr, n, largest, ax)
        
        fig, ax = plt.subplots()
        n = len(self.arr)
        for i in range(n // 2 - 1, -1, -1):
            heapify(self.arr, n, i, ax)
        for i in range(n - 1, 0, -1):
            self.arr[i], self.arr[0] = self.arr[0], self.arr[i]
            self.steps += 1
            ax.clear()
            ax.bar(range(len(self.arr)), self.arr, color='blue')
            ax.set_title(f"Étape {self.steps}")
            plt.pause(0.5)
            heapify(self.arr, i, 0, ax)
        plt.show()
    
    def quickSort(self, low=0, high=None, ax=None):
        if high is None:
            high = len(self.arr) - 1
            fig, ax = plt.subplots()
        
        if low < high:
            pi = self.partition(low, high, ax)
            self.quickSort(low, pi - 1, ax)
            self.quickSort(pi + 1, high, ax)
        
        if low == 0 and high == len(self.arr) - 1:
            plt.show()
    
    def partition(self, low, high, ax):
        pivot = self.arr[high]
        i = low - 1
        
        for j in range(low, high):
            if self.arr[j] < pivot:
                i += 1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
                self.steps += 1
                ax.clear()
                ax.bar(range(len(self.arr)), self.arr, color='blue')
                ax.set_title(f"Étape {self.steps}")
                plt.pause(0.5)
        
        self.arr[i + 1], self.arr[high] = self.arr[high], self.arr[i + 1]
        self.steps += 1
        ax.clear()
        ax.bar(range(len(self.arr)), self.arr, color='blue')
        ax.set_title(f"Étape {self.steps}")
        plt.pause(0.5)
        return i + 1

    def printArray(self):
        print("Tableau trié:", " ".join(map(str, self.arr)))

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    ob = SortedMethods(arr)
    #ob.mergeSort()
    #ob.heapSort()
    ob.quickSort()
    #ob.insertionSort()
    #ob.printArray()
