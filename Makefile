# Makefile
ASMO_DIR := 'asmo.d/utils'


.PHONY:	ssh
.PHONY: pull
.PHONY: add_file_path_comment isort_format black_format ruff_lint ruff_format format f
.PHONY: clean
.PHONY: push_asmo_to_dev
.PHONY: logs

ssh:
	@echo 'Not implemented yet'

add_file_path_comment:
	@python asmo.d/utils/py_utils/add_file_path_comment.py ./

format_isort:
	isort . --line-length 120

format_black:
	black . --line-length 120

format_ruff:
	ruff format .

lint_ruff:
	ruff check --fix . || true

	mkdir -p asmo.d/gitignored
	echo $$(date +"%Y%m%d_%H%M%S") $$(ruff check . | tail  -n 2 | head -n 1) >> asmo.d/gitignored/ruff_check.txt

format: add_file_path_comment lint_ruff format_ruff

f: format

clean:
	@rm -rf .pytest_cache/ .mypy_cache/ junit/ build/ dist/
	@find . -not -path './.venv*' -path '*/__pycache__*' -delete
	@find . -not -path './.venv*' -path '*/*.egg-info*' -delete

push_asmo_to_dev:
	@echo "Merge with dev and push"
	git checkout dev
	git pull origin dev
	git merge dev_asmo
	git push origin dev
	git checkout dev_asmo

logs:
	$(MAKE) -C $(GATEWAY_DIR) logs

# fallback command
# for commands that are not declared in .PHONY
%:
	@$(MAKE) -C $(ASMO_DIR) $@ || $(MAKE) -C $(GATEWAY_DIR) $@ || echo "Command not found"
