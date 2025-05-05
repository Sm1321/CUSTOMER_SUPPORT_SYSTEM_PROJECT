# we can keep all the files to execute the code

from setuptools import find_packages,setup



setup(name = "e-commerce-bot",
      version = "0.0.1",
      author = "Mohan",
      author_email = "siddulamohan1321@gmai.com",
      packages = find_packages(),
      install_requries = ['langchain-astradb','langchain'])


