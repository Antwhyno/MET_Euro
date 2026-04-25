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
        
        # Custom CSS pour forcer la taille et le gras dans tout le tableau
        ui.html("""
        <style>
        /* Entêtes de colonnes */
        .q-table th {
            font-size: 2.5rem !important;
            font-weight: 900 !important;
            padding: 24px !important;
            line-height: 1.2 !important;
        }
        /* Lignes du tableau */
        .q-table td {
            font-size: 2.2rem !important;
            font-weight: 800 !important;
            padding: 20px !important;
            line-height: 1.2 !important;
        }
        </style>
        """)
        table = ui.table(columns=columns, rows=rows, row_key='name').classes('w-full max-w-7xl shadow-xl rounded-3xl overflow-hidden')
        table.props('flat bordered')
        table.style('border-collapse: collapse;')
