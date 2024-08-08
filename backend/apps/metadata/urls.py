from django.urls import path, include

from .apis.tag import (
    TagAPI,
    TagDetailAPI
)


from .apis.country import (
    CountryAPI,
    CountryDetailAPI
)


from .apis.language import (
    LanguageAPI,
    LanguageDetailAPI
)


from .apis.genre import (
    GenreAPI,
    GenreDetailAPI
)


genre_patterns = [
    path('', GenreAPI.as_view(), name='list-or-create-genre'),
    path('<int:pk>/', GenreDetailAPI.as_view(),
         name='get-delete-update-genre')
]


tag_patterns = [
    path('', TagAPI.as_view(), name='list-or-create-tag'),
    path('<int:pk>/', TagDetailAPI.as_view(),
         name='get-delete-update-tag')
]

country_patterns = [
    path('', CountryAPI.as_view(), name='list-or-create-country'),
    path('<int:pk>/', CountryDetailAPI.as_view(),
         name='get-delete-update-counntry')
]

language_patterns = [
    path('', LanguageAPI.as_view(), name='list-or-create-language'),
    path('<int:pk>/', LanguageDetailAPI.as_view(),
         name='get-delete-update-language')
]

urlpatterns = [
    path('tags/', include((tag_patterns, 'tags'))),
    path('genres/', include((genre_patterns, 'genres'))),
    path('countries/', include((country_patterns, 'country'))),
    path('languages/', include((language_patterns, 'language'))),
]
