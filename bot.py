#!/usr/bin/env python
from botflow import Pipe, Bot
from aiohttp import web


p = Pipe(
    {"msg": "hello world!"},
    {"error": "Botflow sucks!"},
    {"error": "Botflow sucks2!"}
)


def create_app():
    app = web.Application()

    app.add_routes([
        web.get('/', p.aiohttp_json_handle)
    ])

    return app


if __name__ == '__main__':
    # BotFlow start web server http://0.0.0.0:8080
    app = create_app()
    Bot.run_app(app)
