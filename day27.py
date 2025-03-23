import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    report_counts = employee.groupby('managerId')['id'].count().reset_index(name='report_count')

    
    managers_with_five_reports = report_counts[report_counts['report_count'] >= 5]
    result = managers_with_five_reports.merge(employee, left_on='managerId', right_on='id')[['name']]

    return result