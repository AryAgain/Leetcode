# Given a non-empty array of integers nums, every element appears twice except for one. 
# Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

def singleNumber(nums) :
    unique_no = 0
    for value in nums:
        unique_no ^= value
        # print(unique_no)
    return unique_no


def main() :
    nums = [4,1,2,1,2]
    print(singleNumber(nums))


if __name__ == '__main__':
    main()
