# google-form-csv-to-http-json
A Python script to POST JSON data with API Key to an endpoint over HTTP. 

The script reads a CSV file (e.g. Google Form Sheet). From every line it creates a JSON (see `GoogleFormJsonBuilder` in [http_executor.py](http_executor.py)) object. 
Every individual JSON object is sent by POST to a server endpoint (see [config.yaml](config.yaml)).


### Testing 
The script is pre-configured (see [config.yaml](config.yaml) to use [RequestBin.com](https://public.requestbin.com/) to inspect HTTP requests.

An example of JSON object generated from [testing_data.csv](testing_data.csv)) file:
`{"source": "google-form-importer", "values": ["2/19/2023 21:45:01", "test@dummy.domain.com", "Joel Dann", "Well Street 8"]}`


### Console output
An example of output:
```
Enter csv file to import:testing_data.csv
---------------------------------------
successful  :  [{'status_code': 200, 'response': '{"success":true}'}, {'status_code': 200, 'response': '{"success":true}'}]
failed  :  []
Count of records: 2
Count of successfully completed requests: 2
Count of unsuccessful requests: 0
Total time elapsed: 0.70 seconds
```


