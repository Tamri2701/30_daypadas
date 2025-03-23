import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    
    students_subjects = students.assign(key=1).merge(subjects.assign(key=1), on='key').drop('key', axis=1)

   
    exam_counts = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name='attended_exams')

    
    result = students_subjects.merge(exam_counts, on=['student_id', 'subject_name'], how='left').fillna({'attended_exams': 0})

    result['attended_exams'] = result['attended_exams'].astype(int)

    result = result.sort_values(by=['student_id', 'subject_name']).reset_index(drop=True)

    return result