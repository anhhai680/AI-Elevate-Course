import PyPDF2
import sys

def read_pdf(file_path):
    """Read PDF file and extract text content"""
    try:
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None

if __name__ == "__main__":
    pdf_file = "Assignment_12.pdf"
    content = read_pdf(pdf_file)
    if content:
        print("PDF Content:")
        print("=" * 50)
        print(content)
        print("=" * 50)
    else:
        print("Failed to read PDF content")
