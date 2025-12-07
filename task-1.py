import timeit
import random


# Сортування вставками (Insertion Sort)
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


# Сортування злиттям (Merge Sort)

# Розділення
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


# Злиття
def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Об'єднання менших елементів
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Додаємо елементи, якщо залишились зліва або зправа
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged


# Сортування Timsort (стандартне - для порівняння)
def timsort_wrapper(lst):
    return sorted(lst)


if __name__ == "__main__":

    # Різні набори даних
    data_sizes = [100, 1000, 5000, 10000]

    # Кількість повторів для timeit (середнє значення) зменщується для великих масивів
    repeats = 5 

    results = {}

    # Тестування
    print(f"{'Algorithm':<20} | {'Size':<10} | {'Time (sec)':<15}")
    print("-" * 50)

    # Прохід по кожному способу у визначену кількість елементів
    for size in data_sizes:
        # Генерація випадкового списку
        original_data = [random.randint(0, 100_000) for _ in range(size)]

        # Тест Insertion Sort (дуже повільний на >10k)
        if size <= 5000: 
            time_insertion = timeit.timeit(lambda: insertion_sort(original_data[:]), number=repeats)
            print(f"{'Insertion Sort':<20} | {size:<10} | {time_insertion:.5f}")
        else:
            print(f"{'Insertion Sort':<20} | {size:<10} | {'Skipped (>5000)':<15}")

        # Тест Merge Sort
        time_merge = timeit.timeit(lambda: merge_sort(original_data[:]), number=repeats)
        print(f"{'Merge Sort':<20} | {size:<10} | {time_merge:.5f}")

        # Тест Timsort
        time_timsort = timeit.timeit(lambda: timsort_wrapper(original_data[:]), number=repeats)
        print(f"{'Timsort (Built-in)':<20} | {size:<10} | {time_timsort:.5f}")
        
        print("-" * 50)
