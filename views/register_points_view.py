import flet as ft
from controllers.user_activity_controller import UserActivityController
from controllers.activity_controller import ActivityController

def register_points_view(page: ft.Page):
    print("==> Executando register_points_view...")  # Verifica se a função foi chamada

    # Buscar lista de atividades para o campo seletor
    activities = ActivityController.list_activities()
    activity_options = [
        ft.dropdown.Option(str(activity.id), f"{activity.name} - {activity.category}") 
        for activity in activities
    ]

    # Lista de usuários (Exemplo; idealmente buscado do banco)
    users = [(1, "Alice"), (2, "Bob"), (3, "Charlie")]
    user_options = [ft.Checkbox(label=user[1], value=False) for user in users]

    # Campos da interface
    activity_selector = ft.Dropdown(label="Atividade", options=activity_options, width=400)

    # Usando Column para exibir o rótulo e o DatePicker
    date_picker = ft.Column(
        [
            ft.Text("Data", size=16),  # Rótulo acima do DatePicker
            ft.DatePicker(),  # DatePicker sem o argumento 'label'
        ],
        spacing=5,
    )

    # Lista de usuários em um campo com scroll
    user_checkboxes = ft.Column(user_options, scroll="adaptive", width=400, height=150)

    # Campo de justificativa
    justification_field = ft.TextField(label="Justificativa (Opcional)", multiline=True, width=400, height=150)

    # Função para registrar pontos
    def register_points(e):
        selected_activity = activity_selector.value
        selected_date = date_picker.controls[1].value  # Pega o valor do DatePicker
        selected_users = [user.label for user in user_checkboxes.controls if user.value]
        justification = justification_field.value

        if not selected_activity or not selected_date or not selected_users:
            page.snack_bar = ft.SnackBar(
                ft.Text("Preencha todos os campos obrigatórios!"), bgcolor=ft.colors.RED
            )
            page.snack_bar.open()
            return

        try:
            for user_name in selected_users:
                UserActivityController.register_activity(
                    user_name, selected_activity, "Pendente", justification
                )
            page.snack_bar = ft.SnackBar(
                ft.Text("Pontos cadastrados com sucesso!"), bgcolor=ft.colors.GREEN
            )
            page.snack_bar.open()
            page.go("/")
        except ValueError as err:
            page.snack_bar = ft.SnackBar(ft.Text(str(err)), bgcolor=ft.colors.RED)
            page.snack_bar.open()

    # Organiza os campos em um GridView para responsividade
    return ft.GridView(
        max_extent=450,  # Define a largura máxima dos itens para ajuste responsivo
        spacing=20,  # Espaçamento entre os itens
        run_spacing=10,  # Espaçamento entre linhas
        child_aspect_ratio=1.5,  # Ajusta a proporção largura/altura dos campos
        controls=[
            activity_selector,
            date_picker,
            ft.Text("Selecione os Usuários", size=18, weight="bold"),
            user_checkboxes,
            justification_field,
            ft.Row(
                [
                    ft.ElevatedButton("Cadastrar Pontos", on_click=register_points),
                    ft.ElevatedButton("Voltar", on_click=lambda _: page.go("/")),
                ],
                spacing=20,
            ),
        ],
    )
