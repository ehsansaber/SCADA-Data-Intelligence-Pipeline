import pandas as pd
import numpy as np
import logging

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class SCADAPreprocessor:
    def __init__(self, config):
        self.config = config

    def apply_physical_constraints(self, df):
        """
        Enforce physical reality and log the number of clipped records.
        """
        rated_power = self.config['turbine']['rated_power']
        
        # Track initial state to report modifications
        initial_power_out = df['PowerOutput'].copy()
        
        df['PowerOutput'] = df['PowerOutput'].clip(lower=0, upper=rated_power)
        df['GeneratorSpeed'] = df['GeneratorSpeed'].clip(lower=0)
        df['RotorSpeed'] = df['RotorSpeed'].clip(lower=0)
        df['PitchDeg'] = df['PitchDeg'].clip(lower=0, upper=90)
        
        # Calculate modifications
        clipped_count = (df['PowerOutput'] != initial_power_out).sum()
        logger.info(f"Physical constraints applied. {clipped_count} records clipped for PowerOutput.")
        
        return df

    def handle_temporal_noise(self, df):
        """
        Smooth out high-frequency sensor noise and log columns processed.
        """
        window = self.config['preprocessing']['window_size']
        cols_to_smooth = ['WindSpeed', 'GeneratorTemperature', 'PowerOutput']
        
        for col in cols_to_smooth:
            df[f'{col}_smoothed'] = df[col].rolling(window=window, center=True).mean()
        
        logger.info(f"Temporal smoothing applied with window size: {window} for columns: {cols_to_smooth}")
        return df

    def detect_anomalies(self, df):
        """
        Flag potential sensor failures and log anomaly statistics.
        """
        # Identifying anomalies based on physical domain logic
        df['is_anomaly'] = (df['PowerOutput'] > 0) & (df['GeneratorSpeed'] < 10)
        
        anomaly_count = df['is_anomaly'].sum()
        if anomaly_count > 0:
            logger.warning(f"Anomaly detection: {anomaly_count} anomalous records identified.")
        else:
            logger.info("Anomaly detection: No anomalies found.")
        
        return df
    
    def handle_missing_values(self, df):
        """
        Use temporal interpolation to fill gaps for numeric columns only, respecting physical continuity.
        """
        # Select only numeric columns to avoid Pandas FutureWarning
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        
        # Interpolate missing values based on time/index for numeric data
        df[numeric_cols] = df[numeric_cols].interpolate(method='linear', limit_direction='both')
        
        # Fill remaining NaNs at the edges with forward/backward fill
        df = df.ffill().bfill()
        
        logger.info("Missing values handled via linear interpolation.")
        return df