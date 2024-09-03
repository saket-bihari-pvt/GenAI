provider "oci" {
  region = var.region
}

resource "oci_database_autonomous_database" "adw_instance" {
  admin_password           = var.admin_password
  compartment_id           = var.compartment_id
  db_name                  = var.db_name
  cpu_core_count           = var.cpu_core_count
  data_storage_size_in_tbs = var.data_storage_size_in_tbs

  db_workload    = "DW" # Specify the workload type, "DW" for Data Warehouse
  display_name   = var.display_name
}