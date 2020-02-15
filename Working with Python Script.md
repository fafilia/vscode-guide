Working with python script
>**Important Notes**: 
>Please note that this guide assume you to already installed python environment. If you haven't installed it yet, please follow [this_guide](google.com)


# finder + terminal
We will try to use our terminal (or in Windows, make sure to use `command prompt`)

### 1. Make new directory
It is recomended that we use a separate directory for each project. In this example, we will make one called `python_exercise`. 

<details><summary>using terminal</summary>

Open your terminal, create new directory and enter it
```bash
mkdir python_excercise
cd python_excercise
```
</details>

<details><summary>using file explorer</summary>
Using your file explorer, crete new directory and enter it. 
</details>

### 2. Create and edit python file 

```bash
touch example.py
open example.py
```
when doing `open exaple.py`, you're opening a python file using current default software. I recommend you to set the default software as `Visual Studio Code` since we are going to deal with it alot. 

**(Optional) Changing the default file opener**
<details><summary>Mac</summary>

Using your `Finder` :
- Right click on your .py file 
- Select 'Get Info'
- Open 'Open with' dropdown menu
- Select `Visual Studio Code`

![](res/default-open-mac.png)
</details>

<details><summary>Windows</summary>

Using your `File Explorer`:
- Right click on you .py file 
- Select 'Open WIth'
- Select 'Choose Another App', find `Visual Studio Code` and check it. Check also the 'Always use this app to open `.py` file'
<!-- Todo: Kasih gambar  -->
</details>

<details><summary>Linux</summary>
<!-- Todo: 
- Kasih instruksi 
- Kasih gambar
 -->
</details>

**Edit python file**
After opening the `.py` file, you can edit it whatever you want. For the sake of easiness, let's try with something simple like this: 
```python 
text = 'algoritma'
for i in range(10):
    print(text[:i])
```
Copy-paste code above into your `example.py`, and hit `save`. Now your python script is ready to run. 


### 3. Run python file
1. Open your terminal, change directory to where your `example.py` file located. If your path is too long to type, you can copy-paste it to your terminal.

<details><summary>windows</summary>
</details>

<details><summary>mac</summary>

- On your `Finder`, right click on your `python_exercise` folder
- hold `option` button to see the `
</details>

<details><summary>windows</summary>
</details>

select python environment 

run .py file 

# vscode 
open directory 
create .py file 
open terminal



### Select Interpreter
### Open file/folder
### Runing file on terminal



___
# Advanced Python Script
*Please note that this section needs a basic competency of python*


## Function or Method
In python function and method are basically the same thing. What makes it differs is a method belongs to an object while function can be freely made and unattached into a specific object. 

When I said `Object`, it refers to `Class` in Object Oriented Programming. An `Object` is a manifestation of `Class`. Let's not talk this further. 

You can make a function called `tambah` by doing this thing
```python 
def tambah(a,b):
    return a+b
```

and to run in simply call `tambah(x,y)` where x and y is any data type (could be int, float, list, array) that support addition operation. 

On the other hand, you can make a method but first you have to define the `Class` too 
```python
Class Matematika:
    def tambah(a,b):
    return a+a+b+b
```

and to call it, you should create the instance of `Matematika` first. 

```python 
mat = Matematika()
mat.tambah(a,b)
```

Now, are you familiar with it ? don't be confused with `Object Oriented Programming`, for we won't do that much. 

## Module
Imagine if you are going to make a tons of functions. Will you do that in one `.py` file? NO. We should have a file that saves the functions. 

On its best practice, we write very specific functions in one `.py` file. Then we grouped the similar `.py` files into one directory. 

A `module`, is how we call the `.py` file containing functions, separated from our main `.py` file. 

If you still confused, let's try it out. Create file named `OperasiDasar.py` and edit it into the following: 
```python 
def tambah(a,b):
    return (a+b) 

def kurang(a,b):
    return (a-b)

def kali(a,b):
    return (a*b)

def bagi(a,b):
    return (a/b)
```

after that, create new `.py` file or `.ipynb` file and if you write this correctly, the return should be `3`. 

```python
>>> import OperasiDasar as od
>>> od.tambah(1,2)
3
```
## Package
Package is a set of modules grouped into one directory. 

To make a package, simply create new directory called `kalkulus`.
Copy `OperasiDasar.py` file inside it, and create new `.py` files called `OpeariLanjut.py`. Fill these code into `OperasiLanjut.py`

```python 
def faktorial(a):
    if a>= 0 :
        if a <= 1 :
            return 1
        else:
            return (a* faktorial(a-1))

def jumlah(a):
    res = 0
    if a>= 0:
        for i in range (1,a+1):
            res += i 
    return res 

```