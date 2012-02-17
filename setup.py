from setuptools import setup


setup(
    name='django-mmstats',
    url='https://github.com/schmichael/django-mmstats',
    version='0.1.0',
    license='BSD',
    author='Michael Schurter',
    author_email='m@schmichael.com',
    description=u'MmStats \u2764 Django',
    long_description=open('README.rst').read(),
    packages=['django_mmstats'],
    include_package_data=True,
    #test_suite='tests',
    install_requires=['mmstats'],
    classifiers=['License :: OSI Approved :: BSD License'],
    # It might actually be zip-safe, I just hate eggs. File an issue or pull
    # request if mmstats is actually zip_safe and you care
    zip_safe=False
)
