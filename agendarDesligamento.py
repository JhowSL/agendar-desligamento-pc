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
            "  [3] Agendar desligamento em um horário específico\n"
            "  [4] Cancelar desligamento\n"
            "Escolha: "
        )

        if escolha in {"1", "2", "3", "4"}:
            break
        else:
            print(
                "Opção inválida. Por favor, escolha '1' para horas, '2' para minutos, '3' para horário específico ou '4' para cancelar."
            )
            linha_divisoria()

    if escolha == "4":
        cancelar_desligamento()
        return

    if escolha == "3":
        tempo_agendado = obter_tempo_especifico()
    else:
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


def obter_tempo_especifico():
    # Agendamento para um horário específico
    hora_minuto = input(
        "Digite o horário no formato HH:MM para agendar o desligamento: "
    )
    hora, minuto = map(int, hora_minuto.split(":"))

    agora = datetime.datetime.now()
    horario_agendado = agora.replace(hour=hora, minute=minuto, second=0, microsecond=0)

    # Verificar se o horário agendado já passou, se sim, agendar para o próximo dia
    if agora > horario_agendado:
        horario_agendado += datetime.timedelta(days=1)

    tempo_agendado = int((horario_agendado - agora).total_seconds())
    return tempo_agendado


def cancelar_desligamento():
    os.system("shutdown /a")  # Comando para cancelar o desligamento
    linha_divisoria()
    print("Desligamento cancelado.\n")


if __name__ == "__main__":
    agendar_desligamento()
