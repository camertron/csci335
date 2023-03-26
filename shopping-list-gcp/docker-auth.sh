#! /bin/bash

echo "Grabbing application default credentials (ADC)"
gcloud auth application-default login

echo "Configuring Docker client to talk to GCP's Artifact Registry"
gcloud auth configure-docker us-central1-docker.pkg.dev

echo "Done!"
