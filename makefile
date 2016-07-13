FILES :=                              \
    .gitignore					 	  \
    makefile						  \
    apiary.apib						  \
    IDB2.log						  \
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


models.html: app/models.py
	pydoc3 -w app/models.py

IDB2.log:
	git log > IDB2.log


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
	rm -f  IDB2.log
	rm -rf __pycache__


config:
	git config -l

html: models.html

log: IDB2.log

format:
	autopep8 -i app/models.py
	autopep8 -i app/tests.py

status:
	make clean
	@echo
	git branch
	git remote -v
	git status

test: .pylintrc models.html IDB2.log format check