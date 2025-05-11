import sqlite3




class Book:

        def __init__(self,isbn,title,author,price,pages) -> None:
                Book.validator_book(isbn,title,author,price,pages)
                self.isbn = isbn
                self.title = title
                self.author = author
                self.price = price
                self.pages = pages
                self.save()

       

        @staticmethod
        def validator_book(isbn,title,author,price,pages):
                if len(isbn) != 8:
                        raise Exception("isbn must be 8 character",'isbn')
                if len(title) <= 3 or   not(title.upper().isupper()):
                        raise Exception("title must be 4 character and atleast have one alphabet character",'title')
                if not(author.upper().isupper()):
                        raise Exception("author must have one alphabet character",'author')
                if (price.upper().isupper()):
                        raise Exception("author must be number",'price')
                if (pages.upper().isupper()):
                        raise Exception("author must be number",'pages')
                return True
                

        def save(self):
                data={'isbn': self.isbn,
                 'title': self.title,
                 'author': self.author,
                 'price': self.price,
                 'pages': self.pages}
                Book.run_sql("""INSERT INTO book VALUES(:isbn , :title 
                , :author , :price , :pages)""",data)


        @staticmethod
        def one_book(id):
                data = Book.run_sql('SELECT rowid, * FROM book WHERE rowid = ?', (id,)) 
                data = Book.dict_factory(data)     
                return data


        @staticmethod
        def update_one_book(data):
                Book.run_sql("""UPDATE book SET isbn=? , title= ? , author=?, price=?, pages= ?
                             WHERE rowid= ?""",(data['isbn'],data['title'],data['author'],data['price'],data['pages'],data['id']))        


        @staticmethod
        def all_books():
                data = Book.run_sql('SELECT rowid , * FROM book')
                data = Book.dict_factory(data)
                return data

        @staticmethod
        def delete(id):
                return Book.run_sql('DELETE FROM book WHERE rowid = ?',(id,))
                
        
        @staticmethod
        def run_sql(sql,values= None):
                try:
                        connection = sqlite3.connect('./bookApp.sqlite.db')
                        cursor = connection.cursor()
                        if values:
                                result = cursor.execute(sql,values).fetchall() 
                        else:
                                result = cursor.execute(sql).fetchall() 
                        connection.commit()
                except Exception as e:
                        connection.close()
                        raise e
                return result
        

        @staticmethod 
        def dict_factory(list_items):
                d = dict()
                if len(list_items) != 1:
                        result = list()
                        for item in list_items:
                                d['id']=item[0]
                                d['isbn']=item[1]
                                d['title']=item[2]
                                d['author']=item[3]
                                d['price']=item[4]
                                d['pages']=item[5]
                                result.append(d)
                                d=dict()
                        return result
                else:
                        item = list_items[0]
                        d['id']=item[0]
                        d['isbn']=item[1]
                        d['title']=item[2]
                        d['author']=item[3]
                        d['price']=item[4]
                        d['pages']=item[5]
                        return d


              














