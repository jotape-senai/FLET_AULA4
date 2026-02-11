import flet as ft

def main(page: ft.Page):
    def mostrar_mensagem(e):
        page.add(ft.Text("EU SOU O ATUAL CAMPEÃO DO MUNDO, E VIM TE CONVIDAR A PARTICIPAR DA NOSSA EQUIPE"))
    page.add(
        ft.Text("Olá! eu sou da EKIPE_ROZETA!"),
        ft.Image(
            src="imagens/ekipe_rozeta.jpg",
            width=200,
            height=200
        ),
        ft.Button(
            content="Faça parte da nossa jornada",
            on_click=mostrar_mensagem  
        )
    )
ft.app(main)