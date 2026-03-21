
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class LanaSecurityApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='LANA SECURITY CORE', font_size='24sp'))
        layout.add_widget(Label(text='Status: Monitoring Jaringan Aktif'))
        return layout

if __name__ == '__main__':
    LanaSecurityApp().run()
