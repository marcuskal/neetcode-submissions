class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # I will use a hashmap here to store the seen values
        seen = {}

        for i, x in enumerate(nums):
            need = target - x
            if need in seen:
                # return smaller index first
                j = seen[need]
                return [j, i] if j < i else [i, j]
            seen[x] = i
        return []