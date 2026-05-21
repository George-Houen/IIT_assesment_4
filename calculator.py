

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
    
    

    def full_calc_pipeline(self) -> dict[str, float] | None:
        return
    def get_errors(self) -> list[str]:
        return self._error_log
    