import setuptools

setuptools.setup(
    name="translation_delivered_event_tools",
    version="0.0.1",
    author="Sérgio Copeto",
    author_email="sergio.copeto@gmail.com",
    description="A small package for translation delivered event handling and feature extraction",
    packages=setuptools.find_packages(),
    install_requires=[
          'pandas',
      ],
)