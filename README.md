# Description

This is a package that converts images to a specified format. It searches recursively into a directory and converts all images.


# Install
```python
php3 install convertify
```

# Basic usage
```python
convertify --source=/path/to/your/images/
```
Converted images will be saved one path behind the source, in a directory named "converted-images". You can change destination path by specifyind the path via ```--destination=<your-destination-path>```

## Default Options:
- **source** = <given-path>
- **destination** = "../converted-images/"
- **from** = {All file types}
- **to** = "webp"
- **recursive** = True

# Advanced usage
```python
convertify --source=/path/to/your/images/ --destination=/path/to/your/destination/ -from=png -to=webp -recursive=false
```
