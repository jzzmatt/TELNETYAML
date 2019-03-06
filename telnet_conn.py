#!/usr/bin/env python
import telnetlib
import time
import sys


class MyTelConn(object):
    connection_timeout = 10
    reading_timeout = 10

    def __init__(self, port=23):
        self._conn = None
        self.port = port
        self.login_prompt = b"Username: "
        self.password_prompt = b"Password: "
        self.host = None

    def connect(self, host, user, passwd):
        self.host = host
        try:
            self._conn = telnetlib.Telnet(self.host, self.port, self.connection_timeout)
            self._conn.read_until(self.login_prompt, self.connection_timeout)
            self._conn.write(user.encode('ascii') + b"\n")
            time.sleep(1)
            self._conn.write(passwd.encode('ascii') + b"\n")
            time.sleep(1)

        except IOError:
            return "Input parameter error found!, Check your username or password"

    def sendtemplate(self, template):
        try:
            self._conn.write(b"\n")
            self._conn.write("config t\n".encode('ascii'))
            time.sleep(1)

            with open(template, 'r') as f_command:
                for line in f_command.readlines():
                    self._conn.write(line.encode('ascii') + b'\n')
                    time.sleep(.5)

            print("SEND CONFIG TO {} DEVICE".format(self.host))

        except IOError:
            return "Make sure File Configuration Exist"

        finally:
            output = self._conn.read_very_eager().decode(encoding="utf-8#")
            print(output)
            self._conn.close()
