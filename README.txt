# Saber Aprender

Este é um projeto Django REST Framework para gerenciar estudantes e cursos. O projeto permite a criação, leitura, atualização e exclusão de informações sobre estudantes e cursos, além de gerenciar matrículas.

## Estrutura do Projeto

```
Saber_Aprender/
├── .gitignore
├── db.sqlite3
├── manage.py
├── popular_banco_cursos.py
├── popular_banco_estudantes.py
├── requirements.txt
├── escola/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── validators.py
│   ├── views.py
│   └── migrations/
├── scripts/
└── setup/
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

## Instalação

1. Clone o repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd Saber_Aprender
   ```

2. Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/Mac
   venv\Scripts\activate  # Para Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure o banco de dados:
   ```bash
   python manage.py migrate
   ```

5. Crie um superusuário para acessar o painel administrativo:
   ```bash
   python manage.py createsuperuser
   ```

## Uso

Para iniciar o servidor de desenvolvimento, execute:
```bash
python manage.py runserver
```

Acesse a aplicação em [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Endpoints

- **Estudantes**
  - `GET /estudantes/` - Lista todos os estudantes
  - `POST /estudantes/` - Cria um novo estudante
  - `GET /estudantes/{id}/` - Obtém detalhes de um estudante específico
  - `PUT /estudantes/{id}/` - Atualiza um estudante específico
  - `DELETE /estudantes/{id}/` - Remove um estudante específico
  - `GET /estudantes/?version=v2` - Lista todos os estudantes com a versão 2 do endpoint

- **Cursos**
  - `GET /cursos/` - Lista todos os cursos
  - `POST /cursos/` - Cria um novo curso
  - `GET /cursos/{id}/` - Obtém detalhes de um curso específico
  - `PUT /cursos/{id}/` - Atualiza um curso específico
  - `DELETE /cursos/{id}/` - Remove um curso específico

- **Matrículas**
  - `GET /matriculas/` - Lista todas as matrículas
  - `POST /matriculas/` - Cria uma nova matrícula
  - `GET /matriculas/{id}/` - Obtém detalhes de uma matrícula específica
  - `PUT /matriculas/{id}/` - Atualiza uma matrícula específica
  - `DELETE /matriculas/{id}/` - Remove uma matrícula específica
