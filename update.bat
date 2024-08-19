@echo off
echo Чтобы использовать скрипт обновления, у вас должен быть установлен git и указан путь к нему. Продолжайте, если все в порядке
pause
git init
REM Проверяем, существует ли папка Downloader_gif
if not exist Downloader_gif (
    REM Если папка не существует, клонируем репозиторий в текущую директорию
    git clone https://github.com/WarvickFurry/Downloader_gif.git
) else (
    REM Если папка существует, выполняем git pull для обновления
    git -C Downloader_gif pull
)

REM Получаем список всех файлов в репозитории
git -C Downloader_gif ls-files > all_files.txt

REM Проверяем, существуют ли файлы на локальной системе
for /f "delims=" %%f in (all_files.txt) do (
    if not exist "Downloader_gif\%%f" (
        REM Если файла нет, докачиваем его
        git -C Downloader_gif checkout -- "%%f"
    )
)

REM Удаляем временный файл со списком всех файлов
del all_files.txt

REM Завершаем скрипт
echo Все недостающие файлы были докачаны!
pause