from nicegui import ui

def render_artworks():
    artworks = [
    {
        "title": "Booklet with Scenes of the Passion",
        "artist": "",
        "date": "ca. 1300 (carving); ca. 1310\u201320 (painting)",
        "medium": "Elephant ivory, polychromy, and gilding",
        "image": "https://images.metmuseum.org/CRDImages/md/web-large/DT133.jpg"
    },
    {
        "title": "The Backgammon Players",
        "artist": "Philip Webb",
        "date": "1861",
        "medium": "Painted pine, oil paint on leather, brass, copper",
        "image": "https://images.metmuseum.org/CRDImages/es/web-large/DP169654.jpg"
    },
    {
        "title": "Shrine",
        "artist": "Matthias Walbaum",
        "date": "1598\u20131600",
        "medium": "Ebony, silver, gilded silver, gouache on parchment",
        "image": "https://images.metmuseum.org/CRDImages/es/web-large/DP259735.jpg"
    },
    {
        "title": "Jaharis Byzantine Lectionary",
        "artist": "",
        "date": "ca. 1100",
        "medium": "Tempera, gold, and ink on parchment; leather binding",
        "image": "https://images.metmuseum.org/CRDImages/md/web-large/DP160636.jpg"
    },
    {
        "title": "Emperor Xuanzong's flight to Shu",
        "artist": "Unidentified artist",
        "date": "mid-12th century",
        "medium": "Hanging scroll; ink, color, and gold on silk",
        "image": "https://images.metmuseum.org/CRDImages/as/web-large/DP247676.jpg"
    },
    {
        "title": "Pepsi-Cola Company's annual exhibition : paintings of the year",
        "artist": "Pepsi-Cola Company",
        "date": "1946",
        "medium": "",
        "image": ""
    },
    {
        "title": "Old Plum",
        "artist": "Kano Sansetsu",
        "date": "1646",
        "medium": "Four sliding-door panels (fusuma); ink, color, gold, and gold leaf on paper",
        "image": "https://images.metmuseum.org/CRDImages/as/web-large/DT229.jpg"
    },
    {
        "title": "Royal processions, ceremonies and entertainments",
        "artist": "Court of King Mindon or Thibaw, or associated workshops",
        "date": "1870s\u20131880s",
        "medium": "Watercolor and gold on mulberry paper, with gilt lacquered wood covers and cloth lined box",
        "image": "https://images.metmuseum.org/CRDImages/as/web-large/DP-14374-040.jpg"
    },
    {
        "title": "Great Indian Fruit Bat",
        "artist": "Bhawani Das",
        "date": "ca. 1777\u201382",
        "medium": "Pencil, ink, and opaque watercolor on paper",
        "image": "https://images.metmuseum.org/CRDImages/is/web-large/DP167067.jpg"
    },
    {
        "title": "The Liar, the copy of the Liar - 1",
        "artist": "Francis Al\u00ffs",
        "date": "1991\u201394",
        "medium": "Enamel on metal sheet, oil on paperboard with masking tape and oil and wax on canvas glued to particle board",
        "image": ""
    },
    {
        "title": "Wall painting from the west wall of Room L of the Villa of P. Fannius Synistor at Boscoreale",
        "artist": "",
        "date": "ca. 50\u201340 BCE",
        "medium": "Fresco",
        "image": "https://images.metmuseum.org/CRDImages/gr/web-large/DP141474.jpg"
    },
    {
        "title": "Wall painting from Room H of the Villa of P. Fannius Synistor at Boscoreale",
        "artist": "",
        "date": "ca. 50\u201340 BCE",
        "medium": "Fresco",
        "image": "https://images.metmuseum.org/CRDImages/gr/web-large/DP105943.jpg"
    },
    {
        "title": "Bamboo in the Wind",
        "artist": "Yi Jeong (artist name: Taneun)",
        "date": "early 17th century",
        "medium": "Hanging scroll; ink on silk with gold on colophon",
        "image": "https://images.metmuseum.org/CRDImages/as/web-large/DP355790.jpg"
    },
    {
        "title": "Madonna and Child",
        "artist": "Giovanni Bellini",
        "date": "late 1480s",
        "medium": "Oil on wood",
        "image": "https://images.metmuseum.org/CRDImages/ep/web-large/DT375.jpg"
    },
    {
        "title": "Wall painting on black ground: landscape, from the imperial villa at Boscotrecase",
        "artist": "",
        "date": "last decade of the 1st century BCE",
        "medium": "Fresco",
        "image": "https://images.metmuseum.org/CRDImages/gr/web-large/DP146610.jpg"
    },
    {
        "title": "Wall painting: Perseus and Andromeda in landscape, from the imperial villa at Boscotrecase",
        "artist": "",
        "date": "last decade of the 1st century BCE",
        "medium": "Fresco",
        "image": "https://images.metmuseum.org/CRDImages/gr/web-large/DP138761.jpg"
    },
    {
        "title": "Condesa de Altamira and Her Daughter, Mar\u00eda Agustina",
        "artist": "Goya (Francisco de Goya y Lucientes)",
        "date": "1787\u201388",
        "medium": "Oil on canvas",
        "image": "https://images.metmuseum.org/CRDImages/rl/web-large/DP295708.jpg"
    },
    {
        "title": "Cardinal Fernando Ni\u00f1o de Guevara (1541\u20131609)",
        "artist": "El Greco (Domenikos Theotokopoulos)",
        "date": "ca. 1600",
        "medium": "Oil on canvas",
        "image": "https://images.metmuseum.org/CRDImages/ep/web-large/DP-17777-001.jpg"
    },
    {
        "title": "Cubiculum (bedroom) from the Villa of P. Fannius Synistor at Boscoreale",
        "artist": "",
        "date": "ca. 50\u201340 BCE",
        "medium": "Fresco",
        "image": "https://images.metmuseum.org/CRDImages/gr/web-large/DP143704.jpg"
    },
    {
        "title": "Clothing the Naked",
        "artist": "Michiel Sweerts",
        "date": "ca. 1661",
        "medium": "Oil on canvas",
        "image": "https://images.metmuseum.org/CRDImages/ep/web-large/DP-15762-001.jpg"
    }
]
    
    # We create a page-section for EACH artwork, so the user can scroll through them 1 by 1
    for idx, art in enumerate(artworks):
        if not art.get('image'):
            continue
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
