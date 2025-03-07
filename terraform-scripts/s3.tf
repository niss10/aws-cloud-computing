provider "aws" {
    region = "us-east-1"
}

resource "aws_s3_bucket" "nisarg_bucket" {
  bucket = "nisarg-terraform-s3-bucket-v1"  # Replace with a globally unique name
}

resource "aws_s3_bucket_versioning" "versioning_example" {
  bucket = aws_s3_bucket.nisarg_bucket.id
  versioning_configuration {
    status = "Enabled"
  }
}
