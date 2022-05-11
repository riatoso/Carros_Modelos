import PySimpleGUI as sg


if __name__ == "__main__":
    from modulo import Carros

    carro_marca = Carros()
    lista = carro_marca.buscar_marcas()


    def cadastro():
        sg.theme("DarkTeal12")
        layout = [
            [sg.Text("Insira os dados do carro.", size=20)],
            [sg.Text("Modelo do carro.", size=20)],
            [sg.Input(key="modelo", size=50)],
            [sg.Text(f"{40 * '--'}", size=45)],
            [sg.Text("Motor do carro.", size=20)],
            [sg.Input(key="motor", size=50)],
            [sg.Text("Combustivel do carro.", size=40)],
            [sg.Listbox(values=["ETANOL", "GASOLINA", "ELETRICO", "FLEX"], key="combustivel",
                        default_values=["ETANOL"], no_scrollbar=True, size=(50, 4))],
            [sg.Text("Transmissão do carro.", size=40)],
            [sg.Listbox(values=["AUTOMATICO", "SEMI-AUTOMATICO", "MANUAL"], key="transmissao",
                        default_values=["AUTOMATICO"], size=(50, 3), no_scrollbar=True)],
            [sg.Text(" * Selecione a marca do carro.", size=30)],
            [sg.Listbox(values=lista, default_values=["CHEVROLET"], size=(50, 5),
                        key='marca')],
            [sg.Button('Cadastrar', size=20), sg.Button("Finalizar", size=20)],
            [sg.Button('Gerar planilha de inventario.', size=50)]
        ]
        return sg.Window('Cadastro de carros.', size=(350, 550), icon="login.ico", layout=layout,
                         finalize=True)


    def executa():
        janela1, janela2 = cadastro(), None
        while True:
            window, events, values = sg.read_all_windows()
            if events == janela1 and sg.WINDOW_CLOSED:
                break
            if window == janela1 and events == "Cadastrar":
                if values["modelo"] and values["motor"]:
                    modelo = values["modelo"]
                    modelo = modelo.upper()
                    motor = values["motor"]
                    combustivel = values["combustivel"]
                    transmissao = values["transmissao"]
                    marca = values["marca"][0]
                    lista_marcas = carro_marca.id_marcas
                    id_marca = [i[0] for i in lista_marcas if i[1] == marca]
                    id_marca = id_marca[0]
                    inserir = carro_marca.inserir_marcas(id_marca, modelo, motor, combustivel[0], transmissao[0])
                    if inserir == 1:
                        sg.popup_no_border("Cadastro de inventario de carro executado com sucesso.",
                                           background_color="silver", button_color="gray")
                        janela1["modelo"].update("")
                        janela1["motor"].update("")
                        janela1["modelo"].set_focus()
                        continue
                    if inserir == 2 or inserir == 1:
                        sg.popup_no_border("Cadastro de inventario de carro executado com sucesso.",
                                           background_color="silver", button_color="gray")
                        janela1["modelo"].update("")
                        janela1["motor"].update("")
                        janela1["modelo"].set_focus()
                        continue
                if not values["modelo"] and values["motor"]:
                    sg.popup_no_border("Digite o modelo do carro.",
                                       background_color="silver", button_color="gray")
                    janela1["modelo"].set_focus()
                    continue
                if values["modelo"] and not values["motor"]:
                    sg.popup_no_border("Digite o motor do carro.",
                                       background_color="silver", button_color="gray")
                    janela1["motor"].set_focus()
                    continue
                if not values["modelo"] and not values["motor"]:
                    sg.popup_no_border("Digite os dados do carro.",
                                       background_color="silver", button_color="gray")
                    janela1["modelo"].set_focus()
                    continue

            if window == janela1 and events == "Finalizar":
                sg.popup_no_border("Finalizando sistema.",
                                   background_color="silver", button_color="gray")
                break
            if window == janela1 and events == 'Gerar planilha de inventario.':
                arquivo = "Inventario_carros.xlsx"
                sg.popup_no_border(f"Planilha {arquivo} gerada com sucesso.",
                                   background_color="gray", button_color="silver")
                df_gerado = carro_marca.buscar_modelos()
                df_gerado.to_excel(arquivo, index=False)
                continue
            if window == janela1 and events == sg.WINDOW_CLOSED:
                break


    executa()
