import pandas as pd

def generate_summary(df):
    """
    Generates department-wise sales summary.
    """

    summary = (
        df.groupby("Department")["Sales"]
        .sum()
        .reset_index()
    )

    return summary


def save_report(final_df, summary_df):
    """
    Saves consolidated report and summary
    into a single Excel workbook.
    """

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_path= os.path.join(BASE_DIR,'output',"consolidated_report.xlsx")
                              
    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:

        final_df.to_excel(
            writer,
            sheet_name="Consolidated Data",
            index=False
        )

        summary_df.to_excel(
            writer,
            sheet_name="Summary",
            index=False
        )

    print(f"Report saved to {output_path}")
