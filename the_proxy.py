import asyncio
import aiohttp


async def tasks():
    url = 'http://aiohttp.readthedocs.io/en/stable/_modules/aiohttp/client_reqrep.html' # "http://cwer.ws/"
    headers = {'Content-type': 'text/html', 'Accept-Encoding': 'identity'} # 'Accept-Encoding': 'identity'
    session = aiohttp.ClientSession()
    async with session.get(url=url, proxy='http://127.0.0.1:8080', headers=headers) as resp:
        print(f'===Response from proxy=== \nStatus: {resp.status}')
        print('\n'.join(f'{str(k)}: {str(v)}' for k, v in resp.headers.items()))
        a = await resp.text()
        print('\n' + a)
    await session.close()

loop = asyncio.get_event_loop()
task = asyncio.ensure_future(tasks())
loop.run_until_complete(task)
loop.close()
