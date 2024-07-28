from pdf.PdfReader import PdfReader
from ai.Translate import Translator
from docx import Document
from huggingface_hub import login

def main():
    counter = 1

    pdf_path = "C:/Users/moham/Downloads/questioning-the-influence-of-political-trust-on-individuals-unconventional-political-participation-in-palestine.pdf"
    output_docx_path = "C:/Users/moham/OneDrive/Desktop/Translator/translated_document.docx"

    pdf_reader = PdfReader(pdf_path)
    translator = Translator()
    document = Document()
    
    pages = pdf_reader.parse()
    
    for page in pages:
        print("started with the page" + str(counter))
        document.add_heading(f'Page {page.page_number}', level=1)
        document.add_paragraph(f'Header: {page.header}')
        
        for paragraph in page.paragraphs:
            if paragraph:  # Ensure the paragraph is not empty
                translated_paragraph = translator.translate(paragraph)
                document.add_paragraph(translated_paragraph)
        
        document.add_paragraph(f'Footer: {page.footer}')
        document.add_page_break()
        print("done from page" + str(counter))
        counter += 1

    document.save(output_docx_path)

if __name__ == "__main__":
    main()
