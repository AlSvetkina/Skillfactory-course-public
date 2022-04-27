def qsort(array, left, right):
    middle = (left+right) // 2

    p = array[middle]
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)


def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2

    if middle > 0 and array[middle] >= element and array[middle - 1] < element:
        return middle - 1

    if element < array[middle]:
        return binary_search(array, element, left, middle - 1)

    return binary_search(array, element, middle + 1, right)


def run():
    numbers = input("enter a sequence of number by separting via space:")
    try:
        numbers = [int(x) for x in numbers.split(" ")]
        print(f"numbers: {numbers}")

        number = int(input("enter a number:"))
        print(f"number: {number}")
    except ValueError:
        print("input error")
        return

    qsort(numbers, 0, len(numbers) - 1)
    print(f"sorted numbers: {numbers}")

    position = binary_search(numbers, number, 0, len(numbers) - 1)
    print(f"position: {position}")


run()
