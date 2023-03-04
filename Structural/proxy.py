"""
    Proxy
"""

class RealSubject:
    def request(self):
        print("RealSubject handles the request")

class Proxy:
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        if self._check_access():
            self._real_subject.request()

    def _check_access(self):
        print("Proxy: Checking access prior to firing a real request.")
        return True

real_subject = RealSubject()
proxy = Proxy(real_subject)
proxy.request()