#4
from city_functions import city_country

def test_city_country():
    result = city_country('santiago', 'chile')
    assert result == "Santiago, Chile"
    print(result)
