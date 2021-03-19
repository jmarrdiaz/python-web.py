import web
from web import form

render = web.template.render('templates/')

urls = (
'/', 'index'
)

app = web.application(urls, globals())


class index:
    def GET(self):
        i = web.input(nombre=None)
        return render.index(i.nombre)



if __name__ == "__main__":
    app.run()