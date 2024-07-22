---
tags:
  - location
---

column_name is_nullable data_type description
key	NO	STRING
mg_id	YES	STRING
created_time	YES	TIMESTAMP
last_updated_time	YES	TIMESTAMP
synced_at	YES	TIMESTAMP
action	NO	STRING
ingest_time	NO	TIMESTAMP
is_support	YES	BOOL

code	YES	STRING

name	YES	STRING
district_code	YES	STRING
district_name	YES	STRING

level	YES	STRING
province_code	YES	STRING
province_name YES	STRING
region_code	YES	STRING
region_name	YES	STRING

hash_tag	YES	STRING
fee_province_value	YES	FLOAT64
fee_district_value	YES	FLOAT64
fee_region_value	YES	FLOAT64
extra_props	YES	JSON
