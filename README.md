Link do Site: https://projetomaquinas.onrender.com/pag-inicial/
Se precisar do login de superusuário favor entrar em contato;

* Tecnologias Utilizadas:
Django – Framework backend em Python;
Amazon S3 (AWS) – Armazenamento das imagens das peças;
HTML + Django Templates – Estrutura de front-end;
CSS externo via GitHub Pages – Estilização da interface;
PostgreSQL – Banco de dados(Render);
Render – Hospedagem e deploy automático da aplicação;

* Funcionalidades:
* Autenticação
Registro de usuários;
Login;
Logout e redirecionamento após login;
Controle de acesso por tipo de usuário (usuário comum e supervisor).

* Acesso diferenciado:
Colaboradores: apenas visualizam peças;
Supervisores: cadastram e excluem peças.

* Gerenciamento de Peças:
Listagem de todas as peças separadas por maquina (acesso público após login);
Cadastro de novas peças com:
  Nome;
  Código;
  Valor;
  Imagem (enviada diretamente para o Amazon S3);

Apenas usuários com permissão de supervisor podem cadastrar novas peças.
Exclusão de peças (apenas por supervisores);

* Estrutura de Arquivos Principais
core/models.py
Define os modelos principais da aplicação, como:
Peca: contém nome, codigo, valor e imagem.

core/views.py
Implementa as views para:
Listagem de peças;

Cadastro (restrito a supervisores);
Login e logout de usuários;
Proteção de páginas com autenticação.

core/forms.py
Formulários customizados para login, cadastro de usuários e cadastro de peças.
core/permissions.py
Gerencia regras de permissão:
Apenas usuários autenticados com permissão de supervisor podem criar peças.

core/serializers.py
Define os serializadores da API para:
Usuários (registro e autenticação);

Peças (envio e listagem via API).

core/urls.py
Define as rotas da aplicação:
/login/ – tela de login;


/cadastro/ – cadastro de usuários;
/pecas/ – listagem das peças;
/cadastrar-peca/ – adicionar nova peça (supervisores).

settings.py
Contém as configurações do projeto, como:
Configuração do Django REST Framework;

* Hospedagem e Deploy
A aplicação está hospedada na Render;
Imagens são enviadas diretamente para o Amazon S3;
O CSS está disponível publicamente via GitHub Pages.

* Exemplo de Uso (usuário comum)
Colaborador acessa a listagem de peças filtradas por máquina.
Supervisor pode adicionar uma nova peça com nome, código, valor e imagem.
As imagens são exibidas corretamente pois estão no Amazon S3 com permissões públicas.

* Exemplo de Uso (Superusuário)
* Login como superusuário
 O supervisor acessa a aplicação e realiza o login com suas credenciais.
* Seleciona uma máquina
 Após o login, é redirecionado para a página /selecionar-maquina/, onde pode escolher uma das máquinas da fábrica.
* Cadastrar uma nova peça
 Na página de cadastro, o supervisor preenche o formulário com:

Nome da peça
Código único
Valor da peça
Imagem (que será enviada automaticamente para o Amazon S3)

* Visualiza o feedback
 Após o envio, recebe uma mensagem de sucesso (“Peça adicionada com sucesso!”) ou erro (como código já existente).

* Visualiza a peça na listagem pública
 A nova peça é listada automaticamente na página de consulta dos colaboradores, com a imagem carregada diretamente do S3.


* Pode excluir peças
 O superusuário também possui a opção de excluir peças já cadastradas, se necessário.
