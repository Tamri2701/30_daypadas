import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
 
    max_salary = employee.groupby("departmentId")["salary"].max().reset_index()
    

    merged = employee.merge(max_salary, on=["departmentId", "salary"])
    
    result = merged.merge(department, left_on="departmentId", right_on="id")[["name_y", "name_x", "salary"]]
    
    result.columns = ["Department", "Employee", "Salary"]
    
    return result