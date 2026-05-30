from rouge_score import rouge_scorer
import pandas as pd


# --------------------------------------------------
# COMPUTE ROUGE SCORES
# --------------------------------------------------

def compute_rouge(
    reference_summary,
    generated_summary
):
    """
    Compute ROUGE-1, ROUGE-2, ROUGE-L
    and return float values.
    """

    scorer = rouge_scorer.RougeScorer(
        [
            "rouge1",
            "rouge2",
            "rougeL"
        ],
        use_stemmer=True
    )

    scores = scorer.score(
        reference_summary,
        generated_summary
    )

    return {

        "rouge1": float(
            scores["rouge1"].fmeasure
        ),

        "rouge2": float(
            scores["rouge2"].fmeasure
        ),

        "rougeL": float(
            scores["rougeL"].fmeasure
        )
    }


# --------------------------------------------------
# PRINT SCORES
# --------------------------------------------------

def print_rouge_scores(
    scores
):

    print("\n" + "=" * 50)

    print(
        "ROUGE EVALUATION RESULTS"
    )

    print("=" * 50)

    print(
        f"ROUGE-1 : "
        f"{scores['rouge1']:.4f}"
    )

    print(
        f"ROUGE-2 : "
        f"{scores['rouge2']:.4f}"
    )

    print(
        f"ROUGE-L : "
        f"{scores['rougeL']:.4f}"
    )

    print("=" * 50)


# --------------------------------------------------
# SAVE RESULTS
# --------------------------------------------------

def save_results(
    scores,
    output_file="evaluation_results.csv"
):

    df = pd.DataFrame({

        "Metric": [
            "ROUGE-1",
            "ROUGE-2",
            "ROUGE-L"
        ],

        "Score": [

            round(
                scores["rouge1"],
                4
            ),

            round(
                scores["rouge2"],
                4
            ),

            round(
                scores["rougeL"],
                4
            )
        ]
    })

    df.to_csv(
        output_file,
        index=False
    )

    print(
        f"\nResults saved to "
        f"{output_file}"
    )


# --------------------------------------------------
# DASHBOARD HELPER
# --------------------------------------------------

def get_dashboard_metrics(
    scores
):

    return {

        "ROUGE-1":
            round(
                scores["rouge1"],
                4
            ),

        "ROUGE-2":
            round(
                scores["rouge2"],
                4
            ),

        "ROUGE-L":
            round(
                scores["rougeL"],
                4
            )
    }


# --------------------------------------------------
# TEST
# --------------------------------------------------

if __name__ == "__main__":

    reference_summary = """
    Artificial Intelligence is transforming
    industries by automating repetitive
    tasks and improving decision making.
    """

    generated_summary = """
    AI helps industries automate tasks
    and improve business decisions.
    """

    scores = compute_rouge(
        reference_summary,
        generated_summary
    )

    print_rouge_scores(
        scores
    )

    save_results(
        scores
    )

    print(
        "\nReturned Dictionary:"
    )

    print(
        scores
    )

    print(
        "\nType Check:"
    )

    print(
        type(scores["rouge1"])
    )