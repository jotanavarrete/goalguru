
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
