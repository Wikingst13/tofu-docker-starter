variable "name" {
  type = string
}

variable "vpc_id" {
  type = string
}

variable "ingress_cidrs" {
  type    = list(string)
  default = ["0.0.0.0/0"]
}
