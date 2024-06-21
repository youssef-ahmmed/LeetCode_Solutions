# Write your MySQL query statement below
SELECT
    m.name AS Employee
FROM
    Employee m
    JOIN Employee e ON e.id = m.managerId
WHERE
    m.salary > e.salary;
