from pytest import mark

@mark.api
def test_prueba01():
    assert  True

@mark.data
def test_prueba02():
    assert True

@mark.ui
@mark.parametrize('nombre', ['Juan', 'Luis', 'Restitutivo'])
def test_prueba03(nombre):
    print("Valor parametro: " + nombre)
    assert nombre in ['Juan', 'Luis', 'Restitutivo', 'sanchez']