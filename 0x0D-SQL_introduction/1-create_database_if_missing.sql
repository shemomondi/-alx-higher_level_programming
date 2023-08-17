-- creating a database if it doesn't exist in hbtn_0c_0
USE information_schema;

SELECT table_name
FROM tables
WHERE table_schema = 'mysql';
