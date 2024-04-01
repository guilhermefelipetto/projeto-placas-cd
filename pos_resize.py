"""script para redimensionar as imagens do dateset"""

from PIL import Image
from pathlib import Path

def resize_img(dir, largura, altura):
    with open(dir, 'r') as path:
        rows = path.readlines()
    
    for row in rows:
        img_path = row.split()[0].replace('\\', '/')
        abs_img_path = Path(img_path)
    
    try:
        with Image.open(abs_img_path) as img:
            img_resized = img.resize((largura, altura))

            new_path = abs_img_path.parent / f'resized_{abs_img_path.name}'
            img_resized.save(new_path)

            print(f'img_resized: {new_path}')

    except FileNotFoundError:
        print('bro, cade as imagens')
        
    except Exception as e:
        print(f'Erro: {e}')

largura = 320
altura = 180

resize_img('positives.txt', largura=largura, altura=altura)
