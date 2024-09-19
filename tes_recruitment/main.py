import os
from pandasql import sqldf
import pandas as pd
os.chdir(os.path.dirname(os.path.abspath(__file__)))

orders = pd.read_csv("data/orders.csv")
customers = pd.read_csv("data/customers.csv")

def get_sql() -> str:
    with open('edit_this.sql', 'r') as file:
        return file.read()


def main() -> None:
    df = sqldf(get_sql(), globals())
    print(df)

if __name__ == "__main__":
    main()
    
