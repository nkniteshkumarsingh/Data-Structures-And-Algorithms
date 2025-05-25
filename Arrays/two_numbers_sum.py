# Given an array of integers and an integer, find two numbers in the array whose sum equals the sum integer.
# [3, 5, -4, 8, 11, 1, -1, 6], 10
# [-4, -1, 1, 3, 5, 6, 8, 11], 13


# O(N^2) Time
# O(1) Space
# def two_numbers_sum(arr, given_sum):
#     for i in range(len(arr) - 1):
#         for j in range(i+1, len(arr)):
#             if arr[i] + arr[j] == given_sum:
#                 return arr[i], arr[j]
#     return False


# O(N) Time
# O(N) Space
# def two_numbers_sum(arr, given_sum):
#     numbers = {}
#     for num in arr:
#         diff = given_sum - num
#         if diff in numbers:
#             return diff, num
#         numbers.update({num: True})
#     return False


# O(nLogN) Time
# O(1) Space
def two_numbers_sum(arr, given_sum):
    arr.sort()
    left_idx, right_idx = 0, len(arr) - 1
    while left_idx < right_idx:
        if given_sum > arr[left_idx] + arr[right_idx]:
            left_idx += 1
            continue
        if given_sum < arr[left_idx] + arr[right_idx]:
            right_idx -= 1
            continue
        return arr[left_idx], arr[right_idx]
    return False


if __name__ == "__main__":
    print(two_numbers_sum([3, 5, -4, 8, 11, 1, -1, 6], 10))
    print(two_numbers_sum([-4, -1, 1, 3, 5, 6, 8, 11], 13))
