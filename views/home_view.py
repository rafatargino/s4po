import flet as ft

def home_view(page: ft.Page):
    print("==> Executando home_view...")  # Verifica se a função foi chamada

    # Função que navega para a rota ao clicar no card
    def on_card_click(route):
        page.go(route)  # Navega para a rota correspondente

    # Lista dos cards com textos, rotas e cores
    cards = [
        {"label": "Cadastrar Pontos", "route": "/register", "color": "#B2FF59"},
        {"label": "Avaliar Pontos", "route": "/evaluate", "color": "#81D4FA"},
        {"label": "Listar Pontos", "route": "/list", "color": "#FFF176"},
        {"label": "Aprovar Pontos", "route": "/approve", "color": "#F8BBD0"},
    ]

    # Gera os widgets de cards dinamicamente
    card_widgets = [
        ft.Container(
            content=ft.Text(
                card["label"],
                size=18,
                font_family="Roboto",
                weight=ft.FontWeight.NORMAL,
            ),
            alignment=ft.alignment.center,
            bgcolor=card["color"],
            width=200,
            height=150,
            border_radius=10,
            margin=10,
            on_click=lambda e, route=card["route"]: on_card_click(route),  # Evento de clique
        )
        for card in cards
    ]

    # Layout principal usando GridView para responsividade
    return ft.Column(
        controls=[
            ft.Text("S4PO Game Points", size=24, font_family="Roboto"),
            ft.Text("Selecione uma funcionalidade", size=18, font_family="Roboto"),
            ft.GridView(
                controls=card_widgets,
                max_extent=220,  # Largura máxima por item
                child_aspect_ratio=1.3,  # Proporção entre largura e altura dos itens
                spacing=10,  # Espaçamento entre os itens
                run_spacing=10,  # Espaçamento entre linhas
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=30,
    )
