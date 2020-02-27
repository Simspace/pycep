# pycep plugin guide!

## linter plugin

The linter plugin runs configured cep checks for any errors in a package export.

### Use pycep linter plugin against tar.gz export

When not using the default mode with the linter plugin only CEP checks that don't pass will be displayed to stdout

    cepcli.py -f examplepackage.tar.gz -p linter 
    
    ERROR:root:ELSA 0.0.0: Example pycep package content module name: CEP 2006 Test Failed! | More info: https://simspace.github.io/cep/ceps/2006/#requirements

### Use pycep linter plugin against tar.gz export in debug mode

When using the debug flag -d or --debug pycep will show debug level logging information and even display which ceps passed.

    cepcli.py -f Demo_Package_export.tar.gz -p linter -d
    
    Debug mode is on
    Process Time: 2020-02-11 12:40:21 | pycep linter plugin running now...
    Process Time: 2020-02-11 12:40:21 | ELSA 0.0.0: Example pycep package content module name: Rendering 10 slides into raw data.
    Process Time: 2020-02-11 12:40:21 | ELSA 0.0.0: Example pycep package content module name: Processing slides with linter now!
    Process Time: 2020-02-11 12:40:21 | ELSA 0.0.0: Example pycep package content module name: CEP 2000 - Passed
    Process Time: 2020-02-11 12:40:21 | ELSA 0.0.0: Example pycep package content module name: CEP 2006 Test Failed! | More info: https://simspace.github.io/cep/ceps/2006/#requirements
    Process Time: 2020-02-11 12:40:21 | ELSA 0.0.0: Example pycep package content module name: CEP 2007 - Passed


## spellcheck plugin
The spellcheck plugin searches for errors using a default spelling word list included in pycep/data/word_list.txt.

### How to use the spellcheck plugin against tar.gz export

    cepcli.pp --plugin spellcheck --input_file Demo_Package_export.tar.gz 
    
    ERROR:root:Content Module Name: Training Demo: Introduction to Pycep
    Slide Title: How to use spellcheck
    Line Number: 1
    Line Data:     volatilty is misspelled 
    Spelling Error: volatilty
    Suggested replacement: volatility

### How to use the spellcheck plugin against tar.gz export with custom word list

    cepcli.pp --plugin spellcheck --input_file Demo_Package_export.tar.gz --word_list /path/to/example_word_list.txt


## Render plugin

Currently the render plugin only supports exporting a package export json tar.gz file into a markdown output by default. It could be easy to implement a html output format as well and convert markdown back to export package portal format.

    cepcli.py -f Demo_Package_export.tar.gz -p render -o /path/to/export/dir/


## Info plugin

Currently the info plugin prints basic information about modules.

    cepcli.py -f Demo_Package_export.tar.gz -p packageinfo