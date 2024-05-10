import os
from local_csv.extract import extract
from local_csv.transform import transform
from polars import Series, DataFrame


def format_currency(value: Series) -> str:
    formatted_value = value['amount'][0] / 100
    return f'R$ {formatted_value}'

def print_by_date(dataframe: DataFrame):
    column = 'date'
    print("Total gasto por data:")
    print("="*40)

    for key, value in getattr(dataframe, column).data['total'].items():
        currency = format_currency(value)
        print(f"{key}: {currency}")

    print()
    print("Média gasta por data:")
    print("="*40)
    for key, value in getattr(dataframe, column).data['mean'].items():
        currency = format_currency(value)
        print(f"{key}: {currency}")

def print_by_category(dataframe: DataFrame):
    column = 'category'
    print("Total gasto por categoria:")
    print("="*40)

    for key, value in getattr(dataframe, column).data['total'].items():
        translated = getattr(dataframe, column).translate(key)
        currency = format_currency(value)
        print(f"{translated}: {currency}")

    print()
    print("Média gasta por categoria:")
    print("="*40)
    for key, value in getattr(dataframe, column).data['mean'].items():
        translated = getattr(dataframe, column).translate(key)
        currency = format_currency(value)
        print(f"{translated}: {currency}")

def main():
    dirname = os.path.dirname(__file__)
    path = os.path.join(dirname, '../fixtures/inawo.csv')

    dataframe = extract(path)
    transformed = transform(dataframe)

    print_by_category(transformed)
    print("="*40)
    print()
    print_by_date(transformed)

main()
