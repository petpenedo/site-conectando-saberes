# 📝site-conectando-saberes


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


## 🛠️Clonando o repositório

Perfeito! A parte que você quer inserir pode ficar bem clara e didática se estruturarmos assim, com uma explicação breve seguida de comandos diretos. Aqui está uma sugestão de redação para a seção **🛠️Clonando o repositório** que combina bem com o estilo do restante do seu README:

---

## 📂Clonando o repositório

Antes de seguir para a **Configuração do Ambiente de Desenvolvimento**, é necessário clonar este repositório para a sua máquina. Isso permitirá que você tenha uma cópia local do projeto, podendo executá-lo, explorar o código e até fazer alterações.

Siga os passos abaixo para clonar o repositório:

### 1. Copie a URL do repositório

Acesse a página do projeto no GitHub e copie a URL do repositório. Ela deve ter o seguinte formato:

```
https://github.com/SEU-USUARIO/site-conectando-saberes.git
```

Substitua `SEU-USUARIO` pelo nome correto do repositório se necessário.

### 2. Abra o terminal e navegue até o local onde deseja salvar o projeto

Por exemplo, para acessar a pasta Documentos:

```sh
cd ~/Documentos
```

### 3. Clone o repositório usando o Git

No terminal, execute o comando:

```sh
git clone https://github.com/SEU-USUARIO/site-conectando-saberes.git
```

Esse comando vai criar uma pasta com os arquivos do projeto dentro do seu computador.

### 4. Acesse a pasta do projeto

```sh
cd site-conectando-saberes
```

Pronto! Agora você já pode seguir para a próxima etapa: **Configuração do Ambiente de Desenvolvimento**.  


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
