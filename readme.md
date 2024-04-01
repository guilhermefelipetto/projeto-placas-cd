## como usar? 🤔🤨

# 1. No caso de tudo estar pronto
Voce precisa conferir esses aquivos dentro dessa pasta.

- positives.vec
- negatives.txt
- negatives\
- ..\opencv\build\x64\vc15\bin\

Caso esses arquivos estejam presentes nessa pasta, eh provavel que voce deva apenas executar o ´train.bat´

# 2. Caso voce precise preparar o treinamento

1. Primeiramente execute o positives.py, lembre-se de conferir o positives para garantir que ele esta pegando os dados corretamente.
2. Agora voce tem o positives.txt, em seguida execute o arquivo vec.bat para gerar o positives.vec para o treinamento.
3. Agora voce tem o positives.vec, execute o train.bat e aguarde o treinamento.

# 3. Alterando parametros ou scripts

1. Antes de alterar qualquer parametro dos arquivos .bat apenas tenha noção do que você esta fazendo para não quebrar os comandos.
2. Antes de alterar funcionamento das funcoes dos scripts python, tenha noção do que você esta fazendo para não quebrar os scripts.

# 4. Criação do ambiente virtual Python para rodar os .py caso necessário

1. rode 'pip install -r requirements.txt' e aguarde a instalação das libs necessárias.

download.https://www.inf.ufpr.br/vri/databases/tbFcZE-RodoSol-ALPR.zip