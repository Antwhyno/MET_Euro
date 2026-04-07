from nicegui import ui

def dessiner_page():
    with ui.element('div').classes('min-h-screen w-full flex flex-col items-center justify-center bg-white py-16').props('id="diapo1"'):
        ui.label('The Metropolitan Museum of Art').classes('text-5xl font-bold text-slate-800 mb-6 tracking-wide text-center')
        
        with ui.row().classes('w-3/4 max-w-6xl items-center justify-between gap-12 mt-8'):
            # Image de gauche
            with ui.column().classes('flex-1 relative group'):
                ui.image('/assets/met_hero.png').classes('w-full rounded-2xl shadow-2xl transition-transform duration-700 ease-in-out group-hover:scale-[1.02]')
                ui.label('Central Park, New York').classes('absolute bottom-4 left-4 bg-black/60 text-white px-4 py-1 rounded-md text-sm')

            # Texte explicatif à droite
            with ui.column().classes('flex-1 gap-6 bg-slate-50 p-8 rounded-2xl border border-slate-100 shadow-sm'):
                ui.label('Un Musée de Légende').classes('text-3xl font-semibold text-slate-700')
                ui.label('Le MET est l\'un des plus grands musées du monde avec ses 58 800 mètres carrés. Il se classe juste derrière Le Louvre, l\'Ermitage et le Musée national de Chine.').classes('text-lg text-slate-600 font-light leading-relaxed')
                ui.label('Situé sur l\'île de Manhattan à New York, juste à côté de Central Park, il abrite plus de 2 millions d\'œuvres d\'art retraçant 5 000 ans d\'histoire de l\'humanité, réparties dans 280 salles !').classes('text-lg text-slate-600 font-light leading-relaxed')
                
        # Bouton pour descendre
        with ui.row().classes('w-full justify-center mt-16'):
            ui.button('Découvrir l\'Histoire ⬇️', on_click=lambda: ui.run_javascript('document.getElementById("diapo2").scrollIntoView({behavior: "smooth"})')).classes('bg-slate-900 text-white px-8 py-3 rounded-full hover:bg-slate-700 hover:shadow-lg transition-all animate-bounce')