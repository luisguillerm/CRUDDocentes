import json
from docentes import agregar, buscar, eliminar, a_json, a_xml, a_yaml

# Datos ficticios de ejemplo para las pruebas
DATOS = [{"nombre": "Memo", "materia": "Ciberseguridad", "salon": "Hell"}]

def test_agregar():
    # Agregar un docente a una lista vacía debe dejar 1 elemento
    l = []
    agregar(l, "Memo", "Ciberseguridad", "Hell")
    assert len(l) == 1

def test_buscar():
    # Buscar "mem" debe encontrar a Memo
    assert len(buscar(DATOS, "mem")) == 1

def test_eliminar():
    # Eliminar a Memo debe regresar True y dejar la lista vacía
    l = list(DATOS)
    assert eliminar(l, "Memo") and l == []

def test_json():
    # El JSON generado debe ser igual a los datos originales
    assert json.loads(a_json(DATOS)) == DATOS

def test_xml():
    # El XML debe contener la etiqueta del nombre
    assert "<nombre>Memo</nombre>" in a_xml(DATOS)

def test_yaml():
    # El YAML debe contener la línea del nombre
    assert "nombre: Memo" in a_yaml(DATOS)
