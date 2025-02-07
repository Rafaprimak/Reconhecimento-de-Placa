import subprocess
import os

# Defina os caminhos completos dos scripts
main_script = 'c:/Users/rafae/OneDrive/Área de Trabalho/detector de placas/automatic-number-plate-recognition-python-yolov8-main/main.py'
add_missing_data_script = 'c:/Users/rafae/OneDrive/Área de Trabalho/detector de placas/automatic-number-plate-recognition-python-yolov8-main/add_missing_data.py'
util_script = 'c:/Users/rafae/OneDrive/Área de Trabalho/detector de placas/automatic-number-plate-recognition-python-yolov8-main/util.py'
tratamento_script = 'c:/Users/rafae/OneDrive/Área de Trabalho/detector de placas/automatic-number-plate-recognition-python-yolov8-main/tratamento.py'
visualize_script = 'c:/Users/rafae/OneDrive/Área de Trabalho/detector de placas/automatic-number-plate-recognition-python-yolov8-main/visualize.py'

# Execute o main.py
subprocess.run(['python', main_script])

# Execute o add_missing_data.py
subprocess.run(['python', add_missing_data_script])

# Execute o util.py
subprocess.run(['python', util_script])

# Variáveis para rastrear quais scripts foram executados
tratamento_executado = False
visualize_executado = False

# Escolha entre tratamento.py e visualize.py
while True:
    if not tratamento_executado and not visualize_executado:
        choice = input("Digite '1' para executar o Tratamento dos dados em JSON, '2' para executar o Visualizador da I.A ou '0' para sair: ")
    elif not tratamento_executado:
        choice = input("Digite '1' para executar o Tratamento dos dados em JSON ou '0' para sair: ")
    elif not visualize_executado:
        choice = input("Digite '2' para executar o Visualizador da I.A ou '0' para sair: ")

    if choice == '1' and not tratamento_executado:
        subprocess.run(['python', tratamento_script])
        tratamento_executado = True
    elif choice == '2' and not visualize_executado:
        subprocess.run(['python', visualize_script])
        visualize_executado = True
    elif choice == '0':
        print("Saindo...")
        break
    else:
        print("Escolha inválida ou script já executado. Tente novamente.")