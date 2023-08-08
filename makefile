run:
	export PYTHONPATH="./src"; python3 -m server.main
init-db:
	export PYTHONPATH="./src"; python3 -m database.init-db