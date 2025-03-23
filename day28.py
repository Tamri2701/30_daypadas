import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
  
    red_company = company[company['name'] == "RED"]
    
    if red_company.empty:  
        return sales_person[['name']]
    

    red_company_id = red_company['com_id'].values[0]


    red_orders = orders[orders['com_id'] == red_company_id]

   
    sales_with_red_orders = red_orders['sales_id'].unique()

   
    result = sales_person[~sales_person['sales_id'].isin(sales_with_red_orders)]

    return result[['name']]
