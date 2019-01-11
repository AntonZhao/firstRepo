import random

def bubble_sort(array):
    length = len(array)
    for i in range(length):
        flag = False
        for j in range(length - i - 1):
            if array[j]>array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                flag = True
        if flag == False:
            break

def insert_sort(array):
    length = len(array)
    for i in range(length - 1):
        i = i + 1
        value = array[i]
        j = i - 1
        while j >= 0:
            if array[j] > value:
                array[j + 1] = array[j]
                j -= 1
            else:
                break
        array[j + 1] = value

def selection_sort(array):
    length = len(array)
    for i in range(length):
        min_index = i
        min_val = array[i]
        for j in range(i,length):
            if array[j] < min_val:
                min_index = j
                min_val = array[j]
        array[i], array[min_index] = array[min_index], array[i]




if __name__ == '__main__':
    array = []
    for i in range(20):
        array.append(random.randint(1,10))
    print(array)
    #bubble_sort(array)
    #insert_sort(array)
    selection_sort(array)
    print(array)

