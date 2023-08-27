import socket

# Configurar o cliente
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 40002))

# Receber e responder às questões
for _ in range(3):
    question = client.recv(4096).decode()
    print(question)

    while True:
        user_answer = input("Insira o número da sua resposta (0 a 3): ")
        if user_answer.isdigit() and 0 <= int(user_answer) <= 3:
            break
        else:
            print("Opção inválida. Por favor, insira um número válido de 0 a 3.")

    client.sendall(str.encode(user_answer))

    feedback = client.recv(4096).decode()
    print(feedback)

client.close()