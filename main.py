"""
    Some Explanation of how the files are searched.
    if the user request some url like: http://example.org/test.html,
    then the program searches for test.html in the given docs' directory.

    if the user requests some url like: http://example.org/test,
    then the program searches for a directory named "test" with an index.[allowed_extensions] inside.
    NOTE: You can edit the allowed_extensions, so free feel to change them.

    if the user requests some url like http://example.org/index.php, and you activated php,
    then the programm searched for the php.exe in the given php_directory and executes the php file.
    After that, it will reply with the result.

    - INFO: If you used the set_cookie function, the script is parsed 2 Times. Why? If you want to access the cookie
            then PHP has to know there is one. And to do this, you have to run it twice.
"""
import socket

from ext.Server import Server


def connection(_s: socket.socket, addr: tuple, path: str) -> None:
    print(f'Connection from {addr[0]}, he wants to: {path}')


def main() -> None:
    server: Server = Server(docs_dir='docs', http_port=3033, on_connection=connection)
    server.activate_php(php_dir='C:\\php',
                        php_ini='c:\\php\\php.ini')
    server.start()


if __name__ == '__main__':
    main()
