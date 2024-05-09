import os
from local_csv.extract import extract
from local_csv.transform import transform


def main():
    dirname = os.path.dirname(__file__)
    path = os.path.join(dirname, '../fixtures/inawo.csv')

    dataframe = extract(path)
    transformed = transform(dataframe)

    categories_total = transformed.category['total']
    category_list = categories_total['category'].to_list()
    amount_list = categories_total['amount'].to_list()

    categories_mean = transformed.category['mean']
    category_mean_list = categories_mean['category'].to_list()
    amount_mean_list = categories_mean['amount'].to_list()

    print("Total gasto por categoria: \n")
    for i in range(0, len(category_list)):
        category = category_list[i]
        amount = amount_list[i] / 100
        print(f'{category}: R$ {amount}')

    print("\n")
    print("Média gasta por categoria: \n")
    for i in range(0, len(category_mean_list)):
        category = category_mean_list[i]
        amount = amount_mean_list[i] / 100
        print(f'{category}: R$ {amount}')

main()
