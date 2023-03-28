provider "google" {
  credentials = file("./credentials/credentials.json")
  project     = "zoomcamp-project-382011"
  region      = "europe-southwest1"
}

resource "google_storage_bucket" "my_bucket" {
  name     = "zoomcamp-project-382011"
  location = "europe-southwest1"
}
