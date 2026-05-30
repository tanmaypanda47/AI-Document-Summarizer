from src.pdf_loader import (
    extract_text_from_pdf
)

from src.summarizer import (
    summarize_document
)

pdf_path = "data/sample.pdf"

text = extract_text_from_pdf(
    pdf_path
)

summary = summarize_document(
    text
)

print(summary)