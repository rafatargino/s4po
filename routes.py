from views.home_view import home_view
from views.register_points_view import register_points_view

def get_route(page):
    """Mapeia as rotas para suas respectivas views."""
    print(f"==> Rota atual em get_route: {page.route}")  # Log da rota atual

    # Mapear rotas corretamente
    routes = {
        "/": home_view,  # Observe que passamos apenas a função, não a execução dela
        "/register": register_points_view,
    }

 # Verifica se a rota existe no dicionário de rotas
    if page.route in routes:
        print(f"==> View encontrada para a rota {page.route}")  # Confirma a rota encontrada
        return routes[page.route](page)  # Executa a função da view e retorna o resultado
    else:
        print(f"Erro: Nenhuma view encontrada para a rota {page.route}")  # Log de erro
        return None  # Retorna None se a rota não for encontrada