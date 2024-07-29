# LLM Translator

LLM Translator is a project designed to translate PDF documents into Arabic using a large language model (LLM) from Hugging Face. The project reads a PDF, translates its content page by page, and saves the translated text in a Word document.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Files and Directories](#files-and-directories)
- [Contributing](#contributing)
- [License](#license)

## Installation

To set up this project locally, follow these steps:

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/Moh097/LLM_Translator.git
    cd LLM_Translator
    ```

2. **Create and Activate a Virtual Environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the Required Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Prepare Your PDF File**:
    Place your PDF file in an accessible location and note its file path.

2. **Run the Translation Script**:
    Update the `main.py` script with the path to your PDF file and the desired output path for the translated document.
    ```python
    pdf_path = "path/to/your/document.pdf"
    output_docx_path = "path/to/save/translated_document.docx"
    ```

3. **Execute the Script**:
    Run the main script to start the translation process.
    ```sh
    python main.py
    ```

## Files and Directories

- `main.py`: The main script to execute the translation.
- `pdf/PdfReader.py`: Contains the `PdfReader` class for reading and parsing the PDF file.
- `ai/Translate.py`: Contains the `Translator` class for translating text using the LLM.
- `requirements.txt`: Lists all the dependencies required to run the project.

## Contributing

Contributions are welcome! If you have suggestions for improvements or find any bugs, please create an issue or submit a pull request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/YourFeature`)
3. Commit your Changes (`git commit -m 'Add some feature'`)
4. Push to the Branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

