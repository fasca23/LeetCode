pngquant --ext .png --force images/*.png
rename 'Вставленное изображение (' '' *.png && rename ')' '' *.png   --- оставляем в именах файлах всех тока цифры
for f in *; do [ -f "$f" ] && mv "$f" "0$f"; done --- переименование массовое - 0 добавляем