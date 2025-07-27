#resource "aws_security_group" "open_sg" {
#  name        = "open-sg"
#  description = "Open to the world"
#  vpc_id      = "vpc-12345678"

#  ingress {
#    from_port   = 22
#    to_port     = 22
#    protocol    = "tcp"
#    cidr_blocks = ["0.0.0.0/0"]
#  }

#  egress {
#    from_port   = 0
#    to_port     = 0
#    protocol    = "-1"
#    cidr_blocks = ["0.0.0.0/0"]
#  }
#}
