# Given an array nums of n integers where nums[i] is in the range [1, n], return an 
# array of all the integers in the range [1, n] that do not appear in nums.


def findDisappearedNumbers(nums):
    length = len(nums)
    arr = []
    numset = set()
    for index in range(length):
        numset.add(nums[index])
    
    for index in range(1, length+1):
        if(index not in numset):
            arr.append(index)

    return arr



def main():
    nums = [4,3,2,7,8,2,3,1]
    print(findDisappearedNumbers(nums))


if __name__ == '__main__':
    main()