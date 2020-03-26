# click errors on atomic write to mounted files

Clone this repo and run

    docker-compose run click-err

Error message:

```
Traceback (most recent call last):
  File "/work/main.py", line 11, in <module>
    main()
  File "/work/main.py", line 7, in main
    f.close()
  File "/usr/local/lib/python3.7/site-packages/click/_compat.py", line 619, in close
    _replace(self._tmp_filename, self._real_filename)
OSError: [Errno 16] Device or resource busy: '.__atomic-writee31adfb9' -> '/work/out.txt'<Paste>
```

All varations of this that I try fail with the same error.

```
docker run -v `pwd`/out.txt:/work/out.txt click-err
```

Also tried specifying bind mounts in docker-compose.yml
