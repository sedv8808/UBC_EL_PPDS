#!/usr/bin/env python
# coding: utf-8

# # UBC
# ## Programming in Python for DS
# 
# October 26, 2022  
# 
# Instructor: Socorro Dominguez Vidana

# ### What is Python?

# - Python is a widely used general-purpose, high-level programming language.
# 
# - Designed by Guido van Rossum in 1991 who developed by Python Software Foundation.
# 
# - Developed to allow programmers express concepts in fewer lines of code.
# 
# - Object-oriented programming language (can model real-world entities). 
# 
# - Dynamically-typed and already interpreted - we don't need to compile it.
# 
# - Python 3 was released in December 2008.

# #### Python's Fun Facts
# 
# - Firstly introduced at the National Research Institute for Mathematics and Computer Science, Netherlands, 1991. [source:https://www.journaldev.com/34415/history-of-python-programming-language]
# 
# - Named after the comedy show Monty Python's Flying Circus.
# 
# - Python has become the most popular coding language in the world. 
#     - This makes a career in Python a great choice. Not just for Data Science/Analytics.
# 
# - Python has just turned 30, but:
#     - Google users have searched "Python" much more than they have searched for Kim Kardashian, Donald Trump, or Tom Cruise etc.

# ![](python_searches.png)

# ### Why Python for Data Science ?
# 
# - Fast programming language to pick up - from a syntax point of view.
#     - Use python as a functional language rather than an OOP language.
# 
# - Active community with a vast selection of libraries (such as pandas and Altair)  and resources.
# 
# - Professionals working with Data Science applications want to focus on insights rather than on complications of language.

# ### What is Jupyter?
# 
# - Simply put, it is an IDE (integrated development environment)
# 
# - We can use Python via Jupyter.
# 
# - You can think of Python like a car's engine, while Jupyter is like a car's dashboard.
#     - Python is the programming language that runs computations
#     - Jupyter is the IDE that provides an interface by adding convenient features and tools.
#     
# - We can use other programs with Jupyter (R, Julia, Matlab,...)

# ### Why Jupyter Notebooks?
# 
# - In Jupyter we can code, do plots, format text, equations, etc. in a single document.
# 
# - Allows us to run Python code interactively.

# - Notebooks are great for exploration and for documenting a complete workflow.
# 
# - Notebooks can be shared in a human readable format:
#     - Share online with nbviewer.jupyter.org
#     - Github, any notebooks you upload are automatically rendered on the site.
#     - Convert to HTML, PDF, etc.

# ### Characteristics of Notebooks
# 
# - A notebook consists of a series of "cells":
#     - Code cells: execute snippets of code and display the output
#     - Markdown cells: formatted text, equations, images, and more

# Note: By default, a new cell is always a code cell.

# ### Python Data Science Ecosystem
# 
# - Python has many uses: 
#     - Web development
#     - Automation or scripting
#     - Software testing and prototyping
#     - Everyday tasks
#     - Data Analysis & Data Science
#     
# - Python has built-in functions. But that is not enough for us (we don't want to reinvent all functions).
# 
# - The Python libraries for data science are developed and maintained by external "3rd party" development teams
# 
# - Python core + 3rd party libraries = **ecosystem**
#     - To install and manage 3rd party libraries, you need to use a package manager such as conda (which comes with Anaconda/Miniconda) - More on this in the DS Toolbox
#     

# Some of the libraries in the Python data science ecosystem:
# 
# ![](ecosystem_big.png)
# 
# During the program, we will be working with Pandas, numPy, and Altair

# ## Tricks with Notebooks

# In[1]:


# This is a code cell

x = 5
3+x # Shows output


# ### Writing a formula 
# - Render with latex using `$`
# 
# Write 
# ```markdown
# $x + y = 8$
# ```
# The output is:
# $x + y = 8$

# - Loading an image:
# 
# ```markdown
# ![](image_path)
# ```

# Writing code as markdown (that doesn't execute) - type:
# ```markdown
#     ```python
#         print("hello world!")
#     ```
# ```
# 

# Renders
# 
# ```python
# print("hello world!")
# ```

# Write variables from the document between `
# 
# `x`

# In[ ]:




