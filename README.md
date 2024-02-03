# gds_hackathon

## Overview
This project aims to develop a real-time data warehousing solution that ingests, processes, and visualizes sales data from Walmart's Black Friday event. The solution provides insights into sales performance, customer behavior, and inventory levels to facilitate data-driven decision-making for inventory management, marketing strategies, and customer experience enhancement.

# Architecture
The architecture consists of the following components:

## Data Sources:

Stream 1: Sales Transactions Stream.

Stream 2: Inventory Updates Stream.

Preloaded Dimensional Data (Products and Stores)

## Data Ingestion:
Google Cloud Pub/Sub for real-time data streaming.
Google Cloud Dataflow for processing and loading data into BigQuery.

## Data Warehouse:
Google BigQuery for storing and querying real-time data.

## Visualization and Dashboards:
Google Data Studio for creating interactive dashboards.

# Installation
Follow the steps below to set up and run the project:

## 1. Prerequisites
Google Cloud Platform account with necessary permissions.
Python and pip installed on your local machine.

## 2. Data Generation
Use the provided Python scripts (sales_data_generator.py and inventory_data_generator.py) to generate mock data for the sales transactions stream and inventory updates stream. Adjust the scripts as needed for your data volume.

## 3. Data Ingestion
Create Pub/Sub topics for sales transactions and inventory updates.
Set up a BigQuery dataset and tables for sales transactions, inventory updates, products, and stores.
Update the Dataflow pipeline script (dataflow_pipeline.py) with your project and dataset details.
Deploy and run the Dataflow pipeline to ingest and process real-time data.

## 4. Visualization and Dashboards
Create a Google Data Studio account.
Connect Data Studio to your BigQuery dataset.
Design dashboards with relevant visualizations based on the identified key metrics.

## 5. GitHub Repository
Check in the complete code into your GitHub repository.
Include a README file with detailed instructions.
Add an architecture diagram to illustrate the project structure.

# Usage
Execute the data generation scripts to simulate real-time data.
Run the Dataflow pipeline to ingest and process data in real-time.
Access Google Data Studio to explore dashboards and gain insights.

# Additional Notes
Ensure proper security measures for credentials and sensitive information.
Monitor the pipeline using Cloud Monitoring and set up alerts if needed.
