import tempfile,shutil


class TempDirectory:
    def __init__(self) -> None:
        pass

    def __enter__(self):
        self.path = tempfile.mkdtemp()
        return self.path 

    def __exit__(self, exc_type, exc, tb):
        shutil.rmtree(self.path)


with TempDirectory() as tmp_dir:
    print(f"临时目录: {tmp_dir}")
    # 可以在这个目录中创建文件
    # 离开 with 块时，目录及其内容自动删除

print("临时目录已清理")
