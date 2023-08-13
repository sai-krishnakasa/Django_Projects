from django.http import HttpResponse
from django.shortcuts import render,redirect
import requests,time
import concurrent.futures
import aiohttp,asyncio
import multiprocessing

# Serial Fetching ( normal )
def home_view(request):
    start=time.time()
    data=[]
    url_list=['https://swapi.dev/api/people/','https://swapi.dev/api/starships/']
    for url in url_list:
        data.append(requests.get(url).json())
    total=time.time()-start
    #12,13,24,15 sec
    print( 'serial'+str(total))
    return render(request,'home.html',{'people':data[0],'starships':data[1],'time':total})
    
async def fetch(session,url):
    async with session.get(url) as resp:
        return await resp.json()
# def fetch(url):
#      return  requests.get(url).json()

async def  home_views(request):
    start=time.time()
    url_list=['https://swapi.dev/api/people/','https://swapi.dev/api/starships/']


    # using Async 
    #7sec,8.3sec,36 sec,6.6 sec,10..
    async with aiohttp.ClientSession() as session:
        tasks=[]
        for url in url_list:
            task=asyncio.ensure_future(fetch(session,url))
            tasks.append(task)
        data=await asyncio.gather(*tasks)

    # Using Concuurent.future a multiprocessing and multithreading Pool
    
    # with concurrent.futures.ThreadPoolExecutor() as exec:
    #     # function as sync 13secs,26,7,8.8,8.7,27.9,11
    #     # with function as async 8.5,8.5,8.4,
    #     # with ThreadPool function as async 9.5,13,33,12
    #     result=exec.map(fetch,url_list)
    #     data=[]
    #     for res in  result:
    #         data.append(res)
    #     print(data)
    # p1=multiprocessing.Process(target=fetch,args=(url_list[0],))
    # p2=multiprocessing.Process(target=fetch,args=(url_list[1],))
    # p1.start()
    # p2.start()
    # print(p1)
    # print(p2)
    # # using multiprocessing 15.5,14.66,12.616,13.4..
    # p1.join()
    # p2.join()
    total=time.time()-start
    print(total)
    return render(request,'home.html',{'people':data[0],'starships':data[1],'time':total,'data':data})
    