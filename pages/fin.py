from nicegui import ui

def render_media():
    # Media Section             ###
    with ui.column().classes('page-section w-full max-w-6xl mx-auto py-20 px-6 font-sans justify-center').style('min-height: calc(100vh - 64px);').props('id=media'):
        ui.label('Explore Further').classes('text-4xl font-bold mb-12 text-center w-full uppercase tracking-widest text-[#8b0000] font-serif')
        
        with ui.row().classes('w-full flex-wrap justify-center gap-12'):
            # Video iframe
            with ui.card().classes('p-0 rounded-3xl overflow-hidden shadow-2xl flex-1 min-w-[300px] md:min-w-[500px] h-[350px]'):
                ui.html('<iframe style="width:100%; height:100%;" src="https://www.youtube.com/embed/7oJrJJoTSaI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>').classes('w-full h-full')
            
            # Links
            with ui.column().classes('flex-1 min-w-[300px] justify-center gap-8 bg-white p-10 shadow-2xl rounded-3xl'):
                ui.label('Official Resources').classes('text-3xl font-bold text-[#1a1a1a] mb-2')
                with ui.link(target='https://www.metmuseum.org/fr/art/collection/search/12127').classes('no-underline text-black w-full'):
                    with ui.row().classes('w-full items-center gap-6 p-6 border-2 border-gray-100 rounded-2xl hover:bg-red-50 hover:border-red-100 transition duration-300 w-full cursor-pointer'):
                        ui.icon('language').classes('text-4xl text-[#8b0000]')
                        with ui.column().classes('gap-1'):
                            ui.label('MET Art Collection').classes('text-xl font-bold text-gray-900')
                            ui.label('Search the collection online').classes('text-sm text-gray-500')
                        
                with ui.link(target='https://www.metmuseum.org/about-the-met/history').classes('no-underline text-black w-full'):
                    with ui.row().classes('w-full items-center gap-6 p-6 border-2 border-gray-100 rounded-2xl hover:bg-red-50 hover:border-red-100 transition duration-300 w-full cursor-pointer'):
                        ui.icon('history_edu').classes('text-4xl text-[#8b0000]')
                        with ui.column().classes('gap-1'):
                            ui.label('History of the MET').classes('text-xl font-bold text-gray-900')
                            ui.label('Read more on the official site').classes('text-sm text-gray-500')
