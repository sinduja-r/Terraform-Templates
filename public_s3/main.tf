resource "aws_s3_bucket" "bad_bucket" {
  bucket = "insecure-public-bucket"
  acl    = "public-read"
}
