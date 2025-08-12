

class Token:
    def __init__(self, x, y, font):
        self.x = x
        self.y = y
        self.font = font


class Layout:
    def __init__(self, tokens=[]):
        self.display = []
        self.tokens = tokens
        

    def layout(self, text, tokens):
        self.width = self.win.winfo_width
        self.height = self.win.winfo_height
        font = tkinter.font.Font()
        display_list = []


    def display_list(self):
        for t in self.tokens:
            if isinstance(t, Text):
                weight = "normal"
                style = "roman"
                for word in t.text.split():
                    w =  self.bi_times.measure(word)
                    if self.cursor_x + w > self.width - self.margin_x:
                        self.cursor_y += self.bi_times.metrics('linespace')*1.25
                        self.cursor_x = self.margin_x
                    
                    self.display_list.append((self.cursor_x, self.cursor_y, word, font))
                    self.cursor_x += w + Browser().bi_times.measure(" ")

    def x():
        for t in tokens:
            if isinstance(t, Text):
                weight = "normal"
                style = "roman"
                for word in t.text.split():
                    w =  self.bi_times.measure(word)
                    if self.cursor_x + w > self.width - self.margin_x:
                        self.cursor_y += self.bi_times.metrics('linespace')*1.25
                        self.cursor_x = self.margin_x
                    
                    display_list.append((self.cursor_x, self.cursor_y, word, font))
                    self.cursor_x += w + font(" ")

            
            elif isinstance(t, Tag):
                pass

            for word in text.split():
                w =  self.bi_times.measure(word)
                if self.cursor_x + w > self.width - self.margin_x:
                    self.cursor_y += self.bi_times.metrics('linespace')*1.25
                    self.cursor_x = self.margin_x
                
                display_list.append((self.cursor_x, self.cursor_y, word, font))
                self.cursor_x += w + font(" ")
