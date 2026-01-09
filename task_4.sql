-- task_4.sql

SELECT 
    COLUMN_NAME AS `Column`,
    COLUMN_TYPE AS `Data Type`,
    IS_NULLABLE AS `Nullable`,
    COLUMN_KEY AS `Key`,
    COLUMN_DEFAULT AS `Default`,
    EXTRA AS `Extra`
FROM 
    INFORMATION_SCHEMA.COLUMNS
WHERE 
    TABLE_SCHEMA = DATABASE() -- current database passed as argument
    AND TABLE_NAME = 'BOOKS'
ORDER BY 
    ORDINAL_POSITION;
