# Write your MySQL query statement below
select eu.unique_id, e.name from Employees e left join EmployeeUNI eu on e.id = eu.id
-- select eu.unique_id, e.name from EmployeeUNI eu right join Employees e on e.id = eu.id