from nicegui import ui

def render_hero():
    # Hero Section
    with ui.column().classes('w-full items-center justify-center bg-[#fdfbf7]').style('height: calc(100vh - 64px); padding: 2rem;'):
        ui.image('assets/MET_premiere.jpg').classes('w-full max-w-5xl rounded-3xl shadow-2xl').style('max-height: 45%; object-fit: contain;')
        ui.image('assets/location.png').classes('w-full max-w-5xl rounded-3xl shadow-2xl mt-8').style('max-height: 45%; object-fit: contain;')
