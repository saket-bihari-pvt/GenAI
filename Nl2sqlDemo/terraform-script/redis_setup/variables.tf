variable "compartment_id" {
  description = "The OCID of the compartment"
  type        = string
  default     = "your_compartment_ocid_here"
}

variable "redis_cluster_display_name" {
  description = "The display name for the Redis cluster"
  type        = string
  default     = "your_redis_cluster_display_name_here"
}

variable "redis_cluster_node_count" {
  description = "The number of nodes in the Redis cluster"
  type        = number
  default     = 3
}

variable "redis_cluster_node_memory_in_gbs" {
  description = "The amount of memory per node in GBs"
  type        = number
  default     = 8
}

variable "redis_cluster_software_version" {
  description = "The software version for the Redis cluster"
  type        = string
  default     = "V7_0_5"
}

variable "subnet_id" {
  description = "The OCID of the existing subnet"
  type        = string
  default     = "your_subnet_ocid_here"
}

variable "region" {
  description = "The OCI region"
  type        = string
  default     = "your_oci_region_here"
}
