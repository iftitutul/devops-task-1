X-Company has a single AWS account which houses both their Production and Staging environment.
A developer with an IAM username of "Sven.Svenson" asks you to create an IAM policy for him that allows him the following permissions:

Full access to an S3 Bucket with the same name as the user (Sven.Svenson).
Access to read a Secret in Secrets Manager with the following ARN:

`"arn:aws:secretsmanager:us-east-1:000011112222:secret:SuperSecretDatabases/SecretDatabase01-l9sSe3"`

There must be a policy condition that Multifactor Authentication is required when accessing the SecretDatabase01 secret.

Access to create, read and update Secrets in Secrets Manager for the "App1" application.

They should ONLY be able to do this for the Staging environment, without allowing access to create or access secrets in the Production environment.

As they share a single AWS Account, you will need to come up with a naming convention that allows for this to be easily done via an IAM policy.
The idea being that it is easy to allow access to either the Production secrets or the Staging secrets via IAM policies.
The base secret name that will be stored in Secrets Manager for the "App1" application will be as follows: 
`App1-Secret-<##> (<##> being a random number between 0 and 100)`

You can find AWS IAM policy information at the following locations:

- [Policies and permissions in IAM - AWS Identity and Access Management (amazon.com)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)
- [Reference - Service Authorization Reference (amazon.com)](https://docs.aws.amazon.com/service-authorization/latest/reference/reference.html)

- For extra assistance, use the AWS Policy generator as a basis for your policy:

  [AWS Policy Generator | AWS News Blog (amazon.com)](https://aws.amazon.com/blogs/aws/aws-policy-generator/)