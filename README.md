# packdemo
This is a demo for python packaging techniques. It contains an importable package 
called le_demo(to avoid conflicts with anything this sounded weird enough to me :) ).
It has a script on the command line called `demo-script` and is importable in
the python in the environment this is used in.

## Python packaging tools

  The tools used here have some built-in python tools such as those provided by the 
  setuptools package. These can get multiple output types:

  * **for development**: a package link is created in the virtual environment but no files are copied
  * **test installation**: files are copied to the environment from the project
  * Binary distributions:
    * **egg**: the original python package format that is a zip file with a manifest inside capable 
    of building C code as well. Quick to build, slow(er) to install.
    * **wheel**: the new python package format geared towards shipping built pyd files 
    rather than building them on installation time. Slow to build quick(er) to install
    * **upload to pipy**: This makes the package available for those wanting to 
    install it via pip. (not covered here... yet)
    
### Detailed commands

#### Development

    python setup.py develop
    
  This is supposed to give you something like this:
  
    (packdemoenv) demouser@demouser-VirtualBox:~/Projects/packdemo$ python setup.py develop
    running develop
    running egg_info
    writing le_demo.egg-info/PKG-INFO
    writing dependency_links to le_demo.egg-info/dependency_links.txt
    writing entry points to le_demo.egg-info/entry_points.txt
    writing top-level names to le_demo.egg-info/top_level.txt
    reading manifest file 'le_demo.egg-info/SOURCES.txt'
    writing manifest file 'le_demo.egg-info/SOURCES.txt'
    running build_ext
    Creating /home/demouser/anaconda3/envs/packdemoenv/lib/python3.7/site-packages/le-demo.egg-link (link to .)
    Adding le-demo 0.0.1 to easy-install.pth file
    Installing demo-script script to /home/demouser/anaconda3/envs/packdemoenv/bin
    
    Installed /home/demouser/Projects/packdemo
    Processing dependencies for le-demo==0.0.1
    Finished processing dependencies for le-demo==0.0.1
    
  After this you should have access to demo-script:
  
    (packdemoenv) demouser@demouser-VirtualBox:~/Projects/packdemo$ demo-script
    Here I am!
    
  Modify [demo_script.py](le_demo/demo_script.py) and see the changes immediately take effect without having to
  re-install because of the package link.
  
    (packdemoenv) demouser@demouser-VirtualBox:~/Projects/packdemo$ demo-script
    Here I am! Modified.

  Uninstalling is also easy, just use pip
  
    (packdemoenv) demouser@demouser-VirtualBox:~/Projects/packdemo$ pip uninstall le-demo
    Found existing installation: le-demo 0.0.1
    Uninstalling le-demo-0.0.1:
      Would remove:
        /home/demouser/anaconda3/envs/packdemoenv/bin/demo-script
        /home/demouser/anaconda3/envs/packdemoenv/lib/python3.7/site-packages/le-demo.egg-link
    Proceed (y/n)? y
      Successfully uninstalled le-demo-0.0.1

  After this demo-script should be gone:
  
    (packdemoenv) demouser@demouser-VirtualBox:~/Projects/packdemo$ demo-script
    bash: /home/demouser/anaconda3/envs/packdemoenv/bin/demo-script: No such file or directory

#### Test installation

    python setup.py install
    
  This output is going to show you that things got copied. An egg was built and that is copied
  over to the environment. Any changes to the code after this will not be reflected until
  you reinstall this package.
  
    running install
    running bdist_egg
    running egg_info
    writing le_demo.egg-info/PKG-INFO
    writing dependency_links to le_demo.egg-info/dependency_links.txt
    writing entry points to le_demo.egg-info/entry_points.txt
    writing top-level names to le_demo.egg-info/top_level.txt
    reading manifest file 'le_demo.egg-info/SOURCES.txt'
    writing manifest file 'le_demo.egg-info/SOURCES.txt'
    installing library code to build/bdist.linux-x86_64/egg
    running install_lib
    running build_py
    copying le_demo/scripts/demo_script.py -> build/lib/le_demo/scripts
    creating build/bdist.linux-x86_64/egg
    creating build/bdist.linux-x86_64/egg/le_demo
    creating build/bdist.linux-x86_64/egg/le_demo/scripts
    copying build/lib/le_demo/scripts/demo_script.py -> build/bdist.linux-x86_64/egg/le_demo/scripts
    copying build/lib/le_demo/scripts/__init__.py -> build/bdist.linux-x86_64/egg/le_demo/scripts
    copying build/lib/le_demo/__init__.py -> build/bdist.linux-x86_64/egg/le_demo
    byte-compiling build/bdist.linux-x86_64/egg/le_demo/scripts/demo_script.py to demo_script.cpython-37.pyc
    byte-compiling build/bdist.linux-x86_64/egg/le_demo/scripts/__init__.py to __init__.cpython-37.pyc
    byte-compiling build/bdist.linux-x86_64/egg/le_demo/__init__.py to __init__.cpython-37.pyc
    creating build/bdist.linux-x86_64/egg/EGG-INFO
    copying le_demo.egg-info/PKG-INFO -> build/bdist.linux-x86_64/egg/EGG-INFO
    copying le_demo.egg-info/SOURCES.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
    copying le_demo.egg-info/dependency_links.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
    copying le_demo.egg-info/entry_points.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
    copying le_demo.egg-info/top_level.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
    zip_safe flag not set; analyzing archive contents...
    creating 'dist/le_demo-0.0.1-py3.7.egg' and adding 'build/bdist.linux-x86_64/egg' to it
    removing 'build/bdist.linux-x86_64/egg' (and everything under it)
    Processing le_demo-0.0.1-py3.7.egg
    Copying le_demo-0.0.1-py3.7.egg to /home/demouser/anaconda3/envs/packdemoenv/lib/python3.7/site-packages
    Adding le-demo 0.0.1 to easy-install.pth file
    Installing demo-script script to /home/demouser/anaconda3/envs/packdemoenv/bin
    
    Installed /home/demouser/anaconda3/envs/packdemoenv/lib/python3.7/site-packages/le_demo-0.0.1-py3.7.egg
    Processing dependencies for le-demo==0.0.1
    Finished processing dependencies for le-demo==0.0.1

#### EGG/Wheel build

    python setup.py bdist_egg
    
  or
  
    python setup.py bdist_wheel
    
  The built packages will be in the [dist](dist) directory created by the setup.py
  
All of the above is python's own and can be managed by pip.

## 3rd party tools

### PyInstaller

  This builds a distribution that collects python and everything else into a folder and 
  makes it ready to be distributed to those who do not have python on their computer.
  The dependency in this case is only the OS on which you build this.
  
    (packdemoenv) demouser@demouser-VirtualBox:~/Projects/packdemo$ pyinstaller le_demo/scripts/demo_script.py 
    43 INFO: PyInstaller: 3.6
    43 INFO: Python: 3.7.7 (conda)
    53 INFO: Platform: Linux-5.0.0-32-generic-x86_64-with-debian-buster-sid
    53 INFO: wrote /home/demouser/Projects/packdemo/demo_script.spec
    57 INFO: UPX is not available.
    58 INFO: Extending PYTHONPATH with paths
    ['/home/demouser/Projects/packdemo', '/home/demouser/Projects/packdemo']
    59 INFO: checking Analysis
    59 INFO: Building Analysis because Analysis-00.toc is non existent
    59 INFO: Initializing module dependency graph...
    60 INFO: Caching module graph hooks...
    77 INFO: Analyzing base_library.zip ...
    3051 INFO: Processing pre-find module path hook   distutils
    3052 INFO: distutils: retargeting to non-venv dir '/home/demouser/anaconda3/envs/packdemoenv/lib/python3.7'
    4969 INFO: Caching module dependency graph...
    5093 INFO: running Analysis Analysis-00.toc
    5100 INFO: Analyzing /home/demouser/Projects/packdemo/le_demo/scripts/demo_script.py
    5103 INFO: Processing module hooks...
    5103 INFO: Loading module hook "hook-pydoc.py"...
    5104 INFO: Loading module hook "hook-distutils.py"...
    5106 INFO: Loading module hook "hook-encodings.py"...
    5188 INFO: Loading module hook "hook-sysconfig.py"...
    5221 INFO: Loading module hook "hook-xml.py"...
    5632 INFO: Looking for ctypes DLLs
    5632 INFO: Analyzing run-time hooks ...
    5654 INFO: Looking for dynamic libraries
    5985 INFO: Looking for eggs
    5985 INFO: Python library not in binary dependencies. Doing additional searching...
    5999 INFO: Using Python library /home/demouser/anaconda3/envs/packdemoenv/lib/libpython3.7m.so
    6003 INFO: Warnings written to /home/demouser/Projects/packdemo/build/demo_script/warn-demo_script.txt
    6061 INFO: Graph cross-reference written to /home/demouser/Projects/packdemo/build/demo_script/xref-demo_script.html
    6094 INFO: checking PYZ
    6098 INFO: Building PYZ because PYZ-00.toc is non existent
    6099 INFO: Building PYZ (ZlibArchive) /home/demouser/Projects/packdemo/build/demo_script/PYZ-00.pyz
    6636 INFO: Building PYZ (ZlibArchive) /home/demouser/Projects/packdemo/build/demo_script/PYZ-00.pyz completed successfully.
    6641 INFO: checking PKG
    6641 INFO: Building PKG because PKG-00.toc is non existent
    6643 INFO: Building PKG (CArchive) PKG-00.pkg
    6692 INFO: Building PKG (CArchive) PKG-00.pkg completed successfully.
    6693 INFO: Bootloader /home/demouser/anaconda3/envs/packdemoenv/lib/python3.7/site-packages/PyInstaller/bootloader/Linux-64bit/run
    6693 INFO: checking EXE
    6693 INFO: Building EXE because EXE-00.toc is non existent
    6693 INFO: Building EXE from EXE-00.toc
    6693 INFO: Appending archive to ELF section in EXE /home/demouser/Projects/packdemo/build/demo_script/demo_script
    6746 INFO: Building EXE from EXE-00.toc completed successfully.
    6748 INFO: checking COLLECT
    6748 INFO: Building COLLECT because COLLECT-00.toc is non existent
    6748 INFO: Building COLLECT COLLECT-00.toc
    6847 INFO: Building COLLECT COLLECT-00.toc completed successfully.
    
  The built distribution is under the dist directory once again:
  
    (packdemoenv) demouser@demouser-VirtualBox:~/Projects/packdemo$ dist/demo_script/demo_script 
    Here I am! Modified.
    
### FPM

  FPM's goal is to make it user-friendly to package to just about anywhere.
  https://github.com/jordansissel/fpm
  
#### DEB/RPM created with FPM

  The package here might require some extra metadata to make it fully compatible but the
  gist is the below process:
  
    (packdemoenv) demouser@demouser-VirtualBox:~/Projects/packdemo$ fpm -t rpm -s python setup.py 
    Doing `require 'backports'` is deprecated and will not load any backport in the next major release.
    Require just the needed backports instead, or 'backports/latest'.
    Created package {:path=>"python-le-demo-0.0.1-1.noarch.rpm"}
    (packdemoenv) demouser@demouser-VirtualBox:~/Projects/packdemo$ fpm -t deb -s python setup.py 
    Doing `require 'backports'` is deprecated and will not load any backport in the next major release.
    Require just the needed backports instead, or 'backports/latest'.
    Debian packaging tools generally labels all files in /etc as config files, as mandated by policy, so fpm defaults to this behavior for deb packages. You can disable this default behavior with --deb-no-default-config-files flag {:level=>:warn}
    Created package {:path=>"python-le-demo_0.0.1_all.deb"}

### Docker

  If you are writing complex loosely coupled microservices docker may be your best friend.
  Containers are just what the name suggests and the concept was pioneered in the usage
  of the standard shipping container that revolutionized the shipping industry. It has 
  everything it needs short of a linux kernel and it has its specific anchor points to
  access files and the network subsystem. Otherwise the containers are isolated from
  one-another unless we tell them to connect and exchange information.
  
#### Build an image

  The repo has a Dockerfile prepared to showcase this hello world program in total isolation.
  
    (packdemoenv) demouser@demouser-VirtualBox:~/Projects/packdemo$ docker build -t demo-docker .
    Sending build context to Docker daemon  23.51MB
    Step 1/5 : FROM python:3.7
     ---> 22c70bba8283
    Step 2/5 : RUN mkdir /application
     ---> Using cache
     ---> cff81d9930ac
    Step 3/5 : WORKDIR "/application"
     ---> Using cache
     ---> 66faecf957be
    Step 4/5 : ADD le_demo/scripts/demo_script.py /application/
     ---> f94c87f46957
    Step 5/5 : CMD [ "python", "demo_script.py" ]
     ---> Running in 95977b29f6b2
    Removing intermediate container 95977b29f6b2
     ---> ea2d7ec450c2
    Successfully built ea2d7ec450c2
    Successfully tagged demo-docker:latest
  
#### Run it with docker run
  
    (packdemoenv) demouser@demouser-VirtualBox:~/Projects/packdemo$ docker run -it --rm demo-docker
    Here I am! Modified.

### Packer

  Assuming you need to go even further you might want to also pack the OS with it.
  Packer does just that and the result is a VM image for virtualbox/vmware/xen...etc
  
  https://packer.io
  