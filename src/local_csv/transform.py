from typing import Dict
from polars import DataFrame
import polars as pl

class GroupData:
    def __init__(self, category: Dict[str, DataFrame], date: Dict[str, DataFrame]) -> None:
        self.category = category 
        self.date = date 

def transform(dataframe: DataFrame) -> GroupData:
    """
    Transform the given DataFrame into a new Dataframe
    composed by:
        groups followed by total and mean amount:
            - category
            - date 

    """
    category_group = {
            'total': dataframe.group_by('category').agg(pl.col('amount').sum()),
            'mean': dataframe.group_by('category').agg(pl.col('amount').mean())
    }

    date_group = {
            'total': dataframe.group_by('date').agg(pl.col('amount').sum()),
            'mean': dataframe.group_by('date').agg(pl.col('amount').mean())
    }

    return GroupData(category_group, date_group)

