def bubble_sort(a):
    n = len(a)
    for i in range(n - 1, 0, -1):   # n - 1 .. 1
        for j in range(i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

def selection_sort(a):
    pass

def insertion_sort(a):
    pass