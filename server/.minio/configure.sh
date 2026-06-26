#!/bin/bash

$CMD_MC alias set tarifia http://$MINIO_HOST:9000 $MINIO_ROOT_USER $MINIO_ROOT_PASSWORD;

# Setup user & acccess policy
$CMD_MC admin user add tarifia $ACCESS_KEY $SECRET_ACCESS_KEY
$CMD_MC admin policy create tarifia tarifia-development $POLICY_FILE
$CMD_MC admin policy attach tarifia tarifia-development --user $ACCESS_KEY

# Create buckets
$CMD_MC mb tarifia/$BUCKET_NAME --with-versioning --ignore-existing

$CMD_MC mb tarifia/$PUBLIC_BUCKET_NAME --with-versioning --ignore-existing
$CMD_MC anonymous set download tarifia/$PUBLIC_BUCKET_NAME

$CMD_MC mb tarifia/$BUCKET_TESTING_NAME --with-versioning --ignore-existing
