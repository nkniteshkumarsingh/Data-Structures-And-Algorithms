# Given an array of distinct integers and a sum integer, find all the triplets in the array whose sum equals the sum integer.
# [12, 3, 1, 2, -6, 5, -8, 6], 0


# O(N^2) Time
# O(N) Space
def three_numbers_sum(arr, given_sum):
    arr.sort()
    result = []
    for i in range(len(arr) - 2):
        left_idx = i + 1
        right_idx = len(arr) - 1
        while left_idx < right_idx:
            current_sum = arr[i] + arr[left_idx] + arr[right_idx]
            if current_sum < given_sum:
                left_idx += 1
            elif current_sum > given_sum:
                right_idx -= 1
            else:
                result.append([arr[i], arr[left_idx], arr[right_idx]])
                left_idx += 1
                right_idx -= 1
    return result


if __name__ == "__main__":
    print(three_numbers_sum([12, 3, 1, 2, -6, 5, -8, 6], 0))
