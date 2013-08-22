import web, datetime, os
from bin import map

urls = (
    '/', 'Index',
    '/hello', 'SayHello',
    '/image', 'Upload',
    '/game', 'GameEngine',
    '/entry', 'Entry'
    )

app = web.application(urls, locals())

# little hack so that debug mode works with sessions
if web.config.get('_session') is None:
    store = web.session.DiskStore('sessions')
    session = web.session.Session(app, store,
                                  initializer={'room': None, 'name': 'Jedi'})
    web.config._session = session
else:
    session = web.config._session
    
render = web.template.render('templates/', base="layout")

class Index:
    def GET(self):
        return render.index()


class SayHello:
    def GET(self):
        return render.hello_form()
    def POST(self):
        form = web.input(name="Nobody", greet="hello")
        if form.name == '':
            form.name = "Nobody"
        if form.greet == '':
            form.greet = "Hello"
        greeting = "%s, %s" % (form.greet, form.name)
        return render.hello(greeting = greeting)


class Upload:
    ''' using cgi to upload and show image '''
    def GET(self):
        return render.upload_form()
    def POST(self):
        form = web.input(myfile={})
        # web.debug(form['myfile'].file.read())
        # get the folder name
        upload_time = datetime.datetime.now().strftime("%Y-%m-%d")
        # create the folder
        folder = os.path.join('./static', upload_time)
        if not os.access(folder, 1):
            os.mkdir(folder)
        # get the file name
        filename = os.path.join(folder, form['myfile'].filename)
        print(type(form['myfile']))
        with open(filename, 'wb') as f:
            f.write(form['myfile'].file.read())
            f.close()
        return render.show(filename = filename)


class count:
    def GET(self):
        session.count += 1
        return str(session.count)


class reset:
    def GET(self):
        session.kill()
        return ""


class Entry(object):
    def GET(self):
        return render.entry()
    def POST(self):
        form = web.input(name="Jedi")
        if form.name != '':
            session.name = form.name
        session.room = map.START
        #session.description = session.room.description
        web.seeother("/game")
    

class GameEngine(object):

    def GET(self):
        if session.room:
            return render.show_room(room=session.room, name=session.name)
        else:
            # why is there here? do you need it?
            return render.you_died()

    def POST(self):
        form = web.input(action=None)

        # there is a bug here, can you fix it?
        web.debug(session.room.name)
        if session.room and session.room.name != "The End" and form.action:
            session.room = session.room.go(form.action)

        web.seeother("/game")

if __name__ == "__main__":
    app.run()
