"""
    Chain Of Responsibility
        - List Of moods
"""

class Handler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle_request(self, request):
        handled = self._handle(request)

        if not handled and self._successor:
            self._successor.handle_request(request)

    def _handle(self, request):
        raise NotImplementedError('Must provide implementation in subclass.')


class ConcreteHandler1(Handler):
    def _handle(self, request):
        if 0 < request <= 10:
            print(f'Request {request} handled by ConcreteHandler1')
            return True


class ConcreteHandler2(Handler):
    def _handle(self, request):
        if 10 < request <= 20:
            print(f'Request {request} handled by ConcreteHandler2')
            return True


class ConcreteHandler3(Handler):
    def _handle(self, request):
        if 20 < request <= 30:
            print(f'Request {request} handled by ConcreteHandler3')
            return True


class DefaultHandler(Handler):
    def _handle(self, request):
        print(f'End of chain, no handler for {request}')
        return True


class Client:
    def __init__(self):
        self.handler = ConcreteHandler1(ConcreteHandler2(ConcreteHandler3(DefaultHandler())))

    def delegate(self, requests):
        for request in requests:
            self.handler.handle_request(request)


c = Client()
c.delegate([5, 15, 25, 35])