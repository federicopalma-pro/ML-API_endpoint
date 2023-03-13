# ML-API_endpoint

## Introduction

This repository offers a comprehensive guide for developing a FastAPI-based endpoint to facilitate querying a machine-learning prediction model. While this solution may not be suitable for deployment in production environments due to the absence of a secure HTTPS protocol, a token has been implemented to ensure adequate protection for pre-production usage. The codebase has been thoughtfully structured into Docker containers, facilitating seamless deployment across various testing and cloud environments.
By leveraging the resources available through this repository, users can seamlessly streamline their machine-learning workflows and enhance the efficiency of their querying systems. The solution presents a powerful and robust FastAPI endpoint, allowing users to efficiently and effectively query their machine-learning models.

## Model

The creation of the diamond prediction model can be found in this repository: https://github.com/federicopalma-pro/ML-Regression. The model was trained using various regression techniques, and the performance was evaluated using metrics such as mean absolute error and R-squared. The best-performing model was chosen and used to create the endpoint included in this repository.

The diamond prediction model is an essential component of the endpoint created in this repository. The model is loaded into memory when the Docker container is started and can be queried using a POST request to the /predict endpoint. The endpoint expects a JSON payload containing the characteristics of the diamond, and it returns a JSON response containing the expected price.
