from nicegui import app, ui
from pages.hero import render_hero
from pages.presentation import render_presentation
from pages.history import render_history
from pages.media import render_media
from pages.ranking import render_ranking
from pages.artworks import render_artworks

# Configure page
app.add_static_files('/assets', 'assets')

# Background color and fonts using generic CSS in nicegui
ui.add_head_html("""
<style>html { scroll-behavior: smooth; } body { background-color: #fdfbf7; color: #1a1a1a; font-family: "Georgia", serif; margin: 0; padding: 0; }</style>
<script>
document.addEventListener('keydown', function(event) {
    if (['Shift', 'Control', 'Alt', 'Meta'].includes(event.key)) return;
    
    const sections = Array.from(document.querySelectorAll('.page-section'));
    if (sections.length === 0) return;

    // Calculer la section actuellement affichée (la plus proche du haut de l'écran + offset du header)
    const headerOffset = 64; // h-16
    let currentIdx = 0;
    let minDiff = Infinity;
    
    sections.forEach((sec, idx) => {
        const rect = sec.getBoundingClientRect();
        const diff = Math.abs(rect.top - headerOffset);
        if (diff < minDiff) {
            minDiff = diff;
            currentIdx = idx;
        }
    });

    let targetIdx = currentIdx;
    
    if (event.key === 'ArrowUp' || event.key === 'PageUp') {
        event.preventDefault();
        targetIdx = Math.max(0, currentIdx - 1);
    } else {
        if (event.key === 'ArrowDown' || event.key === 'PageDown' || event.key === ' ') {
            event.preventDefault();
        }
        // Pour toute autre touche ou espace/flèche bas, on descend
        targetIdx = Math.min(sections.length - 1, currentIdx + 1);
    }

    if (targetIdx !== currentIdx) {
        const target = sections[targetIdx];
        const targetPosition = target.getBoundingClientRect().top + window.scrollY - headerOffset;
        window.scrollTo({
            top: targetPosition,
            behavior: 'smooth'
        });
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
render_hero()

# Presentation Section
render_presentation()

# Global Ranking Section
render_ranking()

# History Section
render_history()

# Artworks Section
render_artworks()

# Media Section             ###
render_media()

# Footer
with ui.row().classes('w-full p-8 bg-[#1a1a1a] text-center justify-center font-sans mt-10'):
    ui.label('Exposition of the MET • Antoine').classes('text-gray-400')

# On ajoute le host et le port spécifique pour Hugging Face
ui.run(title="The MET - Exposition", favicon="🏛️", host="0.0.0.0", port=7860)