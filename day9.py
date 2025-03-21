import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
   
    patients_with_diab1 = patients[patients['conditions'].str.contains(r'\bDIAB1\d*\b', na=False)]
    
    return patients_with_diab1
