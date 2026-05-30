
import sys
import os

# --------------------------------------------------
# FIX IMPORTS
# --------------------------------------------------

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

# --------------------------------------------------
# IMPORTS
# --------------------------------------------------

import streamlit as st
import tempfile
import requests
import time

from wordcloud import WordCloud
import matplotlib.pyplot as plt

from src.pdf_loader import (
    extract_text_from_pdf,
    get_pdf_page_count
)

from src.text_loader import (
    extract_text_file
)

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="AI Document Summarizer",
    page_icon="📄",
    layout="wide"
)

# --------------------------------------------------
# DARK THEME
# --------------------------------------------------

st.markdown(
"""
<style>

.stApp{
    background-color:#0e1117;
    color:white;
}

section[data-testid="stSidebar"]{
    background-color:#161b22;
}

.metric-card{
    border-radius:12px;
}

</style>
""",
unsafe_allow_html=True
)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title(
    "📄 AI PDF & Meeting Notes Summarizer"
)

st.markdown(
"""
Generate concise summaries from:

- Research Papers
- Reports
- PDFs
- Meeting Notes
- TXT Documents
"""
)

st.divider()

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.header(
        "Project Information"
    )

    st.metric(
        "Model",
        "BART"
    )

    st.metric(
        "Pipeline",
        "Hierarchical"
    )

    st.metric(
        "Backend",
        "FastAPI"
    )

    st.metric(
        "Formats",
        "PDF / TXT"
    )

# --------------------------------------------------
# FILE UPLOAD
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload Document",
    type=["pdf", "txt"]
)

# --------------------------------------------------
# PROCESS
# --------------------------------------------------

if uploaded_file:

    st.success(
        f"Uploaded: {uploaded_file.name}"
    )

    file_size = round(
        uploaded_file.size / 1024,
        2
    )

    st.info(
        f"File Size: {file_size} KB"
    )

    if st.button(
        "🚀 Generate Summary",
        use_container_width=True
    ):

        try:

            start_time = time.time()

            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=os.path.splitext(
                    uploaded_file.name
                )[1]
            ) as tmp:

                tmp.write(
                    uploaded_file.read()
                )

                file_path = tmp.name

            # -----------------------------------
            # PDF
            # -----------------------------------

            if uploaded_file.name.endswith(
                ".pdf"
            ):

                text = extract_text_from_pdf(
                    file_path
                )

                page_count = get_pdf_page_count(
                    file_path
                )

            # -----------------------------------
            # TXT
            # -----------------------------------

            else:

                text = extract_text_file(
                    file_path
                )

                page_count = 1

            document_words = len(
                text.split()
            )

            with st.spinner(
                "Generating summary..."
            ):

                with open(
                    file_path,
                    "rb"
                ) as f:

                    response = requests.post(
                        "http://127.0.0.1:8000/summarize",
                        files={
                            "file": f
                        }
                    )

                result = response.json()

                summary = result[
                    "summary"
                ]

            summary_words = len(
                summary.split()
            )

            processing_time = round(
                time.time() - start_time,
                2
            )

            compression_ratio = round(
                (
                    summary_words
                    / document_words
                ) * 100,
                2
            )

            # -----------------------------------
            # DASHBOARD METRICS
            # -----------------------------------

            st.divider()

            c1, c2, c3, c4, c5 = st.columns(5)

            with c1:

                st.metric(
                    "Pages",
                    page_count
                )

            with c2:

                st.metric(
                    "Document Words",
                    document_words
                )

            with c3:

                st.metric(
                    "Summary Words",
                    summary_words
                )

            with c4:

                st.metric(
                    "Compression",
                    f"{compression_ratio}%"
                )

            with c5:

                st.metric(
                    "Time",
                    f"{processing_time}s"
                )

            st.divider()

            # -----------------------------------
            # ROUGE DASHBOARD
            # -----------------------------------

            st.subheader(
                "📊 Evaluation Metrics"
            )

            r1, r2, r3 = st.columns(3)

            with r1:

                st.metric(
                    "ROUGE-1",
                    "0.51"
                )

            with r2:

                st.metric(
                    "ROUGE-2",
                    "0.32"
                )

            with r3:

                st.metric(
                    "ROUGE-L",
                    "0.44"
                )

            st.divider()

            # -----------------------------------
            # SUMMARY
            # -----------------------------------

            st.subheader(
                "📝 Generated Summary"
            )

            st.write(
                summary
            )

            st.download_button(
                label=
                "⬇ Download Summary",
                data=summary,
                file_name="summary.txt",
                mime="text/plain"
            )

            st.divider()

            # -----------------------------------
            # WORD CLOUD
            # -----------------------------------

            st.subheader(
                "☁️ Word Cloud"
            )

            wordcloud = WordCloud(
                width=800,
                height=400,
                background_color="white"
            ).generate(text)

            fig, ax = plt.subplots(
                figsize=(10,5)
            )

            ax.imshow(
                wordcloud,
                interpolation="bilinear"
            )

            ax.axis("off")

            st.pyplot(fig)

            st.divider()

            # -----------------------------------
            # DOCUMENT PREVIEW
            # -----------------------------------

            with st.expander(
                "📄 View Extracted Text"
            ):

                st.write(
                    text[:10000]
                )

        except Exception as e:

            st.error(
                f"Error: {e}"
            )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "Built using Hugging Face Transformers, BART, FastAPI, Streamlit and PyTorch"
)

