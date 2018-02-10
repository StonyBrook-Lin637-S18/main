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

Each homework will be hosted in its own private repository. Only course participants have access to these repositories.

[Homework 1](../../../homework1): due Wed, Feb 07 @ 23:59pm


Using the Virtual Machine Image
-------------------------------

### Installation

1. Download the correct version of [Virtualbox](https://www.virtualbox.org/wiki/Downloads) for your system, and install it.
1. Download the [virtual machine image][vm] as an `ova`-file from the Google drive.
   The file is almost 4GB, so it will take a while.
   Make sure your download does not get interrupted, as this might damage the file.
1. Start Virtualbox. 
   Click on `File` in the menu bar, then select `Import Appliance`.
   Select the ova file you downloaded (you might have to navigate to the folder first where you saved the `ova` file).
1. Virtualbox will start importing the image.
   If you get an error message, the `ova` file is corrupted and must be downloaded again.
1. After the virtual machine image has been imported, select it and click the `Start` button, which is the big green arrow.
1. A window will open loading the fully-configured Linux installation.
1. If everything works correctly, you can delete the `ova` file now.

### Usage

1.  The VM has no GUI-tool for git, instead you are expected to use the command line.
    1. Open the Terminal.
       The icon is on the desktop.
    1. Use the usual git commands.
       For example, to clone a repository with URL `https://foo.bar/repo.git`, type `git clone https://foo.bar/repo.git`
    1. The `cd` command allows you to move into a specific folder.
       So if you type `cd Downloads` right after opening the terminal, you will move into the folder `Downloads`.
       To go one folder up, type `cd ..`.
    1. Use the `ls` command to list the contents of a folder.
1.  You can edit files in a terminal or with the GUI app *Geany*.
1.  For on-the-fly coding in a Python shell, you can run `python3` or `bpython3` from the terminal.
    I recommend `bpython3` as it has excellent command completion.
    Alternatively, you can also start *IDLE3* or the *Jupyter Qt console* from the desktop.

### Installing Software

Additional software, such as Python packages, are installed from the command line.
First we have to make sure we have the most current list of available software.
So we run `sudo aptitude update`

1. `sudo` means to execute the next command with administrator privileges.
1. `aptitude` is the package manager that handles software installations.
1. `update` tells aptitude to get the newest software list.

After that, we can install any software with the command `sudo aptitude install PackageName`.
Here `sudo` and `aptitude` have the same meaning as before.

1. `install` tells *aptitude* that we want to install a package.
1. `PackageName` is the name of the package.

For example, to install *sympy* for Python 3 you would run `sudo aptitude install python3-sympy`.

To find the correct package name, use `aptitude search string`, e.g. `aptitude search sympy`.
Since this doesn't make any changes to the system, the command can be run without `sudo`.

Whenever you run a command with `sudo`, you'll be asked for the password.
For the VM, the password is *student*, which is also the username.

### Optional: Installing Guest Additions

Virtualbox also offers guest additions to make the VM integrate more tightly with your system.
For example, this allows creating shared folders to share files between the VM and your own system, and to dynamically scale the resolution of the VM depending on the window size.

Guest additions are not installed by default due to licensing restrictions.
You'll have to install them yourself if you want the additional features.

1.  Start the VM.
1.  At the top of the VM window, there is a menu bar.
    Click on `Devices`, then select `Insert Guest Additions CD image`.
1.  When asked whether you can to open the CD in the file browser, click cancel.
    Instead open the terminal, then issue the following commands one after the other:
    1. `cd /media/cdrom` to go to the CD.
    1. `sudo su` will promote you to administrator.
    1. Then type `sh VBoxLinuxAdditions.run`.
    1. Once the installation is done, reboot the VM.
1.  To make sure that everything is installed correctly, open a terminal and run `lsmod | grep vboxguest`.
    If you see a line mentioning `vboxguest`, everything worked as intended.
    If there is no output at tall, something went wrong.


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
