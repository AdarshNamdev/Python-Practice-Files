
"""
Author       : Adarsh Namdev
Activity     : GCP POC
GCP Service  : BigQuery
Task(s)      :
              - create table out of GCS file(can be bq and python library)
                format : csv, parquet, json
"""

from google.cloud import bigquery
from google.cloud.exceptions import NotFound



def create_bq_table(project_name, dataset_name, tblname):
    tableID = f"""{project_name}.{dataset_name}.{tblname}"""
    try:
        client.get_table(tableID)
        #print("Table Instance Returned: ", client.get_table(tableID))
        print(f"Table '{tableID}' already exists !")
    
    except NotFound:
        tableobj = bigquery.Table(tableID)
        bqtable = client.create_table(tableobj)
        
        print(f"""Table - '{tableID}' created !""")

def load_data_in_BQtable(project_name, dataset_name, tblname, storage_uri, file_name, fileschema):
    """
    project_name: str, name of the project user is into
    dataset_name: str, name of the dataset where the table is present
    tblname: str, name of the table in the `project_name.dataset_name` to load the data into
    storage_uri : str, uri of the gcp bucket from where the file is to be read
    file_name: str, file name (along with extension) of type csv or parquet or json
                e.g: somefile.csv, somefile.parquet or somefiel.json
    fileschema = schema of the file, when file type is csv.
    """

    if file_name.endswith(".csv"):
        # setting the configurations to read the csv file
        job_configuration = bigquery.LoadJobConfig(
            schema = fileschema
            ,field_delimiter = ","
            ,source_format = bigquery.SourceFormat.CSV
            ,skip_leading_rows = 1           # to skip the header of the csv file if present with column names.
        )

        file_uri = f"{storage_uri}/{file_name}"
        tableID = f"{project_name}.{dataset_name}.{tblname}"
        table_obj = bigquery.Table(tableID)
        
        # now making a call to the api to start the data loading
        load_tbl = client.load_table_from_uri(source_uris = file_uri, 
                                              destination = table_obj, 
                                              job_config = job_configuration)

        load_tbl.result()

        print(f"Data loaded into the BigQuery table- {tblname}")

    if file_name.endswith(".parquet"):
        pass


    if file_name.endswith(".json"):
        pass





client = bigquery.Client()
gcp_project_name = "dataproc-397308"
bq_dataset_name = "NatGeo"
src_file_name = "abalone.csv"
tab_name = "abalone"
csv_file_schema = [
                bigquery.SchemaField("sex","STRING"),
                bigquery.SchemaField("length","NUMERIC"),
                bigquery.SchemaField("diameter","NUMERIC"),
                bigquery.SchemaField("height","NUMERIC"),
                bigquery.SchemaField("whole_weight","NUMERIC"),
                bigquery.SchemaField("shucked_weight","NUMERIC"),
                bigquery.SchemaField("viscera_weight","NUMERIC"),
                bigquery.SchemaField("shell_weight","NUMERIC"),
                bigquery.SchemaField("rings","NUMERIC")
                ]

# Creating a BigQuery table in the dataset
create_bq_table(gcp_project_name, "NatGeo", "Abalone")

# Loading data into the bigquery dataset

load_data_in_BQtable(project_name = gcp_project_name, 
                     dataset_name = bq_dataset_name, 
                     tblname = tab_name, 
                     storage_uri = "gs://dig0axn2", 
                     file_name = "abalone.csv", 
                     fileschema = csv_file_schema)


print("\n============================== EOF ==============================\n")
