# python-dict2dot

Python Dictionary to Dot notation (class) package published in [PyPi](https://pypi.org/project/dict2dot/).  
_Note: This implementation admits dot notation to access nested dictionaries, once the parent is dict._

&nbsp;  
&nbsp;  
## README Map

- To pip install, run: ` pip install dict2dot `
- To use the main class, skip to [The main class](https://github.com/nandoabreu/dict2dot#the-main-class).
- Instructions on advanced/technical documentation, go to [Documentation](https://github.com/nandoabreu/dict2dot#documentation).
- Or click to skip to the [To do](https://github.com/nandoabreu/dict2dot#to-do) list.


## The main class
With the python console and the [dict2doc package](https://github.com/nandoabreu/dict2dot/dict2dot/__init__.py), we can get things running:

    $ python

    >>>
    from dict2dot import Dict2Dot

    my_d2dot = Dict2Dot({'dogs': {'breeds': ['Golden']}, 'birds': {'breeds': ['Cockatiel']}})
    my_d2dot.dogs.breeds.append('Lhasa Apso')
    print( my_d2dot.dogs )

    my_dict = my_d2dot.dict()
    print( my_dict )

    other_dot2dict = Dict2Dot()
    other_dot2dict.a_new_key = 'a new value'
    print( other_dot2dict.a_new_key )


## Documentation
Please try from python console:

    $ python
    >>> from dict2dot import Dict2Dot
    >>> help(Dict2Dot)

Or try from command line:

    $ python -c "import dict2dot; print(dict2dot.__doc__)"

All documentation can be found in [docs](https://github.com/nandoabreu/dict2dot/docs).


## To do

* Remove elements from class.
* Improve documentation.

