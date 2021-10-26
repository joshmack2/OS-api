'''****************************************************************************
title           : JM_main_local.py
author          : TheBigMort
modified_by     : josh mack
date_created    : 20211026
date_modified   : 202110
version         : 2.0
python_version  : 3.9
****************************************************************************'''

from data_parseC import parse_mutant_data
import requests
import time
import pandas as pd

csv_data_file = "mutant_data.csv"

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

        # Get kongs data
        mutants = response.json()['assets']
        # Parse kongs data
        parsed_mutants = [parse_mutant_data(mutant) for mutant in mutants]
        # insert data into kong_data
        df = df.append(parsed_mutants, ignore_index=True)

    # create csv file with kongs data
    df.to_csv(csv_data_file, header=True)

    # calculate and print total program run time
    end_time = time.time()
    time_elapsed = end_time - start_time
    print(time_elapsed)
    time.sleep(100)