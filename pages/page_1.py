from nicegui import ui

def dessiner_page():
    with ui.element('div').classes('min-h-screen w-full flex flex-col items-center justify-center bg-white py-16').props('id="diapo1"'):
        ui.label('The Metropolitan Museum of Art').classes('text-5xl font-bold text-slate-800 mb-6 tracking-wide text-center')
        
        with ui.row().classes('w-full max-w-6xl items-center justify-between mt-8'):
            # Image de gauche
            with ui.column().classes('flex-1 relative group'):
                ui.image('/assets/met_hero.png').classes('w-full rounded-2xl shadow-2xl transition-transform duration-700 ease-in-out group-hover:scale-[1.02]')
                ui.label('Central Park, New York').classes('absolute bottom-4 left-4 bg-black/60 text-white px-4 py-1 rounded-md text-sm')