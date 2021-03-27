# CherryPy


## Config notes

With base app.

```python
class Root(object):
    @cherrypy.expose
    def index(self):
        return "Hello World!"

cherrypy.root = Root()
```

### Single config

You can customized with a single file. Note this must be a keyword otherwise it thinks this is a string.

```
cherrypy.quickstart(Root(), config='http_and_engine.conf')
```

- `http_and_engine.conf`
    ```init
    [global]
    server.socket_port: 9092
    engine.timeout_monitor.frequency: 20

    [/]
    tools.gzip.on: True
    ```

### Multiple configs

```python
# Global settings.
cherrypy.config.update('engine.conf')

# Mount specific settings.
h = os.path.abspath('http.conf')
print h
cherrypy.tree.mount(cherrypy.root, '/', config=h)

cherrypy.engine.start()
cherrypy.engine.block()
```

- `engine.conf`
    ```ini
    [global]
    server.socket_port: 9092
    engine.timeout_monitor.frequency: 20
    ```
- `http.conf`
    ```ini
    [/]
    tools.gzip.on: True
    ```
    
### Object config

```python
conf = {
    # you will get an error for socket at '/'
    'global': {
        'tools.sessions.on': True,
        'server.socket_port':9099
    }
}

cherrypy.config.update(conf)
cherrypy.quickstart(Root())
```
