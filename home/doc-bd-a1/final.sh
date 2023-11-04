#!/bin/bash

# Set your container name or ID
CONTAINER_NAME_OR_ID="2cb988483d9c249930a478a165a007d3c7957cca1c74951af4085604c314e7c3"

# Define the directory where the output files are generated within the container
CONTAINER_OUTPUT_DIR="doc-bd-a1/"

# Define the local directory where you want to copy the files
LOCAL_OUTPUT_DIR="bd-a1/service-result"

# Copy output files from the container to your local machine
docker cp "$CONTAINER_NAME_OR_ID:$CONTAINER_OUTPUT_DIR" "$LOCAL_OUTPUT_DIR"

# Stop and remove the container
#docker stop "$CONTAINER_NAME_OR_ID"
#docker rm "$CONTAINER_NAME_OR_ID"