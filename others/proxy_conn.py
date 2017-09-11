import asyncio, aiohttp

async def tasks():
    # connector = aiohttp.ProxyConnector(proxy="http://127.0.0.1:5000")
    headers = {'content-type': 'text/html'}
    session = aiohttp.ClientSession()
    async with session.head("http://aiohttp.readthedocs.io/en/stable/client.html", proxy='http://127.0.0.1:5000', headers=headers) as resp:
        print(resp.status, resp.headers)
    session.close()

loop = asyncio.get_event_loop()
task = asyncio.ensure_future(tasks())
loop.run_until_complete(task)
loop.close()