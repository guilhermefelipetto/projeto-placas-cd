@echo off
echo iniciando o treinamento do modelo...

"D:\opencv\build\x64\vc15\bin\opencv_traincascade.exe" -data "D:\train_dir" -vec positives20000e24x24.vec -bg negatives.txt -numPos 200 -numNeg 200 -numStages 10 -w 24 -h 24
