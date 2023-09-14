"""
Author       : Adarsh Namdev
Activity     : GCP POC
GCP Service  : BigQuery
Task(s)      :
              - create dataset
              - create table
              - delete table
              - delete dataset
"""

from google.cloud import bigquery
from google.cloud.exceptions import NotFound
# import pandas as pd


def create_bq_dataset(project_name, dataset_name):
    datasetID = f"{project_name}.{dataset_name}"
    try:
        client.get_dataset(datasetID)
        #print("Dataset Instance Returned: ", client.get_dataset(datasetID))
        print(f"Dataset '{datasetID}' already exists!")
    
    except NotFound:
        dataset_obj = bigquery.Dataset(datasetID)
        bqdataset = client.create_dataset(dataset_obj, timeout= 30)
        
        print(f"""Dataset- '{datasetID}' created !""")


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


def delete_bq_table(project_name, dataset_name, tblname):
    tableID = f"""{project_name}.{dataset_name}.{tblname}"""
    try:
        client.delete_table(tableID, not_found_ok= False)
        print(f"table '{tableID}' deleted successfully !")

    except NotFound:
        print(f"Table '{tableID}' not found !")


def delete_bq_dataset(project_name, dataset_name):
    datasetID = f"""{project_name}.{dataset_name}"""
    try:
        client.delete_dataset(datasetID, not_found_ok= False)
        print(f"Dataset '{datasetID}' deleted successfully !")

    except NotFound:
        print(f"Dataset '{datasetID}' not found !")



client = bigquery.Client()
gcp_project_name = "dataproc-397308"

# 1.) Creating a BigQuery dataset
create_bq_dataset(project_name = gcp_project_name, dataset_name = "BostonHousing")

# 2.) Creating a BigQuery table in the dataset
create_bq_table(gcp_project_name, "BostonHousing", "HouseDetails")

# 3.) Deleting a BigQuery table from the dataset
delete_bq_table(gcp_project_name, "BostonHousing", "HouseDetails")

# 4.) Deleting the BigQuery dataset from the project
delete_bq_dataset(gcp_project_name, "BostonHousing")

print("----------------- EOF ---------------------")


