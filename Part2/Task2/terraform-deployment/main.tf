module "vpc" {
  source              = "./modules/vpc"
  vpc_cidr            = "10.0.0.0/16"
  public_subnet_cidr  = "10.0.1.0/24"
  private_subnet_cidr = "10.0.2.0/24"
}

module "ec2" {
  source        = "./modules/ec2"
  ami_id        = "ami-00a929b66ed6e0de6"
  instance_type = "t2.micro"
  subnet_id     = module.vpc.private_subnet_id
  key_name      = "NisargLinuxKey"
}

module "s3" {
  source      = "./modules/s3"
  bucket_name = "nisarg-static-web-bucket-hw2"
}

module "dynamodb" {
  source     = "./modules/dynamodb"
  table_name = "user-logins"
  hash_key   = "username"
}
