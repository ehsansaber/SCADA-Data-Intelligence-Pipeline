<div align="center">

# 🌪️ SCADA Data Intelligence Pipeline

**A Robust Framework for SCADA Data Preprocessing, Anomaly Detection, and Model Benchmarking**

<br>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="scikit-learn">
  <img src="https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/Status-Active-success.svg?style=for-the-badge" alt="Status">
</p>

</div>

---

## 📖 Table of Contents
<details>
  <summary>Click to expand</summary>

  - [Overview](#-overview)
  - [Key Features](#-key-features)
  - [Project Architecture](#-project-architecture)
  - [Scientific Benchmarking](#-scientific-benchmarking)
  - [Installation & Usage](#-installation--usage)
  - [Author](#-author)
</details>

---

## 🎯 Overview
This repository contains a highly optimized, modular pipeline for processing high-frequency SCADA sensor data from wind turbines. It serves as the foundational data engineering layer, transforming noisy, raw data into physically consistent, mathematically rigorous datasets ready for predictive modeling.

## ✨ Key Features
- **🛡️ Physical Constraint Enforcement:** Automatically clips anomalous values based on turbine operational limits.
- **📉 Temporal Noise Reduction:** Rolling window smoothing to reduce transient noise while preserving signal dynamics.
- **🧠 Automated Anomaly Detection:** Domain-specific logic for identifying mechanical inconsistencies.
- **📊 Premium Data Profiling:** Generation of interactive EDA reports via `ydata-profiling`.
- **⚖️ Scientific Benchmarking:** Validates pipeline efficacy by comparing ML model performance (MSE) on raw vs. processed data.

---

## 🏗️ Project Architecture
```text
├── configs/
│   └── config.yaml          # Centralized configuration
├── data/
│   ├── raw/                 # Raw datasets (ignored)
│   └── processed/           # HTML profiling reports
├── src/
│   ├── data_loader.py       # Ingestion and validation
│   ├── preprocess.py        # Physics-based cleaning algorithms
│   └── utils.py             # Benchmarking and evaluation logic
├── main.py                  # CLI pipeline executor
└── requirements.txt         # Dependencies

```

---

## 🔬 Scientific Benchmarking

The pipeline trains a `RandomForestRegressor` (using chronological time-series splitting) to predict `PowerOutput`. Results prove that preprocessing directly improves predictive accuracy.

---

## 🚀 Installation & Usage

### 1. Clone the repository

```bash
git clone [https://github.com/ehsansaber/SCADA-Data-Intelligence-Pipeline.git](https://github.com/ehsansaber/SCADA-Data-Intelligence-Pipeline.git)
cd SCADA-Data-Intelligence-Pipeline

```

### 2. Set up the environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

```

### 3. Run the Pipeline

```bash
python main.py --report

```

---

## 🖥️ Pipeline Execution Log

```text
2026-07-06 03:36:24,188 - INFO - Configuration loaded from configs/config.yaml
2026-07-06 03:36:24,188 - INFO - Pipeline started.
2026-07-06 03:36:24,194 - INFO - Loading data from data/raw/scada_raw.csv...
2026-07-06 03:36:30,143 - INFO - Missing values handled via linear interpolation.
2026-07-06 03:36:30,342 - INFO - Physical constraints applied. 131218 records clipped for PowerOutput.
2026-07-06 03:36:30,655 - INFO - Temporal smoothing applied with window size: 5 for columns: ['WindSpeed', 'GeneratorTemperature', 'PowerOutput']
2026-07-06 03:36:30,669 - WARNING - Anomaly detection: 10235 anomalous records identified.
2026-07-06 03:36:32,193 - INFO - Starting benchmark: Training Random Forest with chronological split...
2026-07-06 03:36:32,327 - INFO - Training on Raw data (Train: 3177278, Test: 794320)...
2026-07-06 03:37:23,995 - INFO - Training on Processed data (Train: 3177278, Test: 794320)...
2026-07-06 03:38:09,209 - INFO - Benchmark Results (Evaluated on Unseen Test Set):
2026-07-06 03:38:09,209 - INFO -  - MSE on Raw Data: 0.0020
2026-07-06 03:38:09,209 - INFO -  - MSE on Processed Data: 0.0020
2026-07-06 03:38:09,209 - INFO -  - Performance Improvement: 0.43%
2026-07-06 03:38:09,383 - INFO - Pipeline completed successfully.
2026-07-06 03:38:09,463 - INFO - Generating premium profiling report...
100%|████████████████████████████████████| 15/15 [00:33<00:00,  2.21s/it]
Summarize dataset: 100%|███████████████| 195/195 [03:17<00:00,  1.01s/it]
2026-07-06 03:41:33,945 - INFO - Beautiful report generated: data/processed/data_report.html

```

## 👨‍💻 Author

**Ehsan Saber**

*Research Engineer | AI & Multi-Objective Optimization*
*Specialized in Digital Twins, Deep Learning, and Metaheuristic Algorithms*
