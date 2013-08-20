import web

urls = (
    '/', 'index'
    )

app = web.application(urls, globals())

render = web.template.render('templates/')

class index:
    def GET(self):
        words = "Yet another website engine"
        greeting = "Hello world"
        #return render.index(greeting = greeting)
        return render.foo(word = words)

if __name__ == "__main__":
    app.run()
