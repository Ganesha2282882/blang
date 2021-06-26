all: blang

blang:
	chmod +x addshebang
	mkdir out 2> /dev/null || true
	./addshebang python app.py out/blang
	./addshebang python bmit.py out/bmit
	./addshebang python brepl.py out/brepl

version_manager:
	chmod +x addshebang
	mkdir out 2> /dev/null || true
	./addshebang python bvm.py out/bvm

ivm: version_manager
	cp out/bvm /usr/local/bin -fp

install: blang
	cp out/* /usr/local/bin -fp

uninstall: blang version_manager
	chmod +x uninstall
	./uninstall