"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

from enum import Enum

class Employee:


    def __init__(self, name, contract, commission, contractPay = 0, commissionPay = 0, hoursWorked = 0, contractsLanded = 0):
        self.name = name
        self.contract = contract
        self.commission = commission
        self.contractPay = contractPay
        self.commissionPay = commissionPay
        self.hoursWorked = hoursWorked
        self.contractsLanded = contractsLanded

    def __str__(self):
        output = self.name + " works on a "
        if self.contract == Contract.MONTHLY:
            output += "montly salary of " + str(self.contractPay)
        elif self.contract == Contract.HOURLY:
            output += "contract of " + str(self.hoursWorked) + " hours at " + str(self.contractPay) + "/hour"

        if self.commission == Commission.FIXED:
            output += " and receives a bonus commission of " + str(self.commissionPay)
        elif self.commission == Commission.PERCONTRACT:
            output += " and receives a commission for " + str(self.contractsLanded) + " contract(s) at " + str(self.commissionPay) + "/contract"

        output += ". Their total pay is " + str(self.get_pay()) + "."


        return output


    def get_pay(self):
        return self.getContractPay() + self.getCommisionPay()

    def getContractPay(self):
        if self.contract == Contract.MONTHLY:
            return self.contractPay
        else:
            return self.contractPay * self.hoursWorked

    def getCommisionPay(self):
        if self.commission == Commission.NONE:
            return 0
        elif self.commission == Commission.FIXED:
            return self.commissionPay
        elif self.commission == Commission.PERCONTRACT:
            return self.commissionPay * self.contractsLanded


class Contract(Enum):
    MONTHLY = 0
    HOURLY = 1


class Commission(Enum):
    NONE = 0
    FIXED = 1
    PERCONTRACT = 2


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', Contract.MONTHLY, Commission.NONE, contractPay = 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', Contract.HOURLY, Commission.NONE, contractPay = 25, hoursWorked = 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', Contract.MONTHLY, Commission.PERCONTRACT, contractPay = 3000, commissionPay = 200, contractsLanded = 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', Contract.HOURLY, Commission.PERCONTRACT, contractPay = 25, hoursWorked =150, commissionPay = 220, contractsLanded = 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', Contract.MONTHLY, Commission.FIXED, contractPay = 2000, commissionPay = 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', Contract.HOURLY, Commission.FIXED, contractPay = 30, hoursWorked = 120, commissionPay = 600)
