import web

urls = (
    '/hello', 'index'
    )

app = web.application(urls, globals())

render = web.template.render('templates/')

class index:
    def GET(self):
        return render.hello_form()
    def POST(self):
        form = web.input(name="Nobody", greet="Hello")
        greeting = "%s, %s" % (form.greet, form.name)
        return render.index(greeting = greeting)

if __name__ == "__main__":
    app.run()
