#!/usr/bin/env python3
"""Hello world

Testando comentário do python.

Como usar:

Tenha a variável LANG configurada.
	
	export LANG=pt_BR

Execução:
	
	python3 hello.py
	ou
	./hello.py
"""

__version__ = "0.0.1"
__author__ = "Alysson"
__license__ = "Unlicense"

# Dunder -> __

import os



current_language = os.getenv("LANG_TEST", "en_US")[:5]

msg = "Hello babyyyyy!"

if current_language == "pt_BR":
    msg = "Olá bebeeeeee!"
elif current_language == "it_IT":
    msg = "Ciao, bebenito!"
elif current_language == "es_SP":
    msg = "Hola, bebeee!"


print(msg)
