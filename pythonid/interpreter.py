"""
Welcome to The Python Indonesia Edition Official Interpreter.
_____________________________________________________

This is a simple interpreter that allows you to execute Python code,
with some Indonesian keywords.
# _____________________________________________________
_____________________________________________________

This interpreter allows you to execute Python code with some Indonesian keywords.
______________________________________________________

The keywords are:
_____________________________________________________
- cetak: prints
- lihat: input
- jalankan: exec
- fungsi: def
- jika: if
- lain: else
- untuk: for
- sambil: while
- coba: try
- tangkap: except
- benar: True
- salah: False
- dan: and
- atau: or
- bukan: not
- tambah: +
- kurang: -
- kali: *
- bagi: /
- sama: ==
- tidak_sama: !=
- lebih_dari: >
- kurang_dari: <
- lebih_dari_sama: >=
- kurang_dari_sama: <=
- tambah_sama: +=
- kurang_sama: -=
- kali_sama: *=
- bagi_sama: /=
- cetak_sama: pr"))
- lihat_sama: input("))
- fungsi_sama: def
- jika_sama: if
- lain_sama: else
- untuk_sama: for
- sambil_sama: while
- coba_sama: try
- tangkap_sama: except
- benar_sama: True
- salah_sama: False
- dan_sama: and
- atau_sama: or
- bukan_sama: not
- tambah_sama: +
- kurang_sama: -
- kali_sama: *
- bagi_sama: /
- sama_sama: ==
- tidak_sama_sama: !=
- lebih_dari_sama: >=
- kurang_dari_sama: <=
- bukan_dari_sama: !=
______________________________________________________
"""

import sys
import io

class PythonID:
    """
The Python Indonesia Edition Interpreter.
______________________________________________________

This interpreter allows you to execute Python code with some Indonesian keywords.
______________________________________________________

The keywords are:
_____________________________________________________
- cetak: prints
- lihat: input
- jalankan: exec
- fungsi: def
- jika: if
- lain: else
- untuk: for
- sambil: while
- coba: try
- tangkap: except
- benar: True
- salah: False
- dan: and
- atau: or
- bukan: not
- tambah: +
- kurang: -
- kali: *
- bagi: /
- sama: ==
- tidak_sama: !=
- lebih_dari: >
- kurang_dari: <
- lebih_dari_sama: >=
- kurang_dari_sama: <=
- tambah_sama: +=
- kurang_sama: -=
- kali_sama: *=
- bagi_sama: /=
- cetak_sama: pr"))
- lihat_sama: input("))
- fungsi_sama: def
- jika_sama: if
- lain_sama: else
- untuk_sama: for
- sambil_sama: while
- coba_sama: try
- tangkap_sama: except
- benar_sama: True
- salah_sama: False
- dan_sama: and
- atau_sama: or
- bukan_sama: not
- tambah_sama: +
- kurang_sama: -
- kali_sama: *
- bagi_sama: /
- sama_sama: ==
- tidak_sama_sama: !=
- lebih_dari_sama: >=
- kurang_dari_sama: <=
- bukan_dari_sama: !=
______________________________________________________
    """
    
    KEYWORDS = {
        "cetak": "print",
        "lihat": "input",
        "jalankan": "exec",
        "fungsi": "def",
        "jika": "if",
        "lain": "else",
        "untuk": "for",
        "sambil": "while",
        "coba": "try",
        "tangkap": "except",
        "benar": "True",
        "salah": "False",
        "dan": "and",
        "atau": "or",
        "bukan": "not",
        "tambah": "+",
        "kurang": "-",
        "kali": "*",
        "bagi": "/",
        "sama": "==",
        "tidak_sama": "!=",
        "lebih_dari": ">",
        "kurang_dari": "<",
        "lebih_dari_sama": ">=",
        "kurang_dari_sama": "<=",
        "tambah_sama": "+=",
        "kurang_sama": "-=",
        "kali_sama": "*=",
        "bagi_sama": "/=",
    }

    def __init__(self, kode: str = ""):
        # ______________________________________________________
        # Set the name, version, author, description, license, and license_url.
        self.name = "Python Indonesia Edition Interpreter"
        # The name of the interpreter.

        self.version = "1.0.0" # The version of the interpreter.
        # The version of the interpreter.

        self.author = "Python Indonesia" # The author of the interpreter.
        # The author of the interpreter.

        self.description = "Python Indonesia Edition Interpreter"
        # The description of the interpreter.

        self.license = "MIT"
        # The license of the interpreter.

        self.license_url = "https://opensource.org/licenses/MIT"
        # The license URL of the interpreter.
        # ______________________________________________________
        
        self.kode = kode
        
        self.output = ""
        
        if kode:
            self.execute(kode)

    def __str__(self) -> str:
        return self.output

    def translate_keywords(self, code: str) -> str:
        for indo, eng in self.KEYWORDS.items():
            code = code.replace(indo, eng)
        
        return code

    def execute(self, code: str) -> str:
        translated = self.translate_keywords(code)
        
        self.output = self._run(translated)
        
        return self.output

    def _run(self, code: str) -> str:
        old_stdout = sys.stdout
        
        buffer = io.StringIO()
        
        sys.stdout = buffer
        
        try:
            exec(code, {})
        
        except Exception as e:
            print(f"[ERROR]: {e}")
        
        sys.stdout = old_stdout
        
        return buffer.getvalue()
