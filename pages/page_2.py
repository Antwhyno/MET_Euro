from nicegui import ui, app

# 1. On crée le "pont" entre Python et le dossier assets
app.add_static_files('/assets', 'assets')


def dessiner_page():
    with ui.row().classes('w-full justify-evenly'):
        ui.image('/assets/met_hero.png').classes('flex-1 rounded-lg shadow-md')
        ui.card().classes('flex-1 bg-red-100 h-64')

    with ui.image('/assets/location.png').classes('w-full rounded-xl'):
        # 2. LE TEXTE (L'Autocollant)
        # On le met dans la boîte, et on utilise des classes spéciales pour le placer
        ui.label('MUSÉE DU MET').classes('absolute bottom-4 left-4 text-white text-5xl font-bold')