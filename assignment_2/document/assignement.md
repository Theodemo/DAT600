# DAT600: Algorithm Theory - Assignment 2

## **I. Matrix Chain Multiplication**

### **1. Solve the parenthesization problem by hand**

Consider the matrices:
- A1: 30x35
- A2: 35x15
- A3: 15x5
- A4: 5x10
- A5: 10x20

Using the matrix chain multiplication recursive formula, we fill the memoization tables **m** (costs) and **s** (splitting points). The formula for computing the minimum cost of multiplying matrices is:
$$ m[i,j] = \min_{i \leq k < j} \{ m[i,k] + m[k+1,j] + p_{i-1} p_k p_j \} $$



---
### **2. Dynamic Programming Implementation**

```python
import sys

def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]
    
    for l in range(2, n + 1):  # Chain length
        for i in range(n - l + 1):
            j = i + l - 1
            m[i][j] = sys.maxsize
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m, s

# Example usage:
p = [30, 35, 15, 5, 10, 20]
m, s = matrix_chain_order(p)
```

---
### **3. Greedy Approach for Matrix Chain Multiplication**
There is no greedy choice that applies because the problem exhibits optimal substructure but not the greedy-choice property.

---

## **II. Fractional and 0-1 Knapsack**

### **1. 0-1 Knapsack Problem Implementation**

```python
def knapsack_01(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacity]

# Example usage:
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5
print(knapsack_01(weights, values, capacity))
```

---
### **2. Fractional Knapsack Problem Implementation**

```python
def fractional_knapsack(weights, values, capacity):
    items = sorted(zip(weights, values), key=lambda x: x[1] / x[0], reverse=True)
    max_value = 0
    for weight, value in items:
        if capacity >= weight:
            max_value += value
            capacity -= weight
        else:
            max_value += (value / weight) * capacity
            break
    return max_value

# Example usage:
print(fractional_knapsack([2, 3, 4, 5], [3, 4, 5, 6], 5))
```

---

## **III. Greedy + Dynamic (Coin Change Problem)**

### **1. Greedy Algorithm for Coin Change**

```python
def greedy_coin_change(coins, amount):
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        count += amount // coin
        amount %= coin
    return count

# Example usage:
coins = [1, 5, 10, 20]
amount = 47
print(greedy_coin_change(coins, amount))
```

---
### **2. Example where Greedy Fails**
Given coins = [1, 5, 11], a greedy solution for N=15 selects 11+1+1+1+1 (5 coins), but an optimal solution is 5+5+5 (3 coins).

---
### **3. Dynamic Programming Solution**

```python
def dp_coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for j in range(coin, amount + 1):
            dp[j] = min(dp[j], dp[j - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

# Example usage:
print(dp_coin_change(coins, amount))
```

---
### **4. Is the Norwegian System Greedy?**
For Norwegian coins [1, 5, 10, 20], a greedy approach always yields an optimal solution, so it is a greedy system.

---
### **5. Time Complexity Analysis**
- **Greedy Coin Change:** O(n) (linear in the number of coin types)
- **Dynamic Coin Change:** O(n * amount) (pseudo-polynomial complexity)

---

### **Conclusion**
This report presented solutions to problems using both greedy and dynamic programming approaches. The matrix chain multiplication problem illustrated the advantage of dynamic programming over naive recursion. The knapsack problem demonstrated differences between 0-1 and fractional versions. Finally, the coin change problem highlighted cases where greedy methods fail and where dynamic programming guarantees an optimal solution.

