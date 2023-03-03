"""
    Singleton
        Just Create Instance one time
"""


class Singleton(type):
    _instance = None

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = super().__call__()

        return  self._instance


class Db(metaclass=Singleton):
    pass

db1 = Db()
db2 = Db()

print(db1 is db2)