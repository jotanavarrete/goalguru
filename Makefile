## No es tan fundamental para este caso.

#################### PACKAGE ACTIONS ###################
reinstall_package:
	@pip uninstall -y goalguru || :
	@pip install -e .


run_api:
	uvicorn goalguru.api.fast:app --reload

run_preprocess:
	python -c 'from goalguru.soccermatch_package.interface.main import preprocess; preprocess()'


#reset_local_files:
#	rm -rf ${ML_DIR}
#	mkdir -p ~/.lewagon/mlops/data/
#	mkdir ~/.lewagon/mlops/data/raw
#	mkdir ~/.lewagon/mlops/data/processed
#	mkdir ~/.lewagon/mlops/training_outputs
#	mkdir ~/.lewagon/mlops/training_outputs/metrics
#	mkdir ~/.lewagon/mlops/training_outputs/models
#	mkdir ~/.lewagon/mlops/training_outputs/params
