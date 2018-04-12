provider "aws" {
  region                  = "us-east-1"
  shared_credentials_file = "~/.aws/terraform"
  profile                 = "default"
}

##################################################################
# Data sources to get VPC, subnet, security group and AMI details
##################################################################

variable "public_ip" {}

resource "aws_security_group" "ssh" {
  name        = "ssh-security-group"
  description = "Allows SSH traffic from internet"
  vpc_id      = "vpc-14051972"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags {
    Name = "ssh-security-group"
  }
}

resource "aws_security_group" "web" {
  name        = "web-security-group"
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
    Name = "web-security-group"
  }
}

data "aws_eip" "proxy_ip" {
  public_ip = "${var.public_ip}"
}

resource "aws_eip_association" "proxy_eip" {
  instance_id   = "${aws_instance.civic.id}"
  allocation_id = "${data.aws_eip.proxy_ip.id}"
}

resource "aws_instance" "civic" {
  ami           = "ami-65d40f1a"
  instance_type = "t2.micro"
  subnet_id     = "subnet-1792345f"
  key_name      = "politicoapps.com"

  vpc_security_group_ids = [
    "${aws_security_group.ssh.id}",
    "${aws_security_group.web.id}",
  ]

  associate_public_ip_address = true

  connection = {
    type        = "ssh"
    user        = "ubuntu"
    private_key = "${file("~/src/privateeye/politicoapps.com.pem")}"
    agent       = true
  }

  provisioner "remote-exec" {
    script = "./scripts/deploy.sh"
  }

  provisioner "file" {
    source      = "./.env"
    destination = "/home/ubuntu/apps/politico-civic/.env"
  }
}
