from cmath import inf
from Expenses.ExpenseFactory import ExpenseFactory
from User import User
from models.ExpenseType import ExpenseType

'''
 2 -> 1

'''


class ExpenseTracker:
    def __init__(self, users):
        self.initialize_expense_tracker(users)
        
    def initialize_expense_tracker(self, users):
        self.expenses = []
        self.users = users
        self.balances = {user.get_user_id(): {} for user in self.users}
            
        # print("BALANCES", self.balances)
        
    # @TODO
    def _validate_percentage_total_as_hundred(self, percentages):
        pass
    
    # @TODO
    def _validate_splitted_total_as_amount(self, amount, splitted_amount):
        pass
    
    def _reduce_number_of_transactions_helper(self, positives: list, negatives: list):
        
        if len(negatives) == 0 or len(positives) == 0: return 0

        negative = negatives[0]
        count = float('inf')
        for positive in positives:
            positive_copy = positives.copy()
            negative_copy = negatives.copy()
            
            positive_copy.remove(positive)
            negative_copy.remove(negative)
            if positive['balance'] < -negative['balance']:
                negative_copy.append({ 'balance': positive['balance'] + negative['balance'], 'user_id': negative['user_id'] })
            elif positive['balance'] > -negative['balance']:
                positive_copy.append({ 'balance': positive['balance'] + negative['balance'], 'user_id': positive['user_id'] })

            count = min(count, 
                        self._reduce_number_of_transactions_helper(positive_copy, negative_copy)
            )
        
        return count + 1
    
    def _reduce_number_of_transactions(self):
        balance_user_mapping = {}
        # print('BALANCES: ', self.balances)
        for key in self.balances:
            # print('KEY: ', key)
            if key not in balance_user_mapping:
                balance_user_mapping[key] = 0
            for key_j in self.balances[key]:
                # print('KEY_J: ', key_j)
                if key_j not in balance_user_mapping:
                    balance_user_mapping[key_j] = 0
                balance_user_mapping[key] += self.balances[key][key_j]['owes']
                balance_user_mapping[key_j] -= self.balances[key][key_j]['owes']
                    
        positives = [{ 'balance': balance_user_mapping[key], 'user_id': key } for key in balance_user_mapping if balance_user_mapping[key] > 0]
        negatives = [{ 'balance': balance_user_mapping[key], 'user_id': key } for key in balance_user_mapping if balance_user_mapping[key] < 0]
                          
        # print('positives and negatives: ', positives, negatives)
        print('Number of transactions: ', self._reduce_number_of_transactions_helper(positives, negatives))
        
    def _reduce_transactions(self, paid_by, user_id):
        if paid_by in self.balances[user_id]:
            if self.balances[paid_by][user_id]['owes'] > self.balances[user_id][paid_by]['owes']:
                self.balances[paid_by][user_id]['owes'] -= self.balances[user_id][paid_by]['owes']
                del self.balances[user_id][paid_by]
            elif self.balances[user_id][paid_by]['owes'] > self.balances[paid_by][user_id]['owes']:
                self.balances[user_id][paid_by]['owes'] -= self.balances[paid_by][user_id]['owes']
                del self.balances[paid_by][user_id]['owes']
            else:
                del self.balances[paid_by][user_id]['owes']
                del self.balances[user_id][paid_by]['owes']
                
    def add_new_expense(self, expense_type, *args):
        new_expense = ExpenseFactory().get_expense(expense_type, *args)
        self.expenses.append(new_expense)
        
        paid_by = new_expense.get_paid_by()
        amount = new_expense.get_amount()
        split_into = new_expense.get_split_into()
        
        if expense_type == ExpenseType.EQUAL:
            splitted_amount = amount / len(split_into)
            for user_id in split_into:
                if user_id == paid_by:
                    continue
                if user_id not in self.balances[paid_by]:
                    self.balances[paid_by][user_id] = {'owes': 0}
                self.balances[paid_by][user_id]['owes'] += splitted_amount
                self._reduce_transactions(paid_by, user_id)
                    
        elif expense_type == ExpenseType.EXACT:
            split_into_amount = new_expense.get_split_into_amount()
            for index, user_id in enumerate(split_into):
                if user_id == paid_by:
                    continue
                if user_id not in self.balances[paid_by]:
                    self.balances[paid_by][user_id] = {'owes': 0}  
                self.balances[paid_by][user_id]['owes'] += split_into_amount[index]
                self._reduce_transactions(paid_by, user_id)

        elif expense_type == ExpenseType.PERCENT:
            split_into_percentage = new_expense.get_split_into_percentage()
            for index, user_id in enumerate(split_into):
                if user_id == paid_by:
                    continue
                if user_id not in self.balances[paid_by]:
                    self.balances[paid_by][user_id] = {'owes': 0}  
                self.balances[paid_by][user_id]['owes'] += (split_into_percentage[index] * amount * 0.01)
                self._reduce_transactions(paid_by, user_id)

        # self._reduce_number_of_transactions()
    
    def get_balances(self):
        return self.balances
    
    def get_balance_for_user(self, user):
        pass
    
    def get_expenses(self):
        return self.expenses
    
    def get_expense_for_user(self, user):
        pass