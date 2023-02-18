class NumArray:
    def __init__(self, nums):
        n = len(nums)
        self.prefix_sum = [0] * (n + 1)

        for i in range(1, n + 1):
            self.prefix_sum[i] = self.prefix_sum[i - 1] + nums[i - 1]

    def sumRange(self, left, right) :
        return self.prefix_sum[right + 1] - self.prefix_sum[left]


def main():
    input_nums = [[-2, 0, 3, -5, 2, -1]]
    queries = [[0, 2], [2, 5], [0, 5]]
    # expected_output = [1, -1, -3]

    # Test the implementation
    num_array = NumArray(input_nums[0])
    output = [num_array.sumRange(query[0], query[1]) for query in queries]
    print(output)  


if __name__ == '__main__':
    main()