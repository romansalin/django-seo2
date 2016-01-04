============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/romansalin/django-seo2/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.
* Expected and actual result you get.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug"
is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "feature"
is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

`django-seo2` could always use more documentation, whether as part of the
official `django-seo2` docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at
https://github.com/romansalin/django-seo2/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `django-seo2` for local development.

1. Fork the `django-seo2` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/django-seo2.git && cd django-seo2
    $ git remote set-url --push origin https://github.com/<your-name>/django-seo2.git

3. Install your local copy into a virtualenv. Assuming you have
   virtualenvwrapper installed, this is how you set up your fork for local
   development::

    $ mkvirtualenv django-seo2
    $ python setup.py develop

4. Create a branch for local development::

    $ git checkout -b your-new-bugfix-or-feature

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass style and
   unit tests::

    $ tox -e lint
    $ tox -e <python version>-<django-version>

6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit    # Please fill all fields that make sense
    $ git push origin your-new-bugfix-or-feature

7. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated.
3. The pull request should work for both Python 2 and 3 and for Django,
   starting from 1.7 version.
   Check https://travis-ci.org/romansalin/django-seo2 under pull requests for
   active pull requests and make sure that the tests pass for all supported
   Python versions.
