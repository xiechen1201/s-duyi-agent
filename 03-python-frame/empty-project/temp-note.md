# 依赖注入

upload_file 函数耦合度太高了，应该让外部决定上传到哪里，这就是 IOC 思想。

把选择权移交出去。

耦合的话，就把内部的逻辑提取成函数的参数。

这样的行为做法就是 IOC。

传递参数的形式非常不舒服，DI 框架就是为了解决这个问题的。

（模拟实现 DOI）

## 完善 API 层

```python
@router.post("", response_model=ProductResponse, status_code=201)
async def create_product(
    data: ProductCreate, db: Annotated[AsyncSession, Depends(get_db)]
):
    return await ProductService(db).create_product(data)
```

依赖注入，db: Annotated[AsyncSession, Depends(get_db)]。

Python 的类型标注工具，Annotated。

声明为 AsyncSession 类型，例如 name: [x, y] = name: x 的类型，y 的类型表示会进入到 name 的元数据中，例如 name.__metadata__.y。

什么作用？

db.__metadata__.Depends(get_db) 的实例。

请求达到 ==> fastapi ==> 路由 ==> 函数

  检查函数的参数，为每个参数赋值，如果发现某个参数的元数据中包含 Depend 的实例，从实例中取出方法，然后执行，将结果作为参数的值。


从实例中取出方法，然后执行，如果发现方法是一个异步生成器，进行一个特殊的处理，进行自动迭代一次，拿到迭代结果，赋值给参数。

路由函数执行完成，继续迭代，直到迭代完成。

todo：整个请求都在上下文中？？？

一个请求一个 session。