# Source Materials

源 PDF 文件用于本项目的目录、术语、流程和页码索引整理：

```text
/Users/zhengrongkai/Downloads/玄学书籍/九紫辰木马七政四余培训教材.pdf
```

为避免重新分发 PDF 原文，本目录不复制 PDF。若在本地重新构建参考资料，请把合法取得的源 PDF 放在本目录或使用原路径，然后运行：

```bash
python antigravity/skills/qz-reader/scripts/extract_pdf_text.py --pdf "/Users/zhengrongkai/Downloads/玄学书籍/九紫辰木马七政四余培训教材.pdf" --out build/pdf_text
python shared/scripts/build_source_map.py --text-dir build/pdf_text --out shared/references/source_map.md
```

提取出的逐页文本只应作为本地中间产物使用，不建议提交或二次分发。
