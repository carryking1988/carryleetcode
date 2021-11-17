class SingleTon(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(SingleTon, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class Myclass(SingleTon):
    pass


a = Myclass()
b = Myclass()

print(id(a))
print(id(b))

# 装饰器单例
from functools import wraps


def single_ton(cls):
    _instance = {}

    @wraps(cls)
    def single(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return single
