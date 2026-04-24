from nicegui import app, ui

# Configure page
app.add_static_files('/assets', 'assets')

# Background color and fonts using generic CSS in nicegui
ui.add_head_html("""
<style>html { scroll-behavior: smooth; } body { background-color: #fdfbf7; color: #1a1a1a; font-family: "Georgia", serif; margin: 0; padding: 0; }</style>
<script>
document.addEventListener('keydown', function(event) {
    if (['Shift', 'Control', 'Alt', 'Meta'].includes(event.key)) return;
    
    if (event.key === 'ArrowUp' || event.key === 'PageUp') {
        event.preventDefault();
        window.scrollBy({ top: -window.innerHeight, behavior: 'smooth' });
    } else {
        if (event.key === 'ArrowDown' || event.key === 'PageDown' || event.key === ' ') {
            event.preventDefault();
        }
        window.scrollBy({ top: window.innerHeight, behavior: 'smooth' });
    }
});
</script>
""")

# Navigation / Header
with ui.row().classes('w-full items-center justify-between p-4 bg-white shadow-md fixed z-50 top-0 left-0 right-0'):
    ui.label('MET Exposition').classes('text-2xl font-bold tracking-widest')
    with ui.row().classes('gap-6 hidden md:flex lg:flex'):
        ui.link('Presentation', '#presentation').classes('text-lg text-gray-700 hover:text-red-800 no-underline font-sans')
        ui.link('History', '#history').classes('text-lg text-gray-700 hover:text-red-800 no-underline font-sans')
        ui.link('Media', '#media').classes('text-lg text-gray-700 hover:text-red-800 no-underline font-sans')

# Since header is fixed, add a spacer
ui.element('div').classes('h-16')

# Hero Section
with ui.column().classes('w-full items-center justify-center bg-[#fdfbf7]').style('height: calc(100vh - 64px); padding: 2rem;'):
    ui.image('assets/MET_premiere.jpg').classes('w-full max-w-5xl rounded-3xl shadow-2xl').style('max-height: 45%; object-fit: contain;')
    ui.image('assets/location.png').classes('w-full max-w-5xl rounded-3xl shadow-2xl mt-8').style('max-height: 45%; object-fit: contain;')

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

# History Section
with ui.column().classes('w-full bg-[#f4f1ea] py-20 px-6 font-sans'):
    with ui.column().classes('max-w-5xl mx-auto w-full').props('id=history'):
        ui.label('History of the Museum').classes('text-4xl font-bold mb-16 text-center w-full uppercase tracking-widest text-[#8b0000] font-serif')
        
        with ui.timeline().classes('w-full ml-0 md:ml-20'):
            with ui.timeline_entry('1866', title='The Initial Idea', icon='lightbulb', color='red-9').classes('text-xl'):
                ui.label("The idea to create a museum came from Paris during a dinner of important American personalities. The most famous among them was the lawyer John Jay, who championed the idea. His vision was to create a national institution and art gallery to educate the American people.").classes('text-gray-800 mt-2')
            
            with ui.timeline_entry('April 13, 1870', title='Official Foundation', icon='account_balance', color='red-9').classes('text-xl'):
                ui.label("The MET was officially founded. Its very first acquisition was a remarkable Roman sarcophagus, marking the beginning of its vast collection.").classes('text-gray-800 mt-2')
                
            with ui.timeline_entry('March 30, 1880', title='Moving to Central Park', icon='location_on', color='red-9').classes('text-xl'):
                ui.label("The museum expanded and moved to its current iconic location at Fifth Avenue and 82nd Street, next to beautiful Central Park.").classes('text-gray-800 mt-2')

# Media Section             ###
with ui.column().classes('w-full max-w-6xl mx-auto py-20 px-6 font-sans').props('id=media'):
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

# Footer
with ui.row().classes('w-full p-8 bg-[#1a1a1a] text-center justify-center font-sans mt-10'):
    ui.label('Exposition of the MET • Antoine').classes('text-gray-400')

# On ajoute le host et le port spécifique pour Hugging Face
ui.run(title="The MET - Exposition", favicon="🏛️", host="0.0.0.0", port=7860)