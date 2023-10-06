numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

index_None_element = numbers.index(None)
sum_ = sum(numbers[0:index_None_element]) + sum(numbers[index_None_element + 1:])
len_ = len(numbers)
numbers[index_None_element] = sum_ / len_
print("Измененный список:", numbers)
