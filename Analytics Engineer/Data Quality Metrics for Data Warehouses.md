![[Pasted image 20240613140732.png]]

### **Intrinsic data quality dimensions**
[**Accuracy**](https://www.metaplane.dev/blog/data-accuracy-definition-examples): Does the data accurately describe the real world? Do the entities actually exist, do they have the attributes you describe in your data model, and do events occur at the times and with the attributes you claim?
- _Example problems_: The number of aquariums sold this month in the warehouse does not match the actual number sold as reported by the sales people
- _Metrics to measure_: Degree to which your data matches against **a reference set**, corroborates with other data, passes rules and thresholds that classify data errors, or **can be verified by humans**.

[**Completeness**](https://www.metaplane.dev/blog/data-completeness-definition-examples): How completely does the data describe the real world? There are at least two levels here. First, **how complete** is your data model? Second, **within the data model you’ve constructed**, how complete is the data itself?
- _Example problems:_ Rainforest’s data warehouse has a table for aquariums, but not for a new product line of subscription fish food. Within the table for aquariums, the new prices of those aquariums are empty.
- _Metrics to measure_: Degree of validation against a complete mapping, the **number of null data** values or data elements or missing data, the **number of satisfied constraints**, degree of validation against an input mechanism

[**Consistency**](https://www.metaplane.dev/blog/data-consistency-definition-examples): Is the data internally consistent? **If there are redundant data values**, do they have the same value? Or, if values are aggregations of each other, are the values consistent with each other? Codd’s Referential Integrity constraint is one example of a consistency check.
- _Example problems_: The engineering team records aquarium models that don’t match the models recorded by the sales team. The monthly profit number is not consistent with the monthly revenue and cost numbers.
- _Metrics to measure_: Number of passed checks to tracking the uniqueness of values or uniqueness of entities , corroboration within the system, whether referential integrity is maintained.

[**Privacy and security**](https://www.metaplane.dev/blog/data-security-data-privacy-definition-examples): Is data being used in accordance with the intended level of privacy and secured against undesired access? This is especially important in our world of regular data breaches, and if your company has compliance (e.g. SOC 2) or regulatory (e.g. HIPAA) requirements.
- _Example problems_: Customer billing and location information is stored in the warehouse and each member of the data science team is able to query that personal data. Access to the warehouse isn’t reviewed on a regular basis and is not granted according to the principle of least privilege.
- Metrics to measure: Number of sensitive data values available to database users, number of database users who should not have access, amount of unmasked sensitive data.

[**Freshness**](https://www.metaplane.dev/blog/data-freshness-definition-examples): Does the data describe the real world right now? Also called “currency” in the literature (Loshin 2001), this dimension is closely related to the timeliness of the data, but is compared against the present moment rather than the time of a task.
- _Example problems_: The reported number of products sold at Aquarium are one week behind because of a data ingest issue from Salesforce. The list of sales reps is not updated from an internal HR system.
- _Metrics to measure_: Difference between latest timestamps against the present moment, difference from a source system, verification against an expected rate of change ([Loshin 2006](https://bja.ojp.gov/sites/g/files/xyckuh186/files/media/document/informatica_whitepaper_monitoring_dq_using_metrics.pdf)), corroboration against other pieces of data.

![[Pasted image 20240617094107.png]]

![[Pasted image 20240617094236.png]]


https://www.metaplane.dev/blog/data-quality-metrics-for-data-warehouses
https://www.linkedin.com/advice/0/what-kpis-should-you-use-measure-success-your