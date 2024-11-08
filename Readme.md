# ETL Pipeline with Docker Compose

## Overview

This ETL pipeline extracts data from a CSV, transforms it according to specified business rules, and loads it into a PostgreSQL database. The pipeline is deployed using Docker Compose.

## Prerequisites

- Docker and Docker Compose
- Python 3.8+

## Setup and Execution

1. Clone the repository.
2. Place the `employee_details.csv` file in the root directory.
3. Run the following command to build and start the containers:
   ```bash
   docker-compose up --build
4. docker-compose.yml sets up PostgreSQL on port 5432.
5. The transformed data is loaded into a PostgreSQL table named employees.

## Runing this project 

1.Build and run the containers with Docker Compose:

  bash
  docker-compose up --build

2.Run Tests by executing the test suite within the container:

  bash
  docker-compose run etl python -m unittest discover -s tests

