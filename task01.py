import timeit
import random

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst

def timsort(arr):
    return sorted(arr)

def generate_data(size):
    return [random.randint(0, 10000) for _ in range(size)]

data_size = [100, 1000, 10000, 100000]

def main():
    for size in data_size:
        print(f"\nВибірка даних розміру: {size}")
        data = generate_data(size)
        time_taken = timeit.timeit(lambda: merge_sort(data.copy()), number=1)
        print(f"Merge Sort: {time_taken:.6f} seconds")
        time_taken = timeit.timeit(lambda: insertion_sort(data.copy()), number=1)
        print(f"Insertion Sort: {time_taken:.6f} seconds")
        time_taken = timeit.timeit(lambda: timsort(data.copy()), number=1)
        print(f"Timsort: {time_taken:.6f} seconds")

if __name__ == "__main__":
    main()
