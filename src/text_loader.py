def extract_text_file(file_path):
    """
    Extract text from txt file.
    """

    try:

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as f:

            text = f.read()

        return text

    except Exception as e:

        print(
            f"Text Extraction Error: {e}"
        )

        return ""


if __name__ == "__main__":

    file_path = "data/sample.txt"

    text = extract_text_file(
        file_path
    )

    print(
        f"Words: {len(text.split())}"
    )

    print("\nPreview:\n")

    print(
        text[:1000]
    )