import six
from setuptools import setup
from setuptools.command.test import test as TestCommand

VERSION = '0.0.1'
TEST_REQUIREMENTS = [
    'six==1.10.0',
    'nose==1.3.7',
    'pytoml==0.1.7'
]
if not six.PY34:
    TEST_REQUIREMENTS += ['pathlib==2.1.0']


class PyTest(TestCommand):
    user_options = []

    def initialize_options(self):
        TestCommand.initialize_options(self)

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import sys
        from run_tests import test_lessons_solutions
        program = test_lessons_solutions(exit=False)

        sys.exit(int(not program.success))


setup(
    name='advanced-python-programming',
    version=VERSION,
    description=("Rmotr.com curriculum for Introduction to Programming with Python"),
    url='http://github.com/rmotr-curriculum/itp-class',
    download_url=(
        "https://github.com/rmotr-curriculum/itp-class/tarball/{version}".format(
            version=VERSION)),
    author='rmotr.com',
    author_email='questions@rmotr.com',
    license='MIT',
    packages=["."],
    tests_require=[
        'nose==1.3.7',
        'pytoml==0.1.7'
    ],
    zip_safe=False,
    cmdclass={'test': PyTest},
)
