

class ApplicationAPI():

    def __init__(self, ctx, auth=None, headers=None, token=None, base_url=None):
        self.ctx = ctx
        # super().__init__(ctx, headers, auth)
        # self._base_url = base_url or ctx.config.get("bridge_base_url")

    async def get_url1(self):
        async with self.ctx.transaction("url1"):
            return await self.ctx.http.get("http://localhost:5002/url1")

    async def get_url2(self):
        async with self.ctx.transaction("url2"):
            return await self.ctx.http.get("http://localhost:5002/url2")

    async def get_url3(self):
        async with self.ctx.transaction("url3"):
            return await self.ctx.http.get("http://localhost:5002/url3")

    async def get_404(self):
        async with self.ctx.transaction("404"):
            return await self.ctx.http.get("http://localhost:5002/404")
