terraform {
  cloud {
    organization = "tarifia-sh"
    workspaces {
      name = "organization"
    }
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.92"
    }
  }

  required_version = ">= 1.5"
}
