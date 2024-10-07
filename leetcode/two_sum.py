from typing import List
import copy

def twoSum(nums: List[int], target: int) -> List[int]:
        
    nums_size = len(nums)

    nums_copy = copy.deepcopy(nums)
    
    index_diff = 0
    
    i = 0
    
    pair_result = []
    
    first_index = 0
    last_index = 0
    
    for i in range(nums_size):
        diff = target - nums[i]
        if diff == nums[i]:
            try:
                first_index = i
                nums_copy.pop(i)
                last_index = nums_copy.index(diff) + 1
                if last_index == 0:
                    continue
                pair_result = [first_index, last_index]
                break
            except:
                continue
        else:
            try:
                index_diff = nums.index(diff)
                pair_result = [i, index_diff]
                break
            except:
                continue
    
    return pair_result

if __name__ == '__main__':
    number_list = [3,2,4]

    target = 6

    print(twoSum(number_list, target))
