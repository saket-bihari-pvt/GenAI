#!/bin/bash

# Variables for importing the custom image
COMPARTMENT_ID="your_compartment_ocid_here"
DISPLAY_NAME="your_image_display_name_here"
PAR_URL="your_pre_authenticated_request_url_here"

# OCI CLI command to import the custom image from the object storage
oci compute image import from-object-uri \
    --compartment-id "$COMPARTMENT_ID" \
    --display-name "$DISPLAY_NAME" \
    --uri "$PAR_URL"