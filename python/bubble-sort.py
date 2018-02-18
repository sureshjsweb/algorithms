nums = [4545,534,3,2,4,5]
print("Original List: ", nums)

for a in range(len(nums)):
  for b in range(len(nums)):
    if (nums[a]<nums[b]):
      t = nums[a]
      nums[a] = nums[b]
      nums[b] = t
print("Bubble Sorted List: ", nums)