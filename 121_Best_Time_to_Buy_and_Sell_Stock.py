# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

def fmaxProfit1(prices) :
    # basic solution of n^2
    length = len(prices)
    max = 0
    for index in range(length):
        for index2 in range(index+1, length):
            diff = prices[index2] - prices[index]
            # print(diff)
            if diff > max:
                max = diff
    return max
    
    
def fmaxProfit(prices) :
    # O(n) solution
    length = len(prices)
    max_profit  = 0
    buy_pointer = 0
    sell_pointer = 1
    while sell_pointer < length:
        currentProfit = prices[sell_pointer] - prices[buy_pointer] 
        if prices[buy_pointer] < prices[sell_pointer]:
            max_profit = max(currentProfit,max_profit)
        else:
            buy_pointer = sell_pointer
        sell_pointer += 1
    return max_profit

def main():
    #prices = [7,6,4,3,1]
    prices = [7,1,5,3,6,4]
    print(fmaxProfit(prices))


if __name__ == '__main__':
    main()

