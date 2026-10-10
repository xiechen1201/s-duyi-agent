# 编写一个元类 `PluginMeta`，使得任何继承自 `Plugin` 的子类都会被自动注册到 `PluginMeta.registry` 字典中（键为类名，值为类本身）：


class PluginMeta(type):
    registry = {}

    def __new__(
        mcls,
        name,
        bases,
        namespace,
    ):
        cls = super().__new__(mcls, name, bases, namespace)
        if name != "plugin":
            mcls.registry[cls] = cls

        return cls


class Plugin(metaclass=PluginMeta):
    pass


class ImagePlugin(Plugin):
    pass


class TextPlugin(Plugin):
    pass


print(PluginMeta.registry)

# 应该输出类似：{'ImagePlugin': <class '__main__.ImagePlugin'>, 'TextPlugin': <class '__main__.TextPlugin'>}
