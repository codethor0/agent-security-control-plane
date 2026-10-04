.PHONY: check release math

check: math release

math:
	python3 -m unittest discover -s tests -v

release:
	python3 scripts/check_release.py
