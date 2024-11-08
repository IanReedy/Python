#6
from city_functions2 import city_country

def test_city_country():
    result = city_country('santiago', 'chile')
    assert result == "Santiago, Chile"
    print(result)

def test_city_country_population():
    result = city_country('santiago', 'chile', 5000000)
    assert result == "Santiago, Chile – population 5000000"
    print(result)

test_city_country()
test_city_country_population()
