import os

def calculate_average_plate_size(directories):
    """
    funcaozinha pra pegar a media do tamanho das placas baseado nos dados de treino
    serve pra rodar o vec, nao precisa ser executado pois deixei o vec configurado
    """
    total_width = 0
    total_height = 0
    count = 0

    for input_dir in directories:
        for filename in os.listdir(input_dir):
            if filename.endswith('.txt'):
                txt_path = os.path.join(input_dir, filename)
                with open(txt_path, 'r') as f:
                    lines = f.readlines()
                    corners_line = [line for line in lines if line.startswith('corners')][0]
                    corners = corners_line.split(': ')[1].strip()
                    corners = corners.split(' ')
                    x1, y1 = map(int, corners[0].split(','))
                    x2, y2 = map(int, corners[2].split(','))

                    width = x2 - x1
                    height = y2 - y1

                    total_width += width
                    total_height += height
                    count += 1

    if count == 0:
        return None, None  # serve pra evita div. por 0

    average_width = total_width / count
    average_height = total_height / count

    return average_width, average_height

# VERIFICA OS DADOS FIO
directories = [
    'dados/RodoSol-ALPR/images/cars-br',
    'dados/RodoSol-ALPR/images/cars-me',
    'dados/RodoSol-ALPR/images/motorcycles-br',
    'dados/RodoSol-ALPR/images/motorcycles-me'
]

average_width, average_height = calculate_average_plate_size(directories)

if average_width is not None and average_height is not None:
    print(f"Largura = {average_width}, Altura = {average_height}")
else:
    print("nao tem valor, verifica os caminho man")


# output com 20k de dados (todos) -> Largura = 107.00515, Altura = 57.53145
# arredondando pra 108 e 58