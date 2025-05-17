# pythonid-interpreter
This is The Public PYthon-InDonesia Official GitHub Repository Created by : NN (Nadi Nataprawira).

# PythonID Interpreter

Interpreter kecil yang menerjemahkan kata kunci Bahasa Indonesia ke Python.

## Fitur

- `cetak`, `lihat`, `jika`, `untuk`, dsb.
- Menangkap output `print()` via `io.StringIO()`
- Unit tests dengan `pytest`
- CI otomatis via GitHub Actions

## Instalasi

```bash
git clone https://github.com/username/pythonid-interpreter.git
cd pythonid-interpreter
pip install -e .
```

## Penggunaan
```python
from pythonid.interpreter import PythonID

kode = '''
cetak("Halo, dunia!")
nama = lihat("Nama kamu? ")
cetak("Selamat datang,", nama)
'''
interp = PythonID(kode)
print(interp)  # output yang di-cetak di kode
```

## Contoh di terminal:
```bash
python examples/demo.py
```

## Testing
```bash
pytest
```

## Lisensi
```text
MIT © 2025
```

### 2. LICENSE

```text
MIT License

Copyright (c) 2025 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy...
[standard MIT text]
```
