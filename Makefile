PYTHON3 := python3

RDLFILES := \
	rdl/ym2612.rdl \
	rdl/vdp.rdl \
	rdl/genesis.rdl \

all: validate

validate: tools/validate.py $(RDLFILES)
	$(PYTHON3) tools/validate.py $(RDLFILES)
