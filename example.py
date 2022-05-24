# async def app(scope, receive, send):
#     assert scope['type'] == 'http'

#     await send({
#         'type': 'http.response.start',
#         'status': 200,
#         'headers': [
#             [b'content-type', b'text/plain'],
#         ],
#     })
#     await send({
#         'type': 'http.response.body',
#         'body': b'Hello, world!',
#     })

from responses import JSONResponse

class Server:
    async def __call__(self, scope, receive, send):
        print(scope)
        self.scope = scope
        self.receive = receive
        self.send = send

        response = JSONResponse(content={'data': "data"})

        await response(scope, receive, send)

app = Server()