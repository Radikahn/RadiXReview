import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        #call gridlayout constructor
        super(MyGridLayout, self).__init__(**kwargs)
        
        #set columns
        self.cols = 2
        
        #Ask user for product details
        self.add_widget(Label(text = "Product (Brand, Model):"))
        
        #input box for product name and model
        self.product = TextInput(multiline=False)
        self.add_widget(self.product)
        
        #Ask user for word list
        self.add_widget(Label(text = 'Enter Key Words to Search For:\n(comma seperated Ex: "broken,not working,restart)'))
        
        #input box for user wordlist
        self.user_words = TextInput(multiline = False)
        self.add_widget(self.user_words)
        
        #Submit button
        self.submit = Button(text = "Submit", font_size = 24)
        
        #button mapp/bind
        self.submit.bind(on_press = self.data_save)
        
        self.add_widget(self.submit)

    def data_save(self, instance):
        product = self.product.text
        key_words = self.user_words.text
        
        with open("Web Files/user_search_words.txt", 'w') as file:
            file.write(key_words)
            file.close()
            
        with open("Web Files/search_query.txt", 'w') as file:
            file.write(product)
            file.close
        
class MyApp(App):
    def build(self):
        return MyGridLayout()
    

if __name__ == '__main__':
    MyApp().run()