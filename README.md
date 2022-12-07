
# AWS - SAM APP ONE REPO BOILERPLATE

Configure a single AWS API Gateway with multiple AWS Lambda Functions in one Repository.

- Run SAM in local machine
- Deploy API Gateway and Lambda Function




## Installation

Prerequisites - Needed to be installed on local machine:

  - Install AWS CLI
  - Configure AWS CLI
  - Install SAM CLI
  - Install Docker
  - Python 3.9
## AWS Configuration

- Add IAM User in order to get the `AWS Access Key ID` and `AWS Secret Access Key`.
    - AWS Console > IAM > Users > Add User
    - Select AWS Credential Type: "Access key - Programmatic access"
    - Set of Permissions:
        - IAMFullAccess
        - AmazonS3FullAccess
        - AWSCloudFormationFullAccess
        - AmazonAPIGatewayAdministrator
        - CloudWatchFullAccess
        - AmazonDynamoDBFullAccess
        - AWSLambda_FullAccess

- If you already have your Security Credentials and AWS CLI Installed, type this aws command on your terminal:

  ```bash
  aws configure
  ```
  Then, enter your `AWS Access Key ID` and `AWS Secret Access Key`





## Run Locally

Clone the project

```bash
  git clone https://gitlab.com/aws-sandbox3/sam-app-one-repo.git
```

Go to the project directory

```bash
  cd sam-app-one-repo
```

Run Virtual Environment (For python 3.x version)

```bash
  python -m venv myenv
  source myenv/bin/activate
```

Install dependencies
- Make sure you are inside your lambda function folder to reference requirements.txt file

```bash
  pip install -r requirements.txt
```

If you want to deactivate your Virtual Environment:

```bash
  deactivate
```

## 2 Options to Run your Functions Locally:

- Invoke function locally:

    ```bash
    sam local invoke -e ./events/event.json HelloWorldFunction
    ```
    ** "HelloWorldFunction" is your function name defined in template.yml

- Start the local api server:

    ```bash
    sam local start-api
    ```
    ** SAM will automatically look for ".yml" configuration file.


## Deployment

Build and Deploy Project

```bash
  sam build
  sam deploy --guided
```

- Go to AWS CloudFormation and look for the deployment "stack" that SAM automatically deployed it for you.

When using the ff. SAM CLI commands:
- `sam build` command - SAM will build your project and install dependencies based on requirements.txt.
- `sam deploy --guided` - SAM will deploy the API Gateway and Lambda functions, as well as any dependencies.


## Reference:


- [AWS SAM Tutorial (with a Lambda Example!)](https://www.youtube.com/watch?v=MipjLaTp5nA)
- [How To Test your AWS Lambda Locally with SAM](https://www.youtube.com/watch?v=AUQRyl1SNcU&t=39s)
- [SAM template: Configure an api gateway with multiple lambdas](https://manuchandrasekhar.medium.com/sam-template-configure-an-api-gateway-with-multiple-lambdas-921b38873389)
- [sam-app boilerplate](https://github.com/beabetterdevv/sam-app)

