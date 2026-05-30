from datasets import load_dataset
from src.summarizer import summarize_document
from src.evaluate import compute_rouge
import pandas as pd

# --------------------------------------------------
# CONFIG
# --------------------------------------------------

SAMPLES = 20
# Increase to 20 after testing

# --------------------------------------------------
# LOAD DATASET
# --------------------------------------------------

print(
    "\nLoading CNN/DailyMail Dataset..."
)

dataset = load_dataset(
    "cnn_dailymail",
    "3.0.0"
)

test_set = dataset["test"]

print(
    f"Dataset Loaded. "
    f"Test Samples: {len(test_set)}"
)

# --------------------------------------------------
# STORAGE
# --------------------------------------------------

rouge1_scores = []
rouge2_scores = []
rougeL_scores = []

results = []

# --------------------------------------------------
# BENCHMARK LOOP
# --------------------------------------------------

for i in range(SAMPLES):

    print(
        f"\nProcessing "
        f"{i+1}/{SAMPLES}"
    )

    article = test_set[i][
        "article"
    ]

    reference_summary = test_set[i][
        "highlights"
    ]

    generated_summary = summarize_document(
        article
    )

    scores = compute_rouge(
        reference_summary,
        generated_summary
    )

    rouge1_scores.append(
        scores["rouge1"]
    )

    rouge2_scores.append(
        scores["rouge2"]
    )

    rougeL_scores.append(
        scores["rougeL"]
    )

    results.append({

        "Sample":
            i + 1,

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
    })

    print(
        f"ROUGE-1: {scores['rouge1']:.4f}"
    )

    print(
        f"ROUGE-2: {scores['rouge2']:.4f}"
    )

    print(
        f"ROUGE-L: {scores['rougeL']:.4f}"
    )

# --------------------------------------------------
# FINAL AVERAGES
# --------------------------------------------------

avg_rouge1 = round(
    sum(rouge1_scores)
    / len(rouge1_scores),
    4
)

avg_rouge2 = round(
    sum(rouge2_scores)
    / len(rouge2_scores),
    4
)

avg_rougeL = round(
    sum(rougeL_scores)
    / len(rougeL_scores),
    4
)

# --------------------------------------------------
# PRINT RESULTS
# --------------------------------------------------

print("\n" + "=" * 50)

print(
    "FINAL BENCHMARK RESULTS"
)

print("=" * 50)

print(
    f"Average ROUGE-1: "
    f"{avg_rouge1}"
)

print(
    f"Average ROUGE-2: "
    f"{avg_rouge2}"
)

print(
    f"Average ROUGE-L: "
    f"{avg_rougeL}"
)

print("=" * 50)

# --------------------------------------------------
# SAVE CSV
# --------------------------------------------------

df = pd.DataFrame(
    results
)

df.loc[
    len(df)
] = [

    "AVERAGE",

    avg_rouge1,

    avg_rouge2,

    avg_rougeL
]

output_file = (
    "benchmark_results.csv"
)

df.to_csv(
    output_file,
    index=False
)

print(
    f"\nResults saved to "
    f"{output_file}"
)