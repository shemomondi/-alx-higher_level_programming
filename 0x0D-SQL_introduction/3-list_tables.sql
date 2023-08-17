-- A script that lists all tables of database

SELECT mysql
FROM information_schema.tables
WHERE table_schema = 'mysql';
