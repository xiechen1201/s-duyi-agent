# 中间件

目标是统一响应格式。

```
{
    "code": 0,
    "msg": "success",
    "data": {}
}
```

还要做做安全控制、身份认证、CORS 处理、（核心业务逻辑）、日志记录等。

所有的业务都要经过上面的过程。通过中间件解决。

## 核心概念

IOC：选择权交出去

AOP：共同的事情切出去

DI 既可以实现 IOC，也可以实现 AOP。DI 不是实现 AOP 的唯一方式。

## 理解中间件

分为函数形式和类形式。

当注册了一个应用的时候，请求 ==> 执行第一个中间件函数 ==> 拿到函数结果作为响应。

通过中间件的函数 call_next 进行串联。`async def my_middleware(request: Request, call_next):`

如果没有调用 call_next 那么中间件函数就中断了。

app.middleware("http")(my_middleware) 可以替换为 websocket，用于匹配 websocket 请求。

response = await call_next(request)

如果这里发生异常，则后续的逻辑代码不会执行。

优化：

1、第一个中间件函数统一出来 error，这样的话就必须把这个中间件函数放到最前面。

2、

## 统一响应格式 

## 性能调试

## 跨域中间件

