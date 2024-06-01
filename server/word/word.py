from docxtpl import DocxTemplate

doc = DocxTemplate("template.docx")
context = { 'tmp' : "Зубенко Михаил Петрович"}
doc.render(context)
doc.save("generated_doc.docx")