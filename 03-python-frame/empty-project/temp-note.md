# 统一异常处理

有的时候异常要做统一的处理：

- 日志记录

- 统一的响应格式


fastapi 如果指定了异常，

if result is None:
        raise HTTPException(status_code=404, detail="商品不存在")
    return result


就会按照指定的异常处理函数，进行处理。

否则，就会按照默认的异常处理函数，进行统一处理，返回固定 500 错误。

（做了一些事情，但是做的不够）

## 设计

异常配置中心（做一个错误映射）：

DataBaseException ==> 422，422001，"数据问题"
RequestValidationError ==> 422，422002，"数据验证失败"

PROTOCOL_ERROR_MAP？