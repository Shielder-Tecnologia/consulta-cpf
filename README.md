
## Installation

### Requirements para instalar pelo source
- Firefox
- Geckodriver => https://medium.com/beelabacademy/baixando-e-configurando-o-geckodriver-no-ubuntu-dc2fe14d91c
- Pip para instalar o resto

```
pip install -r requirements.txt

```

### Instalando pelo folder output
- Só baixar o folder e executar o consulta-cpf!

## Usage 

- Pela CLI executar o código passando como argumento o CPF:

    - Pela instalação source:
    ```
    python3 seleniumapp.py {cpf}
    ```
    
    <br>

    - Pela instalação direta com a pasta:
    ```
    cd output/consulta-cpf

    ./consulta-cpf {cpf}
    ```