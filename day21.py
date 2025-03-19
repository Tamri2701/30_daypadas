import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    order_counts = orders.groupby("customer_number")["order_number"].count().reset_index()

    max_orders = order_counts["order_number"].max()

   
    result = order_counts[order_counts["order_number"] == max_orders][["customer_number"]]

    return result