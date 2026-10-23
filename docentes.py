import json
from docentes import agregar, buscar, eliminar, a_json, a_xml, a_yaml

DATOS = [{"nombre": "Carlos", "materia": "Programación", "salon": "E2-205"}]

def test_agregar():
    l = []
    agregar(l, "Carlos", "Programación", "E2-205")
    assert len(l) == 1

def test_buscar():
    assert len(buscar(DATOS, "car")) == 1      # texto que esté dentro del nombre

def test_eliminar():
    l = list(DATOS)
    assert eliminar(l, "Carlos") and l == []

def test_json():
    assert json.loads(a_json(DATOS)) == DATOS

def test_xml():
    assert "<nombre>Carlos</nombre>" in a_xml(DATOS)

def test_yaml():
    assert "nombre: Carlos" in a_yaml(DATOS)
