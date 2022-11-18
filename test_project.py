from inv_utils import verify_date, verify_category, verify_status


def test_verify_date():
    assert verify_date('3/45/2000') == ''


def test_verify_status():
    assert verify_status(1) == 'Deployed and Working'
    assert verify_status(2) == 'Not Deplopyed But Working'
    assert verify_status(3) == 'Not Working'
    assert verify_status(4) == 'Under Repair'
    assert verify_status(5) == ''


def test_verify_category():
    assert verify_category(1) == 'CPU'
    assert verify_category(2) == 'Monitor'
    assert verify_category(3) == 'Peripheral'
    assert verify_category(4) == 'Laptop'
    assert verify_category(5) == ''
