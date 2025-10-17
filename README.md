# Loja de Carros com cep - Flask

Aplicação web em Flask que permite consultar veículos, cadastrar e excluir carros via API, além de consultar CEP e testar uma API de teste.

---

## Estrutura do projeto

flask_loja_carros/
├── app.py
├── requirements.txt
├── .env
└── templates/
└── index.html

yaml
Copiar código

---

## Pré-requisitos

- Python 3.11 ou superior
- Pip (gerenciador de pacotes Python)
- VS Code (ou outro editor de sua preferência)
- Acesso à internet (para consultar APIs externas)

---

## Configuração do `.env`

Crie um arquivo `.env` na raiz do projeto para definir variáveis de ambiente, como o IP da sua API na AWS:

API_BASE=http://00.000.000.00:8080

yaml
Copiar código

> Substitua `00.000.000.00` pelo IP correto da máquina na AWS quando estiver disponível.

---

## Passo a passo para rodar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/flask_loja_carros.git
cd flask_loja_carros
Substitua seu-usuario pelo seu usuário no GitHub.

2. Criar e ativar o ambiente virtual
No Windows:

bash
Copiar código
python -m venv venv
venv\Scripts\activate
No Linux/Mac:

bash
Copiar código
python3 -m venv venv
source venv/bin/activate
3. Instalar as dependências
bash
Copiar código
pip install -r requirements.txt
O requirements.txt deve conter pelo menos:

nginx
Copiar código
Flask
requests
python-dotenv
4. Rodar a aplicação
bash
Copiar código
python app.py
A aplicação estará disponível em: http://127.0.0.1:5000

Funcionalidades
Adicionar Carro

Informe modelo e preço

Cadastra o carro via API

Carros Cadastrados

Exibe carros cadastrados via API

Permite excluir cada carro individualmente

Consulta de CEP

Consulta dados do CEP informado via ViaCEP

Testar API

Testa a API de teste definida em .env (API_BASE/test)

Estrutura dos arquivos
app.py → arquivo principal da aplicação Flask

requirements.txt → lista de dependências

.env → variáveis de ambiente (API_BASE)

templates/index.html → front-end da aplicação com formulários e tabelas

Como contribuir
Faça um fork do repositório

Crie uma branch para suas alterações:

bash
Copiar código
git checkout -b minha-feature
Faça as alterações e teste localmente

Faça commit:

bash
Copiar código
git add .
git commit -m "Descrição da mudança"
Faça push para sua branch:

bash
Copiar código
git push origin minha-feature
Abra um Pull Request no repositório original

Licença
Este projeto é open source. Sinta-se livre para usar e modificar conforme necessário.

Links úteis
API de consulta de carros na AWS

Consulta de CEP ViaCEP

yaml
Copiar código
