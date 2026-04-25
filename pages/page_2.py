from nicegui import ui

def render_presentation():
    # Presentation Section
    with ui.column().classes('page-section w-full max-w-6xl mx-auto py-20 px-6 justify-center').style('min-height: calc(100vh - 64px);').props('id=presentation'):
        ui.label('Key Figures').classes('text-4xl font-bold mb-12 text-center w-full uppercase tracking-widest text-[#8b0000]')
        
        with ui.grid(columns=1).classes('w-full gap-8 md:grid-cols-2 lg:grid-cols-2 font-sans'):
            def stats_card(title, value, icon, image_path):
                with ui.card().classes('p-0 bg-white shadow-lg rounded-2xl hover:shadow-2xl transition duration-300 w-full flex flex-row items-stretch gap-0 overflow-hidden'):
                    ui.image(image_path).classes('w-2/5 object-cover m-0 min-h-[160px]')
                    with ui.column().classes('w-3/5 p-6 items-center justify-center text-center m-0'):
                        ui.icon(icon).classes('text-5xl text-[#8b0000] mb-2')
                        ui.label(value).classes('text-3xl font-black text-gray-800 mb-1')
                        ui.label(title).classes('text-sm font-semibold text-gray-500 uppercase tracking-wide')
    
            stats_card('Area Size', '58,800 m²', 'straighten', 'assets/visite-metropolitan-museum-art-new-york-une.jpg')
            stats_card('Rooms', '280', 'meeting_room', 'assets/1880_Met_Museum.jpg')
            stats_card('Artworks', '2 M+', 'brush', 'assets/painture.jpeg')
            stats_card('Years of Art', '5,000+', 'history_toggle_off', 'assets/painture2.jpeg')
