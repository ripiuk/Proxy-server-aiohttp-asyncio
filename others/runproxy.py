import logging
from urllib.parse import urljoin

import asyncio
import aiohttp
from aiohttp import web


TARGET_SERVER_BASE_URL = 'http://127.0.0.1:5000'


logger = logging.getLogger("runproxy")


async def proxy(request):
    target_url = urljoin(TARGET_SERVER_BASE_URL, request.match_info['path'])
    logger.info("Requesting to: %s", target_url)
    res = await aiohttp.request('get', target_url)
    raw = await res.text()
    logger.info("Got a response from: %s", target_url)

    return web.Response(text=raw, status=res.status, headers={"Content-Type": "application/json"})


if __name__ == "__main__":
    logging.root.setLevel(logging.INFO)
    logging.root.addHandler(logging.StreamHandler())

    app = web.Application()
    app.router.add_route('GET', '/{path:\w*}', proxy)

    loop = asyncio.get_event_loop()
    f = loop.create_server(app.make_handler(), '127.0.0.1', 8080)
    srv = loop.run_until_complete(f)
    print('serving on', srv.sockets[0].getsockname())
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass