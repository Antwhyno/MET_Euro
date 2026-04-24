from nicegui import ui

def render_presentation():
    # Presentation Section
    with ui.column().classes('w-full max-w-6xl mx-auto py-20 px-6').props('id=presentation'):
        ui.label('Key Figures').classes('text-4xl font-bold mb-12 text-center w-full uppercase tracking-widest text-[#8b0000]')
        
        with ui.grid(columns=2).classes('w-full gap-8 md:grid-cols-4 lg:grid-cols-4 font-sans'):
            def stats_card(title, value, icon):
                with ui.card().classes('items-center text-center p-8 bg-white shadow-lg rounded-2xl hover:shadow-2xl transition duration-300 w-full'):
                    ui.icon(icon).classes('text-6xl text-[#8b0000] mb-4')
                    ui.label(value).classes('text-4xl font-black text-gray-800 mb-2')
                    ui.label(title).classes('text-lg font-semibold text-gray-500 uppercase tracking-wide')
    
            stats_card('Area Size', '58,800 m²', 'straighten')
            stats_card('Rooms', '280', 'meeting_room')
            stats_card('Artworks', '2 M+', 'brush')
            stats_card('Years of Art', '5,000+', 'history_toggle_off')
    
        with ui.card().classes('w-full mt-16 p-10 bg-white shadow-2xl rounded-3xl flex flex-col md:flex-row items-center gap-10'):
            ui.icon('location_city').classes('text-[100px] text-gray-300 hidden md:block')
            with ui.column().classes('flex-1 font-sans'):
                ui.label('Global Ranking & Location').classes('text-3xl font-bold mb-6 text-[#1a1a1a]')
                ui.label("Located in New York City, in the heart of Manhattan next to Central Park, the MET is a monumental institution.").classes('text-xl text-gray-700 leading-relaxed mb-4')
                ui.label("It ranks as one of the world's largest art museums, standing proudly behind other historical giants like The Louvre in Paris, the State Hermitage Museum in St. Petersburg, and the National Museum of China.").classes('text-xl text-gray-700 leading-relaxed')
