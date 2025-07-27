#resource "aws_api_gateway_rest_api" "insecure_api" {
#  name        = "InsecureAPI"
#  description = "Public REST API without authentication"
#  tags = {
#    endpoint_url = "http://insecure.example.com/api"
#  }
#}


#resource "aws_api_gateway_deployment" "deploy" {
#  rest_api_id = aws_api_gateway_rest_api.insecure_api.id
#  stage_name  = "prod"
#}
