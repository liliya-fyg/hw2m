def two_sum(nums, target):
    for i in range(len(nums)):

        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

    return []

if __name__ == "__main__":

    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))

    print(two_sum([3, 2, 4], 6))
    print(two_sum([8, 4, 21, 7], 11))
