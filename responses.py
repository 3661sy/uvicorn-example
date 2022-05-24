import json


class Response:
    media_type = None
    charset = 'utf-8'

    def __init__(self, content = None, status = 200) -> None:
        self.status = status
        self.body = self.content_encode(content)
        self.header = []
        self.append_content_type()
    
    def content_encode(self, content):
        if content is None:
            return b""
        if isinstance(content, bytes):
            return content
        return content.encode(self.charset)
    
    def append_content_type(self):
        if self.media_type is not None:
            self.header.append((b"content-type", self.media_type.encode("latin-1")))
    
    async def __call__(self, scope, receive, send):
        await send(
            {
                'type': 'http.response.start',
                'status': self.status,
                'headers': self.header
            }
        )

        await send(
            {
                'type': 'http.response.body',
                'body': self.body
            }
        )


class JSONResponse(Response):
    media_type = 'application/json'

    def content_encode(self, content):
        return json.dumps(
            content,
            ensure_ascii=False,
            allow_nan=False,
            indent=None,
            separators=(",", ":"),
        ).encode("utf-8")