## No es tan fundamental para este caso.

#################### PACKAGE ACTIONS ###################
reinstall_package:
	@pip uninstall -y goalguru || :
	@pip install -e .


run_api:
	uvicorn goalguru.api.fast:app --reload

run_preprocess:
	python -c 'from goalguru.soccermatch_package.interface.main import preprocess; preprocess()'
