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
        {'rank': 6, 'name': 'Tokyo National Museum', 'location': 'Tokyo, Japan', 'size': '38,000'},
        {'rank': 7, 'name': 'National Museum of Anthropology', 'location': 'Mexico City, Mexico', 'size': '33,000'},
        {'rank': 8, 'name': 'Victoria and Albert Museum', 'location': 'London, UK', 'size': '30,658'},
        {'rank': 9, 'name': 'Art Institute of Chicago', 'location': 'Chicago, USA', 'size': '26,000'},
        {'rank': 10, 'name': 'British Museum', 'location': 'London, UK', 'size': '25,700'}
    ]

    # Full height page
    with ui.column().classes('w-full items-center justify-center bg-white font-sans').style('height: 100vh; padding: 2rem;'):
        ui.label('World\\'s Largest Art Museums').classes('text-4xl font-bold mb-10 text-center uppercase tracking-widest text-[#8b0000] font-serif')
        
        table = ui.table(columns=columns, rows=rows, row_key='name').classes('w-full max-w-5xl shadow-xl rounded-3xl overflow-hidden')
        table.style('font-size: 1.1rem; border-collapse: collapse;')
