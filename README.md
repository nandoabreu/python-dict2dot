# python-dict2dot

Python Dictionary to Dot notation (class) package published in [PyPi](https://pypi.org/project/dict2dot/).

&nbsp;  
&nbsp;  
## README Map

- To pip install, run: ` pip install dict2dot `
- To use the main class, skip to [The main class](https://github.com/nandoabreu/dict2dot#the-main-class).
- Instructions on advanced/technical documentation, go to [Documentation](https://github.com/nandoabreu/dict2dot#documentation).


## The main class
With the python console and the [dict2doc package](https://github.com/nandoabreu/dict2dot/dict2dot/__init__.py), we can get things running:

    $ python
    >>> from dict2dot import Dict2Dot
    >>> my_dict = { 1597184314: { 'urls': ['x.net'], 'ping': {'un':'ms', 'v':10} } }

    >>> dot_dict = Dict2Dot(my_dict)
    >>> print( dot_dict.1597184314.urls, dot_dict.1597184314.ping.v )

    >>> dot_dict.1597184710 = { 'urls': ['x.net'], 'ping': {'un':'ms', 'v':9} } }
    >>> print( my_dict['1597184710']['urls'], my_dict['1597184710']['ping']['v'] )

    >>> new_dot_dict = Dict2Dot()
    >>> new_dot_dict.1597186760 = { 'urls': ['x.net'], 'ping': {'un':'ms', 'v':11} } }
    >>> get_dict = new_dot_dict.dict()
    >>> print( get_dict )


## Documentation
Please try from python console:

    $ python
    >>> from dict2dot import Dict2Dot
    >>> help(Dict2Dot)

Or try from command line:

    $ python -c "import dict2dot; print(dict2dot.__doc__)"

All documentation can be found in [docs](https://github.com/nandoabreu/dict2dot/docs).

