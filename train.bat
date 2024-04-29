@echo off
echo Iniciando o treinamento do modelo...

"Z:\placas_cd\opencv\build\x64\vc15\bin\opencv_traincascade.exe" ^
-data "Z:\placas_cd\train_dir" ^
-vec positives20ke60x24.vec ^
-bg negatives.txt ^
-numPos 9000 ^
-numNeg 8210 ^
-numStages 8 ^
-precalcValBufSize 1024 ^
-precalcIdxBufSize 1024 ^
-featureType HAAR ^
-w 60 ^
-h 24 ^
-mode ALL ^
-maxFalseAlarmRate 0.3 ^
-minHitRate 0.95 ^
-maxDepth 6 ^
-maxWeakCount 200
