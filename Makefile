.PHONY: build

build: sam build 

deploy-infra:
	sam build && aws-vault exec laptop_t --no-session -- sam deploy --no-confirm-changeset

invoke-put:
	sam build && aws-vault exec laptop_t --no-session -- sam local invoke PutFunction