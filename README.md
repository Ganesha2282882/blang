# blang
A programming language. Stands for "Brahma Language"

It now uses a file!

Run:
`APP SCRIPT`

instead of:
`APP CODEINSTRING`

To build it, you neeed `pyinstaller`, and mark the `build1` file executable.

Then, execute like a shell script.

`build1` is used instead of `build` to prevent conflict.
# Help
## Usage

If you supply 0 arguments, an error will occur.
### Print something to the screen
You may only say 3 words.
```
say Hello World
```
will output:
```
Hello World
```
### Addition
Do not use a `+`.
```
add 6 4
```
will output:
```
10
```
### Subtraction
Same with Addition, but use `ta` instead of `add`.
```
ta 7 4
```
will output:
```
3
```
### Load file into RAM
Just specify the file.
```
ram /dev/null
```
will output nothing.
### Try to get input forever
```
inp
```
will output:
```
% 
```
### `if ==`
Similar to Python's `if ==`, but you can't specify what it will do. It will say `yes` or `no`.
```
if "hello" is "hello"
```
will output:
```
yes
```
```
if "hello" is "world"
```
will output:
```
no
```
### `if !=`
Just like `if is`, but use `if not` instead.
### Say `loop` forever
```
lop
```
will output:
```
loop
loop
loop
[Snipped]
```
### Divide
Same as `ta`, but use `div` instead.
### Multiply
Same as `div`, but use `mpy` instead.
