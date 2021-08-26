#!/bin/bash

PY_BUILD_FOLDER=USD_python_build

build_python_bindings() {
  # bash steps to build the python bindings
  # should probably start with
  mkdir -p $PY_BUILD_FOLDER
  
  sudo apt-get install -y cmake \
                       build-essential \
                       curl \
                       git \
                       software-properties-common \
                       wget \
                       libgl1-mesa-dev \
                       mesa-utils \
                       rsync \
                       libqt5gui5

  add-apt-repository -y ppa:deadsnakes/ppa
  apt-get install -y python3.7 libpython3.7-dev
  ln -s /usr/bin/python3.7 /usr/bin/python

  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
  python3.7 get-pip.py

  pip install --upgrade pip
  pip install pyside2
  pip install pyopengl

  python build_scripts/build_usd.py USD_python_build
  # and a handy command to `cd` into a folder to do things inside there is:
  pushd $PY_BUILD_FOLDER
  # do things
  popd
  # consider installing the USD python build to /usr/local/ (bin/lib)
  sudo rsync -a $PY_BUILD_FOLDER/ /usr/local
}

setup_paths() {
  export PYTHONPATH=$PYTHONPATH:/usr/local/USD_python_build/lib/python
  export PATH=$PATH:/usr/local/USD_python_build/bin
}

main() {
  build_python_bindings
  setup_paths
}
main
