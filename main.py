import flet as ft


def pagina_inicial(pagina):
    texto = ft.Text("S4PO Game Points")
    botao_cadpontos = ft.ElevatedButton("Cadastrar Pontos")
    botao_verpontos = ft.ElevatedButton("Ver Pontuação")
    botao_usarpontos = ft.ElevatedButton("Usar Pontos")

    botao_aprovarpontos = ft.ElevatedButton("Aprovar  Pontos")

    pagina.add(texto)
    pagina.add(botao_cadpontos)
    pagina.add(botao_verpontos)
    pagina.add(botao_usarpontos)
    pagina.add(botao_aprovarpontos)

def main(pagina):

    pagina_inicial(pagina)    

ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=8000)
