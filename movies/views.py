from django.http import JsonResponse
from movies.fetch_movies import get_ghibli_data
import requests

from aiocache import cached


async def index(request):
    movies = await get_ghibli_data()
    return JsonResponse(movies, safe=False)
