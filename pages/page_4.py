from nicegui import ui

def dessiner_page():
    with ui.element('div').classes('min-h-screen w-full flex flex-col items-center justify-center bg-slate-900 text-white py-16').props('id="diapo4"'):
        ui.label('Sources & Conclusion').classes('text-5xl font-bold mb-12 uppercase tracking-widest')
        
        with ui.card().classes('bg-slate-800 text-slate-300 w-3/4 max-w-2xl p-8 rounded-2xl shadow-xl border border-slate-700'):
            ui.label('Liens Utiles').classes('text-2xl font-semibold mb-6 text-white')
            
            with ui.column().classes('gap-4'):
                ui.link('Histoire du MET (Site Officiel)', 'https://www.metmuseum.org/about-the-met/history').classes('text-lg text-blue-400 hover:text-blue-300 transition-colors')
                ui.link('Collection John Singer Sargent', 'https://www.metmuseum.org/fr/art/collection/search/12127').classes('text-lg text-blue-400 hover:text-blue-300 transition-colors')
                ui.link('Vidéo de présentation (YouTube)', 'https://youtu.be/7oJrJJoTSaI').classes('text-lg text-blue-400 hover:text-blue-300 transition-colors')
                
        ui.label('Merci de votre visite !').classes('mt-16 text-3xl font-light text-slate-400')

        # Bouton pour remonter tout en haut
        with ui.row().classes('w-full justify-center mt-12'):
            ui.button('Remonter à l\'Accueil ⬆️', on_click=lambda: ui.run_javascript('window.scrollTo({top: 0, behavior: "smooth"})')).classes('bg-white text-slate-900 px-8 py-3 rounded-full hover:bg-slate-200 hover:shadow-[0_0_15px_rgba(255,255,255,0.5)] transition-all font-semibold')
