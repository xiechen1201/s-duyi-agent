const fs = require("node:fs");

/**
 * 合并多个 Markdown 文件，并将标题降级一级。
 * @param {string[]} files Markdown 文件路径列表
 * @param {string} output 合并后的输出路径
 */
function mergeMarkdown(files, output) {
  const sections = ["# 合并结果"];
  const headingPattern = /^( {0,3})(#{1,6})([ \t]+|$)(.*)$/;

  for (const file of files) {
    let inCodeBlock = false;
    const lines = fs.readFileSync(file, "utf8").split(/\r?\n/);

    const convertedLines = lines.map((line) => {
      // ``` 或 ~~~ 表示围栏代码块的开始或结束。
      if (line.trimStart().startsWith("```") || line.trimStart().startsWith("~~~")) {
        inCodeBlock = !inCodeBlock;
        return line;
      }

      if (inCodeBlock) {
        return line;
      }

      const heading = line.match(headingPattern);
      if (!heading) {
        return line;
      }

      const [, indent, marks, space, title] = heading;
      if (marks.length === 6) {
        const text = title.replace(/[ \t]+#+[ \t]*$/, "").trim();
        return `${indent}**${text}**`;
      }

      return `${indent}#${marks}${space}${title}`;
    });

    sections.push(convertedLines.join("\n"));
  }

  fs.writeFileSync(output, `${sections.join("\n\n")}\n`, "utf8");
}

module.exports = { mergeMarkdown };

// 用法：node node_version.js 输出文件.md 输入文件1.md 输入文件2.md
if (require.main === module) {
  const [output, ...files] = process.argv.slice(2);

  if (!output || files.length === 0) {
    console.error("用法：node node_version.js 输出文件.md 输入文件1.md [输入文件2.md ...]");
    process.exitCode = 1;
  } else {
    mergeMarkdown(files, output);
  }
}
