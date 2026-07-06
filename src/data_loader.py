import pandas as pd
import yaml
import logging
import os

logger = logging.getLogger(__name__)

class SCADADataLoader:
    def __init__(self, config_path):
        with open(config_path, 'r') as file:
            self.config = yaml.safe_load(file)

    def load_data(self):
        """
        Loads SCADA data from a CSV file specified in the configuration.
        """
        raw_path = self.config['data']['raw_path']
        
        if not os.path.exists(raw_path):
            logger.error(f"File not found: {raw_path}")
            raise FileNotFoundError(f"Ensure the file exists at {raw_path}")
        
        try:
            logger.info(f"Loading data from {raw_path}...")
            df = pd.read_csv(raw_path)
            
            # Basic validation to ensure required columns exist
            required_cols = ['WindSpeed', 'PowerOutput', 'GeneratorSpeed', 'RotorSpeed', 'PitchDeg']
            if not all(col in df.columns for col in required_cols):
                missing = [c for c in required_cols if c not in df.columns]
                logger.warning(f"Warning: Missing columns in dataset: {missing}")
            
            return df
            
        except Exception as e:
            logger.error(f"Error loading CSV file: {e}")
            raise