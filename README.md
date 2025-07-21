# Terraform-Templates

# 🛠️ IaC Misconfiguration Dataset for Static Analysis

This repository contains intentionally misconfigured **Terraform** files to test and validate rule-based and static analysis tools (e.g., Checkov, custom scanners, Cloudsplaining) for identifying security issues before deployment.

## 🧪 Misconfiguration Types Covered

| Misconfiguration Type        | Description                                                    |
|-----------------------------|-----------------------------------------------------------------|
| Public S3 Buckets           | Buckets with `public-read` or `public-read-write` ACL           |
| Over-Permissive IAM         | IAM policies with `Action = "*"`, `Resource = "*"`              |
| Open Network Ports          | Security groups allowing ingress from `0.0.0.0/0`               |
| Unencrypted Storage         | EBS volumes created without encryption                          |
| Unsecured API Endpoints     | API Gateway setup without authentication or authorization       |
| Disabled CloudTrail Logging | CloudTrail logging disabled or missing entirely                 |


## 📂 Repository Structure
iac-misconfig-dataset/
├── versions.tf # Shared Terraform version/provider config
├── public_s3/ # Publicly accessible S3 bucket
│ └── main.tf
├── over_permissive_iam/ # Wildcard IAM policies
│ └── main.tf
├── open_security_group/ # 0.0.0.0/0 ingress rules
│ └── main.tf
├── unencrypted_storage/ # Unencrypted EBS volumes
│ └── main.tf
├── unsecured_endpoint/ # API Gateway without authentication
│ └── main.tf
├── disabled_cloudtrail/ # CloudTrail logging disabled
│ └── main.tf

