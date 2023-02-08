# Given an array nums containing n distinct numbers in the range [0, n], 
# return the only number in the range that is missing from the array.

def missingNumber(nums) -> int:
        nums.sort()
        for index in range(len(nums)):
            if index != nums[index]:
                return index
        return len(nums)


def main():
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print(missingNumber(nums))


if __name__ == '__main__':
    main()