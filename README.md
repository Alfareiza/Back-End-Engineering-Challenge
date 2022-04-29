<h1 align="center" >
    <img src="https://user-images.githubusercontent.com/63620799/165866730-c52bb38c-2a3a-4909-9b7f-5e16fbd11ac5.png">
</h1>
<h2 align="center" >
    XML o Json Converter <br>
    <img alt="GitHub stars" src="https://img.shields.io/github/stars/Alfareiza/xml-to-json?style=social">
    <img alt="GitHub followers" src="https://img.shields.io/github/followers/Alfareiza?label=Follow%20me%20%3A%29&style=social">
</h2>

## Setting Up

Install Python 3.7 or later if it is not already installed. Then, set up and enter a virtual environment and run `pip install -r requirements.txt` to install the dependencies. You should then be able to run the project from the `exercise` directory by running `python manage.py runserver`.

To verify that the server is running correctly, visit `http:127.0.0.1:8000` in your browser.

## Guidelines

This Django project consists of two parts:
1. A very simple HTML page at `/connected/`.
2. A stubbed out API endpoint at `/api/converter/convert/`

My tasks were:
1. Add a file input to the HTML page and modify the view so that, when a file is submitted, convert it to JSON and return that to the user
2. Add the same functionality to the API endpoint, returning the converted JSON as an `application/json` response.

To test my solution, I run `python manage.py test`. This will execute 3 tests, which attempt to submit a file and check the response.

As a good solution will not only pass the tests, but also work on any user-submitted XML file.
Furthermore, a good solution should never return a 500 error and should show an error message to the user if they upload an invalid XML file.

### JSON Conversion

For the purposes of this exercise, was ignored any XML attributes. I'm only interested in converting the XML node tags and any text values into JSON.

Leaf nodes were converted into a JSON object with the node tag as the key and the node's text value as the value. For example, `<Foo>Bar</Foo>` should be converted to `{"Foo": "Bar"}`.

Non-leaf nodes were converted into a JSON object with the node name as the key and an array of the node's children as the value. For example:
```
<Foo>
    <Bar>Baz</Bar>
</Foo>
```
should be converted to
```javascript
{
    "Foo": [
        {"Bar": "Baz"}
    ]
}
```

The tests provide additional examples of more complex conversions.

### Images

Uploading the xml

![image](https://user-images.githubusercontent.com/63620799/165866576-a1653107-ca21-4864-bf98-66646396663a.png)

XML Converted

![image](https://user-images.githubusercontent.com/63620799/165866328-c8263545-857c-4aee-84e4-3c539a89d65e.png)


