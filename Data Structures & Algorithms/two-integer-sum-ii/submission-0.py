class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # I smell hashmap/hashtable, in order to store the values
        # constraints are: target, sum, and need
        # we loop through the array with two pointers,
        # since this is sorted, we can move both pointers 
        # we move the left pointer if sum is < target
        # we move the right pointer inwards if sum > target
        # if target equals, we return the value

        # edge cases: 1. array is less than 2 in length
        # 2 left and right should not be the same vals
        # if they are, skip and continue loop

        left, right = 0, len(numbers) - 1

        while left < right:
            # if numbers[left] == numbers[right]:
            #     continue
            sum = numbers[left] + numbers[right]
            if target == sum:
                left, right = left +1, right +1
                return [left, right] if left < right else [right, left]
            elif sum > target:
                right -= 1
            else:
                left += 1
        return []
        