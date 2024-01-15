import os
import time
import datetime


def linha_divisoria():
    print("\n" + "#" * 40 + "\n")


def agendar_desligamento():
    print("Bem-vindo ao Agendador de Desligamento!")
    linha_divisoria()

    while True:
        escolha = input(
            "Escolha uma opção:\n"
            "  [1] Agendar desligamento em horas\n"
            "  [2] Agendar desligamento em minutos\n"
            "  [3] Cancelar desligamento\n"
            "Escolha: "
        )

        if escolha in {"1", "2", "3"}:
            break
        else:
            print(
                "Opção inválida. Por favor, escolha '1' para horas, '2' para minutos ou '3' para cancelar."
            )
            linha_divisoria()

    if escolha == "3":
        cancelar_desligamento()
        return

    tempo_agendado = obter_tempo_agendado(escolha)

    linha_divisoria()
    print(f"Desligamento agendado para ocorrer em {tempo_agendado} segundos.")

    data_hora_agendamento = datetime.datetime.now()
    data_hora_desligamento = data_hora_agendamento + datetime.timedelta(
        seconds=tempo_agendado
    )

    print(f"Agendamento: {data_hora_agendamento}")
    print(f"Desligamento: {data_hora_desligamento}")

    # Criar relatório
    relatorio = (
        f"Agendamento: {data_hora_agendamento}\nDesligamento: {data_hora_desligamento}"
    )

    with open("relatorio_desligamento.txt", "w") as file:
        file.write(relatorio)

    linha_divisoria()
    print(f"Relatório criado em 'relatorio_desligamento.txt'.\n")

    # Adicionar pausa para dar tempo ao usuário antes de fechar o terminal
    time.sleep(5)

    os.system(f"shutdown /s /t {tempo_agendado}")  # Comando para desligar o computador

    linha_divisoria()
    print("Desligamento programado. O computador será desligado em breve.")
    print("Pressione Enter para sair...")


def obter_tempo_agendado(opcao):
    if opcao == "1":
        return (
            int(input("Digite o número de horas para agendar o desligamento: ")) * 3600
        )
    elif opcao == "2":
        return (
            int(input("Digite o número de minutos para agendar o desligamento: ")) * 60
        )


def cancelar_desligamento():
    os.system("shutdown /a")  # Comando para cancelar o desligamento
    linha_divisoria()
    print("Desligamento cancelado.\n")


if __name__ == "__main__":
    agendar_desligamento()
