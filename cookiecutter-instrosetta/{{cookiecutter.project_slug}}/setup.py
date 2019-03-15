from setuptools import setup, find_packages


setup(name='{{cookiecutter.project_slug}}',
      version='0.1',
      description='Python implementation of the instrosetta project.',
      url='http://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}',
      author='Yossi Mosbacher',
      author_email='joe.mosbacher@gmail.com',
      license='MIT',
      packages=packages=find_packages(include=['{{ cookiecutter.project_slug }}']),
      install_requires=[
          'grpcio',
          'pint',
          'protobuf',
      ],
      extra_requires={
          "server": "{{cookiecutter.device_dependencies}}".split(",")
      },
      zip_safe=False)