import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    xyz = employees.head(3)
    return xyz