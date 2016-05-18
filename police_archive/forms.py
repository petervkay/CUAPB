from haystack.forms import SearchForm


class SearchForm(SearchForm):

    def no_query_found(self):
        return self.searchqueryset.all()