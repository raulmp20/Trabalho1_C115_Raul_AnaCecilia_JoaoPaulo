import socket

# Configurar o cliente
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 20000))

# Receber e responder às questões
for _ in range(3):
    question = client.recv(4096).decode()
    print(question)
    answer = input("Insira a sua resposta: ").lower()
    client.sendall(str.encode(answer))

    feedback = client.recv(4096).decode()
    print(feedback)

client.close()