# creates and configures the environment
.PHONY: env
env:
	bash -i envsetup.sh

# remove the environment
.PHONY: remove-env
remove-env:
	mamba env remove -n ligo
        
# build the JupyterBook normally
.PHONY: html
html:
	jupyter-book build .

# build the JupyterBook so that you can view it on the hub with the URL proxy trick as indicated above
.PHONY: html-hub
html-hub:
	bash -i html_hub.sh

# clean up the figures, audio and _build folders.
.PHONY: clean
clean:
	rm -rf figures/* audio/* _build/*

# run the jupyter notebook main.ipynb
.PHONY: run-main
run-main:
	jupyter execute main.ipynb --kernel_name=ligo
        
        
  