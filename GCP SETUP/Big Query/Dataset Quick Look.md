#### Table count and size

```sql
SELECT
  dataset_id,
  countif(table_id LIKE '%dim%') AS dim_tables,
  countif(table_id LIKE '%fact%') AS fact_tables,
  countif(table_id not LIKE '%dim%' AND table_id NOT LIKE '%fact%') as nor
  -- SUM(row_count) AS total_rows,
  -- SUM(size_bytes) AS size_bytes,
  -- MIN(creation_time),
  -- MAX(last_modified_time)

FROM  
  (
    SELECT * FROM `lakehouse-prod-394907.silver_buymed_vn.__TABLES__` UNION ALL
    SELECT * FROM `lakehouse-prod-394907.gold_buymed_vn.__TABLES__`
  )
GROUP BY 1
```

#### Table Constrant

```sql
SELECT *
FROM lakehouse-prod-394907.gold_buymed_vn.INFORMATION_SCHEMA.TABLE_CONSTRAINTS;
```

#### Get table ddl created syntax

```sql
SELECT
  ddl
-- FROM `lakehouse-prod-394907.silver_buymed_vn.__TABLES__`
FROM `lakehouse-prod-394907.silver_buymed_vn.INFORMATION_SCHEMA.TABLES`
where table_name = 'seller_prd_purchasing_quotation_export';
```