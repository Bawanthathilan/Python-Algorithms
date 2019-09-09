A=[]
for v in range(10):
    A.append(int(input("enter a number : ")))
print(A)

def selectionSort(A):
    n = len(A)
    for j in range(n):
        smallest = j
        for i in range(j+1,n):
            if(A[i] < A[smallest]):
                smallest = i
        temp = A[j]
        A[j] = A[smallest]
        A[smallest] = temp

print("sorted array")
selectionSort(A)
print(A)
