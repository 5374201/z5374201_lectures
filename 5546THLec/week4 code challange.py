import os
from toolkit_config import toolkit_config as cfg
import yf_example2


def qan_prc_to_csv(year):
    start_date = f"{year}-01-01"
    end_date = f"{year}-12-31"
    tic = 'QAN.AX'

    # Download the data for the specified period and ticker
    data = yf_example2.yf_prc_to_csv(tic, start_date, end_date)

    # Create the name of the output file
    output_filename = f"qan_prc_{year}.csv"

    # Create the path for the output file inside the data folder
    output_path = os.path.join(cfg.data_folder, output_filename)

    # Save the downloaded data to the output file
    data.to_csv(output_path, index=False)


if __name__ == "__main__":
    # Test the function by downloading data for the year 2020
    qan_prc_to_csv(year=2020)
