import flask
from Book import Book
from flask import render_template as render
from flask import redirect

app=flask.Flask(__name__)


@app.route('/')
def home_page():
        return render('./home.html')


@app.route('/add-book', methods = ['POST' , 'GET'])
def add_book():
        if flask.request.method == 'GET' :
                return render('./add-book.html')
        elif flask.request.method == 'POST' :
                data = dict(flask.request.form)
                try:
                         Book(data['isbn'],data['title'],data['author'],data['price'],data['pages'])
                         return redirect('/')
                except Exception as e:
                         if len(e.args) == 2:
                                errorType = e.args[1]
                                errorMessage = e.args[0]
                         else:
                                errorType = 'sqlite3.IntegrityError'
                                errorMessage="isbn must be unique"
                         return render('add-book.html',book=dict(data),errorMessage=errorMessage,errorType=errorType)



@app.route('/all-books')
def all_books():
        books = Book.all_books()
        return render('all-books.html',books=books)



@app.route('/delete/<string:id>')
def delete_book(id):
        Book.delete(id)
        return redirect('/all-books')





@app.route('/update/<string:id>', methods = ['POST' , 'GET'])
def update_book(id):
        if flask.request.method == 'GET':
                book = Book.one_book(id)
                return render('add-book.html',book=book,id=id)
        else:
                book = dict(flask.request.form)
                try:
                        Book.validator_book(book['isbn'],book['title'],book['author'],book['price'],book['pages'])
                        Book.update_one_book(book)
                        return redirect('/all-books')
                except Exception as e:
                        return render('add-book.html',book=book,errorMessage=e.args[0],errorType=e.args[1])



@app.route('/find-book/')
def find_book():
        id = flask.request.args.get('id')
        if id:
                id = str(id)
                book = Book.one_book(id)
                if book:
                        return render('all-books.html',books=book)
                errorMessage= "there is no book with this id"
                return render('find-book.html',errorMessage=errorMessage)
        return render('find-book.html')


app.run()

