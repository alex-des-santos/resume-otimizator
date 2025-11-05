import pathlib
text = pathlib.Path(''index.html'').read_text(encoding=''utf-8'')
idx = text.index('100% Seguro:')
segment = text[idx-80:idx+80]
print(segment)
