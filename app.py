import flet as ft
from routes import get_route
from alembic.config import Config
from alembic import command

from models.base import engine, Base
from models.activity import Activity
from models.user import User
from models.user_activity import UserActivity

from views.register_points_view import register_points_view  # Certifique-se do caminho correto


def run_migrations():
    """Executa as migrações pendentes usando Alembic."""
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")  # Aplica todas as migrações pendentes

def main(page):
    # Executa as migrações ao iniciar o app
    run_migrations()
    
    # Configurações da página inicial
    page.title = "S4PO Game Points"
    page.theme_mode = ft.ThemeMode.LIGHT

    # Função para mudar de rota
    def route_change(route):        
        print(f"==> Evento route_change. Alterando para a rota: {route}")  # Verifica a mudança de rota
        
        # Limpa os controles da página e adiciona a nova view correspondente
        page.clean()  # Garante que a interface anterior seja removida
        new_view = get_route(page)  # Obtém a view com base na rota
        # Se a view for None, exibe uma mensagem de erro
        if new_view:
            page.add(new_view)  # Adiciona a nova view à página

        page.update()  # Atualiza a interface para refletir a mudança

    # # Configura a função de troca de rotas e navega para a rota atual   
    # chamada direta
    #page.add(register_points_view(page))  # Adiciona diretamente a view de cadastro para teste
    #page.update()
    page.on_route_change = route_change
    page.go("/")

if __name__ == "__main__":
    #ft.app(target=main)
    ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=8000)    
