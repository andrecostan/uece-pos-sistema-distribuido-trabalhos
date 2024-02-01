# Sistemas Distribuídos - POS UECE

## _Trabalhos da Disciplina de Sistemas Distribuídos_

- Trabalho 1 – Instalação e Configuração do Wordpress Utilizando Docker
    ##### Start
    ```sh
    docker compose -f "trabalho-1\docker-compose.trabalho1.yml" up -d
    ```
    Browser test -> http://localhost/

- Trabalho 2 – Configuração do Wordpress com Múltiplas Instâncias Utilizando Nginx e Docker Composer
    ##### Start
    ```sh
    docker compose -f "trabalho-2\docker-compose.trabalho2.yml" up -d
    ```

    ```sh
    docker inspect --format '{{.Name}} {{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(docker ps -q)
    ```

    ##### Test Request
    ```sh
    curl -I http://localhost/
    ```

- Trabalho 3 – Realização de Testes de Carga com Múltiplas Instâncias do Wordpress Utilizando o Locust
    ##### Start
    ```sh
    docker compose -f "trabalho-3\docker-compose.trabalho3.yml" up -d
    ```
    Start load test -> http://localhost:8089/
    
# Comandos Úteis

### Docker

##### Listar todas as imagens
```sh
docker images -a
```

##### Remover todas as imagens

```sh
docker rmi $(docker images -q)
```

##### Listar container em execução

```sh
docker ps
```

##### Listar todos containers

```sh
docker ps -a
```

##### Remover container

```sh
docker rm <id-container>
```

##### Informações dos containers

```sh
docker inspect --format '{{.Name}} {{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(docker ps -q)
```

### Docker Compose

##### Start

```sh
docker-compose -f <nome-do-arquivo.yml> up -d
```

##### Stop

```sh
docker-compose -f <nome-do-arquivo.yml> down
```

### Http

##### Fazer requisição

```sh
  curl -I http://localhost/
```
