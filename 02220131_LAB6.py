 #Lab 6 part 1
def quick_sort(arr):
    comparisons = [0]
    swaps = [0]

    def median_of_three(low, high):
        mid = (low + high) // 2
        a, b, c = arr[low], arr[mid], arr[high]
        if a > b:
            if b > c:
                return mid
            elif a > c:
                return high
            else:
                return low
        else:
            if a > c:
                return low
            elif b > c:
                return high
            else:
                return mid

    def partition(low, high):
        pivot_index = median_of_three(low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        swaps[0] += 1

        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            comparisons[0] += 1  # Count every comparison
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                swaps[0] += 1
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        swaps[0] += 1
        comparisons[0] += 1
        return i + 1

    def quick_sort_recursive(low, high):
        if low < high:
            pi = partition(low, high)
            quick_sort_recursive(low, pi - 1)
            quick_sort_recursive(pi + 1, high)

    quick_sort_recursive(0, len(arr) - 1)
    return arr, comparisons[0], swaps[0]

# Example run
if __name__ == "__main__":
    data = [38, 27, 43, 3, 9, 82, 10]
    print("Original List:", data)
    sorted_data, comparison_count, swap_count = quick_sort(data.copy())
    print("Sorted using Quick Sort:", sorted_data)
    print("Number of comparisons:", comparison_count)
    print("Number of swaps:", swap_count)