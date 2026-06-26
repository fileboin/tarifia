module "test_s3_buckets" {
  source = "../modules/s3_buckets"
  providers = {
    aws = aws.us_east_2
  }

  environment     = "test"
  allowed_origins = ["https://test.tarifia.sh"]
}

module "test_application_access" {
  source = "../modules/application_access"
  providers = {
    aws = aws.us_east_2
  }

  username = "tarifia-test-files"
  buckets = {
    customer_invoices = { name = "tarifia-test-customer-invoices" }
    customer_receipts = { name = "tarifia-test-customer-receipts" }
    payout_invoices   = { name = "tarifia-test-payout-invoices" }
    files             = { name = "tarifia-test-files", description = "Policy used by our TEST app for downloadable benefits. Keep permissions to a bare minimum." }
    public_files      = { name = "tarifia-test-public-files", description = "Policy used by our TEST app for public uploads -products medias and such-. Keep permissions to a bare minimum." }
    logs              = { name = "tarifia-test-logs", description = "Policy used by our TEST app to write OpenTelemetry spans to S3 for long-term backup." }
  }
}

import {
  to = module.test_s3_buckets.aws_s3_bucket.customer_invoices
  id = "tarifia-test-customer-invoices"
}

import {
  to = module.test_s3_buckets.aws_s3_bucket.customer_receipts
  id = "tarifia-test-customer-receipts"
}

import {
  to = module.test_s3_buckets.aws_s3_bucket.files
  id = "tarifia-test-files"
}

import {
  to = module.test_s3_buckets.aws_s3_bucket.logs
  id = "tarifia-test-logs"
}

import {
  to = module.test_s3_buckets.aws_s3_bucket.payout_invoices
  id = "tarifia-test-payout-invoices"
}

import {
  to = module.test_s3_buckets.aws_s3_bucket.public_assets
  id = "tarifia-test-public-assets"
}

import {
  to = module.test_s3_buckets.aws_s3_bucket.public_files
  id = "tarifia-test-public-files"
}

import {
  to = module.test_s3_buckets.aws_s3_bucket_cors_configuration.files
  id = "tarifia-test-files"
}

import {
  to = module.test_s3_buckets.aws_s3_bucket_cors_configuration.public_files
  id = "tarifia-test-public-files"
}

import {
  to = module.test_s3_buckets.aws_s3_bucket_policy.public_assets
  id = "tarifia-test-public-assets"
}

import {
  to = module.test_s3_buckets.aws_s3_bucket_policy.public_files
  id = "tarifia-test-public-files"
}

import {
  to = module.test_s3_buckets.aws_s3_bucket_public_access_block.public_assets
  id = "tarifia-test-public-assets"
}

import {
  to = module.test_s3_buckets.aws_s3_bucket_public_access_block.public_files
  id = "tarifia-test-public-files"
}

import {
  to = module.test_application_access.aws_iam_user.this
  id = "tarifia-test-files"
}

import {
  to = module.test_application_access.aws_iam_policy.customer_invoices
  id = "arn:aws:iam::975049931254:policy/tarifia-test-customer-invoices"
}

import {
  to = module.test_application_access.aws_iam_policy.customer_receipts
  id = "arn:aws:iam::975049931254:policy/tarifia-test-customer-receipts"
}

import {
  to = module.test_application_access.aws_iam_policy.files
  id = "arn:aws:iam::975049931254:policy/tarifia-test-files"
}

import {
  to = module.test_application_access.aws_iam_policy.logs
  id = "arn:aws:iam::975049931254:policy/tarifia-test-logs"
}

import {
  to = module.test_application_access.aws_iam_policy.payout_invoices
  id = "arn:aws:iam::975049931254:policy/tarifia-test-payout-invoices"
}

import {
  to = module.test_application_access.aws_iam_policy.public_files
  id = "arn:aws:iam::975049931254:policy/tarifia-test-public-files"
}

import {
  to = module.test_application_access.aws_iam_user_policy_attachment.customer_invoices
  id = "tarifia-test-files/arn:aws:iam::975049931254:policy/tarifia-test-customer-invoices"
}

import {
  to = module.test_application_access.aws_iam_user_policy_attachment.customer_receipts
  id = "tarifia-test-files/arn:aws:iam::975049931254:policy/tarifia-test-customer-receipts"
}

import {
  to = module.test_application_access.aws_iam_user_policy_attachment.files
  id = "tarifia-test-files/arn:aws:iam::975049931254:policy/tarifia-test-files"
}

import {
  to = module.test_application_access.aws_iam_user_policy_attachment.logs
  id = "tarifia-test-files/arn:aws:iam::975049931254:policy/tarifia-test-logs"
}

import {
  to = module.test_application_access.aws_iam_user_policy_attachment.payout_invoices
  id = "tarifia-test-files/arn:aws:iam::975049931254:policy/tarifia-test-payout-invoices"
}

import {
  to = module.test_application_access.aws_iam_user_policy_attachment.public_files
  id = "tarifia-test-files/arn:aws:iam::975049931254:policy/tarifia-test-public-files"
}
