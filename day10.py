import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
  
    if employee.empty or N <= 0:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    
    
    unique_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)

    nth_salary = unique_salaries.iloc[N - 1] if N <= len(unique_salaries) else None
    

    return pd.DataFrame({f'getNthHighestSalary({N})': [nth_salary]})