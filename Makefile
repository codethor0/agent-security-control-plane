.PHONY: check release math hygiene

check: math release hygiene

math:
	python3 -m unittest discover -s tests -v

release:
	python3 scripts/check_release.py

hygiene:
	python3 -m py_compile scripts/check_repository_hygiene.py scripts/check_release.py tests/test_math.py
	python3 scripts/check_repository_hygiene.py
