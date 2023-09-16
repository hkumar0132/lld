from ExpenseTracker import ExpenseTracker
from User import User
from models.ExpenseType import ExpenseType


def main():
    u1 = User(0, "a@gmail.com", "a", '6209090120')
    u2 = User(1, "b@gmail.com", "b", '6209090020')
    u3 = User(2, "c@gmail.com", "c", '6209091120')
    u4 = User(3, "d@gmail.com", "d", '6209056120')
    splitwise = ExpenseTracker([u1, u2, u3, u4])
    
    splitwise.add_new_expense(ExpenseType.EQUAL, u1.get_user_id(), 1000, [
        u1.get_user_id(), u2.get_user_id(), u3.get_user_id(), u4.get_user_id()
    ])
    
    # print('\n\n', splitwise.get_expenses())
    # print(splitwise.get_balances())
    
    splitwise.add_new_expense(ExpenseType.EXACT, u1.get_user_id(), 1250, [
        u2.get_user_id(), u3.get_user_id()
    ], [
        370, 880
    ])
    
    # print('\n\n', splitwise.get_expenses())
    # print(splitwise.get_balances())
    
    splitwise.add_new_expense(ExpenseType.PERCENT, u4.get_user_id(), 1200, [
        u1.get_user_id(), u2.get_user_id(), u3.get_user_id(), u4.get_user_id()
    ], [
        40, 20, 20, 20
    ])
    
    # print(splitwise.get_balances())
    balances = splitwise.get_balances()
    for key in balances:
        for k in balances[key]:
            balance = balances[key][k]['owes']
            print(f'User {k+1} owes User {key+1}: {balance}')
    
    # print(splitwise.get_balance_for_user(u1.get_user_id()))
    # print(splitwise.get_expense_for_user(u1.get_user_id()))

if __name__ == "__main__":
    main()