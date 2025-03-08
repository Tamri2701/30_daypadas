#Table: Customers

#id is the primary key (column with unique values) for this table.
#Each row of this table indicates the ID and name of a customer.
 

#Table: Orders


#id is the primary key (column with unique values) for this table.
#customerId is a foreign key (reference columns) of the ID from the Customers table.
#Each row of this table indicates the ID of an order and the ID of the customer who ordered it.
 

#Write a solution to find all customers who never order anything.

#Return the result table in any order.


import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Perform a left join between Customers and Orders on id = customerId
   df = customers.merge(orders, left_on="id", right_on="customerId", how="left")

   df = df[df["customerId"].isna()][["name"]].rename(columns={"name": "Customers"})
    
   return df