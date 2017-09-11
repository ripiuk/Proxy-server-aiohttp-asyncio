import asyncio
from aiohttp import web
import aiohttp


async def handler(request):
    request_head = {k.encode('utf-8'): v.encode('utf-8') for k, v in request.headers.items()}
    print('request_head ==', request_head)
    session = aiohttp.ClientSession()
    async with session.get(url=request.scheme + '://' + request.host + request.path,
                           headers=request.headers) as resp:
        print('response ==', resp.status, resp.headers)
        # a = await resp.read()
        status = resp.status
        headers = resp.headers
        headers = dict(headers)
        if 'Transfer-Encoding' in headers:
            headers.pop('Transfer-Encoding')
        body = await resp.read()
    await session.close()

    return web.Response(status=status, headers=headers, body=body) # body=resp.content

    # response_head = tuple((k.encode('utf-8'), v.encode('utf-8')) for k, v in resp.headers.items())
    # resp = web.Response(text="\n".join((str(request_head), str(response_head))))
    # return web.Response(text='===Request to proxy===\n' + f'Status: {resp.status}\n' +
    #                          '\n'.join(f'{str(k)}: {str(v)}' for k, v in request.headers.items()) + '\n\n'
    #                          '===Response from target===\n' + f'Status: {resp.status}\n' +
    #                          '\n'.join(f'{str(k)}: {str(v)}' for k, v in resp.headers.items()) + '\n' +
    #                          '\nHTML:\n' + a.decode('utf-8'))


async def main(loop):
    server = web.Server(handler)
    await loop.create_server(server, "127.0.0.1", 8080)
    print("======= Serving on http://127.0.0.1:8080/ ======")

    # pause here for very long time by serving HTTP requests and
    # waiting for keyboard interruption
    await asyncio.sleep(100*3600)


loop = asyncio.get_event_loop()

try:
    loop.run_until_complete(main(loop))
except KeyboardInterrupt:
    pass
loop.close()
