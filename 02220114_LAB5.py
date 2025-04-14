#Part 2 Lab 5. 

def binary_search_iterative(arr, target):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:
        comparisons += 1
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons


def binary_search_recursive(arr, target, low, high, comparisons=0):
    if low > high:
        return -1, comparisons

    comparisons += 1
    mid = (low + high) // 2

    if arr[mid] == target:
        return mid, comparisons
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high, comparisons)
    else:
        return binary_search_recursive(arr, target, low, mid - 1, comparisons)


# Main Program
arr = [12, 23, 34, 45, 56, 67, 89]
target = 67

print("Sorted List:", arr)
print(f"Searching for {target} using Binary Search (Iterative Version)")

# Iterative Search
index, comps = binary_search_iterative(arr, target)
if index != -1:
    print(f"Found at index {index}")
else:
    print("Not found")
print(f"Number of comparisons: {comps}")

print("\nSearching for", target, "using Binary Search (Recursive Version)")

# Recursive Search
index, comps = binary_search_recursive(arr, target, 0, len(arr) - 1)
if index != -1:
    print(f"Found at index {index}")
else:
    print("Not found")
print(f"Number of comparisons: {comps}") 