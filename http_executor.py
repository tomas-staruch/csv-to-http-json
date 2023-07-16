import concurrent.futures
import json
import requests
import traceback

from abc import ABC, abstractmethod
from typing import Optional


class JsonBuilder(ABC):
    """
    Abstract base class which declare method for building of JSON from given input.
    """
    @abstractmethod
    def build(self):
        pass


class GoogleFormJsonBuilder(JsonBuilder):
    """
    Creates a JSON object where values are array.
    """
    def build(self, values):
        return self.to_json({'source': 'google-form-importer', 'values': values})

    @staticmethod
    def to_json(data):
        return json.dumps(data, ensure_ascii=False).encode('utf8')


class HttpExecutor:
    """
    HttpExecutor takes raw data, convert them to JSONs and POST them.
    """
    def __init__(self, json_builder: JsonBuilder, url: str):
        self.json_builder = json_builder
        self.url = url
        self.headers = {}

    def add_json_content_header(self):
        self.headers.update({"Content-Type": "application/json; charset=utf-8"})

        return self

    def add_api_key_header(self, api_key: str):
        self.headers.update({"x-api-key": api_key})

        return self

    def post(self, records: []) -> Optional[str]:
        collected_responses = {'successful': [], 'failed': []}

        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []

            for record in records:
                futures.append(executor.submit(self.__post, record, collected_responses))

        return collected_responses

    def __post(self, record, collected_responses):
        from requests import HTTPError

        try:
            response = requests.post(self.url, data=self.json_builder.build(record), headers=self.headers)

            collected_response = {'status_code': response.status_code, 'response': self.__response_content(response)}

            if response.ok:
                collected_responses['successful'].append(collected_response)
            else:
                collected_responses['failed'].append(collected_response)
        except HTTPError as http_err:
            print(f'HTTPError occurred: {http_err}')
            traceback.print_tb(http_err.__traceback__)
        except Exception as err:
            print(f'An error occurred: {err}')
            traceback.print_tb(err.__traceback__)

    @staticmethod
    def __response_content(response):
        if response.headers.get('content-type') == 'application/json':
            return response.json()
        else:
            return response.text
