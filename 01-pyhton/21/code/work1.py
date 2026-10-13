"""
编写一个函数 `show_tree(dir_path: str, show_hidden: bool = False)`，接收两个参数：

- `dir_path`：目录路径，可以是绝对路径或相对路径（相对当前工作目录 CWD）
- `show_hidden`：布尔类型，表示是否显示隐藏文件/目录

隐藏判断简单处理：文件或目录只要以`.`开头，则视为隐藏文件或目录，否则的话视为可视。

函数的功能是用树形递归的方式展示指定目录下的所有内容。效果类似于 Linux 的 `tree` 命令。
"""

from pathlib import Path


def show_tree(dir_path: str, show_hidden: bool = False) -> None:
    root = Path(dir_path)
    if not root.exists():
        raise FileNotFoundError(f"目录不存在: {dir_path}")
    if not root.is_dir():
        raise NotADirectoryError(f"不是目录: {dir_path}")

    print(root)

    def walk(directory: Path, prefix: str) -> None:

        entries = sorted(
            (
                entry
                for entry in directory.iterdir()
                if show_hidden or not entry.name.startswith(".")
            ),
            key=lambda entry: entry.name.casefold(),
        )

        for index, entry in enumerate(entries):
            is_last = index == len(entries) - 1
            print(f"{prefix}{'└── ' if is_last else '├── '}{entry.name}")
            if entry.is_dir() and not entry.is_symlink():
                walk(entry, prefix + ("    " if is_last else "│   "))

    walk(root, "")


show_tree(".")
