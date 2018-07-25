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

resource "aws_security_group" "ssh" {
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

resource "aws_security_group" "web" {
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

data "aws_eip" "proxy_ip" {
  public_ip = "${var.public_ip}"
}

resource "aws_eip_association" "proxy_eip" {
  instance_id   = "${aws_instance.civic.id}"
  allocation_id = "${data.aws_eip.proxy_ip.id}"
}

# resource "aws_s3_bucket" "civic_codepipeline_bucket" {
#   bucket = "civic-codepipeline-bucket"
#   acl    = "private"
# }

# resource "aws_iam_role" "codepipeline_role" {
#   name = "codepipeline-role"

#   assume_role_policy = <<EOF
# {
#   "Version": "2012-10-17",
#   "Statement": [
#     {
#       "Effect": "Allow",
#       "Principal": {
#         "Service": "codepipeline.amazonaws.com"
#       },
#       "Action": "sts:AssumeRole"
#     }
#   ]
# }
# EOF
# }

# resource "aws_iam_role_policy" "codepipeline_policy" {
#   name = "codepipeline_policy"
#   role = "${aws_iam_role.codepipeline_role.id}"

#   policy = <<EOF
# {
#   "Version": "2012-10-17",
#   "Statement": [
#     {
#       "Effect":"Allow",
#       "Action": "s3:*",
#       "Resource": [
#         "${aws_s3_bucket.civic_codepipeline_bucket.arn}",
#         "${aws_s3_bucket.civic_codepipeline_bucket.arn}/*"
#       ]
#     },
#     {
#       "Effect": "Allow",
#       "Action": "codedeploy:*",
#       "Resource": "*"
#     }
#   ]
# }
# EOF
# }

# resource "aws_codepipeline" "civic_pipeline" {
#   name     = "civic_pipeline"
#   role_arn = "${aws_iam_role.codepipeline_role.arn}"

#   artifact_store {
#     location = "${aws_s3_bucket.civic_codepipeline_bucket.bucket}"
#     type     = "S3"
#   }

#   stage {
#     name = "Source"

#     action {
#       name             = "Source"
#       category         = "Source"
#       owner            = "ThirdParty"
#       provider         = "GitHub"
#       version          = "1"
#       output_artifacts = ["repo"]

#       configuration {
#         Owner  = "The-Politico"
#         Repo   = "politico-civic"
#         Branch = "master"
#       }
#     }
#   }

#   stage {
#     name = "Deploy"

#     action {
#       name            = "Deploy"
#       category        = "Deploy"
#       owner           = "AWS"
#       provider        = "CodeDeploy"
#       input_artifacts = ["repo"]
#       version         = "1"

#       configuration {
#         ApplicationName     = "civic_codedeploy_app"
#         DeploymentGroupName = "civic"
#       }
#     }
#   }
# }

# resource "aws_iam_role" "civic_codedeploy_role" {
#   name = "civic_codedeploy_role"

#   assume_role_policy = <<EOF
# {
#   "Version": "2012-10-17",
#   "Statement": [
#     {
#       "Sid": "",
#       "Effect": "Allow",
#       "Principal": {
#         "Service": "codedeploy.amazonaws.com"
#       },
#       "Action": "sts:AssumeRole"
#     }
#   ]
# }
# EOF
# }

# resource "aws_iam_role_policy" "civic_codedeploy_policy" {
#   name = "civic_codedeploy_policy"
#   role = "${aws_iam_role.civic_codedeploy_role.id}"

#   policy = <<EOF
# {
#   "Version": "2012-10-17",
#   "Statement": [
#     {
#       "Effect": "Allow",
#       "Action": [
#         "CloudWatch:DescribeAlarms",
#         "codedeploy:*",
#         "ec2:DescribeInstances",
#         "ec2:DescribeInstanceStatus",
#         "tag:GetTags",
#         "tag:GetResources",
#         "sns:Publish"
#       ],
#       "Resource": "*"
#     }
#   ]
# }
# EOF
# }

# resource "aws_codedeploy_app" "civic_codedeploy_app" {
#   name = "civic_codedeploy_app"
# }

# resource "aws_sns_topic" "civic" {
#   name = "civic"
# }

# resource "aws_codedeploy_deployment_group" "civic" {
#   app_name              = "${aws_codedeploy_app.civic_codedeploy_app.name}"
#   deployment_group_name = "civic"
#   service_role_arn      = "${aws_iam_role.civic_codedeploy_role.arn}"

#   ec2_tag_filter {
#     key   = "Name"
#     type  = "KEY_AND_VALUE"
#     value = "civic"
#   }

#   trigger_configuration {
#     trigger_events     = ["DeploymentFailure"]
#     trigger_name       = "civic-failure-trigger"
#     trigger_target_arn = "${aws_sns_topic.civic.arn}"
#   }

#   auto_rollback_configuration {
#     enabled = true
#     events  = ["DEPLOYMENT_FAILURE"]
#   }

#   alarm_configuration {
#     alarms  = ["my-alarm-name"]
#     enabled = true
#   }
# }

# resource "aws_iam_role" "civic_ec2_role" {
#   name = "civic_ec2_role"

#   assume_role_policy = <<EOF
# {
#   "Version": "2012-10-17",
#   "Statement": [
#     {
#       "Sid": "",
#       "Effect": "Allow",
#       "Principal": {
#         "Service": "ec2.amazonaws.com"
#       },
#       "Action": "sts:AssumeRole"
#     }
#   ]
# }
#   EOF
# }

# resource "aws_iam_role_policy" "civic_ec2_role_policy" {
#   name = "civic_ec2_role_policy"
#   role = "${aws_iam_role.civic_ec2_role.id}"

#   policy = <<EOF
# {
#     "Version": "2012-10-17",
#     "Statement": [
#         {
#             "Action": [
#                 "ec2:*",
#                 "iam:PassRole",
#                 "iam:ListInstanceProfiles",
#                 "s3:Get*",
#                 "s3:List*"
#             ],
#             "Effect": "Allow",
#             "Resource": "*"
#         }
#     ]
# }
#   EOF
# }

# resource "aws_iam_instance_profile" "civic_ec2_instance_profile" {
#   name = "civic_ec2_instance_profile"
#   role = "${aws_iam_role.civic_ec2_role.name}"
# }

resource "aws_instance" "civic" {
  ami           = "ami-3348294c"
  instance_type = "${var.server_size}"
  subnet_id     = "subnet-1792345f"
  key_name      = "politicoapps.com"

  # iam_instance_profile = "${aws_iam_instance_profile.civic_ec2_instance_profile.name}"

  vpc_security_group_ids = [
    "${aws_security_group.ssh.id}",
    "${aws_security_group.web.id}",
  ]
  associate_public_ip_address = true
  tags {
    Name   = "civic-${var.target}"
    target = "${var.target}"
  }
  connection = {
    type        = "ssh"
    user        = "ubuntu"
    private_key = "${file("~/src/private-eye/politicoapps.com.pem")}"
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
