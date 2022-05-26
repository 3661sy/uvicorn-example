class Request:
    def __init__(self, scope, receive, send) -> None:
        self.scope = scope
    
    @property
    def method(self):
        return self.scope['method']