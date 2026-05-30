from PyPDF2 import PdfReader


def extract_text_from_pdf(pdf_path):

    try:

        reader = PdfReader(pdf_path)

        text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text

    except Exception as e:

        print(
            f"PDF Extraction Error: {e}"
        )

        return ""


def get_pdf_page_count(pdf_path):

    try:

        reader = PdfReader(pdf_path)

        return len(reader.pages)

    except Exception as e:

        print(
            f"Page Count Error: {e}"
        )

        return 0


if __name__ == "__main__":

    pdf_path = "data/sample.pdf"

    text = extract_text_from_pdf(
        pdf_path
    )

    pages = get_pdf_page_count(
        pdf_path
    )

    print(
        f"Pages: {pages}"
    )

    print(
        f"Words: {len(text.split())}"
    )