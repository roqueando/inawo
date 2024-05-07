from polars import DataFrame, read_csv

def extract(path: str) -> DataFrame:
    """read the csv with given path"""
    return read_csv(path)
