﻿# 📝site-conectando-saberes


## 📖Descrição do Projeto

O uso das Tecnologias Digitais da Informação e Comunicação (TDICs) tem ganhado cada vez mais espaço no cenário educacional, servindo como ferramenta essencial no processo de ensino-aprendizagem. Essas tecnologias são utilizadas para promover o desenvolvimento de novas metodologias que facilitem a construção do saber, especialmente na preparação para vestibulares e exames de ingresso ao Ensino Superior, como o Exame Nacional do Ensino Médio (Enem).

Diante disso, este projeto visa desenvolver um website com um banco de questões focado no Enem classificadas por professores, voltado para docentes e estudantes. O site permitirá que os usuários tenham acesso aos conteúdos a qualquer momento e lugar, promovendo a democratização do acesso a materiais de ensino-aprendizagem.

### 🚀Funcionalidades principais:
- Estudantes poderão realizar questões por áreas temáticas e simulados, acompanhando seu progresso e identificando dificuldades;
- Docentes poderão criar listas de exercícios e simulados do Enem organizados por áreas do conhecimento;
- O site será um recurso de acesso livre, promovendo a inclusão digital na educação.

## 🎯Objetivos
- Criar um site com banco de questões do Enem;
- Auxiliar professores e alunos na utilização de questões do Enem nos processos de ensino-aprendizagem;
- Fornecer uma fonte organizada de materiais de estudo, fortalecendo a personalização e acessibilidade do ensino;
- Incentivar a participação de docentes do Ensino Básico na construção do site;
- Promover maior interação do PET C. S. Penedo com a comunidade interna e externa via parceria para construção e uso do site.



## 🛠️Configuração do Ambiente de Desenvolvimento

### Antes de executar o projeto
Para garantir que o projeto funcione corretamente, você precisará configurar um ambiente virtual, instalar as dependências e aplicar as migrações do banco de dados. Isso garantirá que todas as bibliotecas necessárias estejam disponíveis e que a estrutura do banco esteja atualizada. Siga os passos abaixo cuidadosamente para preparar seu ambiente de desenvolvimento.

### 1. Criar um Ambiente Virtual
No terminal, execute:
```sh
python -m venv venv
```

### 2. Ativar o Ambiente Virtual
- **Windows:**
  ```sh
  venv\Scripts\activate
  ```
- **Linux/Mac:**
  ```sh
  source venv/bin/activate
  ```

### 3. Instalar as Dependências
Com o ambiente virtual ativado, instale os pacotes necessários:
```sh
pip install -r requirements.txt
```

### 4. Aplicar Migrações do Django
Antes de rodar o servidor, aplique as migrações do banco de dados:
```sh
python manage.py migrate
```

### 5. Executar o Servidor Local
Finalmente, para rodar o projeto, execute:
```sh
python manage.py runserver
```
O servidor será iniciado e estará acessível em `http://127.0.0.1:8000/`.
