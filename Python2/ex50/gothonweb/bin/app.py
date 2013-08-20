import web, datetime, os


urls = (
    '/', 'Index',
    '/hello', 'SayHello',
    '/image', 'Upload',
    )

app = web.application(urls, globals())

render = web.template.render('templates/', base="layout")


class Index:
    def GET(self):
        return render.index()


class SayHello:
    def GET(self):
        return render.hello_form()
    def POST(self):
        form = web.input(name="Nobody", greet="Hello")
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
        with open(filename, 'wb') as f:
            f.write(form['myfile'].file.read())
            f.close()
        return render.show(filename = filename)
        

if __name__ == "__main__":
    app.run()
