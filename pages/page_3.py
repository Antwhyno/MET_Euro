from nicegui import ui

def dessiner_page():
    with ui.element('div').classes('min-h-screen w-full flex flex-col items-center justify-center bg-stone-50 py-16').props('id="diapo3"'):
        ui.label('Les Peintres du MET').classes('text-5xl font-bold text-slate-800 mb-12 uppercase tracking-widest')
        
        with ui.row().classes('w-3/4 max-w-5xl items-center justify-evenly gap-12'):
            with ui.column().classes('flex-1'):
                ui.label('John Singer Sargent').classes('text-3xl font-semibold text-slate-700 mb-4')
                ui.label('Un peintre extrêmement important de la collection du MET.').classes('text-xl text-slate-600 mb-4')
                ui.label('Né en 1856 à Florence, en Italie, il est devenu l\'un des portraitistes les plus reconnus de son époque. Ses œuvres illustrent parfaitement l\'élégance et la société de la fin du 19ème siècle.').classes('text-lg text-slate-500 leading-relaxed font-light')
            
            ui.image('/assets/DP263942.jpg').classes('flex-1 rounded-xl shadow-2xl hover:scale-105 transition-transform duration-500 h-96 object-cover object-top')

        ui.label('John Singer Sargent - Madame X').classes('text-sm text-slate-400 mt-4 italic')

        # Bouton pour descendre
        with ui.row().classes('w-full justify-center mt-16'):
            ui.button('Sources & Conclusion', on_click=lambda: ui.run_javascript('document.getElementById("diapo4").scrollIntoView({behavior: "smooth"})')).classes('bg-slate-900 text-white px-8 py-3 rounded-full hover:bg-slate-700 hover:shadow-lg transition-all')
