from fastapi import (
    FastAPI,
    UploadFile,
    File,
    HTTPException
)

import tempfile
import os

from src.pdf_loader import (
    extract_text_from_pdf,
    get_pdf_page_count
)

from src.text_loader import (
    extract_text_file
)

from src.summarizer import (
    summarize_document
)

# --------------------------------------------------
# APP
# --------------------------------------------------

app = FastAPI(
    title="AI Document Summarizer API",
    description="Summarize PDFs and TXT files using BART",
    version="1.0.0"
)

# --------------------------------------------------
# ROOT
# --------------------------------------------------

@app.get("/")
def root():

    return {
        "message":
        "AI Document Summarizer API Running"
    }

# --------------------------------------------------
# HEALTH CHECK
# --------------------------------------------------

@app.get("/health")
def health():

    return {
        "status": "healthy"
    }

# --------------------------------------------------
# SUMMARIZE DOCUMENT
# --------------------------------------------------

@app.post("/summarize")
async def summarize_document_api(
    file: UploadFile = File(...)
):

    try:

        extension = os.path.splitext(
            file.filename
        )[1].lower()

        # -------------------------------
        # SAVE TEMP FILE
        # -------------------------------

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=extension
        ) as tmp:

            content = await file.read()

            tmp.write(content)

            file_path = tmp.name

        # -------------------------------
        # PDF
        # -------------------------------

        if extension == ".pdf":

            text = extract_text_from_pdf(
                file_path
            )

            page_count = get_pdf_page_count(
                file_path
            )

        # -------------------------------
        # TXT
        # -------------------------------

        elif extension == ".txt":

            text = extract_text_file(
                file_path
            )

            page_count = 1

        else:

            raise HTTPException(
                status_code=400,
                detail=
                "Only PDF and TXT files are supported."
            )

        # -------------------------------
        # VALIDATION
        # -------------------------------

        if len(text.strip()) == 0:

            raise HTTPException(
                status_code=400,
                detail=
                "No text could be extracted."
            )

        # -------------------------------
        # SUMMARY
        # -------------------------------

        summary = summarize_document(
            text
        )

        return {

            "file_name":
                file.filename,

            "pages":
                page_count,

            "document_words":
                len(
                    text.split()
                ),

            "summary_words":
                len(
                    summary.split()
                ),

            "summary":
                summary
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    finally:

        try:

            if os.path.exists(
                file_path
            ):

                os.remove(
                    file_path
                )

        except:
            pass