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
    def __init__(self, content, status = 200) -> None:
        self.status = status
        self.body = content
    
    async def __call__(self, scope, receive, send):
        await send(
            {
                'type': 'http.response.start',
                'status': self.status,
                'header': [
                    [b'content-type', b'text/plain']
                ]
            }
        )

        await send(
            {
                'type': 'http.response.body',
                'body': self.body
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