def find_ascending_sub_arrays(nums: list[int]) -> list[tuple[int, int]]:
    sub_arrays = list[tuple[int, int]]()

    start_idx = 0

    while start_idx < len(nums):
        sub_array_end_idx = start_idx
        while (sub_array_end_idx < len(nums) - 1
               and nums[sub_array_end_idx] <= nums[sub_array_end_idx + 1]):
            sub_array_end_idx += 1
        if sub_array_end_idx != start_idx:
            sub_arrays.append((start_idx, sub_array_end_idx))
            start_idx = sub_array_end_idx
        start_idx += 1

    return sub_arrays


print(find_ascending_sub_arrays([7, 1, 5, 3, 6, 4]))
print(find_ascending_sub_arrays([1, 2, 3, 4, 5]))
print(find_ascending_sub_arrays([7, 6, 4, 3, 1]))
