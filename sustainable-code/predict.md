# Predict carbon footprint of a person using MindsDB

With MindsDB, you can build, train, optimize, and deploy your ML models without the need for other platforms. And to get
the forecasts, simply query your data and ML models. Read along to see some examples.

MindsDB brings machine learning into databases by employing the concept of AI Tables.

AI Tables are machine learning models stored as virtual tables inside a database. They facilitate making predictions
based on your data. You can perform the time series, regression, and classification predictions within your database and
get the output almost instantly by querying an AI Table with simple SQL statements.

## Prerequisites

Before you begin, make sure you have the following:

- [MindsDB](https://docs.mindsdb.com/Installation/) installed.
- [MySQL](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/) installed.
- [Python](https://www.python.org/downloads/) installed. (for the carbon footprint calculator to work first)

## Step 1: Create a database

Create a database in MySQL. You can do this by running the following command:

```sql
CREATE DATABASE db;
```

## Step 2: Create a table

Create a table in MySQL. You can do this by running the following command:

```sql
CREATE TABLE carbon_footprint
(
    id              INT          NOT NULL AUTO_INCREMENT,
    name            VARCHAR(255) NOT NULL,
    age             INT          NOT NULL,
    income          INT          NOT NULL,
    total_footprint FLOAT        NOT NULL
);
```

## Step 3: Calculate carbon footprint

Calculate carbon footprint for each person and store it in a file. You can do this by running the following command:

```shell
python carbon_footprint_calculator.py >> emmissions.txt
```

## Step 4: Insert data into the table

Insert data into the table. You can do this by running the following command for example:

```sql
INSERT INTO carbon_footprint (name, age, income, total_footprint)
VALUES ('John', 25, 10000, 10000),
       ('Mary', 30, 20000, 20000),
       ('Peter', 35, 30000, 30000)
```

## Step 5: Install MindsDB

Install MindsDB. You can do this by running the following command:

```shell
pip install mindsdb
```

## Step 6: Start MindsDB

Start MindsDB. You can do this by running the following command:

```shell
python -m mindsdb
```

## Step 7: Create mysql datasource in mindsdb

Create mysql datasource in mindsdb. You can do this by running the following command:

```sql
CREATE
DATABASE db
FROM ENGINE='mysql',
PARAMETERS= {
    ...
};
```

## Step 8: Train a model

Train a model. You can do this by running the following command:

```sql
CREATE
MODEL mindsdb.carbon_footprint_model
FROM db.carbon_footprint
PREDICT total_footprint;
```

## Step 9: Make a prediction

Make a prediction. You can do this by running the following command:

```sql
SELECT age, income
FROM mindsdb.carbon_footprint_model
WHERE total_footprint = 90000;
```


