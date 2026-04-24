from nicegui import ui

def render_history():
    # History Section
    with ui.column().classes('page-section w-full bg-[#f4f1ea] py-20 px-6 font-sans justify-center').style('min-height: calc(100vh - 64px);'):
        with ui.column().classes('max-w-5xl mx-auto w-full').props('id=history'):
            ui.label('History of the Museum').classes('text-4xl font-bold mb-16 text-center w-full uppercase tracking-widest text-[#8b0000] font-serif')
            
            with ui.timeline().classes('w-full ml-0 md:ml-20'):
                with ui.timeline_entry('1866', title='The Initial Idea', icon='lightbulb', color='red-9').classes('text-xl'):
                    ui.label("The idea to create a museum came from Paris during a dinner of important American personalities. The most famous among them was the lawyer John Jay, who championed the idea. His vision was to create a national institution and art gallery to educate the American people.").classes('text-gray-800 mt-2')
                
                with ui.timeline_entry('April 13, 1870', title='Official Foundation', icon='account_balance', color='red-9').classes('text-xl'):
                    ui.label("The MET was officially founded. Its very first acquisition was a remarkable Roman sarcophagus, marking the beginning of its vast collection.").classes('text-gray-800 mt-2')
                    
                with ui.timeline_entry('March 30, 1880', title='Moving to Central Park', icon='location_on', color='red-9').classes('text-xl'):
                    ui.label("The museum expanded and moved to its current iconic location at Fifth Avenue and 82nd Street, next to beautiful Central Park.").classes('text-gray-800 mt-2')
