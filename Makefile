## No es tan fundamental para este caso.

#################### PACKAGE ACTIONS ###################
reinstall_package:
	@pip uninstall -y goalguru || :
	@pip install -e .


run_api:
	uvicorn goalguru.api.fast:app --reload

run_preprocess:
	python -c 'from goalguru.soccermatch_package.interface.main import preprocess; preprocess()'

run_api:
	python -c 'from goalguru.soccermatch_package.ml_logic.api_connection import *; get_results()'

run_train:
	python -c 'from goalguru.soccermatch_package.interface.main import train; train()'

run_evaluate:
	python -c 'from goalguru.soccermatch_package.interface.main import evaluate; evaluate()'

run_pred:
	python -c 'from goalguru.soccermatch_package.interface.main import pred; pred()'
