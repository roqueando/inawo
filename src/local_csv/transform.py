from typing import Dict
from polars import DataFrame, Series
import polars as pl

class DateGroup:
    def __init__(self, dataframe: DataFrame):
        self.dates = dataframe['total']['date']

        self.data = {
            'total': {self.dates[i]: self.get_framedata(
                col='total', group='date', index=i, dataframe=dataframe
            ) for i in range(len(self.dates))},
            'mean': {self.dates[i]: self.get_framedata(
                col='mean', group='date', index=i, dataframe=dataframe
            ) for i in range(len(self.dates))},
        }

    def get_framedata(self, dataframe: DataFrame, col: str, group: str, index: int) -> Series:
        date = self.dates[index]
        return dataframe[col].filter(pl.col(group) == date)

class CategoryGroup:
    def __init__(self, dataframe: DataFrame):
        self.translated = {
            'WORK': 'Trabalho',
            'HOME': 'Casa',
            'INVEST': 'Investimento/Apartamento',
            'CREDIT': 'Crédito',
        }

        self.categories = ["WORK", "HOME", "INVEST", "CREDIT"]
        self.data = {
            'total': {self.categories[i]: self.get_framedata(
                group='category', col='total', index=i, frame=dataframe) for i in range(len(self.categories))},
            'mean': {self.categories[i]: self.get_framedata(
                group='category', col='mean', index=i, frame=dataframe) for i in range(len(self.categories))}
        }

    def get_framedata(self, group: str, col: str, index: int, frame: DataFrame) -> Series:
        category = self.categories[index]
        return frame[col].filter(pl.col(group) == category)

    def translate(self, category) -> str:
        return self.translated[category]

class GroupData:
    def __init__(self, category: CategoryGroup, date: DateGroup) -> None:
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
            'total': dataframe.group_by('category')
                            .agg(pl.col('amount').sum()),
            'mean': dataframe.group_by('category').agg(pl.col('amount').mean())
    }

    date_group = {
            'total': dataframe.group_by('date').agg(pl.col('amount').sum()),
            'mean': dataframe.group_by('date').agg(pl.col('amount').mean())
    }

    return GroupData(
                     category=CategoryGroup(category_group),
                     date=DateGroup(date_group))

