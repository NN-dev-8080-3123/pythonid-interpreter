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
git clone https://github.com/NN-dev-8080-3123/pythonid-interpreter.git
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

Copyright (c) 2025 NN-dev-8080-3123 / NN (Nadi Nataprawira).

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
