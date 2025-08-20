name     = "sample"
region   = "us-east-1"
vpc_cidr = "10.0.0.0/16"
azs      = ["us-east-1a", "us-east-1b"]

instance_type     = "t3.micro"
ssh_ingress_cidrs = ["0.0.0.0/0"]
key_name          = null


instance_ami = "ami-1234567890abcdef0"