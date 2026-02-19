.. index:: Setup, Configuration

.. _setup:

#########
The Setup
#########

This part deals with the setup of the project. It includes instructions on how to install necessary dependencies, configure the environment, and get started with the project. 

We need the following tools and libraries to set up the project:

- podman
- Visual Studio Code
- git

=================
Setting up Podman
=================

This chapter shows you how to set up Podman on your system. Podman is a containerization tool that allows you to run and manage containers without requiring a daemon. It is a great alternative to Docker and is compatible with Docker images.

MacOS
=====

MacOS users can install Podman using Homebrew. Open your terminal and run the following command:

.. code-block:: sh

    brew install --cask podman-desktop

Linux
=====

Linux users can install Podman using their package manager. For example, on Debian-based systems, you can use the following commands:

.. code-block:: sh

   # Install Podman on your system
   sudo apt-get update
   sudo apt-get install -y podman

   # Verify the installation
   podman --version

Windows
=======

Windows users can install Podman using the Windows Subsystem for Linux (WSL). Follow these steps to set up WSL and install Podman. 

You can also install `Podman Desktop for Windows <https://podman-desktop.io/docs/installation/windows-install>`_, which provides a graphical interface for managing your containers.

.. code-block:: sh

    # Enable WSL
    wsl --install
    
    # Install a Linux distribution (e.g., Ubuntu)
    wsl --install -d Ubuntu
    
    # Open the installed Linux distribution and install Podman
    sudo apt-get update
    sudo apt-get install -y podman

=============================
Setting up Visual Studio Code
=============================

VS Code is a popular code editor that provides a great development experience. To set up VS Code for your project, follow these steps:

1. Download and install Visual Studio Code from the official website: `https://code.visualstudio.com/ <https://code.visualstudio.com/>`_.

==============
Setting up Git
==============

Git is a version control system that allows you to manage your code and collaborate with others. To set up Git, follow these steps:

MacOS
=====

MacOS users can install ::command:`git` using Homebrew. Open your terminal and run the following command:

.. code-block:: sh

    brew install git

Linux
=====

Linux users can install git using their package manager. For example, on Debian-based systems, you can use the following commands:

.. code-block:: sh

   # Install git on your system
   sudo apt-get update
   sudo apt-get install -y git

Windows
=======

Sub Section 1.1
---------------

This is a sub-section that goes into more detail about a specific aspect of the topic. It includes explanations, examples, and any relevant diagrams or code snippets to enhance understanding.

.. code-block:: python

   # This is a sample code block in Python
   def example_function():
       print("Hello, World!")