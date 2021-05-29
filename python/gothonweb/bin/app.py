import web

urls = ( '/', 'index')
app = web.applications(urls, globals())

class index:
    def GET(self):
        greeting = 'Hello world!'
        return greeting

if __name__ == "__main__":
    app.run

### The libraries for this ex are made for python 2.7
### I couldnt find all of them for python 3 so I'll stop here     
