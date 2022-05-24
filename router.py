from typing import Callable

from request import Request


class Router:
    def __init__(self, path, view: Callable) -> None:
        self.path = path
        self.view = view
    

    async def __call__(self, scope, receive, send):
        request = Request(scope, receive, send)
        response = await self.view(request)
        
        await response(scope, receive, send)