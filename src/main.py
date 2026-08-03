import os
import logging
import pandas as pd

from cleaner import clean_data
from validator import validate_dataframe
from consolidate import consolidate_reports
from report import generate_summary, save_report

# Project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INPUT_FOLDER = os.path.join(BASE_DIR, "input")
OUTPUT_FOLDER = os.path.join(BASE_DIR, "output")
LOG_FOLDER = os.path.join(BASE_DIR, "logs")

os.makedirs(LOG_FOLDER, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(LOG_FOLDER, "automation.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():

    logging.info("Automation Started")

    dataframes = []

    for file in os.listdir(INPUT_FOLDER):

        if file.endswith(".xlsx"):

            path = os.path.join(INPUT_FOLDER, file)

            print(f"Reading {file}")

            df = pd.read_excel(path)

            validate_dataframe(df)

            df = clean_data(df)

            dataframes.append(df)

    final_df = consolidate_reports(dataframes)

    summary = generate_summary(final_df)

    save_report(final_df, summary)

    logging.info("Automation Completed Successfully")


if __name__ == "__main__":
    main()
