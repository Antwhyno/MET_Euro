#tableau classement musé du monde
from nicegui import ui

def render_ranking():
    columns = [
        {'name': 'rank', 'label': 'Rank', 'field': 'rank', 'align': 'center'},
        {'name': 'name', 'label': 'Museum Name', 'field': 'name', 'align': 'left'},
        {'name': 'location', 'label': 'City, Country', 'field': 'location', 'align': 'left'},
        {'name': 'size', 'label': 'Gallery Space (m²)', 'field': 'size', 'align': 'right'}
    ]

    rows = [
        {'rank': 1, 'name': 'Le Louvre', 'location': 'Paris, France', 'size': '72,735'},
        {'rank': 2, 'name': 'State Hermitage Museum', 'location': 'St. Petersburg, Russia', 'size': '66,842'},
        {'rank': 3, 'name': 'National Museum of China', 'location': 'Beijing, China', 'size': '65,000'},
        {'rank': 4, 'name': 'The Metropolitan Museum of Art', 'location': 'New York City, USA', 'size': '58,820'},
        {'rank': 5, 'name': 'Vatican Museums', 'location': 'Vatican City', 'size': '43,000'},
        {'rank': 6, 'name': 'Tokyo National Museum', 'location': 'Tokyo, Japan', 'size': '38,000'}
    ]

    # Full height page
    with ui.column().classes('page-section w-full items-center justify-center bg-white font-sans').style('min-height: calc(100vh - 64px); padding: 2rem;'):
        ui.label("World's Largest Art Museums").classes('text-6xl md:text-7xl font-bold mb-10 text-center uppercase tracking-widest text-[#8b0000] font-serif')
        
        table = ui.table(columns=columns, rows=rows, row_key='name').classes('w-full max-w-7xl shadow-xl rounded-3xl overflow-hidden')
        # On utilise table.props pour bien forcer la taille sur l'en-tête et les lignes dans Quasar
        # On ajoute aussi table-class et table-header-class avec des tailles de texte Quasar
        table.props('table-class="text-h6" table-header-class="text-h5" table-style="font-size: 1.8rem; line-height: 2.5rem;" table-header-style="font-size: 2rem; font-weight: bold; line-height: 3rem;"')
        table.style('border-collapse: collapse;')
