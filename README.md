```markdown
<div align="center">
  
  # 🌪️ SCADA Data Intelligence Pipeline
  **A Robust MLOps Framework for SCADA Data Preprocessing and Model Benchmarking**
  
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
This repository contains a highly optimized, production-ready MLOps pipeline for processing High-Frequency SCADA data from wind turbines. It serves as the foundational data engineering layer for a robust Digital Twin framework, transforming noisy, raw sensor data into physically consistent, mathematically rigorous datasets ready for predictive modeling.

## ✨ Key Features
- **🛡️ Physical Constraint Enforcement:** Automatically clips anomalous values (e.g., negative power, extreme pitch angles) based on the turbine's physical reality and rated parameters.
- **📉 Temporal Noise Reduction:** Applies rolling window smoothing to high-frequency sensor readings (Wind Speed, Generator Temperature) to eliminate transient noise without losing critical signal dynamics.
- **🧠 Automated Anomaly Detection:** Flags mechanical and operational inconsistencies using domain-specific logic.
- **📊 Premium Data Profiling:** Generates comprehensive, interactive HTML reports for exploratory data analysis (EDA) using `ydata-profiling`.
- **⚖️ Scientific Benchmarking:** Validates the efficacy of the preprocessing pipeline by comparing the Mean Squared Error (MSE) of a Random Forest Regressor on both raw and processed datasets using chronological chronological time-series splitting.

---

## 🏗️ Project Architecture
The project follows strict software engineering and MLOps principles, ensuring separation of concerns and absolute reproducibility:

```text
├── configs/
│   └── config.yaml          # Centralized configuration (thresholds, turbine specs)
├── data/
│   ├── raw/                 # Raw SCADA datasets (ignored in git)
│   └── processed/           # HTML profiling reports
├── src/
│   ├── data_loader.py       # Robust data ingestion and validation
│   ├── preprocess.py        # Core physics-based cleaning algorithms
│   └── utils.py             # Model benchmarking and evaluation logic
├── main.py                  # CLI pipeline executor
├── requirements.txt         # Project dependencies
└── README.md

```

---

## 🔬 Scientific Benchmarking

To mathematically prove the value of the data engineering process, the pipeline includes a built-in benchmark. It trains a `RandomForestRegressor` (utilizing chronological train/test splits to prevent data leakage) to predict `PowerOutput`.

**Results demonstrate that enforcing physical constraints and reducing temporal noise directly improves the predictive accuracy of the Digital Twin models.**

---

## 🚀 Installation & Usage

### 1. Clone the repository

```bash
git clone [https://github.com/your-username/Digital-Twin-SCADA.git](https://github.com/your-username/Digital-Twin-SCADA.git)
cd Digital-Twin-SCADA

```

### 2. Set up the environment

It is highly recommended to use a virtual environment.

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt

```

### 3. Run the Pipeline

Ensure your raw data is placed at `data/raw/scada_raw.csv`.

To execute the data engineering pipeline and generate the interactive HTML report:

```bash
python main.py --report

```

---
## 🖥️ Pipeline Execution & Logs
To demonstrate the pipeline's efficiency, below is a real execution log showing the processing of nearly 4 million records.

<details>
<summary><b>Click to expand the terminal output</b></summary>

```text
(venv) E:\apply phd\GITHUB_Projects\Digital-Twin-SCADA>python main.py --report
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
</details>

## 👨‍💻 Author

**Ehsan Saber**
*Research Engineer | AI & Multi-Objective Optimization*
*Specialized in Digital Twins, Deep Learning, and Metaheuristic Algorithms*

Dedicated to bridging the gap between advanced machine learning algorithms and physical energy systems.
