import docx
# 创建一个新的word文档
doc = docx.Document()

# 添加段落
doc.add_paragraph("dfsdfdsfsdfsd")

# 保存文件
doc.save("my_doc.docx")
