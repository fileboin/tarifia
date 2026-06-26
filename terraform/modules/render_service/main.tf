# Tarifia Render service setup
#
# Sets up a service, and the specified workers.
# Includes the environment groups

locals {
  environment = var.backend_config.environment == null ? var.environment : var.backend_config.environment
}

resource "render_env_group" "google" {
  environment_id = var.render_environment_id
  name           = "google-${var.environment}"
  env_vars = {
    TARIFIA_GOOGLE_CLIENT_ID     = { value = var.google_secrets.client_id }
    TARIFIA_GOOGLE_CLIENT_SECRET = { value = var.google_secrets.client_secret }
  }
}

resource "render_env_group" "openai" {
  environment_id = var.render_environment_id
  name           = "openai-${var.environment}"
  env_vars = {
    TARIFIA_OPENAI_API_KEY = { value = var.openai_secrets.api_key }
  }
}

resource "render_env_group" "pydantic_ai_gateway" {
  environment_id = var.render_environment_id
  name           = "pydantic-ai-gateway-${var.environment}"
  env_vars = {
    TARIFIA_PYDANTIC_AI_GATEWAY_API_KEY = { value = var.pydantic_ai_gateway_secrets.api_key }
  }
}

resource "render_env_group" "backend" {
  environment_id = var.render_environment_id
  name           = "backend-${var.environment}"
  env_vars = merge(
    {
      TARIFIA_USER_SESSION_COOKIE_DOMAIN           = { value = var.backend_config.user_session_cookie_domain }
      TARIFIA_AUTHENTICATION_SESSION_COOKIE_DOMAIN = { value = var.backend_config.authentication_session_cookie_domain }
      TARIFIA_OAUTH2_SESSION_STATE_COOKIE_DOMAIN   = { value = var.backend_config.oauth2_session_state_cookie_domain }
      TARIFIA_BASE_URL                             = { value = var.backend_config.base_url }
      TARIFIA_DEBUG                                = { value = var.backend_config.debug }
      TARIFIA_EMAIL_SENDER                         = { value = var.backend_config.email_sender }
      TARIFIA_EMAIL_FROM_NAME                      = { value = var.backend_config.email_from_name }
      TARIFIA_EMAIL_FROM_DOMAIN                    = { value = var.backend_config.email_from_domain }
      TARIFIA_ENV                                  = { value = local.environment }
      TARIFIA_FRONTEND_BASE_URL                    = { value = var.backend_config.frontend_base_url }
      TARIFIA_CHECKOUT_BASE_URL                    = { value = var.backend_config.checkout_base_url }
      TARIFIA_JWKS                                 = { value = var.backend_config.jwks_path }
      TARIFIA_LOG_LEVEL                            = { value = var.backend_config.log_level }
      TARIFIA_TESTING                              = { value = var.backend_config.testing }
      TARIFIA_AUTH_COOKIE_DOMAIN                   = { value = var.backend_config.auth_cookie_domain }
      TARIFIA_INVOICES_ADDITIONAL_INFO             = { value = var.backend_config.invoices_additional_info }
      TARIFIA_INVOICES_VAT_NUMBERS                 = { value = var.backend_config.invoices_vat_numbers }
      TARIFIA_STRIPE_PUBLISHABLE_KEY               = { value = var.backend_secrets.stripe_publishable_key }
      TARIFIA_CURRENT_JWK_KID                      = { value = var.backend_secrets.current_jwk_kid }
      TARIFIA_DISCORD_BOT_TOKEN                    = { value = var.backend_secrets.discord_bot_token }
      TARIFIA_DISCORD_CLIENT_ID                    = { value = var.backend_secrets.discord_client_id }
      TARIFIA_DISCORD_CLIENT_SECRET                = { value = var.backend_secrets.discord_client_secret }
      TARIFIA_DISCORD_PROXY_URL                    = { value = var.backend_secrets.discord_proxy_url }
      TARIFIA_RESEND_API_KEY                       = { value = var.backend_secrets.resend_api_key }
      TARIFIA_RESEND_WEBHOOK_SECRET                = { value = var.backend_secrets.resend_webhook_secret }
      TARIFIA_FIRECRAWL_API_KEY                    = { value = var.backend_secrets.firecrawl_api_key }
      TARIFIA_LOGO_DEV_PUBLISHABLE_KEY             = { value = var.backend_secrets.logo_dev_publishable_key }
      TARIFIA_SECRET                               = { value = var.backend_secrets.secret }
      TARIFIA_SENTRY_DSN                           = { value = var.backend_secrets.sentry_dsn }
      TARIFIA_TAX_PROCESSORS                       = { value = var.backend_config.tax_processors }
      TARIFIA_TAX_RECORD_PROCESSOR                 = { value = var.backend_config.tax_record_processor }
      TARIFIA_NUMERAL_API_KEY                      = { value = var.backend_secrets.numeral_api_key }
      TARIFIA_CUSTOMER_PORTAL_URL_OVERRIDES        = { value = var.backend_config.customer_portal_url_overrides }
    },
    var.backend_config.plain_default_tier_external_id != "" ? {
      TARIFIA_PLAIN_DEFAULT_TIER_EXTERNAL_ID = { value = var.backend_config.plain_default_tier_external_id }
    } : {},
    var.backend_config.user_session_cookie_key != "" ? {
      TARIFIA_USER_SESSION_COOKIE_KEY = { value = var.backend_config.user_session_cookie_key }
    } : {},
    var.backend_config.auth_cookie_key != "" ? {
      TARIFIA_AUTH_COOKIE_KEY = { value = var.backend_config.auth_cookie_key }
    } : {},
  )

  secret_files = {
    "jwks.json" = {
      content = var.backend_secrets.jwks
    }
  }
}

resource "render_env_group" "backend_production" {
  count          = var.environment == "production" ? 1 : 0
  environment_id = var.render_environment_id
  name           = "backend-production-only"
  env_vars = {
    TARIFIA_BACKOFFICE_HOST                = { value = var.backend_config.backoffice_host }
    TARIFIA_CHECKOUT_LINK_HOST             = { value = var.backend_config.checkout_link_host }
    TARIFIA_DISCORD_WEBHOOK_URL            = { value = var.backend_secrets.discord_webhook_url }
    TARIFIA_POSTHOG_PROJECT_API_KEY        = { value = var.backend_secrets.posthog_project_api_key }
    TARIFIA_PLAIN_REQUEST_SIGNING_SECRET   = { value = var.backend_secrets.plain_request_signing_secret }
    TARIFIA_PLAIN_TOKEN                    = { value = var.backend_secrets.plain_token }
    TARIFIA_PLAIN_CHAT_SECRET              = { value = var.backend_secrets.plain_chat_secret }
    TARIFIA_APP_REVIEW_EMAIL               = { value = var.backend_secrets.app_review_email }
    TARIFIA_APP_REVIEW_OTP_CODE            = { value = var.backend_secrets.app_review_otp_code }
    TARIFIA_CHARGEBACK_STOP_WEBHOOK_SECRET = { value = var.backend_secrets.chargeback_stop_webhook_secret }
  }
}

resource "render_env_group" "aws_s3" {
  environment_id = var.render_environment_id
  name           = "aws-s3-${var.environment}"
  env_vars = {
    TARIFIA_AWS_REGION                       = { value = var.aws_s3_config.region }
    TARIFIA_AWS_SIGNATURE_VERSION            = { value = var.aws_s3_config.signature_version }
    TARIFIA_S3_FILES_BUCKET_NAME             = { value = "tarifia-${var.environment}-files" }
    TARIFIA_S3_FILES_PRESIGN_TTL             = { value = var.aws_s3_config.files_presign_ttl }
    TARIFIA_S3_FILES_PUBLIC_BUCKET_NAME      = { value = var.aws_s3_config.files_public_bucket_name }
    TARIFIA_S3_CUSTOMER_INVOICES_BUCKET_NAME = { value = var.aws_s3_config.customer_invoices_bucket_name }
    TARIFIA_S3_CUSTOMER_RECEIPTS_BUCKET_NAME = { value = var.aws_s3_config.customer_receipts_bucket_name }
    TARIFIA_S3_PAYOUT_INVOICES_BUCKET_NAME   = { value = var.aws_s3_config.payout_invoices_bucket_name }
    TARIFIA_S3_LOGS_BUCKET_NAME              = { value = var.aws_s3_config.logs_bucket_name }
    TARIFIA_AWS_ACCESS_KEY_ID                = { value = var.aws_s3_secrets.access_key_id }
    TARIFIA_AWS_SECRET_ACCESS_KEY            = { value = var.aws_s3_secrets.secret_access_key }
    TARIFIA_S3_FILES_DOWNLOAD_SALT           = { value = var.aws_s3_secrets.files_download_salt }
    TARIFIA_S3_FILES_DOWNLOAD_SECRET         = { value = var.aws_s3_secrets.files_download_secret }
  }
}

resource "render_env_group" "worker_sqs" {
  count          = var.worker_sqs_config != null ? 1 : 0
  environment_id = var.render_environment_id
  name           = "worker-sqs-${var.environment}"
  env_vars = {
    TARIFIA_WORKER_SQS_ENABLED               = { value = var.worker_sqs_config.enabled }
    TARIFIA_WORKER_SQS_ACTORS                = { value = var.worker_sqs_config.actors }
    TARIFIA_WORKER_SQS_QUEUE_PREFIX          = { value = var.worker_sqs_config.queue_prefix }
    TARIFIA_WORKER_SQS_AWS_ACCESS_KEY_ID     = { value = var.worker_sqs_config.aws_access_key_id }
    TARIFIA_WORKER_SQS_AWS_SECRET_ACCESS_KEY = { value = var.worker_sqs_config.aws_secret_access_key }
  }
}

resource "render_env_group" "github" {
  environment_id = var.render_environment_id
  name           = "github-${var.environment}"
  env_vars = {
    TARIFIA_GITHUB_CLIENT_ID                           = { value = var.github_secrets.client_id }
    TARIFIA_GITHUB_CLIENT_SECRET                       = { value = var.github_secrets.client_secret }
    TARIFIA_GITHUB_REPOSITORY_BENEFITS_APP_IDENTIFIER  = { value = var.github_secrets.repository_benefits_app_identifier }
    TARIFIA_GITHUB_REPOSITORY_BENEFITS_APP_NAMESPACE   = { value = var.github_secrets.repository_benefits_app_namespace }
    TARIFIA_GITHUB_REPOSITORY_BENEFITS_APP_PRIVATE_KEY = { value = var.github_secrets.repository_benefits_app_private_key }
    TARIFIA_GITHUB_REPOSITORY_BENEFITS_CLIENT_ID       = { value = var.github_secrets.repository_benefits_client_id }
    TARIFIA_GITHUB_REPOSITORY_BENEFITS_CLIENT_SECRET   = { value = var.github_secrets.repository_benefits_client_secret }
  }
}

resource "render_env_group" "stripe" {
  environment_id = var.render_environment_id
  name           = "stripe-${var.environment}"
  env_vars = {
    TARIFIA_STRIPE_CONNECT_WEBHOOK_SECRET = { value = var.stripe_secrets.connect_webhook_secret }
    TARIFIA_STRIPE_SECRET_KEY             = { value = var.stripe_secrets.secret_key }
    TARIFIA_STRIPE_WEBHOOK_SECRET         = { value = var.stripe_secrets.webhook_secret }
  }
}

resource "render_env_group" "logfire" {
  count          = var.logfire_config != null ? 1 : 0
  environment_id = var.render_environment_id
  name           = "logfire-${var.environment}"
  env_vars = {
    TARIFIA_LOGFIRE_PROJECT_NAME = { value = var.logfire_config.project_name }
    TARIFIA_LOGFIRE_TOKEN        = { value = var.logfire_config.token }
  }
}


resource "render_env_group" "apple" {
  environment_id = var.render_environment_id
  name           = "apple-${var.environment}"
  env_vars = {
    TARIFIA_APPLE_CLIENT_ID = { value = var.apple_secrets.client_id }
    TARIFIA_APPLE_TEAM_ID   = { value = var.apple_secrets.team_id }
    TARIFIA_APPLE_KEY_ID    = { value = var.apple_secrets.key_id }
    TARIFIA_APPLE_KEY_VALUE = { value = var.apple_secrets.key_value }
  }
}

resource "render_env_group" "prometheus" {
  count          = var.prometheus_config != null ? 1 : 0
  environment_id = var.render_environment_id
  name           = "prometheus-${var.environment}"
  env_vars = merge(
    {
      TARIFIA_GRAFANA_CLOUD_PROMETHEUS_WRITE_URL      = { value = "${var.prometheus_config.url}/api/prom/push" }
      TARIFIA_GRAFANA_CLOUD_PROMETHEUS_WRITE_USERNAME = { value = var.prometheus_config.username }
      TARIFIA_GRAFANA_CLOUD_PROMETHEUS_WRITE_PASSWORD = { value = var.prometheus_config.password }
      TARIFIA_GRAFANA_CLOUD_PROMETHEUS_WRITE_INTERVAL = { value = var.prometheus_config.interval }
    },
    var.prometheus_config.query_key != null ? {
      TARIFIA_GRAFANA_CLOUD_PROMETHEUS_QUERY_URL  = { value = "${var.prometheus_config.url}/api/prom" }
      TARIFIA_GRAFANA_CLOUD_PROMETHEUS_QUERY_USER = { value = var.prometheus_config.username }
      TARIFIA_GRAFANA_CLOUD_PROMETHEUS_QUERY_KEY  = { value = var.prometheus_config.query_key }
    } : {}
  )
}

resource "render_env_group" "slo_report" {
  count          = var.slo_report_config != null ? 1 : 0
  environment_id = var.render_environment_id
  name           = "slo-report-${var.environment}"
  env_vars = {
    TARIFIA_SLACK_BOT_TOKEN = { value = var.slo_report_config.slack_bot_token }
    TARIFIA_SLACK_CHANNEL   = { value = var.slo_report_config.slack_channel }
  }
}

resource "render_env_group" "tinybird" {
  count          = var.tinybird_config != null ? 1 : 0
  environment_id = var.render_environment_id
  name           = "tinybird-${var.environment}"
  env_vars = {
    TARIFIA_TINYBIRD_API_URL             = { value = var.tinybird_config.api_url }
    TARIFIA_TINYBIRD_CLICKHOUSE_URL      = { value = var.tinybird_config.clickhouse_url }
    TARIFIA_TINYBIRD_API_TOKEN           = { value = var.tinybird_config.api_token }
    TARIFIA_TINYBIRD_READ_TOKEN          = { value = var.tinybird_config.read_token }
    TARIFIA_TINYBIRD_CLICKHOUSE_USERNAME = { value = var.tinybird_config.clickhouse_username }
    TARIFIA_TINYBIRD_CLICKHOUSE_TOKEN    = { value = var.tinybird_config.clickhouse_token }
    TARIFIA_TINYBIRD_WORKSPACE           = { value = var.tinybird_config.workspace }
  }
}

resource "render_env_group" "tarifia_self" {
  count          = var.tarifia_self_config != null ? 1 : 0
  environment_id = var.render_environment_id
  name           = "tarifia-self-${var.environment}"
  env_vars = {
    TARIFIA_TARIFIA_ACCESS_TOKEN     = { value = var.tarifia_self_config.access_token }
    TARIFIA_TARIFIA_WEBHOOK_SECRET   = { value = var.tarifia_self_config.webhook_secret }
    TARIFIA_TARIFIA_ORGANIZATION_ID  = { value = var.tarifia_self_config.organization_id }
    TARIFIA_TARIFIA_FREE_PRODUCT_ID  = { value = var.tarifia_self_config.free_product_id }
    TARIFIA_TARIFIA_API_URL          = { value = var.tarifia_self_config.api_url }
    TARIFIA_TARIFIA_SCALE_PRODUCT_ID = { value = var.tarifia_self_config.scale_product_id }
  }
}

resource "render_env_group" "memory_profile" {
  count          = var.memory_profile_config != null ? 1 : 0
  environment_id = var.render_environment_id
  name           = "memory-profile-${var.environment}"
  env_vars = {
    TARIFIA_MEMORY_PROFILE_ENABLED        = { value = "true" }
    TARIFIA_MEMORY_PROFILE_S3_BUCKET_NAME = { value = var.memory_profile_config.s3_bucket_name }
    TARIFIA_MEMORY_PROFILE_INTERVAL       = { value = var.memory_profile_config.interval }
  }
}

resource "render_env_group" "database" {
  environment_id = var.render_environment_id
  name           = "database-${var.environment}"
  env_vars = {
    TARIFIA_POSTGRES_DATABASE      = { value = var.api_service_config.postgres_database }
    TARIFIA_POSTGRES_HOST          = { value = var.postgres_config.host }
    TARIFIA_POSTGRES_PORT          = { value = var.postgres_config.port }
    TARIFIA_POSTGRES_USER          = { value = var.postgres_config.user }
    TARIFIA_POSTGRES_PWD           = { value = var.postgres_config.password }
    TARIFIA_POSTGRES_READ_DATABASE = { value = var.api_service_config.postgres_read_database }
    TARIFIA_POSTGRES_READ_HOST     = { value = var.postgres_config.read_host }
    TARIFIA_POSTGRES_READ_PORT     = { value = var.postgres_config.read_port }
    TARIFIA_POSTGRES_READ_USER     = { value = var.postgres_config.read_user }
    TARIFIA_POSTGRES_READ_PWD      = { value = var.postgres_config.read_password }
  }
}

resource "render_env_group" "redis" {
  environment_id = var.render_environment_id
  name           = "redis-${var.environment}"
  env_vars = {
    TARIFIA_REDIS_HOST = { value = var.redis_config.host }
    TARIFIA_REDIS_PORT = { value = var.redis_config.port }
    TARIFIA_REDIS_DB   = { value = var.api_service_config.redis_db }
  }
}

# Services


resource "render_web_service" "api" {
  environment_id     = var.render_environment_id
  name               = "api${local.env_suffix}"
  plan               = var.api_service_config.plan
  region             = "ohio"
  health_check_path  = "/healthz"
  pre_deploy_command = "uv run task pre_deploy"

  # Deploy from the "latest" tag so newly created services come up on the most
  # recent main build. CI deploys specific digests out-of-band (deploy_server.sh),
  # so ignore_changes below keeps Terraform from reverting them.
  runtime_source = {
    image = {
      image_url              = split("@", var.api_service_config.image_url)[0]
      registry_credential_id = var.registry_credential_id
      tag                    = "latest"
    }
  }

  lifecycle {
    ignore_changes = [runtime_source.image]
  }

  autoscaling = var.environment == "production" ? {
    enabled = true
    min     = 2
    max     = 4
    criteria = {
      cpu = {
        enabled    = true
        percentage = 90
      }
      memory = {
        enabled    = true
        percentage = 90
      }
    }
    } : var.environment == "sandbox" ? {
    enabled = true
    min     = 2
    max     = 2
    criteria = {
      cpu = {
        enabled    = true
        percentage = 90
      }
      memory = {
        enabled    = true
        percentage = 90
      }
    }
  } : null

  custom_domains = var.api_service_config.custom_domains

  env_vars = {
    SERVICE_NAME             = { value = "api${local.env_suffix}" }
    WEB_CONCURRENCY          = { value = var.api_service_config.web_concurrency }
    FORWARDED_ALLOW_IPS      = { value = var.api_service_config.forwarded_allow_ips }
    TARIFIA_ALLOWED_HOSTS      = { value = var.api_service_config.allowed_hosts }
    TARIFIA_CORS_ORIGINS       = { value = var.api_service_config.cors_origins }
    TARIFIA_DATABASE_POOL_SIZE = { value = var.api_service_config.database_pool_size }
  }
}

resource "render_web_service" "worker" {
  for_each = var.workers

  environment_id    = var.render_environment_id
  name              = each.key
  plan              = each.value.plan
  region            = "ohio"
  health_check_path = "/"
  start_command     = each.value.start_command
  num_instances     = each.value.num_instances

  # Deploy from the "latest" tag so newly created services come up on the most
  # recent main build. CI deploys specific digests out-of-band (deploy_server.sh),
  # so ignore_changes below keeps Terraform from reverting them.
  runtime_source = {
    image = {
      image_url              = split("@", each.value.image_url)[0]
      registry_credential_id = var.registry_credential_id
      tag                    = "latest"
    }
  }

  lifecycle {
    ignore_changes = [runtime_source.image]
  }

  custom_domains = length(each.value.custom_domains) > 0 ? each.value.custom_domains : null

  env_vars = merge(
    {
      SERVICE_NAME             = { value = each.key }
      dramatiq_prom_port       = { value = each.value.dramatiq_prom_port }
      TARIFIA_DATABASE_POOL_SIZE = { value = each.value.database_pool_size }
    },
    (each.value.redis_host != null && each.value.redis_port != null && each.value.redis_db) ? {
      TARIFIA_REDIS_HOST = { value = each.value.redis_host }
      TARIFIA_REDIS_PORT = { value = each.value.redis_port }
      TARIFIA_REDIS_DB   = { value = each.value.redis_db }
    } : {}
  )
}

resource "render_cron_job" "cron" {
  for_each = var.cron_jobs

  environment_id = var.render_environment_id
  name           = each.key
  plan           = each.value.plan
  region         = "ohio"
  schedule       = each.value.schedule
  start_command  = each.value.start_command

  # Cron jobs use tag "latest" instead of a pinned digest so Render
  # automatically pulls the newest image before each run.
  runtime_source = {
    image = {
      image_url              = split("@", coalesce(each.value.image_url, var.api_service_config.image_url))[0]
      registry_credential_id = var.registry_credential_id
      tag                    = "latest"
    }
  }

  # Cron jobs don't support Render secret_files, so we pass JWKS as an env var
  # and write it to a temp file in the start command. TARIFIA_JWKS is set here
  # to override the env group value (/etc/secrets/jwks.json) which doesn't exist.
  env_vars = {
    SERVICE_NAME             = { value = each.key }
    TARIFIA_DATABASE_POOL_SIZE = { value = each.value.database_pool_size }
    TARIFIA_JWKS               = { value = "/tmp/jwks.json" }
    TARIFIA_JWKS_CONTENT       = { value = var.backend_secrets.jwks }
  }
}

locals {
  env_suffix      = var.environment == "production" ? "" : "-${var.environment}"
  worker_ids      = [for w in render_web_service.worker : w.id]
  cron_job_ids    = [for c in render_cron_job.cron : c.id]
  all_service_ids = concat([render_web_service.api.id], local.worker_ids, local.cron_job_ids)
}

# Env group links
resource "render_env_group_link" "database" {
  env_group_id = render_env_group.database.id
  service_ids  = local.all_service_ids
}

resource "render_env_group_link" "redis" {
  env_group_id = render_env_group.redis.id
  service_ids  = local.all_service_ids
}

resource "render_env_group_link" "aws_s3" {
  env_group_id = render_env_group.aws_s3.id
  service_ids  = local.all_service_ids
}

resource "render_env_group_link" "worker_sqs" {
  count        = var.worker_sqs_config != null ? 1 : 0
  env_group_id = render_env_group.worker_sqs[0].id
  service_ids  = local.all_service_ids
}

resource "render_env_group_link" "google" {
  env_group_id = render_env_group.google.id
  service_ids  = local.all_service_ids
}

resource "render_env_group_link" "github" {
  env_group_id = render_env_group.github.id
  service_ids  = local.all_service_ids
}

resource "render_env_group_link" "backend" {
  env_group_id = render_env_group.backend.id
  service_ids  = local.all_service_ids
}

resource "render_env_group_link" "backend_production" {
  count        = var.environment == "production" ? 1 : 0
  env_group_id = render_env_group.backend_production[0].id
  service_ids  = local.all_service_ids
}

resource "render_env_group_link" "stripe" {
  env_group_id = render_env_group.stripe.id
  service_ids  = local.all_service_ids
}

resource "render_env_group_link" "logfire" {
  count        = var.logfire_config != null ? 1 : 0
  env_group_id = render_env_group.logfire[0].id
  service_ids  = local.all_service_ids
}

resource "render_env_group_link" "openai" {
  env_group_id = render_env_group.openai.id
  service_ids  = local.all_service_ids
}

resource "render_env_group_link" "pydantic_ai_gateway" {
  env_group_id = render_env_group.pydantic_ai_gateway.id
  service_ids  = local.all_service_ids
}

resource "render_env_group_link" "apple" {
  env_group_id = render_env_group.apple.id
  service_ids  = [render_web_service.api.id]
}

resource "render_env_group_link" "prometheus" {
  count        = var.prometheus_config != null ? 1 : 0
  env_group_id = render_env_group.prometheus[0].id
  service_ids  = local.all_service_ids
}

resource "render_env_group_link" "slo_report" {
  count        = var.slo_report_config != null ? 1 : 0
  env_group_id = render_env_group.slo_report[0].id
  service_ids  = local.all_service_ids
}

resource "render_env_group_link" "tinybird" {
  count        = var.tinybird_config != null ? 1 : 0
  env_group_id = render_env_group.tinybird[0].id
  service_ids  = local.all_service_ids
}

resource "render_env_group_link" "tarifia_self" {
  count        = var.tarifia_self_config != null ? 1 : 0
  env_group_id = render_env_group.tarifia_self[0].id
  service_ids  = local.all_service_ids
}

resource "render_env_group_link" "memory_profile" {
  count        = var.memory_profile_config != null ? 1 : 0
  env_group_id = render_env_group.memory_profile[0].id
  service_ids  = concat([render_web_service.api.id], local.worker_ids)
}

resource "cloudflare_dns_record" "resend_dkim" {
  zone_id = var.resend_domain.zone_id
  name    = "resend._domainkey.${var.backend_config.email_from_domain}"
  type    = "TXT"
  content = var.resend_domain.dkim_public_key
  ttl     = 1
}

resource "cloudflare_dns_record" "resend_spf_mx" {
  zone_id  = var.resend_domain.zone_id
  name     = "send.${var.backend_config.email_from_domain}"
  type     = "MX"
  content  = "feedback-smtp.us-east-1.amazonses.com"
  priority = 10
  ttl      = 1
}

resource "cloudflare_dns_record" "resend_spf_txt" {
  zone_id = var.resend_domain.zone_id
  name    = "send.${var.backend_config.email_from_domain}"
  type    = "TXT"
  content = var.resend_domain.spf_policy
  ttl     = 1
}
