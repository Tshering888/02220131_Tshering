def merge_sort(arr):
    comparisons = 0
    accesses = 0

    def merge(left, right):
        nonlocal comparisons, accesses
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            comparisons += 1
            accesses += 2
            if left[i] < right[j]:
                result.append(left[i])
                accesses += 1
                i += 1
            else:
                result.append(right[j])
                accesses += 1
                j += 1

        while i < len(left):
            result.append(left[i])
            accesses += 1
            i += 1

        while j < len(right):
            result.append(right[j])
            accesses += 1
            j += 1

        return result

    def sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = sort(arr[:mid])
        right = sort(arr[mid:])
        return merge(left, right)

    sorted_arr = sort(arr)
    return sorted_arr, comparisons, accesses

original_list = [38, 27, 43, 3, 9, 82, 10]
sorted_list, comp, acc = merge_sort(original_list)

print("Original List:", original_list)
print("Sorted using Merge Sort:", sorted_list)
print("Number of comparisons:", comp)
print("Number of array accesses:", acc)