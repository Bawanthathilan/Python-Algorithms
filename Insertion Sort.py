def insertionSort(arr): #create a function

    #traverse through 1 to len(arr) 
    for j in range (1,len(arr)):
        
        key = arr[j]
        i = j - 1

        while i >= 0 and key < arr[i]:
            arr[i+1] = arr[i]
            i -= 1
            arr[i+1] = key

#call the function
arr = ['19','13','15','12','11']
insertionSort(arr)
print("Sorted array is: ")
for i in range(len(arr)):
    print(arr[i])
