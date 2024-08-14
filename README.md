# Text-Summarization-with-AWS-Amazon-Bedrock---Cohere-FM-AWS-Lambda-API-Gateway

![image](https://github.com/user-attachments/assets/12159c75-1cef-422e-a8f9-6cff8ed7dcce)


This project demonstrates how to create a REST API that integrates AWS Bedrock, AWS Lambda, and AWS API Gateway to invoke a large language model (LLM) for summarization tasks. The API receives a prompt, processes it using AWS Lambda, and generates a summarized response using a foundational model from Cohere via AWS Bedrock.

## Project Overview

The flow of the application is as follows:

1. **REST API Request**: A client sends a REST API request containing a prompt to the AWS API Gateway.
2. **Lambda Invocation**: The API Gateway triggers an AWS Lambda function, passing the prompt as an event.
3. **Model Invocation**: The Lambda function invokes an LLM hosted by Cohere through AWS Bedrock, sending the prompt for processing.
4. **Summarized Response**: The LLM generates a summarized response, which is returned to the Lambda function.
5. **API Response**: Finally, the Lambda function sends the summarized response back through the API Gateway to the client.

## Architecture

- **API Gateway**: Exposes a REST API to receive prompts from the client.
- **AWS Lambda**: Acts as the backend for the API, handling the invocation of the LLM.
- **AWS Bedrock**: Hosts the foundational model (LLM) from Cohere used for generating summaries.


## Key Concepts

- **AWS Bedrock**: A fully managed service that allows you to build and scale generative AI applications using foundational models from third parties like Cohere.
- **Cohere Model**: A foundational LLM that can process text input to generate summarized or other forms of transformed text.

