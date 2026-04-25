from nicegui import ui

def render_presentation():
    # Presentation Section
    with ui.column().classes('page-section w-full max-w-6xl mx-auto py-20 px-6 justify-center').style('min-height: calc(100vh - 64px);').props('id=presentation'):
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
