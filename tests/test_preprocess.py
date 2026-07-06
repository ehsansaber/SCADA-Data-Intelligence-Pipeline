import pandas as pd
import pytest
from src.preprocess import SCADAPreprocessor

@pytest.fixture
def sample_config():
    return {
        'turbine': {'rated_power': 7},
        'preprocessing': {'window_size': 3, 'z_threshold': 2.0}
    }

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'WindSpeed': [10.0, 10.2, 10.1],
        'RotorSpeed': [15.0, 16.0, 15.5],
        'GeneratorSpeed': [1500.0, 1510.0, 1505.0],
        'PitchDeg': [5.0, -1.0, 95.0],  
        'GeneratorTemperature': [60.0, 61.0, 60.5],
        'offsetWindDirection': [0.0, 0.0, 0.0],
        'SpeiseSpannung': [400.0, 400.0, 400.0],
        'MaxWindHeute': [12.0, 12.0, 12.0],
        'PowerOutput': [-1.0, 9.5, 5.5],
        'StatusAnlage': [1, 1, 1]
    })

def test_physical_constraints(sample_data, sample_config):
    processor = SCADAPreprocessor(sample_config)
    processed_df = processor.apply_physical_constraints(sample_data)
    
    assert (processed_df['PowerOutput'] >= 0).all()
    assert (processed_df['PowerOutput'] <= 2000).all()
    assert (processed_df['PitchDeg'] >= 0).all()
    assert (processed_df['PitchDeg'] <= 90).all()

def test_anomaly_detection(sample_data, sample_config):
    processor = SCADAPreprocessor(sample_config)
    sample_data.loc[0, 'PowerOutput'] = 3.5
    sample_data.loc[0, 'GeneratorSpeed'] = 0
    
    processed_df = processor.detect_anomalies(sample_data)
    assert processed_df.loc[0, 'is_anomaly'] == True