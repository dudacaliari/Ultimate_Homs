# run_task.py
import os
import django

# Configura o ambiente Django para permitir a importação correta
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HOMS.settings')  
django.setup()

# Importa a tarefa específica para execução
from homsapp.tasks import geocode_imoveis  

# Executa a tarefa manualmente
geocode_imoveis()
