from nicegui import ui
def dessiner_page():
    with ui.row().classes('w-full items-center bg-gray-50'):
        ui.label('Musée du MET').classes('text-5xl font-bold mb-8')
        ui.image('/assets/met_hero.png').classes('w-1/2')
        ui.label('Le MET est un musée situé à New York, fondé en 1870. Il est l\'un des plus grands et des plus importants musées d\'art au monde.').classes('text-xl mb-8')

    with ui.card().classes('w-1/2 bg-red-100 h-64'):
        ui.label('Je suis la grande carte de gauche !')
        
