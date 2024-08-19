@echo off
echo Чтобы использовать скрипт обновления, у вас должен быть установлен git и указан путь к нему. Продолжайте, если все в порядке
pause
git init
cd ..
git pull https://github.com/WarvickFurry/Downloader_gif.git
echo Репозиторий успешно обновлен!
pause