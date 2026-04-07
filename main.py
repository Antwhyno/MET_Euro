# chef d'orchestre
from nicegui import ui

from pages import page_1
def creer_menu():
    # 1. On crée le menu qui restera accroché en haut de l'écran pendant qu'on descend
    with ui.header().classes('bg-slate-900 justify-between items-center p-4'):
        ui.label('Mon Projet Artistique').classes('text-xl font-bold')
        with ui.row():
            ui.link('Accueil', '/').classes('hover:text-blue-400')
            ui.link('Le Projet', '/projet').classes('hover:text-blue-400')
            ui.link('Conclusion', '/conclusion').classes('hover:text-blue-400')

# 3. La page d'accueil (qui va tout empiler)
@ui.page('/')
def page_principale():
    creer_menu()
    page_1.dessiner_page()

# 4. On lance le moteur (avec les réglages Hugging Face prêts au cas où)
ui.run(title="MET", host="0.0.0.0", port=7860)