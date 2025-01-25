import random
import timeit

# Сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# Сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Вбудований Timsort (через sorted)
def timsort(arr):
    return sorted(arr)

# Генерація тестових наборів
def generate_data(size):
    return [random.randint(0, 1000) for _ in range(size)]

# Функція для заміру часу виконання
def measure_time(algorithm, data):
    start = timeit.default_timer()
    algorithm(data.copy())
    end = timeit.default_timer()
    return end - start

# Основна функція
def test_algorithms():
    sizes = [100, 1000, 10000]  # Розміри масивів
    algorithms = {
        "Merge Sort": merge_sort,
        "Insertion Sort": insertion_sort,
        "Timsort (Python sorted)": timsort,
    }

    for size in sizes:
        print(f"\nМасив розміром {size}:")
        data = generate_data(size)
        for name, algorithm in algorithms.items():
            time_taken = measure_time(algorithm, data)
            print(f"{name}: {time_taken:.6f} секунд")

if __name__ == "__main__":
    test_algorithms()