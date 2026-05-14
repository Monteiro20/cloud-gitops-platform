.PHONY: help up down test clean status

help: ## Show this help menu
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

up: ## Start the local environment
	@echo "Starting Docker..."
	sudo service docker start
	@echo "Environment ready."

down: ## Stop the local environment
	@echo "Stopping services..."
	sudo service docker stop

test: ## Run application tests
	@echo "Tests: not yet implemented (Phase 3)"

clean: ## Destroy local resources
	@echo "Cleanup: not yet implemented (Phase 9)"

status: ## Check installed tools
	@echo "=== Environment Status ==="
	@docker --version
	@python3 --version
	@kubectl version --client --short 2>/dev/null
	@terraform --version | head -1
	@ansible --version | head -1
