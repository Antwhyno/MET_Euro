from nicegui import ui

def render_masterpieces():
    masterpieces = [
        {
            "title": "Washington Crossing the Delaware",
            "artist": "Emanuel Leutze",
            "date": "1851",
            "medium": "Oil on canvas • 378.5 × 647.7 cm",
            "description": "Leutze's monumental painting commemorates General Washington's surprise attack at the Battle of Trenton on December 26, 1776. Painted in Düsseldorf to inspire European liberal reformers, it is one of the most iconic images of American history, now a highlight of the MET's American Wing.",
            "image": "assets/painture.jpeg"
        },
        {
            "title": "The Broncho Buster",
            "artist": "Frederic Remington",
            "date": "1895",
            "medium": "Bronze sculpture",
            "description": "Remington's very first sculpture and the first bronze ever cast of a cowboy. It depicts a rugged rider struggling to control a rearing horse, captured with explosive energy. A cast was famously gifted to President Theodore Roosevelt by his Rough Riders regiment. The MET holds multiple casts of this iconic American work.",
            "image": "assets/painture2.jpeg"
        },
        {
            "title": "Crown of the Andes",
            "artist": "Colombian goldsmiths",
            "date": "17th–18th century",
            "medium": "Gold, 442 Colombian emeralds",
            "description": "This magnificently elaborate crown, adorned with 442 Colombian emeralds, is one of the most important surviving examples of colonial South American goldsmithing. According to tradition, it was crafted to give thanks to the Virgin Mary following the city of Popayán's survival of a smallpox epidemic. Now one of the MET's most treasured jewels.",
            "image": "assets/painture3.jpeg"
        },
        {
            "title": "The Veteran in a New Field",
            "artist": "Winslow Homer",
            "date": "1865",
            "medium": "Oil on canvas",
            "description": "Painted immediately after the Civil War, this poignant work shows a Union Army veteran harvesting wheat with a scythe — the traditional symbol of Death. The discarded army jacket at his feet confirms his identity. Homer transforms a hopeful scene of renewal into a meditation on the immense human cost of war.",
            "image": "assets/painture4.jpeg"
        },
        {
            "title": "The Gulf Stream",
            "artist": "Winslow Homer",
            "date": "1899, reworked 1906",
            "medium": "Oil on canvas",
            "description": "Homer's most dramatic seascape depicts a Black man adrift on a dismasted boat, surrounded by sharks, with a waterspout on the horizon. The MET describes it as a powerful allegory of human endurance against the relentless forces of nature. Homer famously refused to explain the painting's narrative, calling it a 'marine puzzle'.",
            "image": "assets/painture5.jpeg"
        },
        {
            "title": "Madame X (Madame Pierre Gautreau)",
            "artist": "John Singer Sargent",
            "date": "1883–84",
            "medium": "Oil on canvas",
            "description": "Sargent's celebrated portrait of the Parisian socialite Virginie Gautreau caused a scandal at the 1884 Paris Salon due to its daring pose and low-cut gown. Sargent himself considered it one of his finest works. He sold it to the MET in 1916, where it remains a masterpiece of the American collection.",
            "image": "assets/painture6.jpeg"
        },
        {
            "title": "Self-Portrait with a Straw Hat",
            "artist": "Vincent van Gogh",
            "date": "1887",
            "medium": "Oil on canvas",
            "description": "During his two years in Paris, van Gogh painted over twenty self-portraits, using himself as a model for lack of funds. This work reflects his growing mastery of Neo-Impressionist color theory, with its vibrant palette of yellows, oranges and blues. Interestingly, the other side of this canvas bears an earlier work, 'The Potato Peeler'.",
            "image": "assets/painture7.jpeg"
        },
        {
            "title": "Hagar in the Wilderness",
            "artist": "Jean-Baptiste-Camille Corot",
            "date": "1835",
            "medium": "Oil on canvas",
            "description": "This large-scale biblical landscape depicts the dramatic moment from Genesis when Hagar and her son Ishmael, banished into the desert by Abraham's wife Sarah, are on the verge of perishing from thirst. An angel appears in the sky to guide them to water. Corot's masterful use of light and shadow gives the arid wilderness a profound sense of divine presence.",
            "image": "assets/painture8.jpeg"
        },
    ]

    for idx, piece in enumerate(masterpieces):
        bg_color = "#0a0a0a" if idx % 2 == 0 else "#0f0f1a"
        with ui.column().classes('page-section w-full relative overflow-hidden items-center justify-center').style(f'min-height: calc(100vh - 64px); background-color: {bg_color};').props(f'id=masterpiece-{idx}'):
            # Blurred background
            ui.image(piece['image']).style('position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; filter: blur(30px); opacity: 0.25; z-index: 1;')

            # Content row: image left, text right
            with ui.row().classes('w-full max-w-6xl mx-auto px-8 items-center gap-12 z-10').style('position: relative; z-index: 2;'):
                # Painting image
                ui.image(piece['image']).style(
                    'max-height: 80vh; max-width: 55%; object-fit: contain; border-radius: 12px;'
                    'box-shadow: 0 20px 60px rgba(0,0,0,0.9); flex-shrink: 0;'
                )

                # Text panel
                with ui.column().classes('flex-1 gap-4'):
                    # Artist + date pill
                    with ui.row().classes('items-center gap-3 mb-2'):
                        ui.label(piece['artist']).classes('text-[#c0392b] font-bold text-xl font-sans uppercase tracking-widest')
                        ui.label('•').classes('text-gray-500 text-xl')
                        ui.label(piece['date']).classes('text-gray-400 font-sans text-lg italic')

                    # Title
                    ui.label(piece['title']).classes('text-4xl font-bold text-white font-serif leading-tight mb-2')

                    # Medium
                    if piece['medium']:
                        ui.label(piece['medium']).classes('text-gray-500 font-sans text-base mb-4 italic')

                    # Separator
                    ui.element('div').style('width: 60px; height: 3px; background: #8b0000; border-radius: 2px; margin-bottom: 1rem;')

                    # Description
                    ui.label(piece['description']).classes('text-gray-300 font-sans text-lg leading-relaxed')

                    # MET link badge
                    ui.label('📍 The Metropolitan Museum of Art, New York').classes('text-gray-500 text-sm mt-6 font-sans italic')
