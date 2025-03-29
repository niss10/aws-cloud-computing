resource "aws_instance" "web" {
  count = 3  # Creates 3 instances

  ami           = "ami-071226ecf16aa7d96"
  instance_type = "t2.micro"

  tags = {
    Name = "Nisarg-Terraform-Instance-${count.index}"
  }
}