# Curly brackets to curly brackets

A simple script which embraces curly brackets with curly brackets. Useful when you have Prometheus deployed in Kubernetes with Helm and want to add custom metrics.

## Reason of usage

While you deploy Prometheus with Helm, custom metrics couldn't be added as "{{ $labels.myData }}", because Helm will try to render it as it's own variables. To avoid this you have to embrace curly brackets to curly brackets, like this "{{ "{{" }} $labels.myData {{ "}}" }}". More information about this issue could be found [here](https://stackoverflow.com/questions/64693812/how-to-fix-the-error-undefined-variable-labelsin-prometheus). This script is useful to embrace curly brackets with curly brackets automatically.

## How to use?

1. create "temp" folder in the directory with script.
2. Put your file with custom Prometheus metrics in it.
3. Fill the variable ```file_name``` on the third line with the name of your file.
4. Run script (```python3 brackets.py```) and it will generate a new formatted file into "temp" folder.
