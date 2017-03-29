WEBPACK=./node_modules/.bin/webpack
WEBPACK_DASHBOARD=./node_modules/.bin/webpack-dashboard


run:
	PYTHONASYNCIODEBUG=1 python3 -m server.main

watch: build_dll
	${WEBPACK_DASHBOARD} -- node webpack-configs/server.js

build: clean build_dll_prod
	${WEBPACK} -p --config webpack-configs/production.js --progress --colors

build_dll:
	${WEBPACK} --config webpack-configs/vendor.js --progress --colors

build_dll_prod:
	NODE_ENV=production ${WEBPACK} -p --config webpack-configs/vendor.js --progress --colors

lint:
	./node_modules/.bin/eslint client/

test:
	py.test -x -s

clean:
	find . | grep -E "(__pycache__|\.pyc|\.pyo)" | xargs rm -rf
	rm -rf server/static/dist
	mkdir server/static/dist
	touch server/static/dist/.gitkeep
