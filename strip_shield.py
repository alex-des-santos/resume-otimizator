import pathlib
text = pathlib.Path("index.html").read_text(encoding="utf-8")
text = text.replace("🛡️ ", "")
text = text.replace("🛡️", "")
text = text.replace("🛡", "")
pathlib.Path("index.html").write_text(text, encoding="utf-8")
