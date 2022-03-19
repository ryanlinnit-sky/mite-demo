class ApplicationAPI:
    def __init__(self, ctx):
        self.ctx = ctx
        self._base_url = ctx.config.get("base_url")

    async def get_url1(self):
        async with self.ctx.transaction("url1"):
            return await self.ctx.http.get(f"{self._base_url}/url1")

    async def get_url2(self):
        async with self.ctx.transaction("url2"):
            return await self.ctx.http.get(f"{self._base_url}/url2")

    async def get_url3(self):
        async with self.ctx.transaction("url3"):
            return await self.ctx.http.get(f"{self._base_url}/url3")

    async def get_404(self):
        async with self.ctx.transaction("404"):
            return await self.ctx.http.get(f"{self._base_url}/404")
