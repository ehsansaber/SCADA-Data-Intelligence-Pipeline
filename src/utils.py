import logging
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

logger = logging.getLogger(__name__)

def benchmark_data_quality(df_raw, df_processed):
    """
    Compares model performance (MSE) between raw and processed data.
    Uses chronological Train/Test split to prevent data leakage in time-series data.
    """
    features = ['WindSpeed', 'RotorSpeed', 'GeneratorSpeed', 'PitchDeg']
    target = 'PowerOutput'
    
    # Ensure no NaNs remain before training
    df_raw_clean = df_raw.ffill().bfill()
    
    logger.info("Starting benchmark: Training Random Forest with chronological split...")
    
    model = RandomForestRegressor(n_estimators=50, random_state=42, n_jobs=-1)
    
    # --- Function for splitting and evaluating ---
    def evaluate_dataset(df, dataset_name):
        X = df[features]
        y = df[target]
        
        # shuffle=False is CRITICAL for time-series data (SCADA)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
        
        logger.info(f"Training on {dataset_name} data (Train: {len(X_train)}, Test: {len(X_test)})...")
        model.fit(X_train, y_train)
        
        # Evaluate ONLY on the unseen test set
        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        return mse

    # 1. Performance on Raw Data
    mse_raw = evaluate_dataset(df_raw_clean, "Raw")
    
    # 2. Performance on Processed Data
    mse_proc = evaluate_dataset(df_processed, "Processed")
    
    logger.info("Benchmark Results (Evaluated on Unseen Test Set):")
    logger.info(f" - MSE on Raw Data: {mse_raw:.4f}")
    logger.info(f" - MSE on Processed Data: {mse_proc:.4f}")
    
    if mse_raw > 0:
        improvement = ((mse_raw - mse_proc) / mse_raw) * 100
        logger.info(f" - Performance Improvement: {improvement:.2f}%")
    
    return mse_raw, mse_proc