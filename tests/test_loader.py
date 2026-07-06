from src.data_loader import SCADADataLoader

def test_loader():
    loader = SCADADataLoader("configs/config.yaml")
    assert loader is not None