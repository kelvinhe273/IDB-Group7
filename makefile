FILES :=                              \
    Collatz.html                      \
    Collatz.log                       \
    Collatz.py                        \
    RunCollatz.in                     \
    RunCollatz.out                    \
    RunCollatz.py                     \
    TestCollatz.out                   \
    TestCollatz.py

ifeq ($(CI), true)
    COVERAGE := coverage
    PYLINT   := pylint
else
    COVERAGE := coverage-3.5
	PYLINT   := pylint3
endif

.pylintrc:
	$(PYLINT) --disable=bad-whitespace,missing-docstring,pointless-string-statement --reports=n --generate-rcfile > $@

collatz-tests:
	git clone https://github.com/cs373-summer-2016/collatz-tests.git

Collatz.html: Collatz.py
	pydoc3 -w Collatz

Collatz.log:
	git log > Collatz.log

RunCollatz.tmp: .pylintrc RunCollatz.in RunCollatz.out RunCollatz.py
	-$(PYLINT) Collatz.py
	-$(PYLINT) RunCollatz.py
	./RunCollatz.py < RunCollatz.in > RunCollatz.tmp
	diff RunCollatz.tmp RunCollatz.out
	python3 -m cProfile RunCollatz.py < RunCollatz.in > RunCollatz.tmp
	cat RunCollatz.tmp

TestCollatz.tmp: .pylintrc TestCollatz.py
	-$(PYLINT) Collatz.py
	-$(PYLINT) TestCollatz.py
	$(COVERAGE) run    --branch TestCollatz.py >  TestCollatz.tmp 2>&1
	$(COVERAGE) report -m                      >> TestCollatz.tmp
	cat TestCollatz.tmp

check:
	@not_found=0;                                 \
    for i in $(FILES);                            \
    do                                            \
        if [ -e $$i ];                            \
        then                                      \
            echo "$$i found";                     \
        else                                      \
            echo "$$i NOT FOUND";                 \
            not_found=`expr "$$not_found" + "1"`; \
        fi                                        \
    done;                                         \
    if [ $$not_found -ne 0 ];                     \
    then                                          \
        echo "$$not_found failures";              \
        exit 1;                                   \
    fi;                                           \
    echo "success";

clean:
	rm -f  .coverage
	rm -f  .pylintrc
	rm -f  *.pyc
	rm -f  Collatz.html
	rm -f  Collatz.log
	rm -f  RunCollatz.tmp
	rm -f  TestCollatz.tmp
	rm -rf __pycache__
	rm -rf collatz-tests

config:
	git config -l

format:
	autopep8 -i Collatz.py
	autopep8 -i RunCollatz.py
	autopep8 -i TestCollatz.py

status:
	make clean
	@echo
	git branch
	git remote -v
	git status

test: Collatz.html Collatz.log RunCollatz.tmp TestCollatz.tmp collatz-tests check
