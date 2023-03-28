# Zoomcamp Project

## Intro

mf-andres final project for the third cohort of the data engineering zoomcamp.

Contains a data pipeline that extracts prices data from wallapop (a digital second hand items market)
and analyzes it.

## Installation

Install poetry as told in their webpage. https://python-poetry.org/docs/

Install dependencies.

```commandline
make install_dependencies
```

Create a Google project and a service account.

1. Go to the Google Cloud Console and sign in with your Google account. If you don't have a Google account, create one
   first.

2. In the Google Cloud Console, click on the project drop-down menu at the top of the screen and click "New Project".
   Enter a name for your project and click "Create".

3. Once your project has been created, select it from the project drop-down menu at the top of the screen.

4. Click on the navigation menu icon at the top left of the screen and select "IAM & admin" > "Service accounts".

5. Click "Create Service Account". Enter a name for your service account and click "Create".

6. In the "Service account permissions" section, grant the service account the appropriate roles and permissions for
   your project. Grant the followin roles: "Storage Admin", ...

7. Click "Continue" and then "Done" to create the service account.

8. Find your newly created service account in the "Service accounts" list and click on the three-dot menu on the right
   side of the screen. Select "Create key" > "JSON" and click "Create". This will download a JSON file containing your
   service account credentials.

9. Save the downloaded JSON file in a the credentials folder with the name credentials.json.

Install terraform as told in their
webpage. https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli

Change the project id in main.tf and put yours as follows.

```terraform
provider "google" {
  credentials = file("./credentials/credentials.json")
  project     = "{{put your project id here}}"
  region      = "europe-southwest1"
}
```

Change the name of the bucket that you are going to create in main.tf as follows.

```terraform
resource "google_storage_bucket" "my_bucket" {
  name     = "{{put your bucket name here}}"
  location = "europe-southwest1"
}
```

Deploy Google infrastructure

```commandline
make deploy_google_infrastructure
```

# Start

Try to load and store some prices from wallapop

```commandline
make store-prices-example
```
