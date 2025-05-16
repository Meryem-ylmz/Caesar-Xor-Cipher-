run:
	python main.py

clean:
	rm -f encrypted.txt xor_encrypted.txt

format:
	black *.py