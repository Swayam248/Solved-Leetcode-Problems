# Write your MySQL query statement below
-- select patient_id, patient_name, conditions from patients WHERE conditions like '%DIAB1%'
select patient_id, patient_name, conditions from patients WHERE conditions REGEXP '\\bDIAB1';
#This regular expression searches for DIAB1 as a whole word.
#\\b denotes a word boundary, ensuring that DIAB1 is not part of a larger word.
#This handles cases where DIAB1 is at the start, end, or surrounded by spaces in the conditions string.