from datetime import datetime

class AccountTransaction:
    date = ""
    location = ""
    cost = 0.0
    accountBalance = 0.0
    gain = 0.0

    def __init__(self, date, location, cost, gain, accountBalanace):
        self.location = location.strip()
        self.cost = cost
        self.accountBalance = accountBalanace
        date = datetime.strptime(date, '%m/%d/%Y')