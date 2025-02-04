from db.models import Movie
from django.db.models import QuerySet


def get_movies(
        genres_ids: int = None,
        actors_ids: int = None
) -> QuerySet:
    queryset = Movie.objects.all()

    if genres_ids is not None:
        queryset = queryset.filter(
            genres__id__in=genres_ids
        )
    if actors_ids is not None:
        queryset = queryset.filter(
            actors__id__in=actors_ids
        )

    return queryset


def get_movie_by_id(movie_id: int) -> str:
    movie = Movie.objects.get(id=movie_id)
    return movie


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None,
) -> Movie:
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    if genres_ids:
        new_movie.genres.set(genres_ids)

    if actors_ids:
        new_movie.actors.set(actors_ids)

    return new_movie
