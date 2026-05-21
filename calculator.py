

class CaclObject:
    def __init__(self, 
                loan_amount : float, 
                interest_rate : float, #annual
                monthly_expenses : float, 
                loan_term : float, 
                monthly_income : float
                ) -> None:
        self._error_log : list[str] = []
        self._loan_amount = loan_amount
        self._interest_rate = interest_rate
        self._monthly_expenses = monthly_expenses
        self._loan_term = loan_term
        self._monthly_income = monthly_income

        self._monthly_interest_rate : float | None = None
        self._monthly_repayment : float | None = None
        self._total_repayment : float | None = None
        self._total_interest : float | None = None
        self._monthly_cash_surplus : float | None = None
        
    def get_monthly_interest_rate(self) -> float | None:
        try:
            if self._interest_rate < 0:
                raise ValueError("interest rate cant be negative.")
            monthly_i_rate = self._interest_rate / (100 * 12)
        except Exception as e:
            self._error_log.append(str(e))
            return None
        self._monthly_interest_rate = monthly_i_rate
        return monthly_i_rate
    
    def get_monthly_repayment(self) -> float | None:
        try:
            if self._loan_amount <= 0:
                raise ValueError("loan amount must be more then 0") 
            if self._loan_term <= 0:
                raise ValueError("loan term must be more then 0") 
            if self._monthly_interest_rate == None:
                raise ValueError("monthly interest rate not calculated yet")
            monthly_repayment = (self._loan_amount * self._monthly_interest_rate * (1+self._monthly_interest_rate) ** self._loan_term) / (((1+self._monthly_interest_rate) ** self._loan_term) - 1)
        except Exception as e:
            self._error_log.append(str(e))
            return None
        self._monthly_repayment = monthly_repayment
        return monthly_repayment
    
    def get_total_repayment(self) -> float | None:
        try:
            if self._loan_term <= 0:
                raise ValueError("loan term must be more then 0") 
            if self._monthly_repayment == None:
                raise ValueError("monthly repayment not calculated yet")
            total_repayment = self._monthly_repayment * self._loan_term
        except Exception as e:
            self._error_log.append(str(e))
            return None
        self._monthly_repayment = total_repayment
        return total_repayment
    
    def get_total_interest(self) -> float | None:
        try:
            if self._total_repayment == None:
                raise ValueError("total repayment not calculated yet")
            total_interest = self._total_repayment - self._loan_amount
        except Exception as e:
            self._error_log.append(str(e))
            return None
        self._total_interest = total_interest
        return total_interest
    
    def get_monthly_cash_surplus(self) -> float | None:
        try:
            if self._monthly_repayment == None:
                raise ValueError("monthly repayment not calculated yet")
            monthly_cash_surplus = self._monthly_income - self._monthly_expenses - self._monthly_repayment
        except Exception as e:
            self._error_log.append(str(e))
            return None
        self._monthly_cash_surplus = monthly_cash_surplus
        return monthly_cash_surplus


    def full_calc_pipeline(self) -> dict[str, float | bool | None] | None:
        self._error_log = []
        self.get_monthly_interest_rate()
        self.get_monthly_repayment()
        self.get_total_repayment()
        self.get_total_interest()
        self.get_monthly_cash_surplus()
        if len(self._error_log) != 0:
            return None
        return {
            "monthly_repayment" : self._monthly_repayment,
            "total_repayment" : self._total_repayment,
            "total_interest" : self._total_interest,
            "monthly_cash_surplus" : self._monthly_cash_surplus,
            "affordable" : self._monthly_cash_surplus > 0 #type: ignore
        }
    
    def get_errors(self) -> list[str]:
        return self._error_log
    