from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from webapp.schema import schema

urlpatterns = [
    # Only a single URL to access GraphQL
    path("api", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]
