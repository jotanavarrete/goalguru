
run_preprocess:
	python -c 'from goalguru.soccermatch_package.interface.main import preprocess; preprocess()'

run_api:
	python -c 'from goalguru.soccermatch_package.ml_logic.api_connection import *; get_results()'
