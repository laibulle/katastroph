import importlib
import os


def load_kata(module_name: str):
    package = os.getenv("KATA_PACKAGE", "katastrof.solutions")
    return importlib.import_module(f"{package}.{module_name}")

