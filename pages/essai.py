from nicegui import ui

# 1. Je crée une ligne qui prend TOUTE la largeur de l'écran (w-full)
with ui.row().classes('w-full'):
    
    # 2. Je crée une carte rouge qui prend 50% de la place (w-1/2)
    with ui.card().classes('w-1/2 bg-red-100 h-64'):
        ui.label('Je suis la grande carte de gauche !')
        
    # 3. Je crée une petite carte bleue à côté (w-1/4 = 25% de la place)
    with ui.card().classes('w-1/4 bg-blue-100 h-32'):
        ui.label('Je suis la petite carte à droite !')

ui.run()