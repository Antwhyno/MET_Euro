from nicegui import ui

# 1. On crée le "pont" entre Python et le dossier assets
app.add_static_files('/assets', 'assets')


def dessiner_page():
    with ui.row().classes('w-full items-center bg-gray-50'):
        ui.card().classes('w-1/2 bg-red-100 h-64')
        ui.image('/assets/met_hero.jpg').classes('w-1/2 rounded-lg shadow-lg')