# Step 4: Produce Hand-Written Calculations

given inputs for my hand written calculatoins

| Variable             | Value   |
| -------------------- | ------- |
| Loan amount          | $15,000 |
| Annual interest rate | 7.5%    |
| Loan term            | 3 years |
| Monthly income       | $8,500  |
| Monthly expenses     | $6,200  |

P (loan amount) = 15,000
Annual_interest_rate = 7.5
loan_term = 3
monthly_income = 8,500
monthly_expenses = 6,200

r (monthly interest rate) 	= 	annual_interest_rate / (100 * 12)
 						= 	7.5 / 1200
						= 	0.00625

n (number of payments) 	= 	loan_term (years) * 12
						=	3 * 12
						=	36

M (monthly repayment) 	= 	(P*r(1+r)^n) /
							(((1+r)^n) - 1)
						= 	(15000 * 0.00625 (1+0.00625)^36) /(((1+0.00625)^36) - 1)
						= 	(93.75 (1.00625)^36) /(((1.00625)^36) - 1)
						= 	(93.75 * 1.25144613551) /(0.25144613551)
						= 	466.593272416

total repayment 			= 	M * n
						=	36 * 466.593272416
						=	16797.357807

total interest				= 	total repayment - P
						= 	16797.357807 - 15000
						= 	1797.357807

monthly cash surplus		=	monthly_income - monthly_expenses - M
						=	8500 - 6200 - 466
						= 	1834

summurised outputs:

| Calculated Value       | Approximate Result      |
| ---------------------- | ----------------------- |
| Monthly repayment      | $466.59                 |
| total repayment amount | $16,797.36              |
| total interest paid    | $1797.36                |
| monthly cash surplus   | 503                     |
| affordablility         | is affordable (503 > 0) |
