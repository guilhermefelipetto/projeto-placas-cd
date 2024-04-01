import os
from video_to_image import frame

def create_negatives_list(negatives_dir, output_file):
    """
    essa funcao medonha pega um mp4 e pega cada frame e transofrma num png
    serve pra converte os videos em imagens negativas pro negatives.txt (ta literalmente escrito no cod.)
    """
    with open(output_file, 'w') as f:
        for filename in os.listdir(negatives_dir):
            if filename.endswith('.png') or filename.endswith('.jpg'):
                f.write(negatives_dir + '\\' + filename + '\n')

negatives_dir = 'negatives'
output_file = 'negatives.txt'
frame('negative-videos\\01.mp4')
create_negatives_list(negatives_dir, output_file)
