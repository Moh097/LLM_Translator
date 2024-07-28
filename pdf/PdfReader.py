import PyPDF2

class PageContent:
    def __init__(self, header, footer, page_number, paragraphs):
        self.header = header
        self.footer = footer
        self.page_number = page_number
        self.paragraphs = paragraphs

class PdfReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def _extract_text_by_page(self):
        text_by_page = []
        with open(self.file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text = page.extract_text()
                text_by_page.append((page_num + 1, text))
        return text_by_page

    def _extract_header_footer(self, lines, page_number):
        header = lines[0].strip() if len(lines) > 0 and len(lines[0].strip()) < 100 else ''
        footer = lines[-1].strip() if len(lines) > 1 and len(lines[-1].strip()) < 100 else ''
        
        # Check for page number in the footer
        if footer.isdigit() and int(footer) == page_number:
            footer = footer
        else:
            footer = ''
            
        return header, footer

    def parse(self):
        pages_content = []
        text_by_page = self._extract_text_by_page()

        for page_number, text in text_by_page:
            lines = text.split('\n')
            header, footer = self._extract_header_footer(lines, page_number)
            paragraph = text.replace('\n', ' ').strip()  # Combine all text into one paragraph and remove newlines

            # Remove header and footer from the paragraph if they exist
            if header:
                paragraph = paragraph.replace(header, '').strip()
            if footer:
                paragraph = paragraph.replace(footer, '').strip()

            page_content = PageContent(header, footer, page_number, [paragraph])
            pages_content.append(page_content)

        return pages_content
