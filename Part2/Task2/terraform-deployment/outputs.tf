output "web_instance_id" {
  value = module.ec2.instance_id
}

output "s3_bucket" {
  value = module.s3.bucket_name
}

output "dynamodb_table" {
  value = module.dynamodb.table_name
}
