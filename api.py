import sys
import sqlite3
import datetime
from bottle import route, run, template, static_file
from bottle import get, put, delete, post, request

db = sqlite3.connect('./db/todo.db')
cur = db.cursor()


@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./static/')


@route('/')
def index():
    rows = cur.execute('SELECT * FROM todo ORDER BY datetime ASC')
    return template('index.tpl', rows=rows)


@route('/test')
def index():
    return '<b> It works</b>'


@route('/new', method=['GET', 'POST'])
def new_task():
    if request.POST.get('save', '').strip():
        todo_title = request.POST.get('task')
        todo_desc = request.POST.get('desc')
        todo_datetime = datetime.datetime.now()
        rec = cur.execute('INSERT INTO todo VALUES (NULL , ?, ?, ?)', (todo_title, todo_desc, todo_datetime))
        db.commit()
        rows = cur.execute('SELECT * FROM todo ORDER BY datetime ASC')
        return template('index.tpl', rows=rows)
    else:
        return template('newtask.tpl')


@route('/item/<id>')
def show_task(id):

    item = cur.execute("""SELECT title, description, datetime FROM todo WHERE id=?""", (id,)).fetchone()
    t_title = item[0]
    t_desc = item[1]
    if item[2]:
        t_date = datetime.datetime.strptime(item[2], "%Y-%m-%d %H:%M:%S.%f").strftime("%A %d %B %Y - %I:%M %p")
    else:
        t_date = datetime.datetime.now()
    if not item:
        return "This Item number doesn't exit!"
    else:
        return template('task.tpl', title=t_title, desc=t_desc, date=t_date, id=id)


@route('/edit/<id>', method=['GET', 'POST'])
def edit_task(id):
    if request.POST.get('save'):
        todo_title = request.POST.get('task')
        todo_desc = request.POST.get('desc')
        todo_datetime = datetime.datetime.now()
        rec = cur.execute('UPDATE todo SET title=?, description=?, datetime=? WHERE id=?', (todo_title, todo_desc,
                                                                                            todo_datetime, id))
        db.commit()
        rows = cur.execute('SELECT * FROM todo ORDER BY datetime ASC')
        return template('index.tpl', rows=rows)
    else:
        rec = cur.execute('SELECT * FROM todo WHERE id=?', (id,)).fetchone()
        title = rec[1]
        desc = rec[2]
        return template('edit.tpl', id=id, title=title, desc=desc)


@route('/about')
def about():
    return template('about.tpl')


run(host='localhost', port='8080', debug=True, reloader='True')
