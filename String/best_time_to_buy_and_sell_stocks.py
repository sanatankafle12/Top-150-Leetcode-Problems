class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Find the maximum profit from buying and selling a stock once.
        
        This function calculates the maximum profit that can be achieved by buying
        the stock on one day and selling it on a later day. The goal is to find
        the maximum difference between a selling price and a buying price.
        
        Args:
            prices (List[int]): Array of stock prices where prices[i] is the price
                              of the stock on the i-th day
                              
        Returns:
            int: Maximum profit that can be achieved, or 0 if no profit is possible
            
        Example:
            >>> solution = Solution()
            >>> solution.maxProfit([7, 1, 5, 3, 6, 4])
            5
            >>> solution.maxProfit([7, 6, 4, 3, 1])
            0
            >>> solution.maxProfit([1, 2, 3, 4, 5])
            4
            
        Time Complexity: O(n) where n is the length of prices array
        Space Complexity: O(1) - uses only a constant amount of extra space
        """
        max_profit = 0
        buy = prices[0]
        for i in range(1,len(prices)):
            if prices[i]<buy:
                buy = prices[i]

            profit = prices[i]-buy
            max_profit = max(profit,max_profit)

        return(max_profit)