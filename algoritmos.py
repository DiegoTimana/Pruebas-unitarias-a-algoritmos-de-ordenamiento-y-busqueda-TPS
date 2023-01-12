##ALGORITMOS A LOS CUALES SE LES APLICARAN PRUEBAS UNITARIAS
#Diego Timaná-Michelle González-Luis Valencia-Luis Ruiz
#Técnicas de pruebas de software- Universidad del Valle- diciembre 2022


#BUBBLE SORT
def bubble_sort(numbers):
  for i in range(len(numbers)):
    for j in range(len(numbers)-1):
      if numbers[j] > numbers[j+1]:
        numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
  return numbers


#INSERTION SORT
def insertion_sort(numbers):
  for i in range(1, len(numbers)):
    j = i
    while j > 0 and numbers[j-1] > numbers[j]:
      numbers[j], numbers[j-1] = numbers[j-1], numbers[j]
      j -= 1
  return numbers


#COUNTING SORT 
def counting_sort(numbers, k):
  counts = [0] * (k+1)
  for number in numbers:
    counts[number] += 1
  sorted_numbers = []
  for i in range(k+1):
    sorted_numbers.extend([i] * counts[i])
  return sorted_numbers

#MERGE SORT
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def call_merge_sort(arr):
    merge_sort(arr)
    return arr

