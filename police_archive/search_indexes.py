import datetime

from .models import Officer


class OfficerIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    first_name=indexes.CharField(model_attr='first_name')
    last_name=indexes.CharField(model_attr='last_name')
    badge=indexes.IntegerField(model_attr='badge')
    department=indexes.CharField(model_attr='department')

    def get_model(self):
        return Officer

   