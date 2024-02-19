# DuckDB examples

This repo contains
- a tutorial showing basic usage of DuckDB via the Python API inside a notebook,
- and an example scenario showcasing one way of how you could use DuckDB to combine and aggregate data from JSON and Parquet files and write the results directly to Postgres.

You can run this with zero setup in GitHub codespaces; all the needed setup is done in the dev container config.

To run the tutorial and the example scenario locally you will need a Python environment with the packages in `requirements.txt`. You will also need a running Postgres database. You should be able to use a MySQL or SQLite database instead of Postgres as well by only changing the ATTACH commands.

You also need to run the script `generate_example_data.py` to generate the data used in the tutorial and example scenario.

Commands to get started:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python generate_example_data.py
```
