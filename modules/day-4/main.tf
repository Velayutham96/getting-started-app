provider "aws" {
  region = "us-east-1" 
}

resource "aws_instance" "velayutham" {
  instance_type = "t2.micro"
  ami = "ami-0e86e20dae9224db8"
  subnet_id = "subnet-0e6adcd743f850cfc"
}