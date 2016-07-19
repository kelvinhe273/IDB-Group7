FILES :=                              \
    .gitignore					 	  \
    makefile						  \
    apiary.apib						  \
    IDB3.log						  \
    models.html						  \
    app/models.py   				  \
    app/tests.py   					  \
    UML.pdf                           

ifeq ($(CI), true)
    COVERAGE := coverage
    PYLINT   := pylint
else
    COVERAGE := coverage-3.5
	PYLINT   := pylint3
endif

IDB3.log:
	git log > IDB3.log

.pylintrc:
	$(PYLINT) disable-msg=E0611 --disable=bad-whitespace,missing-docstring,pointless-string-statement --reports=n --generate-rcfile > $@

TestModels: .pylintrc app/tests.py
	-$(PYLINT) app/tests.py
	$(COVERAGE) run --omit='*flask_testing*' --branch app/tests.py
	$(COVERAGE) report -m

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
	rm -f  *.pyc
	rm -f  *.tmp
	rm -f  IDB3.log
	rm -rf __pycache__
	rm -f app/*.pyc
	rm -rf models.html/

epydoc: app/models.py
	epydoc app/models.py -o models.html
	rm -f app/*.pyc

config:
	git config -l


log: IDB3.log

format:
	autopep8 -i app/models.py
	autopep8 -i app/tests.py

status:
	make clean
	@echo
	git branch
	git remote -v
	git status

test: clean .pylintrc IDB3.log format epydoc TestModels check
