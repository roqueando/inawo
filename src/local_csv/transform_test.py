from .extract import extract
from .transform import transform, CategoryGroup
import os

def test_transform():
    dirname = os.path.dirname(__file__)
    path = os.path.join(dirname, '../../fixtures/inawo.csv')

    data = extract(path)
    transformed = transform(data)
    assert len(transformed.category.data['total']) == 4
    assert len(transformed.date.data['total']) == 2
