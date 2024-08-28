from rest_framework import filters
import json

class JSONFilterBackend(filters.BaseFilterBackend):
    MAX_FILTER_JSON_PARAMS_LENGTH = 1000 
    MAX_ORDENATION_LENGTH = 1000

    def filter_queryset(self, request, queryset, view):
        filter = request.query_params.get('filter')
        order = request.query_params.get('order')

        if filter and len(filter) <= self.MAX_FILTER_JSON_PARAMS_LENGTH:
            filter = "{" + filter + "}"
            try:
                filters_dict = json.loads(filter)
            except json.JSONDecodeError:
                return queryset
            
            for field, value in filters_dict.items():
                filter_kwarg = {field: value}
                queryset = queryset.filter(**filter_kwarg)
        
        if order and len(order) <= self.MAX_ORDENATION_LENGTH:
            queryset = queryset.order_by(order)

        return queryset