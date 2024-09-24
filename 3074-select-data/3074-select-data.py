import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students['student_id']== 101, ['name', 'age']]

'''
Row Filtering: students['student_id'] == 101

students['student_id'] accesses the student_id column of the students DataFrame.

students['student_id'] == 101 creates a Boolean Series where each entry is True if the corresponding student_id is 101, and False otherwise. This is called a Boolean mask.

.loc Indexer: students.loc[...]

.loc is a label-based indexer used to select rows and columns by labels.
students.loc[students['student_id'] == 101] uses the Boolean mask created in step 2 to select only the rows where the student_id is 101.
Column Selection: ['name', 'age']

After selecting the rows where student_id is 101, students.loc
[students['student_id'] == 101, ['name', 'age']] specifies the columns to be selected, which are name and age.
Putting It All Together
The entire code students.loc[students['student_id'] == 101, ['name', 'age']] performs the following operations:

Filter Rows: Selects rows in the students DataFrame where the student_id is 101.
Select Columns: From these filtered rows, selects only the name and age columns.
'''