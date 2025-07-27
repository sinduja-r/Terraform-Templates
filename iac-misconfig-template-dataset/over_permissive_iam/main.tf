#resource "aws_iam_policy" "bad_policy" {
#  name        = "OverPermissivePolicy"
#  description = "Bad IAM policy with wildcard actions"
#  policy      = jsonencode({
#    Version = "2012-10-17",
#    Statement = [
#      {
#        Action   = "*"
#        Effect   = "Allow"
#        Resource = "*"
#      }
#    ]
#  })
#}
