from model_utils import classify_risk


def test_high_risk():
    assert classify_risk(80) == "High"


def test_medium_risk():
    assert classify_risk(50) == "Medium"


def test_low_risk():
    assert classify_risk(20) == "Low"