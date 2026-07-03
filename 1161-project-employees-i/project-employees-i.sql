# Write your MySQL query statement below
SELECT p1.project_id , 
ROUND(IFNULL(SUM(p2.experience_years)/COUNT(p2.experience_years),0),2) AS average_years
FROM Project p1
 JOIN Employee p2 ON p1.employee_id = p2.employee_id
GROUP BY project_id;