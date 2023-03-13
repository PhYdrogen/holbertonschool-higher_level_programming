-- A script that lists the number of records with the same score in the table second_table
select score, count(score) as number from second_table group by score;
