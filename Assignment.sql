show databases; 


use Rfam;

SHOW TABLES;

Select *
from taxonomy;

SELECT DISTINCT species, ncbi_id 
FROM taxonomy 
WHERE species LIKE '%Panthera tigris%';


SELECT ncbi_id,Species
FROM taxonomy 
where species LIKE '%Panthera tigris sumatrae%';


SELECT 
    TABLE_NAME,
    COLUMN_NAME,
    CONSTRAINT_NAME,
    REFERENCED_TABLE_NAME,
    REFERENCED_COLUMN_NAME
FROM
    INFORMATION_SCHEMA.KEY_COLUMN_USAGE
WHERE
    TABLE_SCHEMA = 'Rfam' AND
    REFERENCED_TABLE_NAME IS NOT NULL;

SELECT *
FROM rfamseq;

SELECT *
FROM family;

SELECT family.rfam_id, rfamseq.length
FROM rfamseq,family
ORDER BY length DESC;













