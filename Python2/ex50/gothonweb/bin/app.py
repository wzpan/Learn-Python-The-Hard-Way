import web

urls = (
    '/', 'index'
    )

app = web.application(urls, globals())

render = web.template.render('templates/')

class index:
    def GET(self):
        form = web.input(greet="Hello", name="Nobody")
        words = "Yet another website engine"
        greeting = "%s, %s" % (form.greet, form.name)
        return render.index(greeting=greeting)
        # return render.foo(word = words)

if __name__ == "__main__":
    app.run()
