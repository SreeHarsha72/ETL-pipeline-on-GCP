# Automating an ETL and Reporting Pipeline Using Google Cloud Services  

**Objective:**  
Build and automate a scalable, cost-effective ETL pipeline and reporting system on Google Cloud to extract, transform, load, and visualize employee data.  

## **Tools and Services Used**

### **Google Cloud Services:**
1. **Cloud Storage:** For raw data storage.
2. **Cloud Data Fusion:** ETL tool for data transformation.
3. **BigQuery:** Centralized data warehouse for storage and querying.
4. **Looker Studio:** Dashboards and reports for data visualization.
5. **Cloud Composer:** Managed service to host Airflow for workflow automation.

### **Other Tools:**
1. **Python:** For data extraction and script automation.
2. **Faker Library:** To generate synthetic employee data.
3. **Airflow DAGs:** For orchestrating the pipeline.


## **Project Workflow**

### **Phase 1: ETL Pipeline Creation**
1. **Data Extraction:**
   - Developed a Python script using the Faker library to generate dummy employee data:
   - Stored the generated data in a Google Cloud Storage bucket through gcloud CLI.  

2. **Data Transformation:**
   - Used Cloud Data Fusion to make data transformations like masking the sensitive data and joining fields etc.

3. **Data Loading:**
   - Transformed data was loaded into BigQuery using the ETL pipleine built using Data Fusion, creating a table for storage and querying.

4. **Data Visualization:**
   - Built dashboards in Looker Studio and published it.

---

### **Phase 2: Automation with Cloud Composer (Airflow)**  
Automated the pipeline using Cloud Composer, which hosts Airflow DAGs to streamline tasks.

#### **Steps in Automation:**
1. **Set Up Cloud Composer:**
   - Created a Cloud Composer 2 environment and used Airflow to orchestrate tasks in a sequential workflow.

2. **DAG Creation:**
   - **Task 1: Data Extraction**
     - Written Python script (`extract.py`) to generate and upload dummy employee data to a Cloud Storage bucket.
   - **Task 2: Data Fusion Pipeline**
     - Used the Data Fusion Operator in Airflow to trigger the pre-configured Data Fusion pipeline for data transformation and loading into BigQuery.  

3. **Task Dependency Setup:**
   - Ensured sequential execution:
     - Task 1 (Data extraction) must complete successfully before Task 2 (Trigger Data Fusion pipeline) begins.  

4. **Error Handling:**
   - **Dependency Errors:** 
     - Added task dependencies using the Airflow `>>` operator to ensure proper execution order.
   - **Python Dependencies:**
     - Installed the required `faker` library in the Cloud Composer environment via PyPI configuration to avoid missing module errors.
   - **Quota Limitations:**
     - Addressed free-tier quota errors by:
       - Reducing resource usage (e.g., disk size and number of nodes) in Data Fusion and Cloud Composer configurations.
   - **Pipeline Failures:**
     - Monitored pipeline logs to detect and resolve issues during provisioning or execution in Data Fusion.
   - **Data Validation Errors:**
     - Ensured data integrity through schema validation during BigQuery loading.  

5. **Execution and Validation:**
   - Successfully ran the DAG:
     - Data was extracted and uploaded to Cloud Storage.
     - Data Fusion pipeline transformed and loaded the data into BigQuery.
     - Dashboards in Looker Studio were updated with the latest data.

## **Outcome**
1. **Automated Workflow:**
   - The entire pipeline, from data extraction to visualization, is fully automated using Airflow.
   - Real-time updates in Looker Studio dashboards upon new data arrival.  

2. **Efficiency and Scalability:**
   - Leveraged Google Cloud’s managed services for a robust, scalable solution.
   - Reduced manual intervention with automation.  

3. **Error Resilience:**
   - Addressed common pipeline failures with robust error-handling mechanisms.
   - Implemented retries and task dependencies for smooth execution.

## **Conclusion**
This project showcases the implementation and automation of an end-to-end data engineering pipeline using Google Cloud services. The pipeline efficiently handles data extraction, transformation, and loading while enabling dynamic reporting through Looker Studio. With Airflow automation, the solution is scalable and production-ready, making it ideal for real-time data workflows in enterprise settings.
