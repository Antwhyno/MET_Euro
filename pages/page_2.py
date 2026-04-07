from nicegui import ui, app

# 1. On crée le "pont" entre Python et le dossier assets
app.add_static_files('/assets', 'assets')

def dessiner_page():
    with ui.element('div').classes('min-h-screen w-full flex flex-col items-center justify-center bg-slate-100 py-16').props('id="diapo2"'):
        ui.label('Histoire du MET').classes('text-5xl font-bold text-slate-800 mb-12 uppercase tracking-wide')
        
        with ui.row().classes('w-4/5 max-w-7xl items-start justify-center gap-8'):
            
            # Bloc Création
            with ui.card().classes('flex-1 bg-white p-6 rounded-2xl shadow-xl hover:-translate-y-2 transition-transform duration-300 border-t-8 border-slate-900'):
                ui.label('Création (1866)').classes('text-2xl font-bold text-slate-800 mb-4')
                ui.label('L\'idée de créer ce musée est née à Paris lors d\'un dîner entre plusieurs personnalités importantes, dont le célèbre avocat John Jay.').classes('text-lg text-slate-600 mb-4')
                ui.label('Son objectif était de fonder une institution nationale et une galerie d\'art pour éduquer le peuple américain.').classes('text-lg text-slate-600')
                
            # Bloc Ouverture
            with ui.card().classes('flex-1 bg-white p-6 rounded-2xl shadow-xl hover:-translate-y-2 transition-transform duration-300 border-t-8 border-blue-600'):
                ui.label('Ouverture (1870)').classes('text-2xl font-bold text-slate-800 mb-4')
                ui.label('Le musée a été officiellement fondé le 13 Avril 1870.').classes('text-lg text-slate-600 mb-4')
                ui.label('Fait amusant : sa toute première acquisition artistique fut un majestueux sarcophage romain !').classes('text-lg text-slate-600')
                ui.image('/assets/MET_premiere.jpg').classes('w-full h-40 object-cover mt-4 rounded-xl')

            # Bloc Expansion
            with ui.card().classes('flex-1 bg-white p-6 rounded-2xl shadow-xl hover:-translate-y-2 transition-transform duration-300 border-t-8 border-slate-400'):
                ui.label('Nouvel Emplacement (1880)').classes('text-2xl font-bold text-slate-800 mb-4')
                ui.label('Le 30 Mars 1880, le musée déménage à son emplacement actuel mythique, juste à côté de Central Park.').classes('text-lg text-slate-600 mb-4')
                ui.image('/assets/1880_Met_Museum.jpg').classes('w-full h-40 object-cover mt-4 rounded-xl')

        # Bouton pour descendre
        with ui.row().classes('w-full justify-center mt-16'):
            ui.button('Découvrir les Œuvres ⬇️', on_click=lambda: ui.run_javascript('document.getElementById("diapo3").scrollIntoView({behavior: "smooth"})')).classes('bg-slate-900 text-white px-8 py-3 rounded-full hover:bg-slate-700 hover:shadow-lg transition-all animate-bounce')