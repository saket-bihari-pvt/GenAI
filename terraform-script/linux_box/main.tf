provider "oci" {
  region = var.region
}

resource "oci_core_instance" "test_instance" {
  compartment_id      = var.compartment_id
  availability_domain = var.availability_domain
  shape               = var.instance_shape

  create_vnic_details {
    subnet_id        = var.subnet_id
    assign_public_ip = true
  }

  source_details {
    source_type = "image"
    source_id   = var.custom_image_ocid
  }

  metadata = {
    ssh_authorized_keys = file(var.ssh_public_key)
  }

  display_name = var.image_display_name
}