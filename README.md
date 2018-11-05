# devlog
[![Build Status](https://travis-ci.org/flecho/devlog.svg?branch=master)](https://travis-ci.org/flecho/devlog)

<br>

This is a simple blog that records my development log.

After reading this article, 
["Every developer should have a blog. Here’s why, and how to stick with it."
](https://medium.freecodecamp.org/every-developer-should-have-a-blog-heres-why-and-how-to-stick-with-it-5fd55a247fbf),
I have decided to get my hands dirty to create my own blog. 
This blog will record all my personal noteworthy logs in markdown format.  


<br>

#### Things To Do (2018.11.03)
- [ ] 0. Check these libraries and use them.
    - [Flask-Blogging — Flask-Blogging 1.1.0 documentation](https://flask-blogging.readthedocs.io/en/latest/)
    - [Flask-Bootstrap — Flask-Bootstrap 3.3.7.1 documentation](https://pythonhosted.org/Flask-Bootstrap/index.html)
- [ ] 1. Study HTML & CSS (in progress)
    - [x] https://www.udemy.com/master-the-basics-of-html5-css3-beginner-web-development/
	- [ ] https://www.udemy.com/html5-fundamentals-for-beginners/ (in progress: 15/36)
- [ ] 2. Split the layout(There should be a fixed menu navigating tab, and content should be shown in layout) (in progress)
    - [x] Apply simple layout to make all pages have the same layout.
    - [ ] header, footer size alignment
    - [ ] HTML page inheritance --> to make single layout file to be applied to all pages
- [ ] 3. Make upload_file parts as class
- [ ] 4. Make a list of all `.md` files shown in the main page


#### Long-term plan
- [ ] Refactoring
- [ ] Add code coverage
- [ ] Solve flask logging that is not working

#### Features I'd like to implement
- [ ] drag & drop uploading feature

#### Completed items
- [x] Update to python3.7
- [x] Relative import modification  
- [x] Make `.md` file is shown in main page

#### Set up environment 

```
make venv
source venv/bin/activate
make init
```
