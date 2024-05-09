from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.image import Image

class TelaLogin(BoxLayout):
    def __init__(self, **kwargs):
        super(TelaLogin, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = [50, 20]
        self.spacing = 10

        Window.clearcolor = (0.7, 0.5, 0.9, 1)
        self.add_widget(Image(source='/Users/aluno.sesipaulista/Documents/PagLogin_Kivy/img_icone/th-removebg-preview.png'))

        self.add_widget(Label(text='LOGIN', font_size=24, color=(0, 0, 0, 1)))

        self.username_input = TextInput(hint_text='Usuário', multiline=False)
        self.password_input = TextInput(hint_text='Senha', password=True, multiline=False)
        self.add_widget(self.username_input)
        self.add_widget(self.password_input)

        self.buttons_layout = BoxLayout(padding=[0, 10], spacing=10)
        self.login_button = Button(text='Login', color=(0, 0, 0, 1), size_hint=(None, None), size=(450, 50),
                                   background_color=(100, 100, 100, 100))
        self.login_button.bind(on_press=self.login)
        self.signup_button = Button(text='Cadastre-se', color=(0, 0, 0, 1), size_hint=(None, None), size=(450, 50),
                                    background_color=(100, 100, 100, 100))
        self.signup_button.bind(on_press=self.abrir_tela_cadastro)
        self.buttons_layout.add_widget(self.login_button)
        self.buttons_layout.add_widget(self.signup_button)
        self.add_widget(self.buttons_layout)

    def login(self, instance):
        username = self.username_input.text
        password = self.password_input.text
        print('Username:', username)
        print('Password:', password)

    def abrir_tela_cadastro(self, instance):
        self.clear_widgets()
        self.add_widget(Label(text='CADASTRO', font_size=24, color=(0, 0, 0, 1)))

        self.nome_input = TextInput(hint_text='Nome', multiline=False)
        self.email_input = TextInput(hint_text='E-mail', multiline=False)
        self.celular_input = TextInput(hint_text='Celular', multiline=False)
        self.password_input = TextInput(hint_text='Senha', password=True, multiline=False)
        self.add_widget(self.nome_input)
        self.add_widget(self.email_input)
        self.add_widget(self.celular_input)
        self.add_widget(self.password_input)

        cadastrar_button = Button(text='Cadastrar', color=(0, 0, 0, 1), size_hint=(None, None), size=(450, 50),
                                  background_color=(100, 100, 100, 100))
        cadastrar_button.bind(on_press=self.cadastrar)
        self.add_widget(cadastrar_button)

        voltar_button = Button(text='Voltar para o Login', color=(0, 0, 0, 1), size_hint=(None, None), size=(450, 50),
                               background_color=(100, 100, 100, 100))
        voltar_button.bind(on_press=self.voltar_para_login)
        self.add_widget(voltar_button)

    def cadastrar(self, instance):
        nome = self.nome_input.text
        email = self.email_input.text
        celular = self.celular_input.text
        password = self.password_input.text
        print('Novo usuário cadastrado:')
        print('Nome:', nome)
        print('E-mail:', email)
        print('Celular:', celular)
        print('Password:', password)

    def voltar_para_login(self, instance):
        self.clear_widgets()
        self.add_widget(Label(text='LOGIN', font_size=24, color=(0, 0, 0, 1)))
        self.add_widget(self.username_input)
        self.add_widget(self.password_input)
        self.add_widget(self.buttons_layout)

class MyApp(App):
    def build(self):
        return TelaLogin()

if __name__ == '__main__':
    MyApp().run()