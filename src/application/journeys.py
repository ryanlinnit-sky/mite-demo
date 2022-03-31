from mite_http import mite_http

from . import ApplicationAPI


@mite_http
async def get_url1_journey(ctx):
    app = ApplicationAPI(ctx)
    await app.get_url1()


@mite_http
async def get_url2_journey(ctx):
    app = ApplicationAPI(ctx)
    await app.get_url2()


@mite_http
async def get_url3_journey(ctx):
    app = ApplicationAPI(ctx)
    await app.get_url3()


@mite_http
async def post_url5_journey(ctx):
    app = ApplicationAPI(ctx)
    await app.post_url5()


# A journey that uses a datapool
@mite_http
async def get_profile_journey(ctx, user_id):
    app = ApplicationAPI(ctx)
    await app.get_profile(user_id)


@mite_http
async def get_404_journey(ctx):
    app = ApplicationAPI(ctx)
    await app.get_404()
