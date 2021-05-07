blang is a programming language that is very minimal and does not need a lot of resources. It's built on top of Python and can soon be used in your IDE.

It's very recent; first version being released on 3/5/2021.

You can try it out by making a blang script called `hworld.blang` and put this in the file:
```blang
say Hello, World!
```
and then running the Python script with `hworld.blang` as the argument.

Also, blang handles errors differently. It's not like Python where it figures it out before running it and throwing an error, no. blang runs the code before the error, errors out on the line with an error, and then runs the next line like usual. 

Help is available in the [Wiki](https://github.com/Ganesha2282882/blang/wiki/Usage).
