PC=@python

MAINFILE=main.py
PRACTICE=practice.py
README=README.MD

.PHONY: main prac init

main:
	$(PC) $(MAINFILE)

prac:
	$(PC) $(PRACTICE)

init:
	@echo '#!/usr/bin/env python' > $(MAINFILE)
	@echo '# -*- coding: utf-8 -*-' >> $(MAINFILE)
	@echo 'print "Hello World"' >> $(MAINFILE)
	@echo '#!/usr/bin/env python' > $(PRACTICE)
	@echo '# -*- coding: utf-8 -*-' >> $(PRACTICE)
	@echo 'print "Hello World"' >> $(PRACTICE)
	@echo '# Lesson N' > $(README)
	@echo '' >> $(README)
	@echo '## 主要内容' >> $(README)
	@echo '' >> $(README)
	@echo '## 认知点' >> $(README)
	@echo '' >> $(README)
