from mite_http import mite_http

from . import ApplicationAPI

@mite_http
async def get_url1_journey(ctx):
    app =  ApplicationAPI(ctx)
    return await app.get_url1()

@mite_http
async def get_url2_journey(ctx):
    app =  ApplicationAPI(ctx)
    return await app.get_url2()

@mite_http
async def get_url3_journey(ctx):
    app =  ApplicationAPI(ctx)
    return await app.get_url3()

@mite_http
async def get_404_journey(ctx):
    app =  ApplicationAPI(ctx)
    return await app.get_404()

