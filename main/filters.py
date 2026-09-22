from rest_framework import filters



class BaseFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        params = request.query_params
        
        