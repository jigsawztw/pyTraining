from fixture.application import Application
import pytest
__author__ = "Iv.Osipov"

@pytest.fixture( scope = "session" )
def app(request):
    fixture = Application()  # Создаем фикстуру
    request.addfinalizer(fixture.destroy)  # задаем ей финализацию в виде метода destroy()
    return fixture
