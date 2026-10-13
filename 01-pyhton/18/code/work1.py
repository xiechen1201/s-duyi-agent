# 编写一个抽象基类 `Cache`，定义缓存的基本接口，然后实现 `MemoryCache` 和 `FileCache`：

from abc import ABC, abstractmethod


class Cache(ABC):
    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def set(self, key, value):
        pass

    @abstractmethod
    def delete(self, key):
        pass


class MemoryCache(Cache):
    def __init__(self) -> None:
        super().__init__()


# 实现 MemoryCache（使用字典存储）
# 实现 FileCache（使用文件存储）
