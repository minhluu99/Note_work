```sql
ALTER TABLE lakehouse-prod-394907.silver_buymed_vn_restricted.platform_billing_prd_invoice_v2_invoice
RENAME TO platform_billing_prd_invoice_v2_invoice_old;

CREATE TABLE silver_buymed_vn_restricted.platform_billing_prd_invoice_v2_invoice
PARTITION BY DATE(ingest_time)
CLUSTER BY
  created_time, mg_id
AS (
  SELECT * FROM silver_buymed_vn_restricted.platform_billing_prd_invoice_v2_invoice_old
);

DROP TABLE silver_buymed_vn_restricted.platform_billing_prd_invoice_v2_invoice_old;

```
