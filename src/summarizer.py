from transformers import pipeline
import torch

# --------------------------------------------------
# DEVICE
# --------------------------------------------------

DEVICE = 0 if torch.cuda.is_available() else -1

print(
    f"Using Device: {'GPU' if DEVICE == 0 else 'CPU'}"
)

# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------

summarizer = pipeline(
    task="summarization",
    model="facebook/bart-large-cnn",
    device=DEVICE
)

# --------------------------------------------------
# CHUNKING
# --------------------------------------------------

def chunk_text(
    text,
    max_words=200
):
    """
    Split long text into smaller chunks.
    """

    words = text.split()

    chunks = []

    for i in range(
        0,
        len(words),
        max_words
    ):

        chunk = " ".join(
            words[i:i + max_words]
        )

        chunks.append(
            chunk
        )

    return chunks


# --------------------------------------------------
# SINGLE CHUNK SUMMARY
# --------------------------------------------------

def summarize_chunk(
    chunk
):

    try:

        summary = summarizer(
            chunk,
            max_length=80,
            min_length=20,
            do_sample=False,
            truncation=True
        )

        return summary[0][
            "summary_text"
        ]

    except Exception as e:

        print(
            f"Chunk Error: {e}"
        )

        return ""


# --------------------------------------------------
# DOCUMENT SUMMARY
# --------------------------------------------------

def summarize_document(
    text
):

    if not text:

        return (
            "No text found."
        )

    chunks = chunk_text(
        text,
        max_words=200
    )

    print(
        f"Total Chunks: {len(chunks)}"
    )

    first_pass = []

    for idx, chunk in enumerate(
        chunks
    ):

        print(
            f"Processing Chunk "
            f"{idx+1}/{len(chunks)}"
        )

        summary = summarize_chunk(
            chunk
        )

        if summary:

            first_pass.append(
                summary
            )

    if len(first_pass) == 0:

        return (
            "Unable to generate summary."
        )

    # ------------------------------------------
    # HIERARCHICAL SUMMARY
    # ------------------------------------------

    combined_summary = " ".join(
        first_pass
    )

    print(
        "Generating Final Summary..."
    )

    try:

        final_summary = summarizer(
            combined_summary,
            max_length=200,
            min_length=50,
            do_sample=False,
            truncation=True
        )

        return final_summary[0][
            "summary_text"
        ]

    except Exception as e:

        print(
            f"Final Summary Error: {e}"
        )

        return combined_summary


# --------------------------------------------------
# TEST
# --------------------------------------------------

if __name__ == "__main__":

    sample_text = """
    Artificial Intelligence is transforming
    industries across the world.

    Organizations use machine learning
    to automate repetitive tasks,
    improve decision-making,
    reduce operational costs,
    and create personalized
    customer experiences.

    AI is now being adopted
    across healthcare,
    finance,
    education,
    manufacturing,
    and retail sectors.
    """

    summary = summarize_document(
        sample_text
    )

    print(
        "\nSUMMARY:\n"
    )

    print(
        summary
    )