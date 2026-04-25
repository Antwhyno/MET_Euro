from nicegui import ui

def render_history():
    # Custom CSS pour la timeline (agrandir, gras, rouge et ajustement hauteurs)
    ui.html("""
    <style>
    .q-timeline__subtitle {
        color: #8b0000 !important;
        font-weight: 900 !important;
        font-size: 1.6rem !important;
        margin-bottom: 2px !important;
        padding-bottom: 0 !important;
        line-height: 1.1 !important;
        opacity: 1 !important;
    }
    .q-timeline__subtitle * {
        color: #8b0000 !important;
        font-weight: 900 !important;
    }
    .q-timeline__title {
        margin-top: 2px !important;
    }
    </style>
    """)

    # History Section
    with ui.column().classes('page-section w-full bg-[#f4f1ea] py-20 px-6 font-sans justify-center').style('min-height: calc(100vh - 64px);'):
        with ui.column().classes('max-w-6xl mx-auto w-full').props('id=history'):
            ui.label('History of the Museum').classes('text-4xl font-bold mb-6 text-center w-full uppercase tracking-widest text-[#8b0000] font-serif')
            
            with ui.row().classes('w-full items-center justify-between gap-12 flex-col md:flex-row'):
                # Timeline à gauche
                with ui.column().classes('w-full md:w-1/2 flex-1'):
                    with ui.timeline().classes('w-full'):
                        with ui.timeline_entry('1866', title='The Initial Idea', icon='lightbulb', color='red-9').classes('text-xl'):
                            ui.html('The idea came from <strong>Paris</strong> during a dinner of important American personalities. the lawyer <strong>John Jay</strong>. to create a <strong>national institution</strong> and art gallery to <strong>educate the American people</strong>.').classes('text-gray-800 mt-2 text-base')
                        
                        with ui.timeline_entry('April 13, 1870', title='Official Foundation', icon='account_balance', color='red-9').classes('text-xl'):
                            ui.html('The MET was officially founded. Its first acquisition was a <strong>Roman sarcophagus</strong>, marking the beginning of its vast collection.').classes('text-gray-800 mt-2 text-base')
                            
                        with ui.timeline_entry('March 30, 1880', title='Moving to Central Park', icon='location_on', color='red-9').classes('text-xl'):
                            ui.html('The museum expanded and moved to its current iconic location at <strong>Fifth Avenue and 82nd Street</strong>, next to <strong>Central Park</strong>.').classes('text-gray-800 mt-2 text-base')

                # Images à droite
                with ui.column().classes('w-full md:w-5/12 flex flex-col gap-8 items-center justify-center'):
                    ui.image('/assets/1880_Met_Museum.jpg').classes('w-full rounded-2xl shadow-xl hover:scale-105 transition-transform duration-300 border-4 border-white')
                    ui.image('/assets/museum.jpg').classes('w-full rounded-2xl shadow-xl hover:scale-105 transition-transform duration-300 border-4 border-white')
