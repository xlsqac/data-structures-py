P=$(shell pwd)
test:
	pytest  --cov=$P $P/test.py
