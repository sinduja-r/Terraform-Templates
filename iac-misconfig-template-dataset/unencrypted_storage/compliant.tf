resource "aws_ebs_volume" "encrypted_volume" {
  availability_zone = "us-east-1a"
  size              = 8
  encrypted         = true
}
