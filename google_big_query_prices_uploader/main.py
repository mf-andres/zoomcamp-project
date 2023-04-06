import typer
from google.cloud import storage
from google.cloud import bigquery
from google.cloud.bigquery import TableReference
from google.oauth2.service_account import Credentials

from settings.settings import Settings
from utils.path_utils import get_project_root


def upload_prices_to_big_query_from_storage(prices_file: str):
    settings = Settings(_env_file=get_project_root() / ".env")
    project_id = settings.project_id
    bucket_id = settings.bucket_id
    dataset_id = settings.dataset_id

    # Get the credentials file
    credentials_path = get_project_root() / "credentials/credentials.json"
    credentials = Credentials.from_service_account_file(str(credentials_path))

    # Set the name of the blob you want to download from storage
    source_blob_name = f'{bucket_id}/prices_files/{prices_file}'

    # Set the name of the destination table
    table_name = f'{project_id}.{dataset_id}.prices_raw'

    # Initialize a client object with the credentials
    client = storage.Client(credentials=credentials)

    # Get a reference to the bucket
    bucket = client.get_bucket(bucket_id)

    # Get a reference to the Parquet file
    blob = bucket.blob(source_blob_name)

    # Download the Parquet file to a local temporary file
    local_file_name = '/tmp/' + prices_file
    blob.download_to_filename(local_file_name)

    # Initialize a BigQuery client object with the credentials
    bq_client = bigquery.Client(credentials=credentials)

    # Get a reference to the destination table
    table_ref = TableReference.from_string(table_name)

    # Set the job configuration to load data from a Parquet file
    job_config = bigquery.LoadJobConfig()
    job_config.source_format = bigquery.SourceFormat.PARQUET
    job_config.autodetect = True

    # Start the load job
    with open(local_file_name, 'rb') as file:
        load_job = bq_client.load_table_from_file(file, table_ref, job_config=job_config)

    # Wait for the load job to complete
    load_job.result()

    print(f'Loaded data from {prices_file} into BigQuery table {table_name}.')


if __name__ == '__main__':
    typer.run(upload_prices_to_big_query_from_storage)
