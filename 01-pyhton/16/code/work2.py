def paginated_query(total_items, page_size):
    """
    模拟分页查询
    total_items: 总数据量
    page_size: 每页大小
    每次 yield 返回一页数据（列表）
    """
    if page_size <= 0:
        raise ValueError("page_size 必须大于 0")

    next_start = 0

    while next_start < total_items:
        end = min(next_start + page_size, total_items)

        yield list(range(next_start, end))

        next_start += page_size


for page in paginated_query(25, 10):
    print(page)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# [20, 21, 22, 23, 24]
