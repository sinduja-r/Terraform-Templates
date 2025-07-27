# Simulates a deployment where CloudTrail is not configured at all
# You can create an empty file or leave CloudTrail intentionally absent in this test case
# OR simulate a misconfigured trail:

#resource "aws_cloudtrail" "disabled_trail" {
#  name                          = "disabled-trail"
#  s3_bucket_name                = "some-log-bucket"
#  include_global_service_events = false
#  is_multi_region_trail         = false
#  enable_logging                = false
#}

