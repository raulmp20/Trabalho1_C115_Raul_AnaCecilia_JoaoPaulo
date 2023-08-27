import socket
from pymongo import MongoClient

client = MongoClient("mongodb://mongoadmin:secret@localhost:27017/")
db = client['questions']
questions_collection = db['perguntas']

# Configurar o servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 20000))
server.listen(1)

print("Aguardando conexão...")
connection, address = server.accept()
print("Conexão estabelecida:", address)

# Enviar questões ao cliente e receber respostas
for question in questions_collection.find().limit(3):
    question_text = question['question'] + "\n"
    for idx, choice in enumerate(question['options']):
        question_text += f"{chr(97 + idx)}) {choice}\n"

    connection.sendall(str.encode(question_text))
    answer = connection.recv(1024).decode()

    correct_answer = chr(97 + question['options'].index(question['correct_answer']))

    if answer == correct_answer:
        feedback = "\n Resposta correta! \n"
    else:
        feedback = f"\n Resposta Errada! A resposta correta é {correct_answer} \n"

    connection.sendall(str.encode(feedback))

print("Fechando conexao...")

connection.close()
server.close()