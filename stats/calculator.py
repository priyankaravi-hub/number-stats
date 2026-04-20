def mean(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    return sum(numbers) / len(numbers)

def median(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    sorted_nums = sorted(numbers)
    mid = len(sorted_nums) // 2
    if len(sorted_nums) % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    return sorted_nums[mid]

def mode(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    frequency = {}
    for n in numbers:
        frequency[n] = frequency.get(n, 0) + 1
    return max(frequency, key=frequency.get)
