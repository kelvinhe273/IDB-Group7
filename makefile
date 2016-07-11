FILES :=                              \
    .gitignore					 	  \
    makefile						  \
    apiary.apib						  \
    IDB1.log						  \
    models.html						  \
    FlaskApp/DowningJones/models.py	  \
    FlaskApp/DowningJones/tests.py    \					  \
    UML.pdf                           

ifeq ($(CI), true)
    COVERAGE := coverage
    PYLINT   := pylint
else
    COVERAGE := coverage-3.5
	PYLINT   := pylint3
endif

.pylintrc:
	$(PYLINT)  --generated-members=commit,add,query --disable=bad-whitespace,missing-docstring,pointless-string-statement --reports=n --generate-rcfile > $@

models.html: FlaskApp/DowningJones/models.py
	pydoc3 -w FlaskApp/DowningJones/models.py

IDB1.log:
	git log > IDB1.log

TestModels: .pylintrc FlaskApp/DowningJones/tests.py FlaskApp/DowningJones/models.py
	-$(PYLINT) FlaskApp/DowningJones/tests.py
	python3 FlaskApp/DowningJones/tests.py

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
	rm -f  IDB1.log
	rm -rf __pycache__


config:
	git config -l

html: models.html

log: IDB1.log

format:
	autopep8 -i app/models.py
	autopep8 -i app/tests.py

status:
	make clean
	@echo
	git branch
	git remote -v
	git status

test: .pylintrc models.html TestModels IDB1.log check