STUBPATH=../../src/bindings/java/output

TestHunmorphStub.class: TestHunmorphStub.java
	javac -cp $(STUBPATH)  TestHunmorphStub.java

run: TestHunmorphStub.class
	iconv -f UTF-8 -t ISO-8859-2 | \
	java -Djava.library.path="$(STUBPATH)" -cp $(STUBPATH):. TestHunmorphStub ../../../morphdb.hu/morphdb_hu.bin
