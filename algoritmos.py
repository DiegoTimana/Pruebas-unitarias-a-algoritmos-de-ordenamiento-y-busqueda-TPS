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
