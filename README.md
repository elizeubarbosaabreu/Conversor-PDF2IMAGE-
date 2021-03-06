# Conversor-PDF2IMAGE-

Este é um software construído inteiramente em Python e que tem por finalidade converter páginas de um arquivo PDF em imagens com a extensão JPG. Isso é útil quando queremos enviar um certificado em uma rede social onde somente aceita imagem, por exemplo. Eu já fazia isso via linha de comando, mas resolvi criar esse aplicativo com interface gráfica com o auxilio da Biblioteca [PySimpleGUI](https://pypi.org/project/PySimpleGUI/).

![Conversor-PDF2IMAGE](image.png)

## Instalação do Conversor-PDF2IMAGE em Linux

Verifique se você já tem o git e o python instalado em seu OS.

Clone e configure o **Conversor-PDF2IMAGE** no terminal usando os comandos:

~~~
git clone https://github.com/elizeubarbosaabreu/Conversor-PDF2IMAGE-
cd Conversor-PDF2IMAGE-
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
~~~

Se tudo estiver certo, o **Conversor-PDF2IMAGE** abrirá...

Mova o projeto para a pasta */opt* com o comando:

~~~
cd ../
mv Conversor-PDF2IMAGE- /opt
~~~

Crie um Link para o ambiente virtual *.venv* e o arquivo *app.py*. Eu uso o Alacarte para isso:

~~~
/opt/Conversor-PDF2IMAGE-/.venv/bin/python /opt/Conversor-PDF2IMAGE-/app.py
~~~


## Instalação do Conversor-PDF2IMAGE em Windows

Confira se o git e o python está presente no sistema operacional.
Dentro do prompt de comando cole os comandos abaixo:

~~~
git clone https://github.com/elizeubarbosaabreu/Conversor-PDF2IMAGE-
cd Conversor-PDF2IMAGE-
python -m venv .venv
source .venv\bin\activate.bat
pip install -r requirements.txt
python app.py
~~~

Você pode usar o [Pyinstaller](https://pyinstaller.org/en/stable/) para transformar esse código fonte em um software portátil que pode ser movido para o disco C:/ ou  para um Pendrive por exemplo...