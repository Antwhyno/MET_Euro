# chef d'orchestre
from nicegui import ui

from pages import page_1, page_2, page_3, page_4

def creer_menu():
    # 1. On crée le menu qui restera accroché en haut de l'écran pendant qu'on descend
    with ui.header().classes('bg-slate-900 justify-between items-center p-4 shadow-md'):
        ui.label('The MET').classes('text-xl font-bold text-white tracking-widest')
        with ui.row().classes('gap-6'):
            ui.link('Accueil', '#diapo1').classes('text-slate-300 hover:text-white transition-colors font-medium')
            ui.link('Histoire', '#diapo2').classes('text-slate-300 hover:text-white transition-colors font-medium')
            ui.link('Peintres', '#diapo3').classes('text-slate-300 hover:text-white transition-colors font-medium')
            ui.link('Sources', '#diapo4').classes('text-slate-300 hover:text-white transition-colors font-medium')

# 3. La page d'accueil (qui va tout empiler)
@ui.page('/')
def page_principale():
    creer_menu()
    
    # On ajoute la propriété smooth au html entier pour les liens d'ancre
    ui.add_head_html('<style>html { scroll-behavior: smooth; }</style>')

    # On empile nos sous-pages (nos "diapos")
    page_1.dessiner_page()
    page_2.dessiner_page()
    page_3.dessiner_page()
    page_4.dessiner_page()

# 4. On lance le moteur (avec les réglages Hugging Face prêts au cas où)
ui.run(title="The MET by Antoine", host="0.0.0.0", port=7860, reload=True)