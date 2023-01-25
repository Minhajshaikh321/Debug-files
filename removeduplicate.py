# nums=[1,1,2]
# nums = [0,0,1,1,1,2,2,3,3,4]
def removeduplicate(nums):
        i = 0
        for j in range(1,len(nums)):
            if nums[j] != nums[j-1]:
                nums[i] = nums[j-1]
                i += 1
                nums[i] = nums[-1]
        return i+1
# nums=[1,1,2]
nums = [0,0,1,1,1,2,2,3,3,4]

print(removeduplicate(nums))

# nums=[1,1,2]
# 