# Scanner de Porta Básico

Um simples scanner de portas feito em python.

## Entendendo como o scanner funciona

Bom, o scanner usa de uma lib chamada socket e precisamos especificar dois argumentos antes, o AF_INET que significa que estamos falando de IPv4 e SOCK_STREAM que basicamente diz que se trata do protocolo TCP/IP.

O scanner basicamente vai tentar se conectar com o host na porta desejada utilizando do método Three-way handshake(SYN/ACK). Ele vai enviar uma requisição (SYN) e se a porta estiver aberta vai enviar uma respota (SYN/ACK), se estiver fechada o host apenas ignora a requisição.

## Requisitos

- Python 3.x

## Como usar
```
python main.py -t <ip> [-a] 
-t or --target: Specify the target address.
-a or --all: Scan all ports (default is to scan well-known ports only).
```
## Exemplo
```
python main.py -t example.com -a
```
## License
This project is licensed under the MIT License - see the LICENSE.md file for details.
