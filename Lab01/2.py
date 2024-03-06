"""
Author: Alessandro Amella
Date: 05/03/2024
"""

# 2.1
"""
- Create a numpy array with shape 5x5, that contains numbers from 25..to 0
- create a function that takes an arbitrary numpy array as an input and sets all numbers smaller than the user-defined threshold to 0
- test your function on your array
- make one implementation using loops and one without using loops, compare execution time with **time** library
"""
import numpy as np
import time

arr = np.arange(25, 0, -1).reshape(5, 5)

def set_threshold(arr: np.ndarray, threshold: int) -> np.ndarray:
    return np.where(arr < threshold, 0, arr) # return arr if arr >= threshold, 0 otherwise

threshold = 10
start = time.time()
print(set_threshold(arr, threshold))
print("Time without loops:", time.time() - start)

def set_threshold_loop(arr: np.ndarray, threshold: int) -> np.ndarray:
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            if arr[i, j] < threshold:
                arr[i, j] = 0
    return arr

start = time.time()
print(set_threshold_loop(arr, threshold))
print("Time with loops:", time.time() - start)


# 2.2
"""
The task will be to create a simulation of Digi display that will be able to display an arbitrary integer
   
*hint: to show an image use the library matplotlib.pyplot, also you may find function np.concatenate usefull*
"""
import matplotlib.pyplot as plt

def show_in_digi(input_integer: int) -> None:
    digits = [np.array([[1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]]), # 0
              np.array([[0, 1, 0], [1, 1, 0], [0, 1, 0], [0, 1, 0], [1, 1, 1]]), # 1
              np.array([[1, 1, 1], [0, 0, 1], [1, 1, 1], [1, 0, 0], [1, 1, 1]]), # 2
              np.array([[1, 1, 1], [0, 0, 1], [1, 1, 1], [0, 0, 1], [1, 1, 1]]), # 3
              np.array([[1, 0, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1], [0, 0, 1]]), # 4
              np.array([[1, 1, 1], [1, 0, 0], [1, 1, 1], [0, 0, 1], [1, 1, 1]]), # 5
              np.array([[1, 1, 1], [1, 0, 0], [1, 1, 1], [1, 0, 1], [1, 1, 1]]), # 6
              np.array([[1, 1, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1]]), # 7
              np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 1, 1]]), # 8
              np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1], [1, 1, 1]])] # 9
    digits = np.array(digits)
    input_str = str(input_integer)
    input_arr = np.array([digits[int(i)] for i in input_str])
    plt.imshow(np.concatenate(input_arr, axis=1), cmap='gray')
    plt.axis('off')
    plt.show()
    
show_in_digi(1234567890)