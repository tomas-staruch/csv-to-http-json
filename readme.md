# google-form-csv-to-http-json
A cmd Python script to POST JSON data with API Key to an endpoint over HTTP. 

The script reads a CSV file (Google Form Sheet). From every line is created a JSON (see `GoogleFormJsonBuilder` in http_executor.py) which is send by POST method to an endpoint. 


### Testing 
The script is pre-configured to use [RequestBin.com](https://public.requestbin.com/) for testing of POST requests.
`testing_data.csv` contains dummy data which in result are formatted to JSON. 

An example:
`{"source": "google-form-importer", "values": ["2/19/2023 21:45:01", "test@dummy.domain.com", "Joel Dann", "Well Street 8"]}`

