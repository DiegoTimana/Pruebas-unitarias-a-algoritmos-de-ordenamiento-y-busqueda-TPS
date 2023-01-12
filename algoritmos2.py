##ALGORITMOS A LOS CUALES SE LES APLICARAN PRUEBAS UNITARIAS
#Diego Timaná-Michelle González-Luis Valencia-Luis Ruiz
#Técnicas de pruebas de software- Universidad del Valle- diciembre 2022


#SELECTION SORT
def selectionsort(vectorselect):
    """Esta función ordenara el vector que le pases como argumento con el Método Selection Sort"""
    
    largo = 0
    
    for _ in vectorselect:
        largo += 1 # Obtenemos el largo del vector
        
    for i in range(largo): 
      
        # Encontrar el minimo elemento de los restantes sin ordenar
        minimo = i 
        for j in range(i+1, largo): 
            if vectorselect[minimo] > vectorselect[j]: 
                minimo = j 
                
        # Cambiamos el elemento minimo encontrado con el primer elemento de la matriz
        vectorselect[i], vectorselect[minimo] = vectorselect[minimo], vectorselect[i]
        # Repetimos el proceso hasta terminar
    return vectorselect


#QUICKSORT
def QuickSort(arr):

    elements = len(arr)
    
    #Base case
    if elements < 2:
        return arr
    
    current_position = 0 #Position of the partitioning element

    for i in range(1, elements): #Partitioning loop
         if arr[i] <= arr[0]:
              current_position += 1
              temp = arr[i]
              arr[i] = arr[current_position]
              arr[current_position] = temp

    temp = arr[0]
    arr[0] = arr[current_position] 
    arr[current_position] = temp #Brings pivot to it's appropriate position
    
    left = QuickSort(arr[0:current_position]) #Sorts the elements to the left of pivot
    right = QuickSort(arr[current_position+1:elements]) #sorts the elements to the right of pivot

    arr = left + [arr[current_position]] + right #Merging everything together
     
    return arr

#HEAPSORT
def heap_sort(arr):

    def max_heapify(arr,n,i):
        l = 2 * i + 1
        r = 2 * i + 2
        
        if l < n and arr[l] > arr[i]:
            largest = l
        else:
            largest = i
            
        if r < n and arr[r] > arr[largest]:
            largest = r
            
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            max_heapify(arr, n, largest)
    
    
    def build_heap(arr):
        n = len(arr)
        
        for i in range(n, -1,-1):
            max_heapify(arr, n, i)
            
        for i in range(n-1,0,-1):
            arr[0] ,arr[i] = arr[i], arr[0]
            max_heapify(arr, i, 0)

    build_heap(arr)        
    return arr