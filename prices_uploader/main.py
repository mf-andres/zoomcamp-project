import typer
from google.cloud import storage
from google.oauth2.service_account import Credentials

from utils.path_utils import get_project_root


def upload_prices_to_google_storage(prices_file: str):
    # Set the name of your GCS bucket and Google Cloud project ID
    bucket_name = 'zoomcamp-project-382011'  # TODO config and also config in terraform
    project_id = 'zoomcamp-project-382011'

    # Set the name of the file you want to upload and the name you want to give it in the bucket
    destination_blob_name = f'{bucket_name}/prices_files/{prices_file}'

    # Get the credentials file
    credentials_path = get_project_root() / "credentials/credentials.json"
    credentials = Credentials.from_service_account_file(str(credentials_path))

    # Initialize a client object with the credentials
    client = storage.Client(project=project_id, credentials=credentials)

    # Get a reference to the bucket
    bucket = client.bucket(bucket_name)

    # Upload the file to the bucket
    blob = bucket.blob(destination_blob_name)
    prices_file_path = get_project_root() / "prices_files" / prices_file
    blob.upload_from_filename(prices_file_path)

    print(f'File {prices_file} uploaded to {destination_blob_name} in bucket {bucket_name}.')


if __name__ == '__main__':
    typer.run(upload_prices_to_google_storage)
