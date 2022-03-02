select Email
from Person
group by Email
having count(Email) > 1;

-- where > group by > having > order by