provider "aws" {
  region                  = "us-east-1"
  shared_credentials_file = "~/.aws/terraform"
  profile                 = "default"
}

terraform {
  backend "s3" {
    bucket = "politico-terraform-configs"
    key = "civic/staging/terraform.tfstate"
    region = "us-east-1"
  }
}

##################################################################
# Data sources to get VPC, subnet, security group and AMI details
##################################################################

resource "aws_security_group" "ssh-staging" {
  name        = "ssh-security-group-${var.target}"
  description = "Allows SSH traffic from internet"
  vpc_id      = "vpc-14051972"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags {
    Name = "ssh-security-group-${var.target}"
  }
}

resource "aws_security_group" "web-staging" {
  name        = "web-security-group-${var.target}"
  description = "Allows web traffic from internet"
  vpc_id      = "vpc-14051972"

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 65535
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags {
    Name = "web-security-group-${var.target}"
  }
}

data "aws_eip" "proxy_ip-staging" {
  public_ip = "${var.public_ip}"
}

resource "aws_eip_association" "proxy_eip-staging" {
  instance_id   = "${aws_instance.civic-staging.id}"
  allocation_id = "${data.aws_eip.proxy_ip-staging.id}"
}

resource "aws_instance" "civic-staging" {
  ami           = "ami-7d030c02"
  instance_type = "${var.server_size}"
  subnet_id     = "subnet-1792345f"
  key_name      = "politicoapps.com"

  # iam_instance_profile = "${aws_iam_instance_profile.civic_ec2_instance_profile.name}"

  vpc_security_group_ids = [
    "${aws_security_group.ssh-staging.id}",
    "${aws_security_group.web-staging.id}",
  ]
  associate_public_ip_address = true
  tags {
    Name   = "civic-${var.target}"
    target = "${var.target}"
  }
  connection = {
    type        = "ssh"
    user        = "ubuntu"
    private_key = "${file("${var.pem_path}")}"
    agent       = true
  }
  provisioner "remote-exec" {
    script = "../scripts/deploy.sh"
  }
  provisioner "file" {
    source      = "./.env"
    destination = "/home/ubuntu/apps/politico-civic/.env"
  }
  provisioner "remote-exec" {
    script = "../scripts/postdeploy.sh"
  }
}
