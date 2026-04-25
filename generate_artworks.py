import json

with open("artworks.json", "r", encoding="utf-16") as f:
    artworks = json.load(f)

# generate the nicegui python code
code = """from nicegui import ui

def render_artworks():
    artworks = """ + json.dumps(artworks, indent=4) + """
    
    # We create a page-section for EACH artwork, so the user can scroll through them 1 by 1
    for idx, art in enumerate(artworks):
        with ui.column().classes('page-section w-full relative overflow-hidden items-center justify-center bg-black').style('min-height: calc(100vh - 64px);').props(f'id=artwork-{idx}'):
            # Background image with blur
            ui.image(art['image']).style('position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; filter: blur(20px); opacity: 0.5; z-index: 1;')
            
            # The actual image
            ui.image(art['image']).style('max-height: 70vh; max-width: 90vw; object-fit: contain; z-index: 2; border-radius: 10px; box-shadow: 0px 10px 30px rgba(0,0,0,0.8);')
            
            # The artwork info
            with ui.column().classes('items-center text-center mt-6 z-10 p-6 bg-black/60 backdrop-blur-md rounded-2xl border border-white/10').style('max-width: 800px;'):
                ui.label(art['title']).classes('text-3xl font-bold text-white font-serif mb-2')
                ui.label(f"By {art['artist']} | {art['date']}").classes('text-lg text-gray-300 font-sans italic')
                if art['medium']:
                    ui.label(art['medium']).classes('text-sm text-gray-400 mt-2 font-sans')
"""

with open("pages/artworks.py", "w", encoding="utf-8") as f:
    f.write(code)

print("Created pages/artworks.py successfully.")
