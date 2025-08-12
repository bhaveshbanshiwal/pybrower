import tkinter
from URL_REQUEST import *
from html_simplify import *
import tkinter.font



class Browser:
    def __init__(self, width=1000, height=500):
        self.win = tkinter.Tk()
        self.f_size = 11
        self.margin_x = 50
        self.margin_y = 50
        self.cursor_x = self.margin_x
        self.cursor_y = self.margin_y
        self.width = width
        self.height = height
        self.browser_frame = None
        self.display_list = []
        self.content = {}
        self.css = {}
        self.win.title('CX4 - Web browser')
        self.canvas = tkinter.Canvas(self.win
                                     , width=width
                                     , height=height
                                     )
        self.win.bind("<Down>", self.scrolldown)
        self.win.bind("<Return>", self.search)
        self.bi_times = tkinter.font.Font(family="consolas",
                                          size=14,weight="bold"
                                          ,)

        self.entry_box = tkinter.Entry(self.win, font=self.bi_times, width=70)
        self.entry_box.pack(padx=100, pady=5, anchor="n")
        self.canvas.pack(fill="both", expand=True)
        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)
        self.refresh = tkinter.Button(self.win, text='⟳', font=('consolas', 13, 'bold'), command=self.search)
        self.refresh.place(x=5, y=5)
        self.increase_size = tkinter.Button(self.win, text="+", font=('consolas', 13, 'bold'), width=3,command=self.increase_size_func)
        self.increase_size.place(x=45, y=5)
        self.decrease_size = tkinter.Button(self.win, text="-", font=('consolas', 13, 'bold'), width=3,command=self.decrease_size_func)
        self.decrease_size.place(x=90, y=5)




    def on_mousewheel(self, event):
        if event.num == 5 or event.delta < 0: 
            self.canvas.yview_scroll(3, "units")
        elif event.num == 4 or event.delta > 0:  
            self.canvas.yview_scroll(-3, "units")

    def increase_size_func(self):
        self.f_size += 1
        self.page_reset()
        self.load()

    def decrease_size_func(self):
        self.f_size -= 1
        self.page_reset()
        self.load()

    def load(self):
        try:
            self.win.title(self.content['title'])
        except:
            self.win.title(self.entry_box.get())
        
        self.width = self.win.winfo_width()
        self.height = self.win.winfo_height()

        for tag in ['h1', 'h2', 'h3','p']:
            if tag not in self.content.keys():
                continue
            fill = "black"
            font_size = self.f_size
            if tag in self.css.keys():
                # Perform CSS on words
                # As for now no CSS except font is applied
                if 'background-color' in self.css.keys():
                    fill = self.css[tag]['background-color']
                if 'font-size' in self.css.keys():
                    font_size = int(self.css[tag]['font-size'][0:len(self.css[tag]['font-size']-1)])
                
                


            if type(self.content[tag]) == list:
                content_list = self.content[tag]
            else:
                content_list = [self.content[tag], ]

            f_font = tkinter.font.Font(family="consolas",
                                          size=font_size
                                          ,)
            for line in content_list:
                for word in line.replace("\n", " ").split():
                    w = f_font.measure(word)
                    space_w = f_font.measure(" ")

                    # Wrap to next line if word won't fit
                    if self.cursor_x + w > self.width - self.margin_x:
                        self.cursor_y += f_font.metrics('linespace') * 1.25
                        self.cursor_x = self.margin_x

                    # Draw the word at current position
                    self.display_list.append((self.cursor_x, self.cursor_y, word, f_font , fill))

                    # Move cursor to the right
                    self.cursor_x += w + space_w

                    

            self.cursor_x = self.margin_x
            self.cursor_y += self.bi_times.metrics('linespace')*1.5

        return self.draw()
        
    def page_reset(self):
        self.cursor_x = self.margin_x
        self.cursor_y = self.margin_y
        self.canvas.delete('all')
        self.display_list = []
        return True


    def scrolldown(self, inp):
        print("Scrolled")

    def search(self, url=None):
        self.page_reset()
        inp = self.entry_box.get()
        body = URL(inp).request()
        self.content = Seperate(body)
        css_text = CSS_Scrapper(body)
        self.css = CSS_display_list(css_text)
        return self.load()
    
    def draw(self):
        self.canvas.delete('all')

        for i in self.display_list:
            self.canvas.create_text(i[0], i[1], font=i[3], text=i[2], fill=i[4], anchor='nw')
        self.canvas.config(scrollregion=(0, 0, self.width, self.cursor_y + 100))
        return True



if __name__ == "__main__":
    win1 = Browser()
    tkinter.mainloop()

