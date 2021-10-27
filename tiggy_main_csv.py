'''****************************************************************************
title           : tiggy_main_csv.py
author          : TheBigMort
modified_by     : tiggy
date_created    : 20211026
date_modified   : 202110
version         : 2.0
python_version  : 3.9
****************************************************************************'''

from tiggy_data_parse import parse_mutant_data
import requests
import time
import pandas as pd

csv_data_file = "tiggy_main.csv"

# Infinite loop to constantly run and update database
while True:

    # track time to check how long the program takes to run
    start_time = time.time()
    df = pd.DataFrame()
    url = "https://api.opensea.io/api/v1/assets"

    for i in range(0, 334):
        querystring = {"token_ids": list(range((i * 30), (i * 30) + 30)),
                       "asset_contract_address": "0x60E4d786628Fea6478F785A6d7e704777c86a7c6",
                       "order_direction": "desc",
                       "offset": "0",
                       "limit": "50"}
        response = requests.request("GET", url, params=querystring)

        print(i, end=" ")
        if response.status_code != 200:
            print('ERROR, RESPONSE CODE:')
            print(response.status_code)
            break

        # Get mutants data
        mutants = response.json()['assets']
        # Parse mutants data
        parsed_mutants = [parse_mutant_data(mutant) for mutant in mutants]
        # insert data into mutant_data
        df = df.append(parsed_mutants, ignore_index=True)

    # create csv file with mutants data
    df.to_csv(csv_data_file, header=True)

    # calculate and print total program run time
    end_time = time.time()
    time_elapsed = end_time - start_time
    print(time_elapsed)
    time.sleep(100)
