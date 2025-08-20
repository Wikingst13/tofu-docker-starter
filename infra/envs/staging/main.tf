module "vpc" {
  source     = "../../modules/vpc"
  name       = "${var.name}-${var.env}"
  cidr_block = var.vpc_cidr
  azs        = var.azs
}

module "web_sg" {
  source        = "../../modules/security_group"
  name          = "${var.name}-${var.env}-sg"
  vpc_id        = module.vpc.vpc_id
  ingress_cidrs = var.ssh_ingress_cidrs
}



module "web" {
  source             = "../../modules/ec2"
  name               = "${var.name}-${var.env}-web"
  ami                = var.instance_ami
  instance_type      = var.instance_type
  subnet_id          = module.vpc.public_subnet_ids[0]
  security_group_ids = [module.web_sg.id]
  key_name           = var.key_name
}
