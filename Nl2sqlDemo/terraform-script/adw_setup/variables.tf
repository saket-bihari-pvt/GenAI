variable "region" {
  description = "OCI Region"
  type        = string
  default     = "your_oci_region_here"
}

variable "compartment_id" {
  description = "OCI Compartment OCID"
  type        = string
  default     = "your_compartment_ocid_here"
}

variable "admin_password" {
  description = "Password for the Autonomous Database Admin user"
  type        = string
  default     = "your_admin_password_here"
}

variable "db_name" {
  description = "Name of the Autonomous Database"
  type        = string
  default     = "your_db_name_here"
}

variable "cpu_core_count" {
  description = "Number of OCPUs to be allocated to the Autonomous Database"
  type        = number
  default     = 1
}

variable "data_storage_size_in_tbs" {
  description = "Size of data storage in terabytes"
  type        = number
  default     = 1
}

variable "display_name" {
  description = "Display name of the Autonomous Database"
  type        = string
  default     = "your_display_name_here"
}