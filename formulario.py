import web
from web import form

urls = (
    '/', 'index'
)
 
plantilla = web.template.render('./templates/')
 
app = web.application(urls, globals())
 
myform = form.Form(
    form.Textbox("nombre"),
    form.Textbox("id",
    form.notnull,
    form.regexp('\d+', 'Debe ser un digito'),
    form.Validator('Debe ser mas de 5', lambda x:int(x)>5)),
    form.Textarea('observacion'),
    form.Checkbox('reenviar'),
    form.Dropdown('prioridad', ['baja', 'media', 'alta'])
)

class index:
    def GET(self):
        form = myform()
        return plantilla.formulario_1(form)
 
 
if __name__ == "__main__":
    app.run()