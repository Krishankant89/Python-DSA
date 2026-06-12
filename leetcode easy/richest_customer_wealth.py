class Solution(object):
    
    def maximumWealth(self, accounts):
        
        return max(sum(customer_accounts) for customer_accounts in accounts)