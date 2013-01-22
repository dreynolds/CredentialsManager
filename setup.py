from setuptools import setup


setup(
    name='credentials_manager',
    version='0.1',
    description='Simple credential management',
    url='https://github.com/dreynolds/CredentialsManager',
    author='David Reynolds',
    author_email='david@reynoldsfamily.org.uk',
    license='GPL',
    packages=['credentials_manager'],
    zip_safe=False,
    install_requires=['keyring==0.9.2']
)