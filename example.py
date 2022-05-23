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

class Response:
    async def __call__(self, scope, receive, send):
        await send(
            {
                'type': 'http.response.start',
                'status': 200,
                'header': [
                    [b'content-type', b'text/plain']
                ]
            }
        )

        await send(
            {
                'type': 'http.response.body',
                'body': b'Hello.world'
            }
        )


class Test:
    async def __call__(self, scope, receive, send):
        self.scope = scope
        self.receive = receive
        self.send = send

        response = Response()

        await response(scope, receive, send)

app = Test()