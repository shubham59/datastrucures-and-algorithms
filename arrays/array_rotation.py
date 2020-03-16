# Rotating using extra space


def rotation_extra_space(array, rotation_unit):
    """
    Space Complexity = O(rotation_units)
    Time Complexity = O(n)
    """
    temp = []
    for i in range(rotation_unit):
        temp.append(array[i])
    return array[rotation_unit:] + temp


print(rotation_extra_space([1, 2, 3, 4], 2))


def left_rotate_by_one(array):
    """
    The time complexity of len() function of python O(1)
    """
    temp = array[0]
    for i in range(len(array)-1):
        array[i] = array[i+1]
    array[len(array)-1] = temp
    return array


def rotate_one_by_one(array, rotation_unit):
    """
    Time Complexity = O(n * rotation_unit)
    Space Complexity = O(1)
    """

    for i in range(rotation_unit):
        array = left_rotate_by_one(array)
    return array


print(rotate_one_by_one([1, 2, 3, 4, 5, 6], 3))


def left_rotate_sets(arr, d):
    """
    Time Complexity = O(n)
    Space Complexity = O(1)
    Sets : {1, 4, 7, 10}
           {2, 5, 8, 11}
           {3, 6, 9, 12}
    """
    n = len(arr)
    hcf = HCF(d, n)
    for i in range(hcf):

        temp = arr[i]
        j = i
        while 1:
            k = j + d
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp
    return arr


def HCF(a, b):
    if b == 0:
        return a
    else:
        return HCF(a, a % b)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
n = len(arr)
d = 2
print (left_rotate_sets(arr, d))


