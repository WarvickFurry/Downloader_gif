@echo off
echo �⮡� �ᯮ�짮���� �ਯ� ����������, � ��� ������ ���� ��⠭����� git � 㪠��� ���� � ����. �த������, �᫨ �� � ���浪�
pause
git init
REM �஢��塞, ������� �� ����� Downloader_gif
if not exist Downloader_gif (
    REM �᫨ ����� �� �������, ������㥬 ९����਩ � ⥪���� ��४���
    git clone https://github.com/WarvickFurry/Downloader_gif.git
) else (
    REM �᫨ ����� �������, �믮��塞 git pull ��� ����������
    git -C Downloader_gif pull
)

REM ����砥� ᯨ᮪ ��� 䠩��� � ९����ਨ
git -C Downloader_gif ls-files > all_files.txt

REM �஢��塞, �������� �� 䠩�� �� �����쭮� ��⥬�
for /f "delims=" %%f in (all_files.txt) do (
    if not exist "Downloader_gif\%%f" (
        REM �᫨ 䠩�� ���, ����稢��� ���
        git -C Downloader_gif checkout -- "%%f"
    )
)

REM ����塞 �६���� 䠩� � ᯨ᪮� ��� 䠩���
del all_files.txt

REM �����蠥� �ਯ�
echo �� �������騥 䠩�� �뫨 ����砭�!
pause