import random

def binary_search(data, target, low, high):
    
    mid = (low + high) // 2
    
    while target != data[mid]:
    
        if low > high: 
            return False
        
        if target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1

        mid = (low + high) // 2

    else:
        return True

    ''' if target == data[mid]:
        return True
    elif target < data[mid]:
        return binary_search(data, target, low, mid - 1)
    else:
        return binary_search(data, target, mid + 1, high) '''


if __name__ == '__main__':
    data = [random.randint(0, 100) for i in range(10)]
    
    data.sort()

    print(data)

    target = int(input('What number would you like to find?: '))
    found = binary_search(data, target, 0, len(data) - 1)

    if found:
        print('{} was found'.format(target))
    else:
        print('{} was not found'.format(target))
