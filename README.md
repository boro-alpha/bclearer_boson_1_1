# bCLEARer Process - bOSON 1.1 (bCLEARer Ordnance Survey Open Names) Surface Onomatology

The present code is a Python implementation of the [bCLEARer process](https://borosolutions.net/bclearer-approach) developed by [BORO Solutions](https://borosolutions.net/) being applied over the [Ordnance Survey Open Names](https://www.ordnancesurvey.co.uk/business-government/products/open-map-names) dataset.  The OS Open Names GML data can be downloaded from [here](https://osdatahub.os.uk/downloads/open/OpenNames).

This code shows an example of how to automatically implement (at scale) a surface onomatology pattern over structured data.

The code transparently documents the transformations that arise from the data cleaning and ontological analysis that takes place in the different stages of the process, and it outputs the result in a self-contained folder system divided into sub-folders corresponding to each of the implemented bCLEARer stages and sub-stages.

The bCLEARer process exports the following stages and sub-stages in this sequence:

* **bCLEARer Load Stage**. Exporting to the sub-stage folder:
    * 1l_a1_output_os_inspire - loads the [INSPIRE](https://inspire.ec.europa.eu/) metamodel
* **bCLEARer Evolve Stage**. Exporting to the sub-stage folders:
    * 2e_b1_output_convert - cleans and filters the metamodel
    * 2e_c1_output_merge_bclearer - loads and merges the top level ontology
    * 2e_d1_output_merge_bclearer_link - loads and merges the links between the metamodel and the top level ontology
    * 2e_e1_output_merge_boson - loads and merges objects that are required for the data load
    * 2e_f1_input_cont_uni_gml - loads and merges the OS Open Names GML data
    * 2e_g1_output_shift_obj_to_class - converts the OS Open Names GML Objects to Classes
    * 2e_h - separates UML objects and names
        * 2e_h1_output_uml_to_attr - separates UML names
        * 2e_h2_output_uml_attr_to_ass - separates UML attribute names
    * 2e_i1_output_attr_to_obj - separates objects and names - GML File names
    * 2e_j1_output_gen_names - generalises all names to the general name pattern
    * 2e_k - separates names and name instances
        * 2e_k1_output_sep_standard_instances - separates using the standard pattern
        * 2e_k2_output_sep_bespoke_instances - separates using bespoke code
    * 2e_l - separates name instances and name exemplars
        * 2e_l1_output_sep_standard_exemplars - separates using the standard pattern
        * 2e_l2_output_sep_bespoke_exemplars - separates using bespoke code

For each of the sub-stages, the user can check the progress of the process by opening the csv files stored in the sub-stage output folders.
The process also exports the final sub-stage as XML in the parent output folder.

**This project is currently closed, but may be sporadically updated by the BORO Development Team in the future.**

## Installation

Ensure all the packages related in the file Requirements.txt are successfully installed.

This program has been tested with the [3.7.3 version of the Python interpreter](https://www.python.org/downloads/release/python-373/).

Sometimes, installing Python packages (PyCharm), the filename of any of the copied files is too long and PyCharm gives an error.
To resolve this run GitBash as administrator and run the command: `git config --system core.longpaths true`

If this is unsuccessful, run the command: `git config --global core.longpaths true`

#### Requirements

* Microsoft Visual C++ 14.0 or greater is required. 
    * A free version of "Microsoft C++ Build Tools" can be downloaded from [here](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
    * During the installation, check the Desktop development with C++ and untick all the optional products from the Installation details

## Execution

* Create an output folder to store the results of the process
* Create a folder that contains the GML files that are to be processed
* Run the start-up file: **bclearer_boson_1_source\b_code\a_startup\boson_1_bclearer_runner.py**
* This code runs as a standalone application that can be cloned to your Python IDE of preference
* When run the code asks for two folders: 
    * first, the output folder - this will store a timestamped folder that contains the substage folders, the XML output and the logging
    * second, the data folder - this is the input folder that contains the GML files that are to be processed

## Documentation

#### Background

The Agile Manifesto prefers “working software over comprehensive documentation”. Robert C. Martin, one of the original authors of the Agile Manifesto, is also the author of the book Clean Code.  

In this book, he makes a strong case for code being self-documenting: saying things such as "always try to explain yourself in code." 

He suggests that the goal of every programmer should be to write code so clean and expressive that code comments are unnecessary. 

When a programmer writes a comment, it will usually mean that they have failed to write code that was expressive enough. At the extreme, he suggests, maybe a little rhetorically, that "comments are always failures".

#### The BORO documentation policy

To aim to write code so clean and expressive that code comments are unnecessary. 

## Contributing

This package doesn't allow external contributors.

## Liability and Warranty

This code is provided as-is and without warranty.

Under no circumstances will the developers be liable for any incidental, consequential, or indirect damages including but not limited to lost or damaged data, revenue loss, economic loss, or commercial loss arising out of the use of this code.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Acknowledgements

This work was developed as part of the Information Management Framework to support the [National Digital Twin programme](https://www.cdbb.cam.ac.uk/what-we-do/national-digital-twin-programme), and funded by [Department for Business, Energy & Industrial Strategy](https://www.gov.uk/government/organisations/department-for-business-energy-and-industrial-strategy) through the [Centre for the Protection of National Infrastructure](https://www.cpni.gov.uk/).