resource "aws_api_gateway_rest_api" "secure_api" {
  name        = "SecureAPI"
  description = "API Gateway with authorization enabled"
}

resource "aws_api_gateway_authorizer" "cognito_auth" {
  name                    = "CognitoAuthorizer"
  rest_api_id             = aws_api_gateway_rest_api.secure_api.id
  identity_source         = "method.request.header.Authorization"
  type                    = "COGNITO_USER_POOLS"
  provider_arns           = ["arn:aws:cognito-idp:us-east-1:123456789012:userpool/us-east-1_Example"]
}

resource "aws_api_gateway_deployment" "secure_deploy" {
  rest_api_id = aws_api_gateway_rest_api.secure_api.id
  stage_name  = "prod"
}
