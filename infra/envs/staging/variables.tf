variable "env" {
  type    = string
  default = "dev"
}
variable "name" {
  type    = string
  default = "sample"
}
variable "region" {
  type    = string
  default = "us-east-1"
}

variable "vpc_cidr" {
  type    = string
  default = "10.0.0.0/16"
}
variable "azs" {
  type    = list(string)
  default = ["us-east-1a", "us-east-1b"]
}

variable "instance_ami" {
  type = string

} 
variable "instance_type" {
  type    = string
  default = "t3.micro"
}
variable "ssh_ingress_cidrs" {
  type    = list(string)
  default = ["0.0.0.0/0"]
}
variable "key_name" {
  type    = string
  default = null
}
