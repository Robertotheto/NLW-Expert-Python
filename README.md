# NLW Expert Python
## App de barcode usando Python

**Skills**

![Python](https://img.shields.io/badge/-Python-000?&logo=Python) ![Flask](https://img.shields.io/badge/-Flask-000?&logo=Flask) ![Virtualenv](https://img.shields.io/badge/-Virtualenv-000?&logo=Virtualenv) ![Pylint](https://img.shields.io/badge/-Pylint-000?&logo=Pylint) ![Pytest](https://img.shields.io/badge/-Pytest-000?&logo=Pytest) ![PythonBarcode](https://img.shields.io/badge/-Barcode-009?&logo=PythonBarcode) ![Pillow](https://img.shields.io/badge/-Pillow-009?&logo=Pillow) ![Cerberus](https://img.shields.io/badge/-Cerberus-009?&logo=Cerberus) ![Pre-Commit](https://img.shields.io/badge/-PreCommit-000?&logo=Pre-Commit)

##
App foi desenvolvido durante o **NLW Expert Python** em consiste em uma aplicação backend para gerar tag de barcode.

![Image](https://github.com/Robertotheto/NLW-Expert-Python/blob/main/123-456-789.png)

**Para inicial o projeto primeiro clone o repositorio**

    git clone https://github.com/Robertotheto/NLW-Expert-Python.git
**Crie seu ambiente virtual**

    pip3 install virtualenv
    python3 -m venv nome_do_ambiente
**Ative seu ambiente virtual**
`source nome_do_ambiente/bin/activate` no Linux ou `nome_do_ambiente\Scripts\activate` no Windows.

**Instale as dependências do projeto**
    pip3 install -r requirements.txt
    
*OBS: Use pip3 ou python3 quando estiver em um ambiente Linux, quando no Windows utilize pip e py.*

**Para rodar o projeto digite o comando:**

    python3 run.py

**código importante para a biblioteca de pre-commit**

    .pre-commit-config.yaml
        repos:
          - repo: local
            hooks:
              - id: pylint
                name: pylint
                entry: pylint
                language: system
                types: [python]
                args:
                  [
                    "-rn", # Only display messages
                    "-sn", # Don't display the source
                    "--rcfile=.pylintrc", # Link to your config file
                    "--load-plugins=pylint.extensions.docparams", # Load an extension
                  ]

**código importante para a biblioteca pylint**

    .pylintrc
          C0114, # missing-module-docstring
          C0115, # Missing-class-docstring
          C0116, # missing-function-docstring
          W0703, # Catching too general exception Exception
          R0903, # too-few-public-methods
          W0719, # broad-exception-raised

**comando para gerar nosso arquivo de requirements.txt**
   

     .venv/bin/pip3 freeze > requirements.txt
