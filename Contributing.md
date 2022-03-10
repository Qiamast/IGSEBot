How To Contribute
=================

Every open source project lives from the generous help by contributors that sacrifice their time and ``python-telegram-bot`` is no different. To make participation as pleasant as possible, this project adheres to the `Code of Conduct`_ by the Python Software Foundation.

Setting things up
-----------------

1. Fork the ``IGSEBot`` repository to your GitHub account.

2. Clone your forked repository of ``IGSEBot`` to your computer:

   .. code-block:: bash

      $ git clone https://github.com/<your username>/IGSEBot --recursive
      $ cd python-telegram-bot

3. Add a track to the original repository:

   .. code-block:: bash

      $ git remote add upstream https://github.com/Qiamast/IGSEBot

4. Install dependencies:

   .. code-block:: bash

      $ pip install -r requirements.txt -r requirements-dev.txt


5. Install pre-commit hooks:

   .. code-block:: bash

      $ pre-commit install

Finding something to do
#######################

If you already know what you'd like to work on, you can skip this section.

If you have an idea for something to do, first check if it's already been filed on the `issue tracker`_. If so, add a comment to the issue saying you'd like to work on it, and we'll help you get started! Otherwise, please file a new issue and assign yourself to it.

Another great way to start contributing is by writing tests. Tests are really important because they help prevent developers from accidentally breaking existing code, allowing them to build cool things faster. If you're interested in helping out, let the development team know by posting to the `Telegram group`_ (use `@admins` to mention the maintainers), and we'll help you get started.

That being said, we want to mention that we are very hesitant about adding new requirements to our projects. If you intend to do this, please state this in an issue and get a verification from one of the maintainers.

Instructions for making a code change
#####################################

The central development branch is ``master``, which should be clean and ready for release at any time. In general, all changes should be done as feature branches based off of ``master``.

If you want to do solely documentation changes, base them and PR to the branch ``doc-fixes``. This branch also has its own `RTD build`_.

Here's how to make a one-off code change.

1. **Choose a descriptive branch name.** It should be lowercase, hyphen-separated, and a noun describing the change (so, ``fuzzy-rules``, but not ``implement-fuzzy-rules``). Also, it shouldn't start with ``hotfix`` or ``release``.

2. **Create a new branch with this name, starting from** ``master``. In other words, run:

   .. code-block:: bash

      $ git fetch upstream
      $ git checkout master
      $ git merge upstream/master
      $ git checkout -b your-branch-name

3. **Make a commit to your feature branch**. Each commit should be self-contained and have a descriptive commit message that helps other developers understand why the changes were made.

   - You can refer to relevant issues in the commit message by writing, e.g., "#105".

   - Your code should adhere to the `PEP 8 Style Guide`_, with the exception that we have a maximum line length of 99.

   - Provide static typing with signature annotations. The documentation of `MyPy`_ will be a good start, the cheat sheet is `here`_. We also have some custom type aliases in ``telegram.utils.helpers.typing``.

   - Document your code. This project uses `sphinx`_ to generate static HTML docs. To build them, first make sure you have the required dependencies:

     .. code-block:: bash

        $ pip install -r docs/requirements-docs.txt

     then run the following from the PTB root directory:
   
     .. code-block:: bash
         
        $ make -C docs html

     or, if you don't have ``make`` available (e.g. on Windows):

     .. code-block:: bash

        $ sphinx-build docs/source docs/build/html

     Once the process terminates, you can view the built documentation by opening ``docs/build/html/index.html`` with a browser.

   - Add ``.. versionadded:: version``, ``.. versionchanged:: version`` or ``.. deprecated:: version`` to the associated documentation of your changes, depending on what kind of change you made. This only applies if the change you made is visible to an end user. The directives should be added to class/method descriptions if their general behaviour changed and to the description of all arguments & attributes that changed.

   - For consistency, please conform to `Google Python Style Guide`_ and `Google Python Style Docstrings`_.

   - The following exceptions to the above (Google's) style guides applies:

        - Documenting types of global variables and complex types of class members can be done using the Sphinx docstring convention.

   -  In addition, PTB uses the `Black`_ coder formatting. Plugins for Black exist for some `popular editors`_. You can use those instead of manually formatting everything.

   - Please ensure that the code you write is well-tested.

   - Don’t break backward compatibility.

   - Add yourself to the AUTHORS.rst_ file in an alphabetical fashion.

   - Before making a commit ensure that all automated tests still pass:

