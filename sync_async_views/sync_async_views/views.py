from django.http import HttpResponse
import time,asyncio
from Stories.models import story
from Movies.models import movie
from asgiref.sync import sync_to_async

def get_movies():
    print('Fetching Movies Started')
    time.sleep(6)
    movies=movie.objects.all()
    print(movies)
    print('Movies fetched Successfully')


def get_stories():
    print('Fetching Stories Started')
    time.sleep(8)
    stories=story.objects.all()
    print(stories)
    print('Stories fetched Successfully')
@sync_to_async
def get_movies_async():
    print('Fetching Movies Started')
    time.sleep(6)
    movies=movie.objects.all()
    print(movies)
    print('Movies fetched Successfully')

@sync_to_async
def get_stories_async():
    print('Fetching Stories Started')
    time.sleep(8)
    stories=story.objects.all()
    print(stories)
    print('Stories fetched Successfully')

def home(request):
    return HttpResponse('Hello world')
def main_view(request):
    start_time=time.time()
    get_movies()
    get_stories()
    total_time=(time.time()-start_time)
    print('total_time:'+str(total_time))
    return HttpResponse('sync')

async def main_view_async(request):
    start_time=time.time()
    await asyncio.gather(get_movies_async(),get_stories_async())
    total_time=(time.time()-start_time)
    print('total_time:'+str(total_time))
    return HttpResponse('async')
    
