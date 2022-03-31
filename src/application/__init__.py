class ApplicationAPI:
    def __init__(self, ctx):
        self.ctx = ctx
        self._base_url = ctx.config.get("base_url")

    # An example of a GET request
    async def get_url1(self):
        async with self.ctx.transaction("url1"):
            return await self.ctx.http.get(f"{self._base_url}/url1")

    # An example of a GET request that returns a 201 status code
    async def get_url2(self):
        async with self.ctx.transaction("url2"):
            return await self.ctx.http.get(f"{self._base_url}/url2")

    # An example of a GET request that returns a 202 status code
    async def get_url3(self):
        async with self.ctx.transaction("url3"):
            return await self.ctx.http.get(f"{self._base_url}/url3")

    # An example of a POST request with a payload
    async def post_url5(self):
        async with self.ctx.transaction("post url5"):
            return await self.ctx.http.post(
                f"{self._base_url}/url5", json={"test": 123}
            )

    # An example of a DELETE request
    async def delete_url1(self):
        async with self.ctx.transaction("delete url1"):
            return await self.ctx.http.delete(f"{self._base_url}/url1")

    # An example of a GET request that returns JSON data
    async def get_profile(self, user_id=12345):
        async with self.ctx.transaction("get_profile"):
            return await self.ctx.http.get(f"{self._base_url}/get_profile/{user_id}")

    # An example of a GET request that returns a 404 status code
    async def get_404(self):
        async with self.ctx.transaction("404"):
            return await self.ctx.http.get(f"{self._base_url}/404")
