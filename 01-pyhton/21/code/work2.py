"""
编写一个函数 `merge_markdown(files: list[str], output: str) -> None`，接收两个参数：

- `files`：Markdown 文件路径列表
- `output`：合并后保存的目标文件路径

函数的作用是将多个 Markdown 文件合并为一个文件保存到目标路径。合并规则如下：

1. 最终合并结果的一级标题固定为 `# 合并结果`
2. 所有原始 Markdown 文件的标题需要降级：
   - 一级标题 `#` → 二级标题 `##`
   - 二级标题 `##` → 三级标题 `###`
   - 以此类推
   - 六级标题 `######` → 正文，用 **加粗** 表示
3. 非标题内容（正文、列表、代码块等）保持不变
"""

import re
from pathlib import Path


def merge_markdown(files: list[str], output: str) -> None:
    merged = ["# 合并结果"]
    heading_pattern = re.compile(r"^( {0,3})(#{1,6})([ \t]+|$)(.*)$")

    for file in files:
        lines = []
        in_code_block = False

        for line in Path(file).read_text(encoding="utf-8").splitlines(keepends=True):
            body = line.rstrip("\r\n")
            ending = line[len(body):]

            # ``` 或 ~~~ 表示围栏代码块的开始或结束。
            if body.lstrip().startswith(("```", "~~~")):
                lines.append(line)
                in_code_block = not in_code_block
                continue

            if in_code_block:
                lines.append(line)
                continue

            heading = heading_pattern.match(body)
            if not heading:
                lines.append(line)
                continue

            indent, marks, space, title = heading.groups()
            if len(marks) == 6:
                title = re.sub(r"[ \t]+#+[ \t]*$", "", title).strip()
                lines.append(f"{indent}**{title}**{ending}")
            else:
                lines.append(f"{indent}#{marks}{space}{title}{ending}")

        merged.append("".join(lines))

    Path(output).write_text("\n\n".join(merged) + "\n", encoding="utf-8")
