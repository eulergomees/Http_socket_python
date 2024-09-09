
# Projeto Final

Trabalho final da disciplina Redes de Computadores.

O objetivo do trabalho é implementar um servidor web multithreaded, capaz de responder solicitações de um navegador web.

## Para execução

Utilize o comando "python server_socket.py <host> <port>" para execução.
Como por exemplo: "python server_socket.py 127.0.0.1 8080"

## Explicação do codigo

#### Classe HTTPServer
A classe HTTPServer é responsável por gerenciar o servidor web, aceitar conexões dos clientes, e servir os arquivos solicitados. Ela é inicializada com o endereço IP, a porta e o diretório onde os arquivos estão localizados.

#### Método __init__
Inicializar uma instância do servidor.

Parâmetros:
- host: Endereço IP no qual o servidor irá escutar (ex: '127.0.0.1').
- port: Porta onde o servidor vai escutar as conexões (ex: 8080).
- document_root: Caminho para o diretório onde os arquivos HTML estão localizados.

Ação: Configura o endereço, a porta e o diretório onde os arquivos serão servidos. O caminho para o diretório é convertido em um caminho absoluto usando os.path.abspath.

#### Método start
 Iniciar o servidor e começar a aceitar conexões.

Ação:
- Cria um socket para comunicação TCP.
- Associa (bind) o socket ao endereço IP e porta.
- Configura o socket para escutar conexões.
- Entra em um loop infinito aceitando conexões de clientes.
- Para cada conexão, cria uma nova thread que chama o método handle_client para processar a requisição do cliente.

#### Método handle_client

Processar a requisição do cliente e enviar uma resposta.

Ação:
- Recebe a requisição HTTP do cliente.
- Decodifica a requisição e imprime para depuração.
- Usa get_requested_file_path para determinar o caminho do arquivo solicitado.
- Envia a resposta com o arquivo solicitado ou uma resposta 404 se o arquivo não for encontrado.
- Fecha o socket do cliente após o processamento.

#### Método get_requested_file_path

Determinar o caminho do arquivo solicitado na requisição HTTP.

Ação:
- Divide a requisição em linhas.
- Analisa a primeira linha para obter o método HTTP (GET), o caminho do arquivo, e - a versão do HTTP.

Se o método for GET, lida com o caminho:
- Se o caminho for /, define como /index.html (tratamento da raiz do site).
- Normaliza o caminho e remove barras (/) do início.
- Constrói o caminho absoluto do arquivo.
- Verifica se o arquivo está dentro do diretório raiz do documento e se é um arquivo válido.

#### Método send_response
Enviar uma resposta HTTP com o conteúdo do arquivo solicitado.

Ação:
- Abre o arquivo solicitado em modo binário e lê seu conteúdo.
- Cria um cabeçalho HTTP com status 200 OK e o comprimento do conteúdo.
- Envia o cabeçalho e o conteúdo do arquivo para o cliente.

#### Método send_404_response
Enviar uma resposta HTTP 404 quando o arquivo solicitado não é encontrado.

Ação:
- Define o corpo da resposta como uma mensagem HTML simples de erro 404.
- Cria um cabeçalho HTTP com status 404 Not Found e o comprimento do corpo.
- Envia o cabeçalho e o corpo da resposta para o cliente.
## Autores

- [@eulergomees](https://github.com/eulergomees)
- [@Ambrosio9722](https://github.com/Ambrosio9722)
- [@drgsantaana](https://github.com/drgsantaana)

