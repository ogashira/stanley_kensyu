import pytest
from src.date_manage import DateManage


@pytest.fixture
def get_date_manage():
    date_manage = DateManage()
    return date_manage

def test_get_last_month_end(get_date_manage):
    result = get_date_manage.get_last_month_end('202601')
    assert result == '20251231'
    result = get_date_manage.get_last_month_end('202403')
    assert result == '20240229'
    result = get_date_manage.get_last_month_end('202603')
    assert result == '20260228'

def test_get_last_month(get_date_manage):
    result = get_date_manage.get_last_month('202602')
    assert result == '202601'
    result = get_date_manage.get_last_month('202601')
    assert result =='202512'

def test_get_this_month_end(get_date_manage):
    result = get_date_manage.get_this_month_end('202602')
    assert result == '20260228'
    result = get_date_manage.get_this_month_end('202402')
    assert result == '20240229'
    result = get_date_manage.get_this_month_end('202608')
    assert result == '20260831'
