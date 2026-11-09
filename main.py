alunos = []
logins = []
senhas = []

login_correto = input("Digite o login: ")
logins.append(login_correto)

senha_correta = input("Digite a senha: ")
senhas.append(senha_correta)

login_digitado = input("Digite o login correto: ")
senha_digitada = input("Digite a senha correta: ")

class Aluno:

    def __init__(self, nome, nota, turma):

        self.nome = nome
        self.nota = nota
        self.turma = turma        


from openai import OpenAI
from google.colab import userdata

chave = userdata.get("GROQ_API_KEY")

cliente = OpenAI(
    api_key=chave,
    base_url="https://api.groq.com/openai/v1"
)

def chatbot():
    while True:

        dados = ""
        for a in alunos:
             dados += f"nome: {a.nome}, nota: {a.nota}, turma: {a.turma}\n"

        pergunta = input("Faça uma pergunta: ")
        texto = dados + "\n" + pergunta

        if pergunta == "sair":
            print("Até logo!")
            break         

        resposta = cliente.responses.create(

            model = "openai/gpt-oss-120b",
            input = texto
        )
        print(resposta.output_text)


def mostrar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    for i, a in enumerate(alunos, start=1):
        print(f"{i} - Aluno: {a.nome} | Nota: {a.nota} | Turma: {a.turma}")


if login_digitado in logins:
    posicao = logins.index(login_digitado)
    if senhas[posicao] == senha_digitada:
        print(f"Seja bem-vindo {login_digitado}!")

        while True:
            print("\n1 - Adicionar aluno | 2 - Remover aluno | 3 - Listar alunos e notas | 4 - Assistente IA | 0 - Sair")
            opcao = input("Digite uma opção: ")

            if opcao == "1":
                aluno_digitado = input("Digite o nome do aluno: ")
                try:
                    nota = float(input("Adicione a nota do aluno: ").replace(",", "."))
                except ValueError:
                    print("Nota inválida")
                    continue

                while True:
                    turma_digitada = input("Digite a turma do aluno: ")


                    if len(turma_digitada) == 2 and turma_digitada[0].isdigit() and turma_digitada[1].isalpha():

                        alunos.append(Aluno(aluno_digitado, nota, turma_digitada))
                        print("Informações registradas com sucesso!")
                        break

                    else:
                        print("Turma invalida")


            elif opcao == "2":
                mostrar_alunos()
                try:
                    indice = int(input("Digite o número do aluno que deseja remover: "))
                except ValueError:
                    print("Digite um número válido")
                    continue
                if 1 <= indice <= len(alunos):
                    aluno_removido = alunos.pop(indice - 1) #  
                    print(f"{aluno_removido.nome} removido!")
                else:
                    print("Opção excedeu o número de alunos")

            elif opcao == "3":
                mostrar_alunos()

            elif opcao == "4":
                chatbot()

            elif opcao == "0":
                mostrar_alunos()
                print(f"Programa encerrado, {login_digitado}. Volte sempre!")
                break

            else:
                print("Opção inválida")
    else:
        print("Senha invalida")
else:
    print("Login incorreto")
