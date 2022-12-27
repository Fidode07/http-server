import socket
import sys
from datetime import datetime
from ext.exceptions import *
import _thread
import os
import subprocess
from typing import *


class Server:
    def __init__(self, docs_dir: str, host: str = '0.0.0.0', http_port: int = 5055,
                 on_connection: Union[Callable[[socket.socket, tuple, str], None], None] = None) -> None:
        self.__port = http_port
        self.__docs_dir: str = docs_dir
        self.__host: str = host

        self.error_pages: dict = {'404': 'default/404.html'}
        self.allowed_extensions: list = ['.html', '.css', '.js', '.htm', '.sass', '.scss']
        self.php_parsed_extensions: list = ['.php']

        self.__root_dir: str = os.path.abspath(self.__docs_dir)

        if not os.path.isdir(self.__root_dir):
            raise InvalidDocsDir(f'Can\'t find a Docs Directory at {self.__root_dir}')

        self.__php_allowed: bool = False
        self.__php_dir: str = ''
        self.__php_ini_path: str = ''

        self.__s: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__content_types: dict = content_types.copy()
        self.__on_connection: Union[Callable[[socket.socket, tuple, str], None], None] = on_connection

    def whitelist_php_extension(self, ext: str) -> None:
        if self.__invalid_extension(ext):
            raise InvalidFileExtension(f'Sorry, "{ext}" is not a valid File extension.')
        self.php_parsed_extensions.append(ext) if ext not in self.php_parsed_extensions else None

    def remove_from_whitelist_php(self, ext: str) -> None:
        self.php_parsed_extensions.remove(ext)

    def whitelist_static_extension(self, ext: str) -> None:
        if self.__invalid_extension(ext):
            raise InvalidFileExtension(f'Sorry, "{ext}" is not a valid File extension.')

    def remove_from_whitelist_static(self, ext: str) -> None:
        self.allowed_extensions.remove(ext)

    @staticmethod
    def __invalid_extension(ext: str) -> bool:
        return any(char in ext for char in [' ', '/', '<', '>', ';', '\'', '"', '\\', '?', '|', '*'])

    def get_php_state(self) -> bool:
        return self.__php_allowed

    def get_php_ini_path(self) -> str:
        return self.__php_ini_path

    def activate_php(self, php_dir: str, php_ini: str) -> None:
        if not os.path.isdir(os.path.abspath(php_dir)):
            raise PHPDirectoryNotFound('Unable to find PHP-Directory!')

        self.__php_dir = php_dir
        self.__php_ini_path = php_ini

        self.__php_allowed = True

    def disable_php(self) -> None:
        self.__php_allowed = False

    def __throw_404(self, c: socket.socket) -> None:
        error_page_path: str = os.path.abspath(self.error_pages['404'])
        if os.path.isfile(error_page_path):
            with open(error_page_path, encoding='utf-8') as f:
                c.send(b'HTTP/1.0 404 Not Found\n\n' + f.read().encode())
        else:
            c.send(b'HTTP/1.0 404 Not Found\n\n<h1>Sorry, unable to find this file!</h1>')

    def __handle(self, c: socket.socket, addr: tuple) -> None:
        data: bytes = c.recv(1024)
        h: str = data.decode()
        if not data:
            # The user doesn't send a header, so we only ignore him
            c.send(b'HTTP/1.0 400 Bad Request')
            c.close()
            return

        data: dict = dict(
            [[r.partition(':')[0].strip(), r.partition(':')[2].strip()] for r in h.split('\r\n')])  # noqa
        full_line: str = list(data.keys())[0]
        data['CORRECT_HEADER']: dict = data.copy()
        data['CORRECT_HEADER'].popitem()
        # The first line is everytime METHOD LOCATION HTTP-VERSION
        rq: list = full_line.split()

        data['REQUEST_URI']: str = rq[1]
        data['REQUEST_METHOD']: str = rq[0]
        data['REQUEST_TIME']: str = str(datetime.now())
        location: str = rq[1]

        try:
            p: str = location.split('?')[0]
            data['params']: str = location.split('?')[1]
        except IndexError:
            p: str = location
            data['params']: str = ''

        data['addr']: tuple = addr

        if p == '/':
            data['target_location']: str = '/index.*'
        else:
            l_list: list = p.split('.')
            if '.' + l_list[-1] in self.allowed_extensions and len(l_list) > 1:
                data['target_location'] = p
            elif len(l_list) == 1:
                # He tries to access some location without an ending
                if os.path.isdir(os.path.abspath(self.__docs_dir + p)):
                    for ext in self.allowed_extensions:
                        if os.path.isfile(os.path.abspath(f'{self.__docs_dir}/{p}/index{ext}')):
                            data['target_location'] = p + '/index' + ext
                            break
        if 'target_location' in data:
            path: str = os.path.abspath(self.__docs_dir + '/' + data['target_location'])
            if not os.path.isfile(path):
                if data['target_location'] == '/index.*':
                    # The user is on an url like: http://yourserver.com/directory, so we have to search for
                    # the index.* in the given directory.
                    handled: bool = False

                    if self.__php_allowed:
                        for ext in self.php_parsed_extensions:
                            check_path: str = self.__docs_dir + '/index' + ext
                            if os.path.isfile(check_path):
                                data['target_location'] = p + '/index' + ext
                                if self.__on_connection is not None:
                                    _thread.start_new_thread(self.__on_connection,
                                                             (c, addr, os.path.abspath(check_path)))
                                self.__handle_php(c=c,
                                                  data=data,
                                                  h=h,
                                                  path=check_path)
                                handled = True
                                break

                    if not handled:
                        for ext in self.allowed_extensions:
                            check_path: str = self.__docs_dir + '/index' + ext
                            if os.path.isfile(check_path):
                                if self.__on_connection is not None:
                                    _thread.start_new_thread(self.__on_connection,
                                                             (c, addr, os.path.abspath(check_path)))
                                self.__handle_html(c=c,
                                                   path=check_path)
                                break
                    self.__throw_404(c)
            else:
                if self.__on_connection is not None:
                    _thread.start_new_thread(self.__on_connection, (c, addr, path))
                handled: bool = False
                if self.__php_allowed:
                    for ext in self.php_parsed_extensions:
                        if path.endswith(ext):
                            self.__handle_php(c=c,
                                              data=data,
                                              h=h,
                                              path=path)
                            handled = True
                            break
                if not handled:
                    for ext in self.allowed_extensions:
                        if path.endswith(ext):
                            self.__handle_html(c=c,
                                               path=path)
                            break
                self.__throw_404(c)
        else:
            self.__throw_404(c)
        c.close()

    def start(self) -> None:
        self.__s.bind((self.__host, self.__port))
        self.__s.listen()
        print(f'Server listen on {self.__host}:{self.__port}')
        while True:
            cur_con, con_addr = self.__s.accept()
            _thread.start_new_thread(self.__handle, (cur_con, con_addr))

    def stop(self) -> None:
        self.__s.close()

    def __get_php_response(self, path: str, request_header: dict) -> bytes:
        request_header: dict = request_header.copy()
        key: str = list(request_header.keys())[0]

        request_header['method'] = key
        del request_header[key]

        implement_post: bool = 'POST_PARAMS' in request_header

        if implement_post:
            post_params = '?' + request_header['POST_PARAMS']

        exec_path: str = sys.executable.replace('\\', '\\\\')

        query_str: str = request_header['Host'] + request_header['method'].split()[1]
        user_ip: str = request_header['addr'][0]
        user_port: str = request_header['addr'][1]
        script_name: str = request_header['SCRIPT_FILENAME']
        request_method: str = request_header['REQUEST_METHOD']
        request_time: str = request_header['REQUEST_TIME']
        request_uri: str = request_header['REQUEST_URI']
        php_self: str = request_header['PHP_SELF']
        params: str = request_header['params'].strip()
        cookies: str = request_header['Cookie'] if 'Cookie' in request_header else ''

        path: str = path.replace('\\', '\\\\')

        # We have to declare the $_SERVER Keys by our self.

        os.makedirs('tmp', exist_ok=True)
        cmd: str = f'{self.__php_dir}\\php-cgi.exe -c {self.__php_ini_path} tmp/tmp.php'

        with open('tmp/tmp.php', 'w', encoding='utf-8') as f:
            # If you need any information from python to PHP, you can insert them here.
            script: str = f'''<?php
                    $_SERVER['QUERY_STRING'] = '{query_str}';
                    $_SERVER['REMOTE_ADDR'] = '{user_ip}';
                    $_SERVER['REMOTE_PORT'] = '{user_port}';
                    $_SERVER['DOCUMENT_ROOT'] = '{self.__root_dir}';
                    $_SERVER['SCRIPT_FILENAME'] = '{script_name}';
                    $_SERVER['REQUEST_METHOD'] = '{request_method}';
                    $_SERVER['REQUEST_TIME'] = '{request_time}';
                    $_SERVER['REQUEST_URI'] = '{request_uri}';
                    $_SERVER['SERVER_PORT'] = '{self.__port}';
                    $_SERVER['PYTHON_INTERPRETER_PATH'] = '{exec_path}';
                    $_SERVER['PHP_SELF'] = '{php_self}';
                '''
            if implement_post:
                script += f'parse_str(parse_url(\'{post_params}\', PHP_URL_QUERY), $_POST);' \
                    if post_params != '' else '$_POST = [];'  # noqa

            script += f'parse_str(parse_url(\'?{params}\', PHP_URL_QUERY), $_GET);' \
                if params != '' else '$_GET = [];'  # noqa

            if cookies != '':
                cookies: str = cookies.replace(' ', '').replace(';', '&')
                script += f'parse_str(parse_url(\'?{cookies}\', PHP_URL_QUERY), $_COOKIE);'
            else:
                script += '$_COOKIE = [];'

            for i, k in enumerate(list(request_header['CORRECT_HEADER'].keys())):
                if k.strip() != '' and i != 0:
                    v: str = request_header['CORRECT_HEADER'][k]
                    script += f"$_SERVER['HTTP_{k.upper()}'] = '{v}';"
            script += f'include(\'{path}\');?>'
            f.write(script)
        proc: subprocess.Popen = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        return proc.stdout.read()

    @staticmethod
    def __generate_response_header(header: dict) -> str:
        r: str = ''
        for k in list(header.keys()):
            val: str = header[k]
            r += f'{k}: {val}\n'
        return r

    def __handle_php(self, c: socket.socket, data: dict, path: str, h: str) -> None:
        data['SCRIPT_FILENAME']: str = path
        data['PHP_SELF'] = data['target_location']

        if data['REQUEST_METHOD'] == 'POST':
            params: str = h.split('\r\n\r\n')[-1].strip()
            if params != '' and not h.startswith(params):
                data['POST_PARAMS']: str = params
        response: bytes = self.__get_php_response(os.path.abspath(path), data)
        decoded: str = response.decode(encoding='utf-8')

        response_list: list = decoded.split('\r\n\r\n')
        header_str: str = response_list.pop(0)
        body_str: str = ''.join(response_list)

        if 'Set-Cookie' in header_str:
            set_cookies: list = header_str.split('\r\n')
            parse_cookie: str = ''
            for line in set_cookies:
                if line.startswith('Set-Cookie: '):
                    val: str = line.split('Set-Cookie: ')[1].split(';')[0]
                    parse_cookie += val + ';'
            if 'Cookie' not in data:
                data['Cookie'] = parse_cookie[:-1]
            else:
                # There are already some cookies, so we have to change the syntax a bit
                data['Cookie'] += f'; {parse_cookie}'
            response: bytes = self.__get_php_response(os.path.abspath(path), data)
            response_list: list = response.decode(encoding='utf-8').split('\r\n\r\n')
            del response_list[0]
            body_str: str = ''.join(response_list)

        header: dict = dict(
            [[r.partition(':')[0].strip(), r.partition(':')[2].strip()] for r in header_str.split('\r\n')])  # noqa
        status: str = 'HTTP/1.0 200 OK'
        if 'Status' in header:
            status: str = f'HTTP/1.0 {header["Status"]}'

        c.send(status.encode() + b'\r\n')
        c.send(header_str.encode() + b'\r\n\r\n')
        c.send(body_str.encode())

    @staticmethod
    def __parse_sass(path: str) -> bytes:
        if not os.path.isfile('interpreter/sass/sass.bat'):
            raise NoInterpreterFound('Cant find SASS Interpreter.')
        proc: subprocess.Popen = subprocess.Popen(f'"interpreter/sass/sass.bat" {os.path.abspath(path)}',
                                                  stdout=subprocess.PIPE)
        return proc.stdout.read()

    def __handle_html(self, path: str, c: socket.socket) -> None:
        with open(path, 'r', encoding='utf-8') as f:
            response: bytes = f.read().encode()
        file_ext: str = path.split('.')[-1]

        if file_ext == 'sass' or file_ext == 'scss':
            response: bytes = self.__parse_sass(path)
            file_ext: str = 'css'

        content_type: str = self.__content_types[
            '.' + file_ext] if '.' + file_ext in self.__content_types else 'text/html'
        response_header: str = self.__generate_response_header(
            {'Server': 'ServHTTP/1.0 (Win64)',
             'Content-Length': f'{len(response.decode())}',
             'Keep-Alive': 'timeout=5, max=100',
             'Connection': 'Keep-Alive',
             'Content-Type': f'{content_type}'
             })
        c.send(b'HTTP/1.0 200 OK\r\n')
        c.send(response_header.encode() + b'\r\n')
        c.send(response)
