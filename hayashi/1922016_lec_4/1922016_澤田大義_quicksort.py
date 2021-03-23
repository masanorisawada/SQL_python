import random
N = 10

def input_data(data):
    for i in range(N):
        data.append(random.randint(0, N))
    return data

def quicksort(left, right):
    if left >= right:
        return
    else:
        pivot = data[right]
        partition = division(left, right, pivot)
        quicksort(left, partition - 1)
        quicksort(partition + 1, right)



def division(left, right, pivot):
    x = left - 1
    for i in range(left,right):
        if data[i] <= pivot:
            x += 1
            data[x], data[i] = data[i], data[x] 
            print('x',x)
            print('i',i)
    print(data)
    data[x+1], data[right] = data[right], data[x+1]
    print(data)
    print('@',x)
    p = x + 1
    return p


if __name__ == "__main__":
    data = []
    data = input_data(data)
    print(data)
    quicksort(0, N - 1)
    print(data)


