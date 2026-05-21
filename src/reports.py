from calculator import CalcObject
from config import OUTPUT_DIR

def generate_html(calc : CalcObject) -> None:
    html = f"""
        <html>
            <head>
                <title>Loan Affordability Report</title>
            </head>
    
            <body>
    
                <h1>Loan Affordability Report</h1>
    
                <h2>Input Values</h2>
    
                <table border="1" cellpadding="5">


                </table>
    
                <h2>Calculated Results</h2>
    
                <table border="1" cellpadding="5">

                </table>
    
                <h2>Affordability Status</h2>
    
    
            </body>
        </html>
        """
    
    with open(OUTPUT_DIR/"load_report.html", "w") as file:
        file.write(html)

def generate_txt(calc : CalcObject) -> None:
    pass

def generate_sql(calc : CalcObject) -> None:
    pass