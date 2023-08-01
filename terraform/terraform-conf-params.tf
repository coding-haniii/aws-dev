# terraform-conf-params.tf
# prj
variable "project_name" {
  default = "projectName"
} 

# local / dev/ prod
variable "environment" {
  default = "dev"
}

# network
variable "cidr_vpc" {
  default = "192.168.0.0/16"
}
variable "cidr_public1" {
  default = "192.168.0.0/20"
}
variable "cidr_public2" {
  default = "192.168.16.0/20"
}
variable "cidr_private1" {
  default = "192.168.32.0/20"
}
variable "cidr_private2" {
  default = "192.168.48.0/20"
}

