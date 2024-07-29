import PyPDF2
from PageContent import PageContent

class PdfReader:
    def __init__(self, file_path: str):
        """
        Initializes the PdfReader with the path to the PDF file.

        :param file_path: The file path to the PDF.
        """
        self.file_path = file_path

    def _extract_text_by_page(self) -> list:
        """
        Extracts text from each page of the PDF.

        :return: A list of tuples with page number and text.
        """
        text_by_page = []
        try:
            with open(self.file_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                for page_num in range(len(reader.pages)):
                    page = reader.pages[page_num]
                    text = page.extract_text()
                    text_by_page.append((page_num + 1, text))
        except Exception as e:
            print(f"Error extracting text from PDF: {e}")
        return text_by_page

    def _extract_header_footer(self, lines: list, page_number: int) -> tuple:
        """
        Extracts the header and footer from a page's text.

        :param lines: The lines of text in the page.
        :param page_number: The page number.
        :return: A tuple containing the header and footer.
        """
        header = lines[0].strip() if len(lines) > 0 and len(lines[0].strip()) < 100 else ''
        footer = lines[-1].strip() if len(lines) > 1 and len(lines[-1].strip()) < 100 else ''
        
        # Check for page number in the footer
        if footer.isdigit() and int(footer) == page_number:
            footer = footer
        else:
            footer = ''
            
        return header, footer

    def parse(self) -> list:
        """
        Parses the PDF and extracts content from each page.

        :return: A list of PageContent objects.
        """
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
