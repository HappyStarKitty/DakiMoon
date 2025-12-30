import re
from docx import Document
from opencc import OpenCC

# 初始化繁体转简体转换器
cc = OpenCC('t2s')

doc = Document("career.docx")

career_out_dict = []
code = 1

pattern = re.compile(r'^(\d+)[\t ]+.*?([\u4e00-\u9fff]+)')

for para in doc.paragraphs:
    text = para.text.strip()
    match = pattern.match(text)
    if match:
        trad_label = match.group(2)
        simp_label = cc.convert(trad_label)
        career_out_dict.append({
            "code": code,
            "label": simp_label
        })
        code += 1

with open("career_dict.py", "w", encoding="utf-8") as f:
    f.write("career_out_dict = [\n")
    for item in career_out_dict:
        f.write(f'    {{ "code": {item["code"]}, "label": "{item["label"]}" }},\n')
    f.write("]\n")



