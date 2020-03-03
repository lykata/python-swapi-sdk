from os import mkdir
from os.path import exists
from typing import List, KeysView

import requests
from jsonschemacodegen import python as pygen
from requests import Response

SWAPI_BASE_URL = "https://swapi.co/api"


class CodeGenerator:
    def __init__(self, output_dir):
        if not exists(output_dir):
            mkdir(output_dir)
        self.generator = pygen.GeneratorFromSchema(output_dir)

    def gen(self, schema, filename: str, cls: str):
        self.generator.Generate(schema, cls.capitalize(), filename)


def gen_swapi():
    response: Response = requests.get(SWAPI_BASE_URL, verify=False)
    resources: dict = response.json()
    schema_names : KeysView = resources.keys()
    generator = CodeGenerator("swapi_gen")
    for schema_name in schema_names:
        url = f"{SWAPI_BASE_URL}/{schema_name}/schema"
        schema = requests.get(url, verify=False).json()
        schema_name = schema_name[:-1] if schema_name.endswith('s') else schema_name
        generator.gen(schema, schema_name, schema_name)


gen_swapi()
