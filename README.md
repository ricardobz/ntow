# NTOW - NUM TO WORDS

Retorna Json de chave informada por extenso

## Como rodar projeto:

1. Clone o repositório
2. Crie um virtualenv com Python 3.5
3. Ative o virtualenv
4. Instale as dependências
6. Rode os testes
7. Execute o app

```console
git clone https://github.com/ricardobz/ntow.git
cd ntow
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m unittest
python app.py
```

## Exemplo:

```console
curl http://127.0.0.1:5000/42
{
    "extenso": "quarenta e dois"
}

curl http://127.0.0.1:5000/1025
{
    "extenso": "mil e vinte e cinco"
}
```