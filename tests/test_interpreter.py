from pythonid.interpreter import PythonID

def test_cetak_saja():
    interp = PythonID('cetak("abc")')
    
    assert interp.output.strip() == "abc"

def test_variabel_dan_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda prompt="": "Bot")
    
    code = '''
a = lihat("Siapa? ")

cetak(a)
'''
    
    interp = PythonID(code)
    
    assert interp.output.strip() == "Bot"

def test_syntax_error():
    interp = PythonID('cetak("hello"')  # missing parenthesis.
    
    assert "[ERROR]" in interp.output
