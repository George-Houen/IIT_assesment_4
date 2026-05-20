# step 2: Identify Inputs and Outputs

*overview* in the task sheet gives us these as our inputs:

* loan amount,
* interest rate,
* loan term,
* monthly income, and
* monthly expenses.

and then *Case Study: Small Business Loan Repayment Planner* gives us these outputs:

* the monthly repayment,
* the total repayment amount,
* the total interest paid,
* the monthly cash surplus after paying the loan, and
* whether the loan appears affordable.

# tablulized

| Input            | Description                                   | Unit              | Example Value |
| ---------------- | --------------------------------------------- | ----------------- | ------------- |
| Loan amount      | Amount borrowed from the bank                 | Dollars           | 15000         |
| interest rate    | increase of amount owed every month           | percent per month | 2.1           |
| loan term        | time over whole loan is payed off             | months            | 32            |
| monthly income   | total income of store every month             | Dollars per month | 12,500        |
| monthly expenses | income deducted each month for other purposes | Dollars per month | 11,250        |

| Output                 | Description                                                    | Unit              |
| ---------------------- | -------------------------------------------------------------- | ----------------- |
| Monthly repayment      | Estimated monthly loan payment                                 | Dollars per month |
| total repayment amount | Estimated sum of payments made (loan amount plus interest)     | Dollars           |
| total interest paid    | Estimated sum of interest payed over entire term               | Dollars           |
| monthly cash surplus   | Estimated net cash after monthly expenses and monthly payments | Dollars per month |
| affordablility         | affordability                                                  | boolean (yes/no)  |
