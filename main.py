#!/usr/bin/env python3
from csv_file_reader import CsvFileReader
from http_executor import HttpExecutor, GoogleFormJsonBuilder

import os
import time


def main():
    api_key = os.environ.get('API_KEY')
    if not api_key:
        print("API_KEY environment variable not found.")
        return

    csv_reader = CsvFileReader()

    while True:
        filename = input("Enter csv file to import:")
        try:
            records = csv_reader.read_file(filename)
            break
        except OSError as e:
            print(e)

    # for record in records:
    #     print(record)

    tm1 = time.perf_counter()

    collected_responses = HttpExecutor(json_builder=GoogleFormJsonBuilder(), url='https://en05wt4mqo56yq.x.pipedream.net/') \
        .add_json_content_header() \
        .add_api_key_header(api_key) \
        .post(records)

    tm2 = time.perf_counter()

    print("---------------------------------------")
    for key in collected_responses:
        print(key, ' : ', collected_responses[key])

    print(f'Count of records: {len(records)}')
    print(f'Count of successfully completed requests: {len(collected_responses["successful"])}')
    print(f'Count of unsuccessful requests: {len(collected_responses["failed"])}')
    print(f'Total time elapsed: {tm2-tm1:0.2f} seconds')


if __name__ == '__main__':
    main()
