pngquant --ext .png --force images/*.png
for f in *; do [ -f "$f" ] && mv "$f" "0$f"; done --- переименование массовое - 0 добавляем
rename 'Вставленное изображение (' '' *.png && rename ')' '' *.png   --- оставляем в именах файлах всех тока цифры