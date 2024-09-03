variable "compartment_id" {
  description = "The OCID of the compartment"
  type        = string
  default     = "your_compartment_ocid_here"
}

variable "region" {
  description = "The OCI region"
  type        = string
  default     = "your_oci_region_here"
}

variable "availability_domain" {
  description = "The availability domain to launch the instance in"
  type        = string
  default     = "your_availability_domain_here"
}

variable "subnet_id" {
  description = "The OCID of the existing subnet"
  type        = string
  default     = "your_subnet_ocid_here"
}

variable "instance_shape" {
  description = "The shape of the instance"
  type        = string
  default     = "your_instance_shape_here"
}

variable "custom_image_ocid" {
  description = "The OCID of the custom image"
  type        = string
  default     = "your_custom_image_ocid_here"
}

variable "ssh_public_key" {
  description = "The path to the SSH public key file"
  type        = string
  default     = "path_to_your_ssh_public_key_here"
}

variable "image_display_name" {
  description = "Display name for the custom image."
  type        = string
  default     = "your_image_display_name_here"
}