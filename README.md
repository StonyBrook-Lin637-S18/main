Computational Linguistics 2
===========================


Overview
--------

This is the primary course website for Computational Linguistics 2 (Lin 637), offered by the [Department of Linguistics][department] at [Stony Brook University][sbu].
For a brief list of topics, check the [syllabus][syllabus].

This repository is publicly accessible and hosts the LaTeX source code for the lecture notes.
Compiled pdfs of each chapter are available in the [pdf][pdf] folder.


Prerequisites
-------------

This course assumes a certain degree of familiarity with generative syntax, phonology, and basic mathematics (sets, functions, relations, first-order logic).
Please take the [online survey][survey] to ensure that you satisfy the prerequisites.
Giving a few wrong answers is okay, but if you feel that you do not know enough in a certain area, you should brush up on that in the first two weeks of the class.
Relevant materials are suggested in the [readings repository][readings] (access restricted to enrolled students).

In addition, you will have to use Python and possibly markdown and/or LaTeX at various points during this course.
The [link list](#link-list) at the end of this document has some useful tutorials.

If you don't want to deal with installing Python and git, you can download our [virtual machine][vm] that already comes with everything preconfigured.
Access is restricted to Stony Brook affiliates.
See the section below for details.


Readings
--------

Course readings are made available through the private [readings repository][readings].
You must be enrolled in this class in order to get access.


Homeworks
---------

Each homework will be hosted in its own private repository.
Only course participants have access to these repositories.

- [Homework 0](../../../homework0): no due date
- [Homework 1](../../../homework1): due Wed, Feb 07 @ 23:59pm
- [Homework 2](../../../homework2): due Sat, Feb 17 @ 23:59pm
- [Homework 3](../../../homework3): due Sat, Feb 24 @ 23:59pm
- [Homework 4](../../../homework4): due Sat, Mar 24 @ 23:59pm
- [Homework 5](../../../homework5): due Wed, Apr 04 @ 23:59pm


Compilation Instructions
------------------------

If you want to compile the lecture notes yourself, or use them as the basis for your own course, carefully follow the steps below.

1.  Make sure you have all necessary software installed and set up correctly, in particular
    - a recent LaTeX distribution with `Tikz` >= 3.00 and recent versions of `minted` and `forest`
    - the Python `pygments` package (required by minted)

2.  Clone the repository via `git`, or download and extract the [zip file](../../archive/master.zip).
    Note that the project folder will also contain an empty _build_ folder, which is used for temporary files to speed up compilation.

3.  Use the standard `tex --> pdf` compilation tool chain (**not** `tex --> dvi --> ps --> pdf`), but make sure that `pdflatex` is run with the parameters `--shell-escape` and `--etex`.


Link List
---------

### Using git

- I highly recommend github's [interactive git tutorial](https://try.github.io).
- [Github app for Windows](http://windows.github.com); supports only Windows 7 or later
- [Github app for Mac](http://mac.github.com); supports only OS X 10.9 or later
- List of alternative [GUI clients for git](http://git-scm.com/downloads/guis)
- Tutorials for using [git via the command line](https://www.atlassian.com/git/tutorials)
- Official [documentation for git](http://git-scm.com/doc)

### Markdown

- Interactive tutorial to [markdown basics](http://markdowntutorial.com/)
- [Complete markdown syntax](http://daringfireball.net/projects/markdown/syntax)
- Overview of [Github's markdown dialect](https://help.github.com/categories/writing-on-github/)

### LaTeX

- [Overleaf](https://www.overleaf.com/) (formerly writeLaTeX) is an online LaTeX editor with live preview
- List of [commonly used math symbols](http://web.ift.uib.no/Teori/KURS/WRK/TeX/symALL.html)
- Andrew Roberts' [Getting to Grips with LaTeX](http://www.andy-roberts.net/writing/latex)

### Python

- A succinct yet extensive [tutorial for Python 3](http://www.python-course.eu/python3_course.php)
- The official [Python 3 documentation](https://docs.python.org/3/)
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) is an excellent introduction that covers the basics of Python and applies them to real-world tasks.
- The [repository for LIN 120 *Language & Technology*](https://github.com/CompLab-StonyBrook/lin120_public) also contains Jupyter notebooks that cover the basics of Python, with an emphasis on programming techniques for computational linguistics.

[department]: http://linguistics.stonybrook.edu
[pdf]: ../../tree/master/pdf
[readings]: ../../../readings
[sbu]: http://www.stonybrook.edu
[survey]: https://testmoz.com/432409
[syllabus]: ../../blob/master/pdf/0_syllabus.pdf?raw=true
[vm]: https://drive.google.com/file/d/1ti5dhXh1ZzHKYa-dCHZtzI7WIapWPr2V/view?usp=sharing
