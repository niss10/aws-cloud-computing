resource "aws_s3_bucket" "static_files" {
  bucket = var.bucket_name

  tags = {
    Name = "StaticWebFiles"
  }
}
