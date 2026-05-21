from calculator import CalcObject
from config import OUTPUT_DIR

def generate_html(inputs : dict[str, float], results : dict[str, float | str]) -> None:
    html = f"""
        <html>
            <head>
                <title>Loan Affordability Report</title>
            </head>
    
            <body>
    
                <h1>Loan Affordability Report</h1>
    
                <h2>Input Values</h2>
    
                <table border="1" cellpadding="5">
                    <tr>
                        <th>Input</th>
                        <th>Value</th>
                    </tr>
    
                    <tr>
                        <td>Loan Amount</td>
                        <td>${inputs["loan_amount"]:,.2f}</td>
                    </tr>
    
                    <tr>
                        <td>Interest Rate</td>
                        <td>{inputs["interest_rate"]}%</td>
                    </tr>
    
                    <tr>
                        <td>Loan Term</td>
                        <td>{inputs["loan_term"]} months</td>
                    </tr>
    
                    <tr>
                        <td>Monthly Income</td>
                        <td>${inputs["monthly_income"]:,.2f}</td>
                    </tr>
    
                    <tr>
                        <td>Monthly Expenses</td>
                        <td>${inputs["monthly_expenses"]:,.2f}</td>
                    </tr>
                </table>
    
                <h2>Calculated Results</h2>
    
                <table border="1" cellpadding="5">
                    <tr>
                        <th>Calculation</th>
                        <th>Value</th>
                    </tr>
    
                    <tr>
                        <td>Monthly Repayment</td>
                        <td>${results['monthly_repayment']:,.2f}</td>
                    </tr>
    
                    <tr>
                        <td>Total Repayment</td>
                        <td>${results['total_repayment']:,.2f}</td>
                    </tr>
    
                    <tr>
                        <td>Total Interest</td>
                        <td>${results['total_interest']:,.2f}</td>
                    </tr>
    
                    <tr>
                        <td>Monthly Cash Surplus</td>
                        <td>${results['monthly_cash_surplus']:,.2f}</td>
                    </tr>
                </table>
    
                <h2>Affordability Status</h2>
    
                <p>
                    <strong>{results['affordable']}</strong>
                </p>
    
            </body>
        </html>
        """
    
    with open(OUTPUT_DIR/"report.html", "w") as file:
        file.write(html)

def generate_txt(inputs : dict[str, float], results : dict[str, float | str]) -> None:

    report = f"""
        
    """
    pass

def generate_sql(calc : CalcObject) -> None:
    pass