

class CaclObject:
    def __init__(self, 
                loan_amount : float, 
                interest_rate : float, 
                monthly_expenses : float, 
                loan_term : float, 
                monthly_income : float
                ) -> None:
        self._error_log : list[str] = []
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate
        self.monthly_expenses = monthly_expenses
        self.loan_term = loan_term
        self.monthly_income = monthly_income
        pass
    def full_calc_pipeline(self) -> dict[str, int] | None:
        return 
    def get_errors(self) -> list[str]:
        return self._error_log
    