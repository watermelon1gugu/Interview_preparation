def three_node_quick_sort(nums: list):
    if len(nums) == 1:
        return nums
    if len(nums) == 2:
        return [nums[1], nums[0]] if nums[1] < nums[0] else nums

    first_node, second_node = (nums[0], nums[1]) if nums[1] < nums[0] else (nums[1], nums[0])
    left = []
    mid = []
    right = []

    for i in range(2, len(nums)):
        if nums[i] < first_node:
            left.append(nums[i])
        elif nums[i] < second_node:
            mid.append(nums[i])
        else:
            right.append(nums[i])
    return three_node_quick_sort(left) + [first_node] + three_node_quick_sort(mid) + [
        second_node] + three_node_quick_sort(right)


def three_exchange(nums, start, end):
    if len(nums) == 1:
        return nums
    if len(nums) == 2:
        return [nums[start + 1], nums[start]] if nums[start + 1] < nums[start] else nums
    nodes = [start, start + 1] if nums[start + 1] < nums[start] else [start + 1, start]
    last_start = start + 2
    for node in nodes:
        i = last_start
        j = end
        while i != j:
            while j >= nums[node]:
                j -= 1
            while i <= nums[node]:
                i += 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[node], nums[i] = nums[i], nums[node]
        last_start = i + 1


def quick_sort(nums: list, start, end):
    if end - start <= 1:
        return
    i = exchange(nums, start, end)
    quick_sort(nums, start, i - 1)
    quick_sort(nums, i + 1, end)
    return


def exchange(nums, start, end):
    label = nums[start]
    i = start + 1
    j = end
    while i != j:
        while nums[j] >= label and i < j:
            j -= 1
        while nums[i] <= label and i < j:
            i += 1
        nums[i], nums[j] = nums[j], nums[i]
    print(nums)
    return i


if __name__ == '__main__':
    a = [11, 9, 0, 4, 12, 2, 5, 17, 6, 7, 1, 8, 3, 18, 19, 20, 13, 15, 16, 14]

    print(exchange(a, 0, len(a) - 1))
