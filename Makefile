all: blang

blang:
	chmod +x addshebang
	mkdir out 2> /dev/null || true
	./addshebang python app.py out/blang
	./addshebang python bmit.py out/bmit
	./addshebang python brepl.py out/brepl

install: blang
	cp out/* /usr/local/bin -fp

uninstall: blang
	chmod +x uninstall
	./uninstall