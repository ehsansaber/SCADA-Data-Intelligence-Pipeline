import yaml
import logging
import argparse
from ydata_profiling import ProfileReport
from src.data_loader import SCADADataLoader
from src.preprocess import SCADAPreprocessor

# Configure logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def run_pipeline(config_path):
    # 1. Load configuration
    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
        logger.info(f"Configuration loaded from {config_path}")
    except Exception as e:
        logger.error(f"Failed to load configuration: {e}")
        return None
    
    logger.info("Pipeline started.")
    
    # 2. Load data
    loader = SCADADataLoader(config_path)
    df_raw = loader.load_data()

    # 3. Preprocess
    preprocessor = SCADAPreprocessor(config)
    df = preprocessor.handle_missing_values(df_raw.copy())
    df = preprocessor.apply_physical_constraints(df)
    df = preprocessor.handle_temporal_noise(df)
    df = preprocessor.detect_anomalies(df)

    # 4. Benchmark
    from src.utils import benchmark_data_quality
    benchmark_data_quality(df_raw, df)
    
    logger.info("Pipeline completed successfully.")
    return df

def generate_report(df, output_path="data/processed/data_report.html"):
    """
    Generates a highly customized and visually appealing profiling report.
    """
    logger.info("Generating premium profiling report...")
    
    profile = ProfileReport(
        df,
        title="SCADA Condition Monitoring - Data Profile",
        dataset={
            "description": "Exploratory Data Analysis for Wind Turbine Digital Twin Framework.",
            "author": "Ehsan Saber",
            "copyright": "2026",
        },
        html={
            "style": {
                "theme": "flatly",
                "primary_color": "#2c3e50"
            }
        },
        correlations={
            "pearson": {"calculate": True},
            "spearman": {"calculate": False},
        }
    )
    
    profile.to_file(output_path)
    logger.info(f"Beautiful report generated: {output_path}")

if __name__ == "__main__":
    # Command-line interface setup
    parser = argparse.ArgumentParser(description="SCADA Data Engineering Pipeline")
    parser.add_argument("--config", default="configs/config.yaml", help="Path to config file")
    parser.add_argument("--report", action="store_true", help="Generate profiling report")
    args = parser.parse_args()
    
    # Execution
    processed_df = run_pipeline(args.config)
    
    if processed_df is not None and args.report:
        generate_report(processed_df)