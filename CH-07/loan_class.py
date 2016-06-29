class Loan():
    def __init__(self, APR = 2.5, years = 5, amount = 2000, borrower = " "):
        self.__APR = APR
        self.__years = years
        self.__amount = amount
        self.__borrower = borrower

    def get_APR(self):
        return self.__ARP
     

    def get_num_of_years(self):
        return self.__years
    

    def get_loan_amount(self):
        return self.__amount
    

    def get_borrower(self):
        return self.__borrower


    def set_APR(self, APR):
        self.__APR = APR

    
    def set_num_of_years(self, num_of_years):
        self.__years = years

    
    def set_loan_amount(self, loan_amount):
        self.__amount = amount
    

    def set_borrower(self, borrower):
        self.__borrower = borrower
    

    def get_monthly_payment(self):
        monthly_interest_rate = self.__APR / 1200
        monthly_payment = self.__amount * monthly_interest_rate / ( 1 - (1 / ( 1 + monthly_interest_rate) ** (self.__years * 12)))
        return monthly_payment
    

    def get_total_payment(self):
        total_payment = self.get_monthly_payment() * self.__years * 12
        return total_payment