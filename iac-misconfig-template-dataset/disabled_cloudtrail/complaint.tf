resource "aws_s3_bucket" "trail_logs" {
  bucket = "secure-cloudtrail-logs"
}

resource "aws_cloudtrail" "enabled_trail" {
  name                          = "secure-trail"
  s3_bucket_name                = aws_s3_bucket.trail_logs.bucket
  include_global_service_events = true
  is_multi_region_trail         = true
  enable_logging                = true
}
