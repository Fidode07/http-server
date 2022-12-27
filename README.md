<p align="center">
  <img src='https://raw.githubusercontent.com/Fidode07/ImageHost/main/httpserv.png' alt='HTTPServ Logo' width=500>
</p>

# 📱 HTTPServ 📱
A powerfull web server (GET and POST supported), with PHP, SASS and CSS integration. Only built-in libraries were used and the usage is extremely simple.

# 🖊️ Features 🖊️
- PHP Support
- SASS/SCSS Support
- Events
- Only Built-In Libraries

# 📙 Usage 📙
First you need to create a folder. In this folder you will find the files that should be accessible via the web server. Then we import the server class:
```py
from ext.Server import Server
```

Now you only have to start it.
There are 2 ways to boot the server. The first is to load it static. That means PHP is not usable. This requires only 2 lines of code:
```python
server: Server = Server(docs_dir='docs', http_port=3033)
server.start()
```
The second way would be to start it with PHP. PHP should already be installed for this, but it doesn't matter if it is in the PATH or not. It is only important that the php-cgi.exe file exists in the given folder.
```python
server: Server = Server(docs_dir='docs', http_port=3033)
server.activate_php(php_dir='C:\\php',
                    php_ini='C:\\php\\php.ini')
server.start()
```

# 🎆 Events 🎆
Events must be specified during initialization. The given method must accept ``socket.socket``, ``tuple`` and ``str``.
```python
def on_connect(s: socket.socket, addr: tuple, target_location: str) -> None:
    print(f'Connection from {addr}, target_location is {target_location}')
    
server: Server = Server(docs_dir='docs', http_port=3033, on_connection=connection)
server.start()
```

# 🏳 Whitelist other extensions 🏳
To save performance and increase security, I have implemented a whitelist. One determines which file extensions are processed as HTML files and the other decides which have to go through the PHP interpreter. It is of GREAT importance that an extension does not appear in both lists.
<h3>HTML-Parser:</h3>
To add a file extension to the HTML parser, simply do:

```python
server.whitelist_static_extension('.extension')
```

To remove a file extension from the HTML parser, simply do:

```python
server.remove_from_whitelist_static('.extension')
```
<h3>PHP-Parser</h3>
To add a file extension to the PHP parser, just do:

```python
server.whitelist_php_extension('.extension')
```
To remove a file extension from the PHP parser, you can simply do:

```python
server.remove_from_whitelist_php('.extension')
```
# 🚨 Errors 🚨
Ehmmmm okay, before you all start yelling at me, I'm sorry. I really messed up the error handling, I'll make it better sometime. But hey, you can change the error 404 page. How?:

```python
server.error_pages['404'] = 'your/new/path.html' # Currently only Static Files are Supported
```

# 🔎 Wait ... HOW??? 🔎
Okay, now you know how to execute it. But wait ... How does the file search work exactly? Well, it's simple. Let's assume the user goes to the url ``http://example.org/test.php``. Then the Docs dir is searched for the ``test.php``. 

But wait, what happens when the user goes to a URL like ``http://example.org/home``? Well, then the Docs dir is searched for a directory called ``home``. And in this ``home`` directory an ``index.*`` is searched (every extension that is on the whitelist is scanned).
