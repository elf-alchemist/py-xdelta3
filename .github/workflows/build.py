name: Build py-xdelta3

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  build:
    name: Build
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.11

      - name: Install Dependencies
        run: |
          python -m pip install --upgrade pip
          pip install wheel setuptools
          pip install -r requirements.txt

      - name: Build Package
        run: python setup.py sdist bdist_wheel

      - name: Upload Package
        uses: actions/upload-artifact@v2
        with:
          name: python-package
          path: dist/
