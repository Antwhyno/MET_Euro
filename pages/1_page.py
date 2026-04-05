# Fichier : pages/1_page.py
#introduction, image MET

from nicegui import ui

def dessiner_section():
    # Le py-16 (padding Y) ajoute un grand espace en haut et en bas de cette section pour la faire respirer
    with ui.column().classes('w-full items-center bg-gray-50'):
        ui.label('Musée du MET').classes('text-5xl font-bold mb-8')
        
        with ui.row().classes('w-full flex-wrap justify-center gap-12'):
            with ui.card().classes('w-96'):
                ui.label('L\'exposition').classes('text-2xl')
                ui.label('Voici mon projet sur l\'art...')