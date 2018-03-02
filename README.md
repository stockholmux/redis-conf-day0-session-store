# Simple session store demo with Python and Flask (you add Redis)

This is an exercise for [RedisConf](http://redisconf.com/) 18 Day 0 Training. It simulates the problems of file system-based session stores.


# Install

As written, this script uses the filesystem to store sessions. To install and play with it:

```
$ pip install -r requirements.txt
```

Which should install `flask`, `flask-session` and `redis-py`.

After install, you can run
```
$ python app.py
```

This will launch a single instance of the script. A single instance will work as expected.

You can go to the following URLs:

* [http://localhost:5000/](http://localhost:5000/) - view the session store value
* [http://localhost:5000/session/set/some-value](http://localhost:5000/session/set/some-value) - Set the session variable to *some-value* (of course, that can be any URL friendly value)
* [http://localhost:5000/session/unset/](http://localhost:5000/session/unset/) - Unset the session variable.


## Multi-instance: Docker / Docker Compose

A Dockerfile and docker-compose.yml files are included. This will launch two instances of the script and HAProxy to simulate a multi-server setup. In this case, everything will be served from port 5000 (as above), but HAProxy will round robin spread the load to the two instances. Because each instance uses it's own file system (simulated by directories in the container), __the sessions will be broken__. If you set a session value, it will only be able to retrieved every other request. Oh no!

If you have docker and docker-compose, you can run this version with:
```
$ docker-compose up
```

## Multi-instance: Without Docker

You can test your code without docker by using two terminal windows and setting an environment variable:

```
$ export APP_PORT=5001
```

(each terminal window being a different `APP_PORT` value)

Then running `python app.py` as normal for each window. You won't get the load balancing, but you'll see that each process will have different session values. Oh no!

## The Challenge
You can use a Redis Database to store the session instead of a file system. This way both processes (either in Docker or in different terminal windows) will share one session store.

The `requirements.txt` includes [`redis-py`](https://redislabs.com/lp/python-redis/) already, so you'll just need to import it in your script and pass in the correct connection information and credentials.

[flask-session](https://pythonhosted.org/Flask-Session/) includes support for Redis-based sessions, so you should be able to integrate redis-py with flask to rip-and-replace the filesystem-based session. 

Hint: You'll need to change 1 line in the existing code and add in some extra information about your Redis. Otherwise, the script should be able to remain the same!

## MIT License

Copyright 2018 Kyle J. Davis

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.



