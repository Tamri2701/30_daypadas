import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
   
    result = (
        activities.groupby("sell_date")["product"]
        .agg(lambda x: ",".join(sorted(set(x))))  
        .reset_index()
    )

   
    result["num_sold"] = result["product"].apply(lambda x: len(x.split(",")))

    result = result.rename(columns={"product": "products"})[["sell_date", "num_sold", "products"]]

    return result.sort_values(by="sell_date")

