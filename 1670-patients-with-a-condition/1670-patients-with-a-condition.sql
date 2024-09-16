# Write your MySQL query statement below
select patient_id, patient_name, conditions from patients WHERE conditions REGEXP '\\bDIAB1';