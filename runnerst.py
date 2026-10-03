#Para rodar sites de códigos.py feitos :)
import sys
from streamlit.web import cli as stclib

sys.argv = ["Streamlit", "run", "Livros.py"]
sys.exit(stclib.main())
#coloque o nome do seu arquivo.py