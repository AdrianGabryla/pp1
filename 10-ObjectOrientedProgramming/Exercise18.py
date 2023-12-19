class eBook():
    def __init__(self):
        self.author = "Orwell"
        self.title = "1984"
        self.num_of_pages = 254
        self.current_page = 0
        self.open = False
    def open(self):
        self.open = True 
    def close(self):
        self.open = False
    def status(self):
        if self.open == True:    
            return f"Title: {self.title}\nAuthor: {self.author}\nPage number: {self.num_of_pages}\n Current page: {self.current_page}"
        else:
            return f"The book is closed"
    def next_page(self):
        if self.open == True:    
            if self.current_page < self.num_of_pages:
                self.current_page += 1
            else:
                return f"The end"
        else:
            return f"The book is closed"
    def previous_page(self):
        if self.open == True:    
            if self.current_page > 0:
                self.current_page -= 1
            else:
                return f"Start reading"
        else:
            return f"The book is closed"
    
ebook = eBook()
ebook.status()
ebook.open()
for i in range(254):
    ebook.next_page()
ebook.status()
