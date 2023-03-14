# ML-API_endpoint

## Introduction

This repository offers a comprehensive guide for developing a FastAPI-based endpoint to facilitate querying a machine-learning prediction model. While this solution may not be suitable for deployment in production environments due to the absence of a secure HTTPS protocol, a token has been implemented to ensure adequate protection for pre-production usage. The codebase has been thoughtfully structured into Docker containers, facilitating seamless deployment across various testing and cloud environments.
By leveraging the resources available through this repository, users can seamlessly streamline their machine-learning workflows and enhance the efficiency of their querying systems. The solution presents a powerful and robust FastAPI endpoint, allowing users to efficiently and effectively query their machine-learning models.

## Model

The creation of the diamond prediction model can be found in this repository: https://github.com/federicopalma-pro/ML-Regression. The model was trained using various regression techniques, and the performance was evaluated using metrics such as mean absolute error and R-squared. The best-performing model was chosen and used to create the endpoint included in this repository.

The diamond prediction model is an essential component of the endpoint created in this repository. The model is loaded into memory when the Docker container is started and can be queried using a POST request to the /predict endpoint. The endpoint expects a JSON payload containing the characteristics of the diamond, and it returns a JSON response containing the expected price.

## Deploy
### - generate token

To provide sufficient protection , a token has been implemented in the FastAPI-based endpoint. This token can be generated using the [token_generator.py](https://github.com/federicopalma-pro/ML-API_endpoint/blob/main/token_generator.py) script, which provides a secure way to create random tokens and their corresponding SHA256 encoded values. Once developed, the SHA256 encoded token value can be added to the Dockerfile as an environment variable using the ENV command, while the token itself can be used for making POST requests to the endpoint.


​```Token: a161357752f286ff2439cddc9f0e5a985ce3d853d312859550a8f508606bca6f​```

​```Token encoded sha256: edec7e481b0322c89e99b6632a6f51a3c492b571a3e1ddcfad9000dbf6b2abe9​```
