from docxtpl import DocxTemplate
from ..models import Item
from typing import List

# returns file name in /static directory
def generate_doc(items: List[Item], word_name: str) -> str:
    doc = DocxTemplate("template.docx")
    context = { 'items' : items}
    doc.render(context)
    doc.save("generated_doc.docx")
    return "generated_doc.docx"

doc = DocxTemplate("template.docx")
context = { 'tmp' : "Зубенко Михаил Петрович"}
doc.render(context)
doc.save("generated_doc.docx")