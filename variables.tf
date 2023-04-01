variable "project" {
    type        = string
    description = "Google cloud project id"
}

variable "region" {
    type        = string
    description = "Region where services will be hosted"
}

variable "credentials" {
    type        = string
    description = "Local path where your google cloud credentials json is stored"
}

variable "bq_dataset" {
    type        = string
    description = "Name of the big query data set"
}
