# Employee Data ETL Pipeline

## Project Overview
This project demonstrates an ETL (Extract, Transform, Load)
pipeline built using Python, Pandas, and SQLite.

The pipeline extracts employee data from a CSV file,
cleans and transforms the data, and loads it into
a SQLite database for analysis.

## Technologies Used
- Python
- Pandas
- SQLite
- SQL
- Git and GitHub

## ETL Workflow

CSV File
   |
   v
Extract Data (extract.py)
   |
   v
Transform Data (transform.py)
   |
   v
Load Data (load.py)
   |
   v
SQLite Database

## Features
- Extract employee records from CSV
- Remove duplicate records
- Handle missing salary values
- Calculate annual salaries
- Store cleaned data in SQLite
- Analyze employee data using SQL

## Project Structure

employee-etl-project/
    data/
        employee.csv
    extract.py
    transform.py
    load.py
    main.py
    query.py
    README.md

## How to Run

1. Install Pandas:

   pip install pandas

2. Run the ETL pipeline:

   python main.py

3. Query the database:

   python query.py

## Sample SQL Query

SELECT department, SUM(annual_salary) AS total_salary
FROM employees
GROUP BY department;

## Future Improvements
- Add error handling
- Add logging
- Add automated tests
- Integrate REST APIs
- Schedule the ETL pipeline