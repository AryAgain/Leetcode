# Given an integer array nums, return true if any value appears at least 
# twice in the array, and return false if every element is distinct.

def containsDuplicate(nums) -> bool:
    nums.sort()
    print(nums)
    for index in range(len(nums) - 1):
        if nums[index] == nums[index + 1]:
            return True
    return False


def main() :
    nums = [9,6,4,2,3,5,7,0,1]
    # nums = [9,6,4,2,3,5,7,6,0,1]
    print(containsDuplicate(nums))


if __name__ == '__main__':
    main()