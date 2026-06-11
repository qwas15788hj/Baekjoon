# Write your MySQL query statement below
select sub.machine_id, round(sum(processing_time)/count(*), 3) as processing_time
from (
    select a.machine_id, a.process_id, b.timestamp-a.timestamp as processing_time 
    from Activity a
        join Activity b
        on (a.machine_id, a.process_id) = (b.machine_id, b.process_id)
    where a.activity_type = 'start' and b.activity_type = 'end'
    group by machine_id, process_id
) as sub
group by sub.machine_id
order by machine_id