# 📄 AI PDF & Meeting Notes Summarizer

An end-to-end NLP application that automatically summarizes long PDFs, meeting notes, research papers, and text documents using **BART (Bidirectional and Auto-Regressive Transformers)** from Hugging Face Transformers.

The project provides a complete workflow including document ingestion, text extraction, hierarchical summarization, FastAPI backend services, Streamlit dashboard, document analytics, and ROUGE-based evaluation.

---

## 🚀 Features

* 📄 PDF Document Summarization
* 📝 TXT / Meeting Notes Summarization
* 🤖 BART-based Abstractive Summarization
* 🔄 Hierarchical Summarization Pipeline
* 🌐 FastAPI REST API
* 📊 Streamlit Dashboard
* ☁️ Word Cloud Visualization
* 📈 Document Analytics
* 📏 Compression Ratio Calculation
* 🧪 ROUGE-1, ROUGE-2, ROUGE-L Evaluation
* ⬇️ Download Generated Summary

---

## 🏗️ Project Architecture

```text
PDF / TXT Document
          │
          ▼
   Text Extraction
          │
          ▼
     Chunking
          │
          ▼
  BART Summarization
          │
          ▼
 Hierarchical Summary
          │
          ▼
     FastAPI API
          │
          ▼
  Streamlit Dashboard
```

---

## 🛠️ Tech Stack

### Programming Language

* Python

### NLP & Deep Learning

* Hugging Face Transformers
* BART Large CNN
* PyTorch

### Backend

* FastAPI
* Uvicorn

### Frontend

* Streamlit

### Evaluation

* ROUGE Score

### Data Processing

* PyPDF2
* Pandas

### Visualization

* Matplotlib
* WordCloud

---

## 📂 Project Structure

```text
ai-document-summarizer/
│
├── app/
│   └── streamlit_app.py
│
├── src/
│   ├── __init__.py
│   ├── api.py
│   ├── benchmark.py
│   ├── evaluate.py
│   ├── pdf_loader.py
│   ├── summarizer.py
│   ├── text_loader.py
│   └── test_pipeline.py
│
├── data/
├── models/
│
├── requirements.txt
├── README.md
└── benchmark_results.csv
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/ai-document-summarizer.git

cd ai-document-summarizer
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running FastAPI Backend

```bash
uvicorn src.api:app --reload
```

API Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## ▶️ Running Streamlit Dashboard

```bash
streamlit run app/streamlit_app.py
```

---

## 📊 Evaluation

The project uses ROUGE metrics to evaluate summarization quality:

* ROUGE-1
* ROUGE-2
* ROUGE-L

Run benchmark:

```bash
python -m src.benchmark
```

Run evaluation:

```bash
python -m src.evaluate
```

---

## 📈 Benchmark Results

CNN/DailyMail Benchmark Results:

| Metric  | Score  |
| ------- | ------ |
| ROUGE-1 | 0.3138 |
| ROUGE-2 | 0.1069 |
| ROUGE-L | 0.2354 |

---

## 📸 Dashboard Features

* Document Upload
* PDF Page Count
* Word Count Analytics
* Summary Generation
* Compression Ratio
* Processing Time
* Word Cloud Visualization
* Download Summary

---

## 🎯 Resume Highlights

* Built an end-to-end AI document summarization system using BART and Hugging Face Transformers.
* Developed a FastAPI backend and Streamlit dashboard for document analytics and interactive summarization.
* Implemented hierarchical summarization and ROUGE-based evaluation using the CNN/DailyMail benchmark.
* Supported PDF and TXT document ingestion with automated summary generation.


## 🔮 Future Improvements

* PEGASUS-based Summarization
* GPU Optimization
* Docker Deployment
* Multi-language Support
* RAG-based Summarization
* Cloud Deployment (AWS / Azure)


