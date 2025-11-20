FROM texlive/texlive:latest

# installing utils 
RUN apt-get update && \
    apt-get -y install --no-install-recommends \
    git \
    inkscape \
    && rm -rf /var/lib/apt/lists/*
