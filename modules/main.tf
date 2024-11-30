provider "aws" {
    region = "us-east-1"
}

module "ec2_instance" {
  source = "C:\Users\HP 348 G4\devopstraining\getting-started-app\modules\ec2_instance"
  ami_value = "ami-0e86e20dae9224db8"
  instance_type_value = "t2.micro"
  subnet_id_value = "subnet-0e6adcd743f850cfc"
}